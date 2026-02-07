#!/usr/bin/env python3
"""
session-velocity.py — Today's work block velocity and stats
"""

import re
from datetime import datetime
from pathlib import Path

def main():
    today_file = Path("memory/2026-02-07.md")
    
    if not today_file.exists():
        print("No session file found")
        return
    
    content = today_file.read_text()
    
    # Count work blocks
    blocks = re.findall(r'Work Block (\d+)', content)
    if not blocks:
        print("No work blocks found")
        return
    
    first_block = int(blocks[0])
    last_block = int(blocks[-1])
    total_blocks = len(blocks)
    block_range = last_block - first_block + 1
    
    # Find timestamps
    times = re.findall(r'\*\*Time:\*\* (\d{2}:\d{2})', content)
    
    print("=" * 45)
    print("📊 SESSION VELOCITY — 2026-02-07")
    print("=" * 45)
    
    print(f"\n🎯 BLOCKS:")
    print(f"  First block: #{first_block}")
    print(f"  Last block:  #{last_block}")
    print(f"  Today count: {total_blocks}")
    
    if len(times) >= 2:
        print(f"\n⏱️ TIME:")
        print(f"  Start: {times[0]}")
        print(f"  End:   {times[-1]}")
        
        # Parse times
        fmt = "%H:%M"
        try:
            t1 = datetime.strptime(times[0], fmt)
            t2 = datetime.strptime(times[-1], fmt)
            duration = (t2 - t1).total_seconds() / 3600
            
            if duration > 0:
                velocity = total_blocks / duration
                print(f"  Duration: {duration:.1f} hours")
                print(f"  Velocity: {velocity:.1f} blocks/hour")
        except:
            pass
    
    # Count files created
    files_created = len(re.findall(r'\*\*File:\*\*', content))
    tools_created = len(re.findall(r'Tool Created:', content))
    
    print(f"\n📁 OUTPUT:")
    print(f"  Files created: {files_created}")
    print(f"  Tools created: {tools_created}")
    
    print("\n" + "=" * 45)
    print(f"Status: {total_blocks} blocks | {velocity:.0f}/hr" if 'velocity' in dir() else f"Status: {total_blocks} blocks")
    print("=" * 45)

if __name__ == "__main__":
    main()
