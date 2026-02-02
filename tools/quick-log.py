#!/usr/bin/env python3
"""
Quick Log — Fast diary entry tool
Add work block entries to diary.md instantly
"""

import sys
from pathlib import Path
from datetime import datetime

def add_entry(task, status="✅", time_seconds=None):
    """Add a work block entry to diary.md"""
    diary_path = Path("diary.md")

    # Get next block number (read latest)
    if diary_path.exists():
        content = diary_path.read_text()
        # Find last work block number
        import re
        blocks = re.findall(r'WORK BLOCK (\d+)', content)
        next_block = int(blocks[-1]) + 1 if blocks else 1
    else:
        next_block = 1

    # Generate timestamp
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%MZ")

    # Build entry
    entry = f"""

## [WORK BLOCK {next_block} — {timestamp}] ⚡ WORK BLOCK: {task}

**Status:** {status}
**Time:** {time_seconds or 'N/A'} seconds
**Result:** Entry logged via quick-log.py

---
"""

    # Append to diary
    with open(diary_path, 'a') as f:
        f.write(entry)

    print(f"✅ Added work block #{next_block} to diary.md")
    return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 tools/quick-log.py \"Task description\" [✅|⚠️] [time_seconds]")
        sys.exit(1)

    task = sys.argv[1]
    status = sys.argv[2] if len(sys.argv) > 2 else "✅"
    time = sys.argv[3] if len(sys.argv) > 3 else None

    sys.exit(add_entry(task, status, time))
