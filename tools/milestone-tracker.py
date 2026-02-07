#!/usr/bin/env python3
"""
Milestone Tracker — Visualize progress toward major milestones

Usage:
  python3 tools/milestone-tracker.py              # Current status
  python3 tools/milestone-tracker.py --forecast   # Predict milestone times
"""

import json
import sys
from datetime import datetime, timedelta

VELOCITY_BLOCKS_PER_HOUR = 44

MILESTONES = {
    3000: "🚀 Major ecosystem milestone — $1.49M pipeline built",
    5000: "🌟 Empire builder — $2.47M projected",
    10000: "🏆 Legendary — Autonomous agent nation"
}

def parse_diary_blocks():
    """Extract current block count from today.md"""
    try:
        with open("today.md", "r") as f:
            content = f.read()
            # Find "Work blocks: NNNN"
            for line in content.split("\n"):
                if "Work blocks:" in line:
                    parts = line.split("Work blocks:")[1].strip()
                    current = int(parts.split()[0])
                    return current
    except Exception as e:
        print(f"Error reading today.md: {e}")
        return 2848  # Fallback from today's status

def calculate_eta(current_blocks, target_blocks):
    """Calculate estimated time to milestone"""
    remaining = max(0, target_blocks - current_blocks)
    hours = remaining / VELOCITY_BLOCKS_PER_HOUR
    return hours, remaining

def display_progress():
    """Show current progress toward all milestones"""
    current = parse_diary_blocks()
    now = datetime.utcnow()

    print(f"📊 Milestone Tracker — Current: {current} blocks\n")

    for milestone, description in sorted(MILESTONES.items()):
        if current >= milestone:
            status = "✅ COMPLETE"
            hours = 0
            remaining = 0
        else:
            status = "🔄 IN PROGRESS"
            hours, remaining = calculate_eta(current, milestone)

        percentage = min(100, (current / milestone) * 100)

        print(f"{description}")
        print(f"  Target: {milestone:,} blocks | Progress: {percentage:.1f}% ({current:,}/{milestone:,})")
        print(f"  Status: {status}")

        if remaining > 0:
            eta = now + timedelta(hours=hours)
            print(f"  Remaining: {remaining:,} blocks | ETA: {eta.strftime('%Y-%m-%d %H:%M')} UTC ({hours:.1f} hours)")
        print()

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--forecast":
        # Detailed forecast mode
        current = parse_diary_blocks()
        print(f"🔮 Velocity Forecast — {VELOCITY_BLOCKS_PER_HOUR} blocks/hour\n")
        for milestone in sorted(MILESTONES.keys()):
            if milestone > current:
                hours, remaining = calculate_eta(current, milestone)
                eta = datetime.utcnow() + timedelta(hours=hours)
                print(f"{milestone:,} blocks: {remaining:,} remaining → {eta.strftime('%Y-%m-%d %H:%M')} UTC")
    else:
        display_progress()

if __name__ == "__main__":
    main()
