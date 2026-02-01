#!/usr/bin/env python3
"""
Nova's Velocity Checker
Quick count of tasks completed today from diary.md
"""
import re
from datetime import datetime

def count_tasks_today(diary_path="/home/node/.openclaw/workspace/diary.md"):
    """Count tasks with today's date"""
    try:
        with open(diary_path, 'r') as f:
            content = f.read()
        
        today = datetime.now().strftime("%Y-%m-%d")
        pattern = rf'{today}.*?✅|{today}.*?Done|{today}.*?Completed'
        
        matches = re.findall(pattern, content, re.IGNORECASE)
        return len(matches)
    except Exception as e:
        return 0

if __name__ == "__main__":
    count = count_tasks_today()
    print(f"🚀 Tasks completed today: {count}")
