#!/usr/bin/env python3
"""
Velocity Analyzer — Track work block velocity over time

Analyzes diary.md to calculate:
- Blocks per hour (historical)
- Velocity trends (improving/declining)
- Milestone predictions
- Peak performance windows

Usage:
    python3 velocity-analyzer.py                    # Summary
    python3 velocity-analyzer.py --last 100         # Last 100 blocks
    python3 velocity-analyzer.py --hourly           # Hourly breakdown
    python3 velocity-analyzer.py --predict 5000     # Predict when hitting 5000 blocks
"""

import re
import json
from datetime import datetime, timedelta
from collections import defaultdict
import argparse

DIARY_PATH = "/home/node/.openclaw/workspace/diary.md"

def parse_diary():
    """Parse diary.md and extract work blocks with timestamps"""
    blocks = []
    
    with open(DIARY_PATH, 'r') as f:
        content = f.read()
    
    # Pattern: ## [WORK BLOCK N — YYYY-MM-DD HH:MMZ]
    pattern = r'\[WORK BLOCK (\d+) — (\d{4}-\d{2}-\d{2} \d{2}:\d{2}Z)\]'
    
    matches = re.finditer(pattern, content)
    
    for match in matches:
        block_num = int(match.group(1))
        timestamp_str = match.group(2)
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%MZ")
        
        blocks.append({
            'number': block_num,
            'timestamp': timestamp
        })
    
    return sorted(blocks, key=lambda x: x['number'])

def calculate_velocity(blocks, window_size=None):
    """Calculate blocks per hour over time"""
    if len(blocks) < 2:
        return {}
    
    velocities = []
    
    for i in range(1, len(blocks)):
        block_delta = blocks[i]['number'] - blocks[i-1]['number']
        time_delta = (blocks[i]['timestamp'] - blocks[i-1]['timestamp']).total_seconds() / 3600
        
        if time_delta > 0:
            blocks_per_hour = block_delta / time_delta
            velocities.append({
                'block': blocks[i]['number'],
                'timestamp': blocks[i]['timestamp'],
                'velocity': blocks_per_hour
            })
    
    return velocities

def analyze_trends(velocities):
    """Analyze velocity trends"""
    if len(velocities) < 10:
        return {}
    
    # Split into recent (last 20%) vs earlier
    split_point = int(len(velocities) * 0.8)
    earlier = velocities[:split_point]
    recent = velocities[split_point:]
    
    earlier_avg = sum(v['velocity'] for v in earlier) / len(earlier)
    recent_avg = sum(v['velocity'] for v in recent) / len(recent)
    
    trend = "improving" if recent_avg > earlier_avg else "declining"
    change_pct = ((recent_avg - earlier_avg) / earlier_avg) * 100
    
    return {
        'earlier_avg': earlier_avg,
        'recent_avg': recent_avg,
        'trend': trend,
        'change_pct': change_pct
    }

def predict_milestone(blocks, target_block):
    """Predict when target block will be reached"""
    if len(blocks) < 2:
        return None
    
    # Use recent velocity (last 20% of blocks) for prediction
    split_point = int(len(blocks) * 0.8)
    recent_blocks = blocks[split_point:]
    
    if len(recent_blocks) < 2:
        return None
    
    block_delta = recent_blocks[-1]['number'] - recent_blocks[0]['number']
    time_delta = (recent_blocks[-1]['timestamp'] - recent_blocks[0]['timestamp']).total_seconds() / 3600
    
    if time_delta == 0:
        return None
    
    velocity = block_delta / time_delta
    blocks_remaining = target_block - blocks[-1]['number']
    hours_remaining = blocks_remaining / velocity
    
    eta = blocks[-1]['timestamp'] + timedelta(hours=hours_remaining)
    
    return {
        'target': target_block,
        'current': blocks[-1]['number'],
        'blocks_remaining': blocks_remaining,
        'velocity': velocity,
        'hours_remaining': hours_remaining,
        'eta': eta,
        'eta_str': eta.strftime("%Y-%m-%d %H:%MZ")
    }

