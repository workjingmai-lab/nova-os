#!/usr/bin/env python3
"""
Today.md Context Monitor
Checks today.md work block count and warns if approaching bloat threshold
Helps prevent context injection bloat before it becomes critical
"""

import re
from pathlib import Path

TODAY_PATH = "/home/node/.openclaw/workspace/today.md"
WARNING_THRESHOLD = 50  # Warn at 50 work blocks
CRITICAL_THRESHOLD = 70  # Critical alert at 70 work blocks

def count_work_blocks():
    """Count number of work blocks in today.md"""
    try:
        with open(TODAY_PATH, 'r') as f:
            content = f.read()
        
        # Count work block entries
        work_blocks = re.findall(r'- Work block \d+:', content)
        return len(work_blocks)
    except FileNotFoundError:
        return 0

def get_file_size_kb():
    """Get today.md file size in KB"""
    try:
        size = Path(TODAY_PATH).stat().st_size
        return round(size / 1024, 1)
    except FileNotFoundError:
        return 0

def main():
    count = count_work_blocks()
    size_kb = get_file_size_kb()
    
    if count >= CRITICAL_THRESHOLD:
        print(f"🚨 CRITICAL: {count} work blocks ({size_kb}KB)")
        print(f"→ Run: python3 tools/trim-today.py 10")
        print(f"→ Context bloat is SEVERE")
    elif count >= WARNING_THRESHOLD:
        print(f"⚠️  WARNING: {count} work blocks ({size_kb}KB)")
        print(f"→ Consider running: python3 tools/trim-today.py 10")
        print(f"→ Context growing large")
    else:
        print(f"✅ {count} work blocks ({size_kb}KB) - healthy")
        print(f"→ Optimal: < {WARNING_THRESHOLD} blocks")
        print(f"→ Warning at: {WARNING_THRESHOLD}+")
        print(f"→ Critical at: {CRITICAL_THRESHOLD}+")

if __name__ == "__main__":
    main()
