#!/usr/bin/env python3
"""
Velocity Calculator - Quick work block metrics

Usage:
    python3 tools/velocity-calc.py              # Today's metrics
    python3 tools/velocity-calc.py --week       # Weekly summary
    python3 tools/velocity-calc.py --total      # All-time total
"""

import re
from datetime import datetime, timedelta
from pathlib import Path

DIARY_PATH = Path("/home/node/.openclaw/workspace/diary.md")

def parse_work_blocks():
    """Extract work blocks from diary.md"""
    if not DIARY_PATH.exists():
        return []

    content = DIARY_PATH.read_text()
    pattern = r'\[WORK BLOCK (\d+) — ([^\]]+)\]'
    matches = re.findall(pattern, content)

    blocks = []
    for block_num, timestamp in matches:
        try:
            # Handle 'Z' suffix (UTC) and make timezone-aware
            if timestamp.endswith('Z'):
                dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            else:
                dt = datetime.fromisoformat(timestamp)
                if dt.tzinfo is None:
                    # Assume UTC if no timezone
                    dt = dt.replace(tzinfo=None)
            blocks.append((int(block_num), dt))
        except:
            pass

    # Sort by block number instead of datetime to avoid timezone issues
    return sorted(blocks, key=lambda x: x[0])

def calculate_metrics(blocks):
    """Calculate velocity metrics"""
    if not blocks:
        return {}

    total = len(blocks)
    first_time = blocks[0][1]
    last_time = blocks[-1][1]
    duration = (last_time - first_time).total_seconds() / 60  # minutes

    return {
        "total_blocks": total,
        "first_block": first_time,
        "last_block": last_time,
        "duration_minutes": duration,
        "blocks_per_hour": (total / (duration / 60)) if duration > 0 else 0,
        "avg_block_time": (duration / total) if total > 0 else 0,
    }

def format_metrics(metrics):
    """Format metrics for display"""
    if not metrics:
        return "No work blocks found"

    output = []
    output.append(f"📊 Velocity Metrics")
    output.append(f"")
    output.append(f"Total Work Blocks: {metrics['total_blocks']}")
    output.append(f"Duration: {metrics['duration_minutes']:.0f} minutes")
    output.append(f"Velocity: {metrics['blocks_per_hour']:.1f} blocks/hour")
    output.append(f"Avg Block Time: {metrics['avg_block_time']:.1f} minutes")
    output.append(f"")
    output.append(f"First Block: {metrics['first_block'].strftime('%Y-%m-%d %H:%M')}")
    output.append(f"Last Block: {metrics['last_block'].strftime('%Y-%m-%d %H:%M')}")

    return "\n".join(output)

def main():
    import sys

    blocks = parse_work_blocks()

    if not blocks:
        print("No work blocks found in diary.md")
        return

    # Filter by timeframe if needed
    if "--week" in sys.argv:
        cutoff = datetime.now(datetime.now().astimezone().tzinfo) - timedelta(days=7)
        blocks = [b for b in blocks if b[1] >= cutoff]

    metrics = calculate_metrics(blocks)
    print(format_metrics(metrics))

if __name__ == "__main__":
    main()
