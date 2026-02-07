#!/usr/bin/env python3
"""
Velocity Snapshot — Current execution speed vs targets.

Shows:
- Work blocks completed today
- Velocity (blocks/hour)
- Comparison to targets

Usage:
    python3 velocity-snapshot.py

Created: 2026-02-07 (Work block 3223)
"""

import re
from datetime import datetime, timedelta
from pathlib import Path

DIARY_FILE = "/home/node/.openclaw/workspace/diary.md"

def count_blocks_today():
    """Count work blocks in today's diary entries."""
    today = datetime.utcnow().strftime("%Y-%m-%d")

    with open(DIARY_FILE, 'r') as f:
        content = f.read()

    # Count WORK BLOCK entries for today
    pattern = rf'\[{today}.*?\] — WORK BLOCK (\d+)'
    blocks = re.findall(pattern, content)

    return len(blocks), blocks[-1] if blocks else None

def main():
    print("📊 VELOCITY SNAPSHOT")
    print("=" * 50)
    print(f"Time: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}")

    count, last_block = count_blocks_today()
    print(f"\nWork blocks today: {count}")
    if last_block:
        print(f"Latest block: #{last_block}")

    # Estimate velocity (assume ~8 hours of work so far today)
    hours_active = 8  # Conservative estimate
    velocity = count / hours_active if hours_active > 0 else 0

    print(f"\nEstimated velocity: {velocity:.1f} blocks/hour")
    print(f"Target: 44 blocks/hour")

    if velocity >= 44:
        print(f"✅ Above target! (+{velocity - 44:.1f} blocks/hr)")
    else:
        print(f"⚠️  Below target (-{44 - velocity:.1f} blocks/hr)")

    # Project milestone
    blocks_to_1000 = 1000 - int(last_block) if last_block else 1000
    if velocity > 0:
        hours_to_1000 = blocks_to_1000 / velocity
        print(f"\n🎯 Blocks to 1000: {blocks_to_1000}")
        print(f"   At current velocity: {hours_to_1000:.1f} hours")

if __name__ == '__main__':
    main()
