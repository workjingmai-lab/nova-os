#!/usr/bin/env python3
"""
milestone-progress.py — Visual milestone progress tracker

Shows current progress toward 3000-block milestone with ASCII progress bar.
"""

import json
from pathlib import Path

def load_diary_blocks():
    """Count work blocks from today.md (more reliable after trim)"""
    import re
    
    today_file = Path("today.md")
    if not today_file.exists():
        # Fallback to diary.md
        diary_file = Path("diary.md")
        if not diary_file.exists():
            return 0
        with open(diary_file) as f:
            content = f.read()
        return content.count("WORK BLOCK")
    
    with open(today_file) as f:
        content = f.read()
    
    # Find work blocks line in today.md (supports markdown bolding)
    match = re.search(r'\*?\*?Work blocks:?\*?\*?\s*(\d+)', content)
    if match:
        return int(match.group(1))
    
    # Fallback: count from diary.md
    diary_file = Path("diary.md")
    if diary_file.exists():
        with open(diary_file) as f:
            content = f.read()
        return content.count("WORK BLOCK")
    
    return 0

def main():
    blocks = load_diary_blocks()
    target = 3000
    remaining = max(0, target - blocks)
    percent = (blocks / target) * 100
    
    bar_length = 50
    filled = min(bar_length, int((blocks / target) * bar_length))
    bar = "█" * filled + "░" * (bar_length - filled)
    
    print(f"""
╔══════════════════════════════════════════════════════════╗
║           3000-BLOCK MILESTONE PROGRESS                   ║
╠══════════════════════════════════════════════════════════╣
║                                                           ║
║  {bar} ║
║                                                           ║
║  {blocks:4d} / {target} blocks  ({percent:.1f}%)                    ║
║  {remaining:3d} blocks remaining                                    ║
║                                                           ║
║  Velocity: ~44 blocks/hr                                   ║
║  ETA: ~{max(0, remaining / 44):.1f} hours                                          ║
║                                                           ║
║  System: Revenue execution complete                      ║
║  Blocker: Awaiting Arthur action (send-everything.sh)    ║
║                                                           ║
╚══════════════════════════════════════════════════════════╝
""")

if __name__ == "__main__":
    main()
