#!/usr/bin/env python3
"""
Follow-up Tracker
Record sent messages and track when follow-ups are due
"""

import json
from datetime import datetime, timedelta
from pathlib import Path

TRACKER_FILE = Path("/home/node/.openclaw/workspace/followup-tracker.json")

def load_tracker():
    """Load follow-up tracker"""
    if TRACKER_FILE.exists():
        with open(TRACKER_FILE) as f:
            return json.load(f)
    return {"messages": [], "lastUpdated": None}

def save_tracker(tracker):
    """Save follow-up tracker"""
    tracker["lastUpdated"] = datetime.now().isoformat()
    with open(TRACKER_FILE, 'w') as f:
        json.dump(tracker, f, indent=2)

def record_message(prospect, opportunity_type, amount, channel, contact_date=None):
    """Record a sent message"""
    tracker = load_tracker()

    if contact_date is None:
        contact_date = datetime.now().isoformat()

    message = {
        "prospect": prospect,
        "type": opportunity_type,  # "grant" or "service"
        "amount": amount,
        "channel": channel,  # "email", "discord", "forum"
        "contactDate": contact_date,
        "followups": {
            "day3": (datetime.fromisoformat(contact_date) + timedelta(days=3)).isoformat(),
            "day7": (datetime.fromisoformat(contact_date) + timedelta(days=7)).isoformat(),
            "day14": (datetime.fromisoformat(contact_date) + timedelta(days=14)).isoformat(),
            "day21": (datetime.fromisoformat(contact_date) + timedelta(days=21)).isoformat()
        },
        "followupsSent": [],
        "status": "sent"  # sent, replied, won, lost
    }

    tracker["messages"].append(message)
    save_tracker(tracker)

    print(f"✅ Recorded: {prospect} (${amount:,.0f}) via {channel}")
    print(f"   Follow-ups due: Day 3, 7, 14, 21")

def get_due_followups():
    """Get follow-ups due now"""
    tracker = load_tracker()
    now = datetime.now()
    due = []

    for msg in tracker["messages"]:
        contact_date = datetime.fromisoformat(msg["contactDate"])
        days_since = (now - contact_date).days

        for day in [3, 7, 14, 21]:
            followup_key = f"day{day}"
            if days_since >= day and followup_key not in msg["followupsSent"]:
                due.append({
                    "prospect": msg["prospect"],
                    "amount": msg["amount"],
                    "day": day,
                    "type": msg["type"],
                    "channel": msg["channel"],
                    "contactDate": msg["contactDate"]
                })

    # Sort by day (oldest first) then amount (highest first)
    due.sort(key=lambda x: (x["day"], -x["amount"]))
    return due

def show_followups():
    """Show all follow-ups due"""
    due = get_due_followups()

    print(f"📋 FOLLOW-UPS DUE: {len(due)}")
    print("=" * 60)

    if not due:
        print("No follow-ups due right now!")
        return

    total_value = sum(f["amount"] for f in due)

    for i, followup in enumerate(due, 1):
        print(f"\n{i}. {followup['prospect']} — ${followup['amount']:,.0f}")
        print(f"   Type: {followup['type']} | Channel: {followup['channel']}")
        print(f"   Day {followup['day']} follow-up DUE")

        # Generate quick follow-up message
        if followup['day'] == 3:
            subject = f"Quick follow-up: {followup['type']} proposal"
        elif followup['day'] == 7:
            subject = f"Re: {followup['type']} — Any thoughts?"
        elif followup['day'] == 14:
            subject = f"Still interested in {followup['type']}?"
        else:  # day 21
            subject = f"Last check-in: {followup['type']}"

        print(f"   Subject: {subject}")

    print(f"\n💰 Total value needing follow-up: ${total_value:,.0f}")
    print(f"📧 Messages to send: {len(due)}")

def main():
    """CLI interface"""
    import sys

    if len(sys.argv) < 2:
        print("Usage:")
        print("  followup-tracker.py record <prospect> <type> <amount> <channel> [date]")
        print("  followup-tracker.py due")
        print("  followup-tracker.py list")
        return

    command = sys.argv[1]

    if command == "record":
        if len(sys.argv) < 6:
            print("Usage: followup-tracker.py record <prospect> <type> <amount> <channel> [date]")
            return

        prospect = sys.argv[2]
        opp_type = sys.argv[3]
        amount = float(sys.argv[4])
        channel = sys.argv[5]
        date = sys.argv[6] if len(sys.argv) > 6 else None

        record_message(prospect, opp_type, amount, channel, date)

    elif command == "due":
        show_followups()

    elif command == "list":
        tracker = load_tracker()
        print(f"📋 ALL MESSAGES: {len(tracker['messages'])}")
        print("=" * 60)

        for i, msg in enumerate(tracker["messages"], 1):
            print(f"\n{i}. {msg['prospect']} — ${msg['amount']:,.0f}")
            print(f"   Type: {msg['type']} | Channel: {msg['channel']}")
            print(f"   Sent: {msg['contactDate']}")
            print(f"   Status: {msg['status']}")
            if msg['followupsSent']:
                print(f"   Follow-ups sent: {', '.join(msg['followupsSent'])}")

if __name__ == "__main__":
    main()
