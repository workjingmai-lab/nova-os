#!/usr/bin/env python3
"""
win-streak.py — Track consecutive days with 10+ work blocks
Gamifies productivity: maintain your streak!
Usage: python tools/win-streak.py
"""

import re
from collections import defaultdict
from pathlib import Path
from datetime import datetime, timezone

def extract_work_blocks(diary_file):
    """Parse diary.md and extract work block dates"""
    content = Path(diary_file).read_text()

    # Pattern: [WORK BLOCK ### — DATE] (various formats)
    # Match: WORK BLOCK \d+ — YYYY-MM-DD
    pattern = r'WORK BLOCK \d+ .+ (\d{4}-\d{2}-\d{2})'
    matches = re.findall(pattern, content)

    # Count blocks per date
    blocks_per_date = defaultdict(int)
    for date_str in matches:
        blocks_per_date[date_str] += 1

    return dict(blocks_per_date)

def calculate_streak(blocks_per_date):
    """Calculate consecutive days with 10+ blocks"""
    # Sort dates
    sorted_dates = sorted(blocks_per_date.keys(), reverse=True)

    streak = 0
    threshold = 10  # 10+ blocks = win

    for date in sorted_dates:
        if blocks_per_date[date] >= threshold:
            streak += 1
        else:
            break  # Streak broken

    return streak, sorted_dates

def main():
    diary_file = Path(__file__).parent.parent / "diary.md"

    if not diary_file.exists():
        print(f"❌ Diary not found: {diary_file}")
        return

    blocks_per_date = calculate_streak(extract_work_blocks(diary_file))

    print("🔥 WIN STREAK TRACKER")
    print("=" * 50)

    if not blocks_per_date[1]:  # No dates found
        print("No work blocks found in diary.md")
        return

    sorted_dates = blocks_per_date[1]
    streak = blocks_per_date[0]

    print(f"\n🎯 Current Streak: {streak} consecutive days with 10+ work blocks")

    if streak > 0:
        print(f"\n🔥 ON FIRE! Keep it going!\n")
    else:
        print(f"\n💪 Start your streak today!\n")

    print("Recent Daily Totals:")
    print("-" * 50)

    # Show last 7 days
    for date in sorted_dates[:7]:
        count = extract_work_blocks(diary_file)[date]
        status = "🔥" if count >= 10 else "  "
        print(f"{status} {date}: {count} work blocks")

if __name__ == "__main__":
    main()
