#!/usr/bin/env python3
"""
blocks-remaining.py — Calculate remaining blocks to milestone

Usage:
    python3 tools/blocks-remaining.py              # Show remaining to 3000
    python3 tools/blocks-remaining.py 3300         # Show remaining to custom target
    python3 tools/blocks-remaining.py 3000 50      # Custom target and velocity
"""

import sys
from pathlib import Path

WORKSPACE = Path.home() / ".openclaw/workspace"
DIARY_FILE = WORKSPACE / "diary.md"

def get_current_blocks():
    """Parse current block count from diary.md"""
    try:
        with open(DIARY_FILE) as f:
            content = f.read()
            # Find the most recent "WORK BLOCK" entry
            for line in content.split('\n'):
                if 'WORK BLOCK' in line and '—' in line:
                    # Extract block number from format: "### [WORK BLOCK 2940 — ..."
                    parts = line.split('WORK BLOCK')[1].split('—')[0].strip()
                    try:
                        return int(parts)
                    except ValueError:
                        continue
    except Exception:
        return None

def calculate_eta(current, target, velocity=44):
    """Calculate ETA based on velocity (blocks per hour)"""
    remaining = max(0, target - current)
    hours = remaining / velocity if velocity > 0 else 0
    return remaining, hours

def format_time(hours):
    """Format decimal hours to readable time"""
    h = int(hours)
    m = int((hours - h) * 60)
    return f"{h}h {m}m"

def main():
    # Get parameters
    target = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    velocity = int(sys.argv[2]) if len(sys.argv) > 2 else 44

    # Get current block count
    current = get_current_blocks()
    if current is None:
        print("❌ Could not determine current block count from diary.md")
        return 1

    # Calculate
    remaining, hours = calculate_eta(current, target, velocity)
    percentage = (current / target) * 100 if target > 0 else 0
    surplus = max(0, current - 300)  # Above weekly target

    # Display
    print(f"🎯 MILESTONE: {target:,} blocks")
    print(f"📍 Current: {current:,} blocks ({percentage:.1f}%)")
    print(f"⏳ Remaining: {remaining:,} blocks")
    print(f"🚀 Velocity: {velocity} blocks/hr")
    print(f"⏱️  ETA: {format_time(hours)}")
    print(f"📊 Weekly surplus: +{surplus:,} blocks")

    # Motivational message
    if remaining <= 100:
        print(f"\n🔥 FINAL SPRINT! {remaining} blocks to go!")
    elif remaining <= 500:
        print(f"\n💪 Almost there! Keep pushing!")
    else:
        print(f"\n✨ Steady progress. Execute the next block.")

    return 0

if __name__ == "__main__":
    sys.exit(main())
