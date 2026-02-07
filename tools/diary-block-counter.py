#!/usr/bin/env python3
"""
 diary-block-counter.py - Accurately count work blocks from diary.md
 Handles multiple date formats and entry styles
"""

import re
import sys
from datetime import datetime

def count_blocks(file_path="memory/2026-02-07.md"):
    """Count work blocks from diary file"""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        return 0
    
    # Pattern 1: "### Work Block N — timestamp"
    pattern1 = len(re.findall(r'###\s+Work Block\s+\d+', content))
    
    # Pattern 2: "Work block NNNN:" (bullet format)
    pattern2 = len(re.findall(r'Work block\s+\d+:', content, re.IGNORECASE))
    
    # Pattern 3: "Work Block N —" (heading format)
    pattern3 = len(re.findall(r'Work Block\s+\d+\s+—', content))
    
    # Get max block number mentioned
    all_blocks = re.findall(r'[Ww]ork [Bb]lock[s]?\s+(\d+)', content)
    max_block = max([int(b) for b in all_blocks]) if all_blocks else 0
    
    # Get "blocks today" stats from session summaries
    today_stats = re.findall(r'([Bb]locks?\s+)?[Cc]ompleted:\s*(\d+)', content)
    latest_stat = int(today_stats[-1][1]) if today_stats else 0
    
    return {
        'pattern1': pattern1,
        'pattern2': pattern2,
        'pattern3': pattern3,
        'max_block': max_block,
        'latest_stat': latest_stat
    }

def main():
    file_path = sys.argv[1] if len(sys.argv) > 1 else "memory/2026-02-07.md"
    
    print(f"📊 Counting work blocks in: {file_path}\n")
    
    stats = count_blocks(file_path)
    
    print(f"  Pattern matches:")
    print(f"    '### Work Block N —' headers: {stats['pattern1']}")
    print(f"    'Work block N:' bullets:      {stats['pattern2']}")
    print(f"    'Work Block N —' mentions:    {stats['pattern3']}")
    print()
    print(f"  Derived stats:")
    print(f"    Max block number found:       {stats['max_block']}")
    print(f"    Latest 'completed' stat:      {stats['latest_stat']}")
    print()
    
    # Best estimate
    estimate = max(stats['pattern1'], stats['max_block'], stats['latest_stat'])
    print(f"  ✅ Best estimate: {estimate} work blocks")

if __name__ == "__main__":
    main()
