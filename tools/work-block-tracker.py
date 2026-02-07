#!/usr/bin/env python3
"""
Work Block Velocity Tracker

Tracks work block completion rates, predicts milestones,
and identifies peak performance periods.

Usage:
    python3 tools/work-block-tracker.py status
    python3 tools/work-block-tracker.py predict --target 4000
    python3 tools/work-block-tracker.py analyze --period 24h
"""

import argparse
import json
import re
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict

DIARY_PATH = Path("diary.md")
STATE_PATH = Path(".heartbeat_state.json")


def parse_diary_blocks():
    """Extract work block data from diary.md"""
    if not DIARY_PATH.exists():
        return []
    
    content = DIARY_PATH.read_text()
    blocks = []
    
    # Pattern: "Work block NNNN: description" or "Work block NNNN (cron): description"
    pattern = r'Work block\s+(\d+)(?:\s+\([^)]+\))?:\s+(.+?)(?=\n- Work block|\n\n|$)'
    
    for match in re.finditer(pattern, content, re.DOTALL):
        block_num = int(match.group(1))
        description = match.group(2).strip()
        blocks.append({
            'number': block_num,
            'description': description
        })
    
    return blocks


def get_velocity_stats(blocks):
    """Calculate velocity statistics"""
    if not blocks or len(blocks) < 2:
        return {}
    
    # Get block numbers
    numbers = [b['number'] for b in blocks]
    min_block = min(numbers)
    max_block = max(numbers)
    total_blocks = max_block - min_block + 1
    
    # Count actual completed blocks
    completed = len(blocks)
    
    # Load state for timing data
    start_time = None
    if STATE_PATH.exists():
        try:
            state = json.loads(STATE_PATH.read_text())
            start_ms = state.get('sessionStartMs') or state.get('firstBlockMs')
            if start_ms:
                start_time = datetime.fromtimestamp(start_ms / 1000)
        except:
            pass
    
    # If no state, estimate from work block count
    if not start_time:
        # Assume ~78 blocks/hour as baseline
        hours_running = completed / 78.4
        start_time = datetime.now() - timedelta(hours=hours_running)
    
    elapsed = datetime.now() - start_time
    elapsed_hours = elapsed.total_seconds() / 3600
    
    velocity = completed / elapsed_hours if elapsed_hours > 0 else 0
    
    return {
        'total_completed': completed,
        'current_block': max_block,
        'elapsed_hours': round(elapsed_hours, 2),
        'velocity': round(velocity, 2),
        'start_time': start_time.isoformat()
    }


def predict_milestone(current, velocity, target):
    """Predict when a milestone will be reached"""
    if velocity <= 0:
        return "Unable to predict (velocity = 0)"
    
    blocks_needed = target - current
    if blocks_needed <= 0:
        return f"Target {target} already reached!"
    
    hours_needed = blocks_needed / velocity
    predicted_time = datetime.now() + timedelta(hours=hours_needed)
    
    return {
        'target': target,
        'blocks_remaining': blocks_needed,
        'hours_remaining': round(hours_needed, 2),
        'predicted_time': predicted_time.strftime('%Y-%m-%d %H:%M UTC'),
        'predicted_date': predicted_time.strftime('%A, %B %d')
    }


def analyze_patterns(blocks):
    """Analyze work patterns from block descriptions"""
    categories = defaultdict(int)
    
    for block in blocks:
        desc = block['description'].lower()
        
        if any(word in desc for word in ['article', 'knowledge', 'document']):
            categories['Documentation'] += 1
        elif any(word in desc for word in ['tool', 'script', 'code', 'python']):
            categories['Tool Development'] += 1
        elif any(word in desc for word in ['outreach', 'message', 'post', 'content']):
            categories['Outreach/Content'] += 1
        elif any(word in desc for word in ['research', 'analyze', 'study']):
            categories['Research/Analysis'] += 1
        else:
            categories['Other'] += 1
    
    return dict(categories)


def print_status(stats, blocks):
    """Print current status"""
    print("=" * 50)
    print("📊 WORK BLOCK VELOCITY TRACKER")
    print("=" * 50)
    print(f"Current Block:     {stats['current_block']}")
    print(f"Total Completed:   {stats['total_completed']}")
    print(f"Elapsed Time:      {stats['elapsed_hours']} hours")
    print(f"Current Velocity:  {stats['velocity']} blocks/hour")
    print("=" * 50)
    
    # Milestone progress
    milestones = [1000, 2000, 3000, 4000, 5000]
    print("\n🏆 MILESTONE PROGRESS:")
    for m in milestones:
        if stats['current_block'] >= m:
            print(f"  ✅ {m:,} blocks — ACHIEVED")
        else:
            remaining = m - stats['current_block']
            print(f"  ⏳ {m:,} blocks — {remaining} to go")
    
    # Category breakdown
    patterns = analyze_patterns(blocks)
    if patterns:
        print("\n📁 WORK CATEGORY BREAKDOWN:")
        for cat, count in sorted(patterns.items(), key=lambda x: -x[1]):
            pct = (count / len(blocks)) * 100
            print(f"  {cat}: {count} ({pct:.1f}%)")


def print_prediction(stats, target):
    """Print milestone prediction"""
    prediction = predict_milestone(
        stats['current_block'],
        stats['velocity'],
        target
    )
    
    if isinstance(prediction, str):
        print(prediction)
        return
    
    print("=" * 50)
    print(f"🔮 MILESTONE PREDICTION: {prediction['target']:,} blocks")
    print("=" * 50)
    print(f"Current Block:     {stats['current_block']}")
    print(f"Target Block:      {prediction['target']}")
    print(f"Blocks Remaining:  {prediction['blocks_remaining']}")
    print(f"Current Velocity:  {stats['velocity']} blocks/hour")
    print("-" * 50)
    print(f"Time Remaining:    {prediction['hours_remaining']} hours")
    print(f"Predicted Date:    {prediction['predicted_date']}")
    print(f"Predicted Time:    {prediction['predicted_time']}")
    print("=" * 50)


def main():
    parser = argparse.ArgumentParser(
        description='Track work block velocity and predict milestones'
    )
    parser.add_argument(
        'command',
        choices=['status', 'predict', 'analyze'],
        help='Command to run'
    )
    parser.add_argument(
        '--target',
        type=int,
        default=4000,
        help='Target block number for prediction (default: 4000)'
    )
    
    args = parser.parse_args()
    
    blocks = parse_diary_blocks()
    stats = get_velocity_stats(blocks)
    
    if args.command == 'status':
        print_status(stats, blocks)
    elif args.command == 'predict':
        print_prediction(stats, args.target)
    elif args.command == 'analyze':
        patterns = analyze_patterns(blocks)
        print("\n📊 WORK PATTERN ANALYSIS:")
        for cat, count in sorted(patterns.items(), key=lambda x: -x[1]):
            print(f"  {cat}: {count} blocks")


if __name__ == '__main__':
    main()
