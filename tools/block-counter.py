#!/usr/bin/env python3
"""
Block Counter — Quick work block statistics
Counts work blocks in diary.md for instant metrics
"""

import re
import sys
from pathlib import Path
from datetime import datetime

def count_blocks(diary_path="diary.md"):
    """Count work blocks and generate stats"""
    path = Path(diary_path)

    if not path.exists():
        print(f"❌ Diary not found: {diary_path}")
        return 1

    content = path.read_text()

    # Count work blocks (format: ## [WORK BLOCK NNN — date])
    block_pattern = r'\[WORK BLOCK (\d+)'
    blocks = re.findall(block_pattern, content)

    if not blocks:
        print("📊 No work blocks found in diary.md")
        return 0

    # Get latest block number
    latest_block = int(blocks[-1])
    total_blocks = len(blocks)

    # Estimate blocks today (parse dates from recent blocks)
    date_pattern = r'\[WORK BLOCK \d+ — ([\d\-T:Z]+)'
    dates = re.findall(date_pattern, content)

    today_count = 0
    if dates:
        today = datetime.utcnow().strftime("%Y-%m-%d")
        today_count = sum(1 for d in dates if d.startswith(today))

    print(f"📊 Work Block Statistics")
    print(f"═" * 40)
    print(f"  Total blocks:  {latest_block}")
    print(f"  Blocks today:  {today_count}")
    print(f"  Diary size:     {len(content):,} characters")
    print(f"  Avg per block:  {len(content) // latest_block:,} chars")

    if today_count >= 10:
        print(f"\n🔥 Streak alive! {today_count} blocks today")

    return 0

if __name__ == "__main__":
    diary_file = sys.argv[1] if len(sys.argv) > 1 else "diary.md"
    sys.exit(count_blocks(diary_file))
