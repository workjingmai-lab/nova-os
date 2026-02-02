#!/usr/bin/env python3
"""
Wins Tracker - Log and review accomplishments

Usage:
    python3 tools/wins.py add "Description"           # Add a win
    python3 tools/wins.py list                        # List all wins
    python3 tools/wins.py today                       # Today's wins
    python3 tools/wins.py recent                      # Last 10 wins
"""

import json
from datetime import datetime, date
from pathlib import Path

WINS_FILE = Path("/home/node/.openclaw/workspace/.wins.json")

def load_wins():
    """Load wins from file"""
    if WINS_FILE.exists():
        try:
            return json.loads(WINS_FILE.read_text())
        except:
            return []
    return []

def save_wins(wins):
    """Save wins to file"""
    WINS_FILE.write_text(json.dumps(wins, indent=2))

def add_win(description):
    """Add a new win"""
    wins = load_wins()
    win = {
        "description": description,
        "timestamp": datetime.now().isoformat(),
        "date": date.today().isoformat()
    }
    wins.insert(0, win)  # Add to beginning
    save_wins(wins)
    print(f"✓ Win logged: {description}")

def list_wins(wins, limit=None):
    """List wins"""
    if not wins:
        print("No wins logged yet.")
        return

    display_wins = wins[:limit] if limit else wins

    print(f"🏆 Wins Log ({len(display_wins)} shown)")
    print()

    for win in display_wins:
        dt = datetime.fromisoformat(win['timestamp'])
        time_str = dt.strftime('%Y-%m-%d %H:%M')
        print(f"{time_str} | {win['description']}")

def todays_wins():
    """Get today's wins"""
    wins = load_wins()
    today = date.today().isoformat()
    todays = [w for w in wins if w['date'] == today]
    list_wins(todays)

def recent_wins():
    """Get recent wins (last 10)"""
    wins = load_wins()
    list_wins(wins, limit=10)

def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: wins.py [add|list|today|recent] [description]")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: wins.py add 'Description of win'")
            return
        add_win(' '.join(sys.argv[2:]))

    elif command == "list":
        list_wins(load_wins())

    elif command == "today":
        todays_wins()

    elif command == "recent":
        recent_wins()

    else:
        print(f"Unknown command: {command}")
        print("Available: add, list, today, recent")

if __name__ == "__main__":
    main()
