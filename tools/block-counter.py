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

    # Count work blocks (multiple formats supported)
    # Format 1: ## [WORK BLOCK NNN — date]
    # Format 2: ### Work Block NNNN: description
    patterns = [
        r'\[WORK BLOCK (\d+)',  # Old format
        r'### Work Block (\d+):',  # New format
    ]

    blocks = []
    for pattern in patterns:
        found = re.findall(pattern, content)
        blocks.extend(found)

    if not blocks:
        print("📊 No work blocks found in diary.md")
        return 0

    # Get latest block number (max of all found)
    latest_block = max(int(b) for b in blocks) if blocks else 0
    total_blocks = len(set(blocks))  # Unique blocks only

    # Count blocks today by finding blocks under current date header
    today = datetime.utcnow().strftime("%Y-%m-%d")
    date_header_pattern = rf'## {today}'

    # Find today's section
    today_section = ""
    if re.search(date_header_pattern, content):
        # Split by date headers and find today's section
        sections = re.split(r'## \d{4}-\d{2}-\d{2}', content)
        # Find the section that comes after today's date header
        date_headers = re.findall(r'## (\d{4}-\d{2}-\d{2})', content)
        for i, date in enumerate(date_headers):
            if date == today and i + 1 < len(sections):
                today_section = sections[i + 1]
                break

    # Count blocks in today's section
    today_count = 0
    if today_section:
        for pattern in patterns:
            found = re.findall(pattern, today_section)
            today_count += len(found)

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
