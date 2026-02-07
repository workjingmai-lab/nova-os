#!/usr/bin/env python3
"""
follow-up-reminder.py — Check for due follow-ups and send reminders

Scans follow-up-tracker.json for messages due for follow-up.
Outputs reminder checklist with urgency indicators.

Usage:
    python3 tools/follow-up-reminder.py              # All due follow-ups
    python3 tools/follow-up-reminder.py --urgent     # Only overdue
    python3 tools/follow-up-reminder.py --today      # Due today/overdue
"""

import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

# Configuration
TRACKER_FILE = Path.home() / ".openclaw/workspace/outreach/follow-up-tracker.json"
NOW = datetime.now()

def load_tracker():
    """Load follow-up tracker data."""
    if not TRACKER_FILE.exists():
        return {"messages": [], "last_updated": None}
    with open(TRACKER_FILE, "r") as f:
        return json.load(f)

def calculate_urgency(follow_up_date):
    """Calculate urgency indicator."""
    if not follow_up_date:
        return "UNKNOWN", "gray"

    try:
        follow_up = datetime.fromisoformat(follow_up_date)
        delta = (follow_up - NOW).days

        if delta < 0:
            return "OVERDUE", "🔴"
        elif delta == 0:
            return "TODAY", "🟡"
        elif delta <= 2:
            return "SOON", "🟢"
        else:
            return "UPCOMING", "⚪"
    except:
        return "UNKNOWN", "gray"

def format_reminder(msg, urgency, icon):
    """Format reminder line."""
    due = msg.get("next_follow_up", "UNKNOWN")
    message_id = msg.get("message_id", "unknown")
    target = msg.get("target", "unknown")

    return f"{icon} {urgency:8} | {due} | {message_id} → {target}"

def main():
    tracker = load_tracker()
    messages = tracker.get("messages", [])

    if not messages:
        print("✅ No tracked messages requiring follow-up")
        return 0

    # Parse filters
    filter_urgent = "--urgent" in sys.argv
    filter_today = "--today" in sys.argv

    # Filter and categorize
    overdue = []
    today = []
    soon = []
    upcoming = []

    for msg in messages:
        follow_up = msg.get("next_follow_up")
        urgency, icon = calculate_urgency(follow_up)

        item = (msg, urgency, icon)

        if urgency == "OVERDUE":
            overdue.append(item)
        elif urgency == "TODAY":
            today.append(item)
        elif urgency == "SOON":
            soon.append(item)
        else:
            upcoming.append(item)

    # Apply filters
    if filter_urgent:
        display_items = overdue
        header = "🔴 OVERDUE Follow-Ups"
    elif filter_today:
        display_items = overdue + today
        header = "🔴 OVERDUE + 🟡 TODAY Follow-Ups"
    else:
        display_items = overdue + today + soon
        header = "Follow-Up Reminder Checklist"

    # Output
    print(f"\n{header}")
    print("=" * 60)

    if not display_items:
        print("✅ No matching follow-ups")
        return 0

    for msg, urgency, icon in display_items:
        print(format_reminder(msg, urgency, icon))

    print("\n" + "=" * 60)
    print(f"Total: {len(display_items)} follow-ups due")
    print(f"\nCommands:")
    print(f"  python3 tools/follow-up-tracker.py export    # Full checklist")
    print(f"  python3 tools/follow-up-tracker.py complete <id>  # Mark done")

    return 0

if __name__ == "__main__":
    sys.exit(main())
