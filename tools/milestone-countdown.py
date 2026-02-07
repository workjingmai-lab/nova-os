#!/usr/bin/env python3
"""
Milestone Countdown — Track progress to work block milestones

Usage:
    python3 tools/milestone-countdown.py                    # Show countdown to 3000
    python3 tools/milestone-countdown.py --milestone 5000   # Countdown to 5000
    python3 tools/milestone-countdown.py --list             # Show all milestones
"""

import sys
import re
from datetime import datetime
from pathlib import Path

DIARY_FILE = "/home/node/.openclaw/workspace/diary.md"
VELOCITY = 44  # blocks/hour (sustained average)

# Milestone definitions
MILESTONES = {
    1000: "Proof of execution",
    2000: "Pipeline builder",
    3000: "Conversion focus",
    4000: "Revenue generator",
    5000: "Ecosystem scale",
}

def get_current_blocks():
    """Parse diary.md for current work block count"""
    try:
        with open(DIARY_FILE, 'r') as f:
            content = f.read()

        # Find all work block numbers
        pattern = r'\[WORK BLOCK (\d+) —'
        blocks = re.findall(pattern, content)

        if blocks:
            return int(blocks[-1])  # Return the highest block number
        return 0
    except Exception as e:
        print(f"Error reading diary.md: {e}")
        return 0

def show_countdown(milestone=3000):
    """Show countdown to milestone"""
    current = get_current_blocks()
    remaining = milestone - current
    hours = remaining / VELOCITY

    # Calculate percentage
    percent = (current / milestone) * 100

    # Progress bar
    bar_length = 40
    filled = int(bar_length * current / milestone)
    bar = "█" * filled + "░" * (bar_length - filled)

    print(f"\n🎯 Milestone Countdown: {milestone:,} Blocks")
    print("=" * 60)
    print(f"Milestone: {MILESTONES.get(milestone, 'Unknown')}")
    print()
    print(f"Current:   {current:,} blocks ({percent:.1f}%)")
    print(f"Remaining: {remaining:,} blocks")
    print(f"ETA:       {hours:.1f} hours (at {VELOCITY} blocks/hr)")
    print()
    print(f"Progress:  [{bar}] {percent:.1f}%")
    print()

    # Motivational message based on progress
    if percent >= 95:
        print("🔥 Almost there! Final push!")
    elif percent >= 80:
        print("⚡ Home stretch — keep the momentum!")
    elif percent >= 50:
        print("💪 Halfway there — sustained execution!")
    elif percent >= 20:
        print("🚀 Building momentum — small executions compound!")
    else:
        print("🌱 Every block counts — just keep going!")

    print()

    # What this milestone means
    if milestone == 1000:
        print("📝 1000 blocks = Proving you can execute consistently")
    elif milestone == 2000:
        print("💰 2000 blocks = Pipeline builder ($500K+ potential)")
    elif milestone == 3000:
        print("🎯 3000 blocks = Shift to conversion (first dollar won)")
    elif milestone == 4000:
        print("💵 4000 blocks = Revenue generator (consistent deals)")
    elif milestone == 5000:
        print("🏆 5000 blocks = Ecosystem scale (multi-agent org)")

def list_milestones():
    """Show all milestones"""
    current = get_current_blocks()

    print(f"\n📍 Milestone Progress (Current: {current:,} blocks)")
    print("=" * 60)

    for milestone, description in sorted(MILESTONES.items()):
        achieved = current >= milestone
        status = "✅" if achieved else "⏳"
        percent = min(100, (current / milestone) * 100)

        print(f"{status} {milestone:,} ({percent:.0f}%) — {description}")

    print()

    # Next milestone
    next_ms = next((m for m in sorted(MILESTONES.keys()) if m > current), None)
    if next_ms:
        remaining = next_ms - current
        hours = remaining / VELOCITY
        print(f"🎯 Next milestone: {next_ms:,} blocks ({remaining:,} remaining, ~{hours:.1f} hours)")

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Milestone countdown tracker")
    parser.add_argument("--milestone", "-m", type=int, default=3000, help="Target milestone")
    parser.add_argument("--list", "-l", action="store_true", help="List all milestones")

    args = parser.parse_args()

    if args.list:
        list_milestones()
    else:
        show_countdown(args.milestone)

if __name__ == "__main__":
    main()
