#!/usr/bin/env python3
"""
work-block-miner.py - Extract insights from diary.md patterns

Scans diary.md for:
- High-velocity periods (most work blocks/hour)
- Task types and frequencies
- Best execution times
- Block-to-block transitions

Usage:
    python tools/work-block-miner.py [--recent N] [--output FILE]
"""

import re
import sys
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime

DIARY_PATH = Path("/home/node/.openclaw/workspace/diary.md")

def parse_diary():
    """Parse diary.md into structured entries."""
    if not DIARY_PATH.exists():
        print(f"❌ {DIARY_PATH} not found")
        return []

    with open(DIARY_PATH) as f:
        content = f.read()

    # Split into blocks (entries starting with ##)
    blocks = re.split(r'^## ', content, flags=re.MULTILINE)[1:]  # Skip first empty split

    entries = []
    for block in blocks:
        lines = block.strip().split('\n')
        if not lines:
            continue

        # Parse timestamp from first line
        header = lines[0]
        # Format: "[WORK BLOCK 338 — 2026-02-02T00:06Z] ⚡ WORK BLOCK: Documented Execution Velocity Insight"
        match = re.search(r'\[WORK BLOCK (\d+) — ([^\]]+)\] .+?: (.+)', header)
        if match:
            block_num, timestamp, task = match.groups()
            # Extract time from ISO timestamp (format: 2026-02-02T00:06Z)
            time_match = re.search(r'T(\d{2}):(\d{2})', timestamp)
            if time_match:
                time_str = f"{time_match.group(1)}:{time_match.group(2)}:00"
            else:
                time_str = "00:00:00"
            
            entries.append({
                'block': int(block_num),
                'time': time_str,
                'task': task.strip(),
                'timestamp': timestamp,
                'full_entry': block
            })

    return entries

def analyze_velocity(entries, recent_n=None):
    """Analyze execution velocity over time."""
    if recent_n:
        entries = entries[-recent_n:]

    if len(entries) < 2:
        return {}

    # Calculate time deltas between blocks
    velocities = []
    for i in range(1, len(entries)):
        try:
            t1 = datetime.strptime(entries[i-1]['time'], '%H:%M:%S')
            t2 = datetime.strptime(entries[i]['time'], '%H:%M:%S')
            delta = (t2 - t1).total_seconds() / 60  # minutes
            if delta > 0:
                velocities.append(delta)
        except:
            continue

    if not velocities:
        return {}

    return {
        'total_blocks': len(entries),
        'avg_gap_minutes': sum(velocities) / len(velocities),
        'fastest_gap': min(velocities),
        'blocks_per_hour': 60 / (sum(velocities) / len(velocities)) if velocities else 0
    }

def categorize_tasks(entries):
    """Categorize task types."""
    categories = defaultdict(int)

    for entry in entries:
        task = entry['task'].lower()

        # Simple keyword-based categorization
        if any(kw in task for kw in ['create', 'build', 'wrote', 'generated']):
            categories['Creation'] += 1
        elif any(kw in task for kw in ['update', 'refactor', 'polish']):
            categories['Improvement'] += 1
        elif any(kw in task for kw in ['read', 'check', 'analyze']):
            categories['Analysis'] += 1
        elif any(kw in task for kw in ['post', 'share', 'comment']):
            categories['Engagement'] += 1
        elif any(kw in task for kw in ['fix', 'debug', 'resolve']):
            categories['Problem-solving'] += 1
        else:
            categories['Other'] += 1

    return dict(categories)

def find_best_windows(entries, window_minutes=60):
    """Find highest-velocity time windows."""
    if len(entries) < 2:
        return []

    # Convert to minutes since midnight
    minute_positions = []
    for entry in entries:
        try:
            t = datetime.strptime(entry['time'], '%H:%M:%S')
            minutes = t.hour * 60 + t.minute
            minute_positions.append((minutes, entry['block']))
        except:
            continue

    # Find densest windows
    best_windows = []
    for i, (start_min, start_block) in enumerate(minute_positions):
        end_min = start_min + window_minutes
        count = sum(1 for m, _ in minute_positions if start_min <= m < end_min)
        best_windows.append({
            'start_time': f"{start_min // 60:02d}:{start_min % 60:02d}",
            'blocks_in_window': count,
            'density': count / window_minutes
        })

    # Sort by density
    best_windows.sort(key=lambda x: x['density'], reverse=True)
    return best_windows[:3]  # Top 3 windows

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--recent', type=int, help='Analyze last N entries')
    parser.add_argument('--output', type=str, help='Output file (default: stdout)')
    args = parser.parse_args()

    entries = parse_diary()
    if not entries:
        print("❌ No entries found")
        return 1

    recent_n = args.recent if args.recent else len(entries)
    entries = entries[-recent_n:]

    # Run analyses
    velocity = analyze_velocity(entries)
    categories = categorize_tasks(entries)
    windows = find_best_windows(entries)

    # Format output
    output_lines = [
        f"# 📊 Work Block Analysis — Last {recent_n} blocks",
        f"",
        f"## 🚀 Velocity Metrics",
        f"- Total blocks analyzed: {velocity.get('total_blocks', 0)}",
        f"- Average gap: {velocity.get('avg_gap_minutes', 0):.1f} minutes",
        f"- Fastest gap: {velocity.get('fastest_gap', 0):.1f} minutes",
        f"- Blocks per hour: {velocity.get('blocks_per_hour', 0):.1f}",
        f"",
        f"## 📁 Task Distribution",
    ]

    for cat, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        pct = (count / len(entries)) * 100
        output_lines.append(f"- {cat}: {count} ({pct:.1f}%)")

    output_lines.extend([
        f"",
        f"## ⏰ Peak Execution Windows",
    ])

    for i, win in enumerate(windows, 1):
        output_lines.append(f"{i}. {win['start_time']} — {win['blocks_in_window']} blocks ({win['density']:.2f} blocks/minute)")

    output_lines.append("")
    output = "\n".join(output_lines)

    if args.output:
        with open(args.output, 'w') as f:
            f.write(output)
        print(f"✅ Analysis written to {args.output}")
    else:
        print(output)

    return 0

if __name__ == '__main__':
    sys.exit(main())
