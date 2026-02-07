#!/usr/bin/env python3
"""
work-block-counter.py — Quick work block stats

Shows today's blocks, total blocks, and rate.
"""

import re
import os
from datetime import datetime

def count_blocks_today():
    """Count work blocks in today's diary."""
    today_file = f"memory/{datetime.now().strftime('%Y-%m-%d')}.md"
    
    if not os.path.exists(today_file):
        return 0
    
    with open(today_file, 'r') as f:
        content = f.read()
    
    # Count "Work Block N" patterns
    pattern = r'Work Block (\d+)'
    matches = re.findall(pattern, content)
    
    if matches:
        return max(int(m) for m in matches)
    return 0

def count_total_blocks():
    """Estimate total blocks from all diary files."""
    memory_dir = "memory"
    total = 0
    
    if not os.path.exists(memory_dir):
        return 0
    
    for filename in os.listdir(memory_dir):
        if filename.endswith('.md') and filename[0:4].isdigit():
            filepath = os.path.join(memory_dir, filename)
            with open(filepath, 'r') as f:
                content = f.read()
            
            # Count work block mentions
            pattern = r'Work Block (\d+)'
            matches = re.findall(pattern, content)
            if matches:
                total += len(set(matches))  # Unique block numbers per file
    
    return total

def main():
    today = count_blocks_today()
    total = count_total_blocks()
    
    # Calculate rate (assuming 16 hours of active time)
    hour = datetime.now().hour
    active_hours = max(1, hour - 8)  # Assume 8am start
    rate = today / active_hours if active_hours > 0 else 0
    
    print("=" * 40)
    print("⚡ WORK BLOCK COUNTER")
    print("=" * 40)
    print(f"Today:     {today} blocks")
    print(f"Rate:      {rate:.1f} blocks/hour")
    print(f"Total:     ~{total} blocks")
    print("=" * 40)
    
    # Target check
    target = 300
    remaining = max(0, target - today)
    if remaining > 0:
        print(f"📊 Target:  {today}/{target} ({remaining} to go)")
    else:
        print(f"📊 Target:  {today}/{target} ✓ EXCEEDED")
    print("=" * 40)

if __name__ == "__main__":
    main()