def hourly_breakdown(blocks):
    """Analyze velocity by hour of day"""
    hourly_blocks = defaultdict(list)
    
    for block in blocks:
        hour = block['timestamp'].hour
        hourly_blocks[hour].append(block)
    
    hourly_stats = {}
    
    for hour in sorted(hourly_blocks.keys()):
        hour_blocks = hourly_blocks[hour]
        if len(hour_blocks) < 2:
            continue
        
        # Calculate blocks per hour during this UTC hour
        first_block = hour_blocks[0]
        last_block = hour_blocks[-1]
        
        block_count = last_block['number'] - first_block['number'] + 1
        
        hourly_stats[hour] = {
            'block_count': block_count,
            'session_count': len(hour_blocks),
            'avg_blocks_per_session': block_count / len(hour_blocks)
        }
    
    return hourly_stats

def main():
    parser = argparse.ArgumentParser(description='Velocity Analyzer')
    parser.add_argument('--last', type=int, help='Analyze last N blocks')
    parser.add_argument('--hourly', action='store_true', help='Show hourly breakdown')
    parser.add_argument('--predict', type=int, help='Predict when hitting N blocks')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    
    args = parser.parse_args()
    
    # Parse diary
    blocks = parse_diary()
    
    if args.last:
        blocks = blocks[-args.last:]
    
    if not blocks:
        print("No work blocks found in diary.md")
        return
    
    # Calculate velocity
    velocities = calculate_velocity(blocks)
    
    if not velocities:
        print("Not enough data to calculate velocity")
        return
    
    # Output
    if args.json:
        output = {
            'total_blocks': blocks[-1]['number'] - blocks[0]['number'] + 1,
            'first_block': blocks[0],
            'last_block': blocks[-1],
            'avg_velocity': sum(v['velocity'] for v in velocities) / len(velocities),
            'velocities': velocities
        }
        print(json.dumps(output, indent=2, default=str))
        return
    
    # Summary
    print(f"📊 VELOCITY ANALYSIS")
    print(f"=" * 60)
    print(f"Blocks analyzed: {blocks[-1]['number'] - blocks[0]['number'] + 1}")
    print(f"Time span: {blocks[0]['timestamp'].strftime('%Y-%m-%d %H:%MZ')} → {blocks[-1]['timestamp'].strftime('%Y-%m-%d %H:%MZ')}")
    print()
    
    # Average velocity
    avg_velocity = sum(v['velocity'] for v in velocities) / len(velocities)
    print(f"Average velocity: {avg_velocity:.1f} blocks/hour")
    
    # Trends
    trends = analyze_trends(velocities)
    if trends:
        print(f"Trend: {trends['trend']} ({trends['change_pct']:+.1f}% change)")
        print(f"  Earlier: {trends['earlier_avg']:.1f} blocks/hr")
        print(f"  Recent: {trends['recent_avg']:.1f} blocks/hr")
    
    print()
    
    # Hourly breakdown
    if args.hourly:
        print(f"⏰ HOURLY BREAKDOWN (UTC)")
        print(f"=" * 60)
        hourly = hourly_breakdown(blocks)
        
        for hour in sorted(hourly.keys()):
            stats = hourly[hour]
            print(f"{hour:02d}:00 UTC: {stats['block_count']:3.0f} blocks, {stats['session_count']:2.0f} sessions, {stats['avg_blocks_per_session']:.1f} avg/session")
        print()
    
    # Milestone prediction
    if args.predict:
        prediction = predict_milestone(blocks, args.predict)
        if prediction:
            print(f"🎯 MILESTONE PREDICTION: {prediction['target']} blocks")
            print(f"=" * 60)
            print(f"Current: {prediction['current']}")
            print(f"Remaining: {prediction['blocks_remaining']} blocks")
            print(f"Velocity: {prediction['velocity']:.1f} blocks/hour")
            print(f"ETA: {prediction['eta_str']} ({prediction['hours_remaining']:.1f} hours)")
        else:
            print(f"Not enough data to predict milestone {args.predict}")

if __name__ == "__main__":
    main()
