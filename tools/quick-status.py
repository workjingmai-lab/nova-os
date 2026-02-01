#!/usr/bin/env python3
"""Quick 24h activity summary from diary.md"""
import re
from datetime import datetime, timedelta
import sys

def last_24h_summary():
    try:
        with open('diary.md', 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print("No diary.md found")
        return
    
    # Find all timestamps in last 24h
    now = datetime.now()
    cutoff = now - timedelta(hours=24)
    
    # Extract entries with dates
    pattern = r'\[([^\]]+)\]\s*\*\*([^*]+)\*\*'
    matches = re.findall(pattern, content)
    
    recent = []
    for ts, activity in matches[-20:]:  # Last 20 entries
        try:
            dt = datetime.strptime(ts.split()[0] + ' ' + ts.split()[1][:5], '%Y-%m-%d %H:%M')
            if dt > cutoff:
                recent.append((ts, activity.strip()))
        except:
            pass
    
    print(f"📊 Last 24h Activity ({len(recent)} entries)")
    print("=" * 40)
    for ts, act in recent[-5:]:
        print(f"• {act[:50]}{'...' if len(act) > 50 else ''}")
    print("=" * 40)

if __name__ == '__main__':
    last_24h_summary()
