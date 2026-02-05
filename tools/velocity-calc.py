#!/usr/bin/env python3
"""
Calculate and predict work block velocity.
Shows blocks/hr, blocks/day, milestone predictions.
"""

import json
import re
from datetime import datetime, timedelta

def read_diary_blocks() -> dict:
    """Parse diary.md to extract block counts by date."""
    diary_path = '/home/node/.openclaw/workspace/diary.md'

    try:
        with open(diary_path, 'r') as f:
            content = f.read()
    except IOError:
        return {}

    # Pattern: "## YYYY-MM-DD (Weekday)"
    date_pattern = r'## (\d{4}-\d{2}-\d{2})'
    dates = re.findall(date_pattern, content)

    # Count work blocks per date
    blocks_by_date = {}
    current_date = None

    for line in content.split('\n'):
        # Check for date header
        date_match = re.match(r'## (\d{4}-\d{2}-\d{2})', line)
        if date_match:
            current_date = date_match.group(1)
            blocks_by_date[current_date] = 0
            continue

        # Check for work block entries
        if 'Work Block' in line and '—' in line:
            block_match = re.search(r'Work Block (\d+)', line)
            if block_match and current_date:
                block_num = int(block_match.group(1))
                if block_num > blocks_by_date.get(current_date, 0):
                    blocks_by_date[current_date] = block_num

    return blocks_by_date

def calculate_velocity(blocks_by_date: dict) -> dict:
    """Calculate velocity metrics from block history."""
    if not blocks_by_date:
        return {}

    # Get recent days (last 7 days or all if less)
    dates = sorted(blocks_by_date.keys())[-7:]
    recent_blocks = [blocks_by_date[d] for d in dates]

    if not recent_blocks:
        return {}

    avg_blocks_per_day = sum(recent_blocks) / len(recent_blocks)

    # Assuming 23 workable hours per day (1 hour maintenance/rest)
    blocks_per_hour = avg_blocks_per_day / 23

    # Calculate trend (last 3 days vs all 7)
    if len(recent_blocks) >= 3:
        recent_avg = sum(recent_blocks[-3:]) / 3
        overall_avg = avg_blocks_per_day
        trend = ((recent_avg - overall_avg) / overall_avg) * 100
    else:
        trend = 0

    return {
        'avg_blocks_per_day': round(avg_blocks_per_day, 1),
        'blocks_per_hour': round(blocks_per_hour, 1),
        'trend_percent': round(trend, 1),
        'total_days': len(dates),
        'max_blocks': max(recent_blocks) if recent_blocks else 0
    }

def predict_milestone(blocks_per_hour: float, target: int, current: int) -> str:
    """Predict when milestone will be reached."""
    if blocks_per_hour <= 0:
        return "∞ (no velocity data)"

    remaining = target - current
    if remaining <= 0:
        return "✅ REACHED"

    hours_needed = remaining / blocks_per_hour
    days_needed = hours_needed / 23

    if days_needed < 1:
        return f"~{int(hours_needed)} hours"
    elif days_needed < 30:
        return f"~{int(days_needed)} days"
    else:
        months = days_needed / 30
        return f"~{int(months)} months"

def main():
    # Read diary blocks
    blocks_by_date = read_diary_blocks()

    # Calculate velocity
    velocity = calculate_velocity(blocks_by_date)

    if not velocity:
        print("❌ No block data found in diary.md")
        return

    # Get current block count
    heartbeat_path = '/home/node/.openclaw/workspace/.heartbeat_state.json'
    try:
        with open(heartbeat_path, 'r') as f:
            heartbeat = json.load(f)
        current_blocks = heartbeat.get('blocksToday', 0)
    except:
        current_blocks = velocity.get('max_blocks', 0)

    # Display velocity
    print(f"📊 Work Block Velocity")
    print(f"=" * 40)
    print(f"Current blocks: {current_blocks}")
    print(f"Avg blocks/day: {velocity['avg_blocks_per_day']} (last {velocity['total_days']} days)")
    print(f"Blocks/hour: {velocity['blocks_per_hour']}")
    print(f"Trend: {velocity['trend_percent']:+}% (recent vs overall)")
    print()

    # Predict milestones
    print(f"🎯 Milestone Predictions")
    print(f"=" * 40)

    milestones = [
        ("2000 blocks", 2000),
        ("2500 blocks", 2500),
        ("5000 blocks", 5000),
        ("10000 blocks", 10000),
    ]

    for name, target in milestones:
        prediction = predict_milestone(velocity['blocks_per_hour'], target, current_blocks)
        print(f"{name}: {prediction}")

if __name__ == '__main__':
    main()
