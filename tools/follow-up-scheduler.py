#!/usr/bin/env python3
"""
Follow-Up Scheduler — Track and remind about follow-ups

Usage:
    python3 tools/follow-up-scheduler.py add           # Add new follow-up
    python3 tools/follow-up-scheduler.py list          # List all follow-ups
    python3 tools/follow-up-scheduler.py due           # Show due follow-ups
    python3 tools/follow-up-scheduler.py complete ID   # Mark as complete
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path

SCHEDULER_FILE = "/home/node/.openclaw/workspace/follow-ups.json"

def load_followups():
    """Load follow-up data"""
    if os.path.exists(SCHEDULER_FILE):
        with open(SCHEDULER_FILE, 'r') as f:
            return json.load(f)
    return {
        "created": datetime.now().isoformat(),
        "lastUpdated": datetime.now().isoformat(),
        "followups": []
    }

def save_followups(data):
    """Save follow-up data"""
    data["lastUpdated"] = datetime.now().isoformat()
    with open(SCHEDULER_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def add_followup(target, days, stage="response", notes=""):
    """Add a new follow-up"""
    data = load_followups()

    followup = {
        "id": len(data["followups"]) + 1,
        "target": target,
        "stage": stage,
        "days": days,
        "dueDate": (datetime.now() + timedelta(days=days)).isoformat(),
        "notes": notes,
        "status": "pending",
        "created": datetime.now().isoformat()
    }

    data["followups"].append(followup)
    save_followups(data)

    return followup

def list_followups():
    """List all follow-ups"""
    data = load_followups()
    followups = data["followups"]

    if not followups:
        print("\n📭 No follow-ups scheduled")
        return

    print(f"\n📋 All Follow-Ups ({len(followups)} total)")
    print("=" * 60)

    now = datetime.now()

    for fu in sorted(followups, key=lambda x: x["dueDate"]):
        due = datetime.fromisoformat(fu["dueDate"])
        days_until = (due - now).days

        # Status emoji
        if fu["status"] == "complete":
            status = "✅"
        elif days_until < 0:
            status = "🔴 OVERDUE"
        elif days_until == 0:
            status = "⚠️ DUE TODAY"
        elif days_until <= 2:
            status = "🟡 Due soon"
        else:
            status = "⏳"

        print(f"\n{status} ID {fu['id']}: {fu['target']}")
        print(f"   Stage: {fu['stage']}")
        print(f"   Due: {due.strftime('%Y-%m-%d')} ({days_until} days)")
        if fu.get("notes"):
            print(f"   Notes: {fu['notes']}")

def show_due():
    """Show due follow-ups"""
    data = load_followups()
    followups = data["followups"]

    now = datetime.now()
    due_followups = []

    for fu in followups:
        if fu["status"] != "complete":
            due = datetime.fromisoformat(fu["dueDate"])
            days_until = (due - now).days

            if days_until <= 1:  # Due today or overdue
                due_followups.append((fu, days_until))

    if not due_followups:
        print("\n✅ No follow-ups due today")
        return

    print(f"\n⚠️ Due Follow-Ups ({len(due_followups)} need attention)")
    print("=" * 60)

    for fu, days_until in sorted(due_followups, key=lambda x: x[1]):
        due = datetime.fromisoformat(fu["dueDate"])

        if days_until < 0:
            print(f"\n🔴 OVERDUE: {fu['target']} (overdue by {-days_until} days)")
        else:
            print(f"\n⚠️ DUE TODAY: {fu['target']}")

        print(f"   Stage: {fu['stage']}")
        print(f"   Notes: {fu.get('notes', 'No notes')}")
        print(f"   Mark complete: python3 tools/follow-up-scheduler.py complete {fu['id']}")

def complete_followup(id):
    """Mark follow-up as complete"""
    data = load_followups()

    for fu in data["followups"]:
        if fu["id"] == id:
            fu["status"] = "complete"
            fu["completedAt"] = datetime.now().isoformat()
            save_followups(data)
            print(f"\n✅ Follow-up {id} marked complete: {fu['target']}")
            return

    print(f"\n❌ Follow-up {id} not found")

def main():
    import sys

    if len(sys.argv) < 2:
        list_followups()
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 4:
            print("Usage: follow-up-scheduler.py add <target> <days> [stage] [notes]")
            return

        target = sys.argv[2]
        days = int(sys.argv[3])
        stage = sys.argv[4] if len(sys.argv) > 4 else "response"
        notes = sys.argv[5] if len(sys.argv) > 5 else ""

        fu = add_followup(target, days, stage, notes)
        print(f"\n✅ Follow-up scheduled: {target} in {days} days (ID: {fu['id']})")

    elif command == "list":
        list_followups()

    elif command == "due":
        show_due()

    elif command == "complete":
        if len(sys.argv) < 3:
            print("Usage: follow-up-scheduler.py complete <id>")
            return

        complete_followup(int(sys.argv[2]))

    else:
        print(f"Unknown command: {command}")
        print("Usage: follow-up-scheduler.py [add|list|due|complete]")

if __name__ == "__main__":
    main()
