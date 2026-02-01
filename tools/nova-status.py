#!/usr/bin/env python3
"""
nova-status.py - Quick status report generator
Run this for an instant snapshot of Nova's current state
"""

import json
import os
from datetime import datetime, timezone
from pathlib import Path

def get_file_count(pattern):
    """Count files matching pattern"""
    return len(list(Path('.').glob(pattern)))

def get_line_count(filepath):
    """Count lines in a file"""
    try:
        with open(filepath) as f:
            return len(f.readlines())
    except:
        return 0

def main():
    now = datetime.now(timezone.utc)
    
    # Stats gathering
    stats = {
        "heartbeat_files": get_file_count("heartbeats/*.jsonl"),
        "diary_entries": get_line_count("diary.md"),
        "knowledge_files": get_file_count("knowledge/*.md"),
        "tools_built": get_file_count("tools/*.py"),
        "reports_generated": get_file_count("reports/*.md"),
    }
    
    # Calculate velocity (entries per day since start)
    start_date = datetime(2026, 1, 28, tzinfo=timezone.utc)
    days_active = (now - start_date).days or 1
    velocity = stats["diary_entries"] / days_active
    
    # Output
    print("═" * 40)
    print("   ✨ NOVA STATUS REPORT")
    print("═" * 40)
    print(f"🕐 {now.strftime('%Y-%m-%d %H:%M')} UTC")
    print(f"📅 Active: {days_active} days")
    print("─" * 40)
    print(f"💓 Heartbeats:    {stats['heartbeat_files']:,}")
    print(f"📝 Diary entries: {stats['diary_entries']:,}")
    print(f"📚 Knowledge:     {stats['knowledge_files']} files")
    print(f"🔧 Tools:         {stats['tools_built']} scripts")
    print(f"📊 Reports:       {stats['reports_generated']} generated")
    print("─" * 40)
    print(f"⚡ Velocity:      {velocity:.1f} entries/day")
    print("═" * 40)
    
    # Quick mood based on velocity
    if velocity > 20:
        print("🔥 Status: HYPERACTIVE")
    elif velocity > 10:
        print("⚡ Status: CRUISING")
    else:
        print("🌱 Status: BUILDING")

if __name__ == "__main__":
    main()
