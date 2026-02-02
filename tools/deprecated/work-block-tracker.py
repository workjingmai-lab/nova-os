#!/usr/bin/env python3
"""
work-block-tracker.py — Track and analyze Nova's work block patterns

Usage:
    python tools/work-block-tracker.py                    # Last 24h
    python tools/work-block-tracker.py --hours 6          # Last 6 hours
    python tools/work-block-tracker.py --day 2026-02-01   # Specific day
    python tools/work-block-tracker.py --trend            # 7-day trend analysis
"""

import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

DIARY_PATH = Path("/home/node/.openclaw/workspace/diary.md")

def parse_work_blocks(content: str, date_filter: str = None) -> list:
    """Extract work blocks from diary.md

    Args:
        content: Raw diary.md content
        date_filter: Optional date string (YYYY-MM-DD) to filter

    Returns:
        List of dicts: {time, block_num, task, result, file}
    """
    # Split by work block headers
    # Format: "## HH:MM UTC — Work Block N"
    pattern = r'## (\d{2}:\d{2} UTC) — Work Block (\d+)'

    blocks = []
    matches = list(re.finditer(pattern, content))

    for match in matches:
        start_pos = match.start()
        block_num = int(match.group(2))
        time_str = match.group(1)

        # Find the next work block or end of file
        next_match = None
        for m in matches:
            if m.start() > start_pos:
                next_match = m
                break

        if next_match:
            block_content = content[start_pos:next_match.start()]
        else:
            block_content = content[start_pos:]

        # Extract task, result, file from block content
        task_match = re.search(r'\*\*Task:\*\* ([^\n]+)', block_content)
        result_match = re.search(r'\*\*Result:\*\* ([^\n]+)', block_content)
        file_match = re.search(r'\*\*File created:\*\* ([^\n]+)', block_content)

        block = {
            'time': time_str,
            'block_num': block_num,
            'task': task_match.group(1).strip() if task_match else 'Unknown',
            'result': result_match.group(1).strip() if result_match else 'Unknown',
            'file': file_match.group(1).strip() if file_match else None
        }

        blocks.append(block)

    return blocks

def calculate_velocity(blocks: list) -> dict:
    """Calculate velocity metrics from work blocks

    Args:
        blocks: List of work block dicts

    Returns:
        Dict with velocity metrics
    """
    if not blocks:
        return {
            'total_blocks': 0,
            'time_span_hours': 0,
            'blocks_per_hour': 0,
            'completion_rate': 0,
            'blocks_with_output': 0
        }

    # Parse times to calculate duration
    times = []
    for block in blocks:
        # Extract time from "HH:MM UTC"
        match = re.search(r'(\d{2}):(\d{2})', block['time'])
        if match:
            hour, minute = int(match.group(1)), int(match.group(2))
            # Create a datetime (use today as placeholder)
            dt = datetime.now().replace(hour=hour, minute=minute, second=0, microsecond=0)
            times.append(dt)

    # Calculate time span
    if len(times) >= 2:
        time_span = max(times) - min(times)
        hours_span = max(time_span.total_seconds() / 3600, 0.01)  # Avoid division by zero
    else:
        hours_span = 0.01

    # Calculate metrics
    total_blocks = len(blocks)
    blocks_with_output = sum(1 for b in blocks if b['file'] or 'completed' in b['result'].lower())
    completion_rate = (blocks_with_output / total_blocks * 100) if total_blocks > 0 else 0

    return {
        'total_blocks': total_blocks,
        'time_span_hours': round(hours_span, 2),
        'blocks_per_hour': round(total_blocks / hours_span, 2) if hours_span > 0 else 0,
        'completion_rate': round(completion_rate, 1),
        'blocks_with_output': blocks_with_output
    }

def analyze_trend(blocks: list) -> dict:
    """Analyze 7-day trend from work blocks

    Args:
        blocks: List of work block dicts

    Returns:
        Dict with trend analysis
    """
    if len(blocks) < 2:
        return {'trend': 'insufficient_data', 'change': 0}

    # Split into first half and second half
    mid = len(blocks) // 2
    first_half = blocks[:mid]
    second_half = blocks[mid:]

    # Calculate blocks per hour for each half
    first_velocity = calculate_velocity(first_half)['blocks_per_hour']
    second_velocity = calculate_velocity(second_half)['blocks_per_hour']

    # Determine trend
    if second_velocity > first_velocity * 1.1:
        trend = 'increasing 📈'
    elif second_velocity < first_velocity * 0.9:
        trend = 'decreasing 📉'
    else:
        trend = 'stable ➡️'

    change_percent = ((second_velocity - first_velocity) / first_velocity * 100) if first_velocity > 0 else 0

    return {
        'trend': trend,
        'change_percent': round(change_percent, 1),
        'first_velocity': round(first_velocity, 2),
        'second_velocity': round(second_velocity, 2)
    }

def print_digest(velocity: dict, trend: dict = None):
    """Print formatted work block digest

    Args:
        velocity: Velocity metrics dict
        trend: Optional trend analysis dict
    """
    print("📊 Work Block Digest")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"Total blocks:   {velocity['total_blocks']}")
    print(f"Time span:      {velocity['time_span_hours']}h")
    print(f"Velocity:       {velocity['blocks_per_hour']} blocks/hr")
    print(f"Completion:     {velocity['completion_rate']}% with output")

    if trend and trend.get('trend') != 'insufficient_data':
        print(f"\n📈 Trend (7-day): {trend['trend']}")
        print(f"   Velocity: {trend['first_velocity']} → {trend['second_velocity']} blocks/hr")
        if trend['change_percent'] != 0:
            print(f"   Change: {trend['change_percent']:+}%")

    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Track Nova\'s work blocks')
    parser.add_argument('--hours', type=int, default=24, help='Hours to look back')
    parser.add_argument('--day', type=str, help='Specific day (YYYY-MM-DD)')
    parser.add_argument('--trend', action='store_true', help='Show 7-day trend')
    args = parser.parse_args()

    # Read diary.md
    if not DIARY_PATH.exists():
        print(f"❌ Diary not found: {DIARY_PATH}")
        sys.exit(1)

    content = DIARY_PATH.read_text()

    # Parse work blocks
    if args.day:
        blocks = parse_work_blocks(content, date_filter=args.day)
        print(f"\n📅 Work blocks for {args.day}\n")
    elif args.trend:
        blocks = parse_work_blocks(content)
        print("\n📈 7-Day Trend Analysis\n")
    else:
        blocks = parse_work_blocks(content)
        print(f"\n⚡ Last {args.hours} hours\n")

    # Calculate and display metrics
    velocity = calculate_velocity(blocks)
    trend = analyze_trend(blocks) if args.trend else None

    print_digest(velocity, trend)

if __name__ == '__main__':
    main()
