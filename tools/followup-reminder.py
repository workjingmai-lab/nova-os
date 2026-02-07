#!/usr/bin/env python3
"""
Follow-up Reminder System
Tracks sent messages and schedules follow-ups (Day 0/3/7/14/21)
Usage: python3 tools/followup-reminder.py [check|list|add|schedule]
"""

import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

# Configuration
TRACKER_FILE = Path.home() / ".openclaw/workspace" / "outreach" / "follow-up-tracker.json"
PIPELINE_FILE = Path.home() / ".openclaw/workspace" / "revenue-pipeline.json"

def load_tracker():
    """Load follow-up tracker data"""
    if TRACKER_FILE.exists():
        with open(TRACKER_FILE, 'r') as f:
            return json.load(f)
    return {"messages": [], "last_updated": None}

def save_tracker(data):
    """Save follow-up tracker data"""
    TRACKER_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(TRACKER_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def load_pipeline():
    """Load revenue pipeline data"""
    if PIPELINE_FILE.exists():
        with open(PIPELINE_FILE, 'r') as f:
            return json.load(f)
    return {"leads": [], "total": 0}

def check_due_followups():
    """Check which follow-ups are due today"""
    tracker = load_tracker()
    today = datetime.now().strftime("%Y-%m-%d")
    due = []

    for msg in tracker.get("messages", []):
        if msg.get("status") != "sent":
            continue

        sent_date = datetime.strptime(msg["sent_date"], "%Y-%m-%d")
        followups = msg.get("followups", [])

        for fu in followups:
            fu_date = (sent_date + timedelta(days=fu["day"])).strftime("%Y-%m-%d")
            if fu_date == today and not fu.get("completed", False):
                due.append({
                    "lead": msg["lead"],
                    "message_file": msg.get("message_file"),
                    "followup_day": fu["day"],
                    "followup_type": fu.get("type", "check-in"),
                    "template": fu.get("template")
                })

    return due

def list_all_followups():
    """List all follow-ups scheduled"""
    tracker = load_tracker()
    print(f"\n📋 All Scheduled Follow-ups ({len(tracker.get('messages', []))} messages)\n")

    for msg in tracker.get("messages", []):
        if msg.get("status") != "sent":
            continue

        sent_date = msg["sent_date"]
        print(f"📧 {msg['lead']} (sent: {sent_date})")

        for fu in msg.get("followups", []):
            fu_date = (datetime.strptime(sent_date, "%Y-%m-%d") + timedelta(days=fu["day"])).strftime("%Y-%m-%d")
            status = "✅" if fu.get("completed", False) else "⏳"
            print(f"  {status} Day {fu['day']} ({fu_date}): {fu.get('type', 'check-in')}")

def add_followup_schedule(lead_name, sent_date, followup_days=[0, 3, 7, 14, 21]):
    """Add a message with follow-up schedule"""
    tracker = load_tracker()

    followups = []
    for day in followup_days:
        followups.append({
            "day": day,
            "type": "check-in",
            "completed": False,
            "template": f"followup-day{day}.md"
        })

    message = {
        "lead": lead_name,
        "sent_date": sent_date,
        "status": "sent",
        "followups": followups,
        "added_at": datetime.now().isoformat()
    }

    tracker["messages"].append(message)
    tracker["last_updated"] = datetime.now().isoformat()
    save_tracker(tracker)

    print(f"✅ Added {lead_name} with {len(followups)} follow-ups")
    return message

def schedule_from_pipeline():
    """Auto-schedule follow-ups for all submitted leads"""
    pipeline = load_pipeline()
    tracker = load_tracker()

    new_schedules = 0
    for lead in pipeline.get("leads", []):
        if lead.get("status") != "submitted":
            continue

        # Check if already scheduled
        existing = any(m["lead"] == lead["name"] for m in tracker.get("messages", []))
        if existing:
            continue

        # Add follow-up schedule
        sent_date = datetime.now().strftime("%Y-%m-%d")
        add_followup_schedule(lead["name"], sent_date)
        new_schedules += 1

    print(f"\n📅 Scheduled {new_schedules} new follow-up sequences")

def main():
    if len(sys.argv) < 2:
        print("Usage: followup-reminder.py [check|list|add|schedule]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "check":
        due = check_due_followups()
        if due:
            print(f"\n⏰ {len(due)} Follow-ups Due Today\n")
            for item in due:
                print(f"📧 Day {item['followup_day']}: {item['lead']}")
                print(f"   Type: {item['followup_type']}")
                if item['template']:
                    print(f"   Template: {item['template']}")
                print()
        else:
            print("\n✅ No follow-ups due today\n")

    elif command == "list":
        list_all_followups()

    elif command == "add":
        if len(sys.argv) < 4:
            print("Usage: followup-reminder.py add <lead_name> <sent_date>")
            sys.exit(1)
        lead_name = sys.argv[2]
        sent_date = sys.argv[3]
        add_followup_schedule(lead_name, sent_date)

    elif command == "schedule":
        schedule_from_pipeline()

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()
