#!/usr/bin/env python3
"""
blocks-to-go.py — Quick milestone progress check

Shows how many blocks until 2000 milestone and ETA at current velocity.

Usage:
    python3 tools/blocks-to-go.py
"""

import json
from datetime import datetime, timedelta

def main():
    # Read diary.md to get current block count
    try:
        with open('/home/node/.openclaw/workspace/diary.md', 'r') as f:
            content = f.read()

        # Find the most recent work block number
        import re
        matches = re.findall(r'WORK BLOCK (\d+) —', content)
        if matches:
            current_block = int(matches[0])
        else:
            print("❌ No work blocks found in diary.md")
            return
    except Exception as e:
        print(f"❌ Error reading diary.md: {e}")
        return

    # Calculate progress to 2000
    milestone = 2000
    remaining = milestone - current_block
    percentage = (current_block / milestone) * 100

    # Velocity scenarios
    sustained_velocity = 44  # blocks/hr
    burst_velocity = 55      # blocks/hr
    current_session_velocity = 67  # blocks/hr (from cron session)

    # Calculate ETAs
    now = datetime.utcnow()
    sustained_eta = now + timedelta(hours=remaining/sustained_velocity)
    burst_eta = now + timedelta(hours=remaining/burst_velocity)
    current_eta = now + timedelta(hours=remaining/current_session_velocity)

    # Output
    print(f"🎯 2000-Block Milestone Progress")
    print(f"{'='*50}")
    print(f"Current: {current_block} blocks ({percentage:.2f}%)")
    print(f"Target: {milestone} blocks")
    print(f"Remaining: {remaining} blocks")
    print()
    print(f"📊 Velocity Scenarios:")
    print(f"  Sustained (44/hr): {remaining/sustained_velocity:.1f}hr → ~{sustained_eta.strftime('%H:%M')} UTC")
    print(f"  Burst (55/hr):     {remaining/burst_velocity:.1f}hr → ~{burst_eta.strftime('%H:%M')} UTC")
    print(f"  Current (67/hr):   {remaining/current_session_velocity:.1f}hr → ~{current_eta.strftime('%H:%M')} UTC")
    print()
    print(f"💪 Keep going! {remaining} blocks to milestone!")

if __name__ == '__main__':
    main()
