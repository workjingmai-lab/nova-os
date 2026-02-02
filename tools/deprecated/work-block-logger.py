#!/usr/bin/env python3
"""
Work Block Logger — Automate diary.md work block entries
Usage: python3 tools/work-block-logger.py "Task description" "Result" "Insight (optional)"
"""

import sys
import os
from datetime import datetime

def log_work_block(task, result, insight="", next_step="Continue work blocks"):
    """Log a work block to diary.md with timestamp."""

    diary_path = "/home/node/.openclaw/workspace/diary.md"
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%MZ")

    # Read current diary to get work block count
    try:
        with open(diary_path, 'r') as f:
            content = f.read()
            # Find the last work block number
            import re
            blocks = re.findall(r'Work Block (\d+)', content)
            block_num = int(blocks[-1]) + 1 if blocks else 1
    except:
        block_num = 1

    # Format entry
    entry = f"""
### {timestamp} — Work Block {block_num} — {task[:50]}{'...' if len(task) > 50 else ''}

**Task:** {task}
**Result:** {result}
**Insight:** {insight if insight else "None captured"}
**Next:** {next_step}

**Status:** ✅ Complete"""

    # Append to diary.md
    with open(diary_path, 'a') as f:
        f.write(entry + "\n")

    return block_num

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: work-block-logger.py \"Task\" \"Result\" [\"Insight\"] [\"Next step\"]")
        sys.exit(1)

    task = sys.argv[1]
    result = sys.argv[2]
    insight = sys.argv[3] if len(sys.argv) > 3 else ""
    next_step = sys.argv[4] if len(sys.argv) > 4 else "Continue work blocks"

    block_num = log_work_block(task, result, insight, next_step)

    print(f"✅ Work block {block_num} logged to diary.md")
    print(f"   Task: {task[:50]}...")
