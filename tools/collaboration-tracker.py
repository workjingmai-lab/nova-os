#!/usr/bin/env python3
"""
Collaboration Tracker — Track collaboration messages and responses
Part of Nova's workspace toolkit
"""

import json
import os
from datetime import datetime
from pathlib import Path

COLLAB_FILE = Path("data/collaborations.json")

def ensure_collab_file():
    """Ensure collaborations file exists."""
    COLLAB_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not COLLAB_FILE.exists():
        COLLAB_FILE.write_text(json.dumps({"collaborations": []}, indent=2))

def load_collabs():
    """Load collaborations from file."""
    ensure_collab_file()
    return json.loads(COLLAB_FILE.read_text())

def save_collabs(data):
    """Save collaborations to file."""
    COLLAB_FILE.write_text(json.dumps(data, indent=2))

def log_contact(target, platform, status="sent", notes=""):
    """Log a collaboration contact."""
    data = load_collabs()
    collab = {
        "target": target,
        "platform": platform,
        "status": status,
        "timestamp": datetime.now().isoformat(),
        "notes": notes
    }
    data["collaborations"].append(collab)
    save_collabs(data)
    print(f"✅ Logged: {target} ({platform}) — {status}")

def update_status(target, new_status, notes=""):
    """Update status of a collaboration."""
    data = load_collabs()
    for collab in data["collaborations"]:
        if collab["target"] == target:
            collab["status"] = new_status
            collab["updated"] = datetime.now().isoformat()
            if notes:
                collab["notes"] = f"{collab.get('notes', '')}\n{notes}"
            save_collabs(data)
            print(f"✅ Updated: {target} → {new_status}")
            return
    print(f"❌ Not found: {target}")

def show_status():
    """Show collaboration pipeline status."""
    data = load_collabs()
    collabs = data["collaborations"]
    
    if not collabs:
        print("📭 No collaborations tracked yet.")
        return
    
    # Count by status
    sent = sum(1 for c in collabs if c["status"] == "sent")
    responded = sum(1 for c in collabs if c["status"] == "responded")
    collaborating = sum(1 for c in collabs if c["status"] == "collaborating")
    declined = sum(1 for c in collabs if c["status"] == "declined")
    
    print("📊 Collaboration Pipeline")
    print("=" * 40)
    print(f"  Sent: {sent}")
    print(f"  Responded: {responded}")
    print(f"  Collaborating: {collaborating}")
    print(f"  Declined: {declined}")
    print(f"  Total: {len(collabs)}")
    print("=" * 40)
    
    # Show recent
    print("\n📋 Recent Collaborations:")
    for collab in collabs[-5:]:  # Last 5
        status_emoji = {
            "sent": "📤",
            "responded": "💬",
            "collaborating": "🤝",
            "declined": "❌"
        }.get(collab["status"], "❓")
        
        print(f"  {status_emoji} {collab['target']} ({collab['platform']}) — {collab['status']}")
        if collab.get('notes'):
            print(f"     Note: {collab['notes'][:60]}...")
    print()

def list_pending():
    """List pending follow-ups."""
    data = load_collabs()
    pending = [c for c in data["collaborations"] if c["status"] == "sent"]
    
    if not pending:
        print("✅ No pending follow-ups.")
        return
    
    print(f"📤 Pending Follow-Ups ({len(pending)}):")
    for collab in pending:
        # Calculate days since sent
        sent_time = datetime.fromisoformat(collab["timestamp"])
        days_ago = (datetime.now() - sent_time).days
        
        urgency = "🔴" if days_ago >= 7 else "🟡" if days_ago >= 3 else "🟢"
        
        print(f"  {urgency} {collab['target']} — {days_ago} days ago")
        if collab.get('notes'):
            print(f"     {collab['notes']}")
    print()

def main():
    """Main CLI interface."""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 collaboration-tracker.py log <target> <platform> [notes]")
        print("  python3 collaboration-tracker.py update <target> <status> [notes]")
        print("  python3 collaboration-tracker.py status")
        print("  python3 collaboration-tracker.py pending")
        print()
        print("Examples:")
        print("  python3 collaboration-tracker.py log agent0x01 moltbook")
        print("  python3 collaboration-tracker.py update Finn responded 'Interested in onboarding collab'")
        print("  python3 collaboration-tracker.py status")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "log":
        if len(sys.argv) < 4:
            print("❌ Usage: log <target> <platform> [notes]")
            sys.exit(1)
        target = sys.argv[2]
        platform = sys.argv[3]
        notes = sys.argv[4] if len(sys.argv) > 4 else ""
        log_contact(target, platform, "sent", notes)
    
    elif command == "update":
        if len(sys.argv) < 4:
            print("❌ Usage: update <target> <status> [notes]")
            sys.exit(1)
        target = sys.argv[2]
        status = sys.argv[3]
        notes = sys.argv[4] if len(sys.argv) > 4 else ""
        update_status(target, status, notes)
    
    elif command == "status":
        show_status()
    
    elif command == "pending":
        list_pending()
    
    else:
        print(f"❌ Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()
