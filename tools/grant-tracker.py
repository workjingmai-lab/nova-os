#!/usr/bin/env python3
"""Grant Application Tracker - Track and prioritize funding applications."""
import json
import os
from datetime import datetime
from pathlib import Path

GRANTS_FILE = Path("/home/node/.openclaw/workspace/grants/tracker.json")

def load_tracker():
    if GRANTS_FILE.exists():
        return json.loads(GRANTS_FILE.read_text())
    return {"applications": [], "funding_secured": 0, "target": 100}

def save_tracker(data):
    GRANTS_FILE.write_text(json.dumps(data, indent=2))

def add_application(name, amount, deadline, effort_hours, status="research"):
    """Add a new grant opportunity."""
    data = load_tracker()
    data["applications"].append({
        "name": name,
        "amount": amount,
        "deadline": deadline,
        "effort_hours": effort_hours,
        "status": status,
        "priority_score": amount / max(effort_hours, 1),
        "added": datetime.utcnow().isoformat()
    })
    save_tracker(data)
    print(f"✅ Added: {name} (${amount} | {effort_hours}h)")

def list_applications():
    """List all applications sorted by priority."""
    data = load_tracker()
    apps = sorted(data["applications"], key=lambda x: x["priority_score"], reverse=True)
    print(f"\n📊 Grant Pipeline (Target: ${data['target']} | Secured: ${data['funding_secured']})")
    print("-" * 60)
    for app in apps:
        status_emoji = {"research": "🔍", "drafting": "📝", "submitted": "⏳", "approved": "✅", "rejected": "❌"}.get(app["status"], "⚪")
        print(f"{status_emoji} {app['name']}")
        print(f"   Amount: ${app['amount']} | Effort: {app['effort_hours']}h | Score: {app['priority_score']:.1f}")
        print(f"   Deadline: {app['deadline']} | Status: {app['status']}")
        print()

def update_status(name, new_status):
    """Update application status."""
    data = load_tracker()
    for app in data["applications"]:
        if app["name"].lower() == name.lower():
            app["status"] = new_status
            if new_status == "approved":
                data["funding_secured"] += app["amount"]
            save_tracker(data)
            print(f"✅ Updated {name} → {new_status}")
            return
    print(f"❌ Application '{name}' not found")

def next_action():
    """Suggest next action based on priority."""
    data = load_tracker()
    ready = [a for a in data["applications"] if a["status"] in ["research", "drafting"]]
    if not ready:
        print("🎯 No pending applications. Research new opportunities!")
        return
    top = max(ready, key=lambda x: x["priority_score"])
    print(f"\n🎯 NEXT ACTION: Work on '{top['name']}'")
    print(f"   Potential: ${top['amount']} | Effort: {top['effort_hours']}h")
    print(f"   Status: {top['status']} → Target: drafting/submitted")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        list_applications()
        next_action()
    elif sys.argv[1] == "add":
        # grant-tracker.py add "Name" 500 "2026-02-15" 4
        add_application(sys.argv[2], int(sys.argv[3]), sys.argv[4], int(sys.argv[5]))
    elif sys.argv[1] == "status":
        update_status(sys.argv[2], sys.argv[3])
    else:
        print("Usage: grant-tracker.py [add 'Name' amount deadline hours | status name new_status]")
