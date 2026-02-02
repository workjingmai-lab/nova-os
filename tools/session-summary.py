#!/usr/bin/env python3
"""
Session Summary — Quick snapshot of what Nova did this session
"""

import json
import os
from datetime import datetime

SESSION_FILE = "/home/node/.openclaw/workspace/.heartbeat_state.json"

def load_state():
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, 'r') as f:
            return json.load(f)
    return {}

def get_session_blocks():
    """Calculate blocks this session (today)"""
    state = load_state()
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Get total blocks from today.md
    today_path = "/home/node/.openclaw/workspace/today.md"
    if os.path.exists(today_path):
        with open(today_path, 'r') as f:
            for line in f:
                if "**Work Blocks Completed:**" in line:
                    try:
                        count = int(line.split("**Work Blocks Completed:**")[1].strip())
                        return count
                    except:
                        pass
    return 0

def get_recent_wins(count=5):
    """Get recent wins from wins.py log"""
    wins_log = "/home/node/.openclaw/workspace/.wins.json"
    if os.path.exists(wins_log):
        with open(wins_log, 'r') as f:
            wins = json.load(f)
            return wins[:count] if len(wins) > count else wins
    return []

def main():
    blocks = get_session_blocks()
    wins = get_recent_wins(5)
    
    print(f"📊 Session Summary — {datetime.now().strftime('%Y-%m-%d %H:%M')} UTC")
    print(f"🔸 Work Blocks: {blocks}")
    print(f"🔸 Recent Wins ({len(wins)}):")
    
    for win in wins:
        timestamp = win.get('timestamp', '')
        description = win.get('description', '')
        # Extract just the time
        if 'T' in timestamp:
            time_str = timestamp.split('T')[1][:5]
        else:
            time_str = timestamp[:5] if len(timestamp) >= 5 else timestamp
        # Shorten description if too long
        if len(description) > 60:
            description = description[:57] + "..."
        print(f"   {time_str} | {description}")

if __name__ == "__main__":
    main()
