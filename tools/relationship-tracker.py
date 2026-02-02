#!/usr/bin/env python3
"""
Relationship Tracker — Track agent connections and follow-ups

Purpose:
- Track agents you've connected with on Moltbook
- Remind when to follow up
- Note collaboration opportunities

Usage:
    python3 tools/relationship-tracker.py add "@agent_name" "context"
    python3 tools/relationship-tracker.py list
    python3 tools/relationship-tracker.py followup    # Show due follow-ups
    python3 tools/relationship-tracker.py note "@agent_name" "note"
"""

import json
from datetime import datetime, timedelta
from pathlib import Path
import sys

TRACKER_FILE = Path("/home/node/.openclaw/workspace/.relationships.json")

def load_relationships():
    """Load relationships from file"""
    if TRACKER_FILE.exists():
        try:
            return json.loads(TRACKER_FILE.read_text())
        except:
            return {"agents": []}
    return {"agents": []}

def save_relationships(data):
    """Save relationships to file"""
    TRACKER_FILE.write_text(json.dumps(data, indent=2))

def add_agent(name, context=""):
    """Add a new agent relationship"""
    data = load_relationships()
    
    # Check if already exists
    for agent in data["agents"]:
        if agent["name"].lower() == name.lower():
            print(f"⚠️  Agent '{name}' already tracked")
            return
    
    agent = {
        "name": name,
        "added": datetime.now().isoformat(),
        "context": context,
        "notes": [],
        "last_contact": None,
        "followup_due": None
    }
    
    data["agents"].append(agent)
    save_relationships(data)
    print(f"✓ Added: {name}")
    if context:
        print(f"   Context: {context}")

def add_note(name, note):
    """Add a note to an agent"""
    data = load_relationships()
    
    for agent in data["agents"]:
        if agent["name"].lower() == name.lower():
            agent["notes"].append({
                "text": note,
                "timestamp": datetime.now().isoformat()
            })
            save_relationships(data)
            print(f"✓ Note added for {name}")
            return
    
    print(f"⚠️  Agent '{name}' not found")

def set_followup(name, days=7):
    """Set follow-up reminder for an agent"""
    data = load_relationships()
    
    due_date = (datetime.now() + timedelta(days=days)).isoformat()
    
    for agent in data["agents"]:
        if agent["name"].lower() == name.lower():
            agent["followup_due"] = due_date
            save_relationships(data)
            print(f"✓ Follow-up set for {name} in {days} days")
            return
    
    print(f"⚠️  Agent '{name}' not found")

def list_relationships():
    """List all tracked agents"""
    data = load_relationships()
    
    if not data["agents"]:
        print("No agents tracked yet.")
        return
    
    print(f"🤝 Tracked Relationships ({len(data['agents'])})")
    print()
    
    for agent in data["agents"]:
        print(f"🔸 {agent['name']}")
        if agent.get('context'):
            print(f"   Context: {agent['context']}")
        if agent.get('last_contact'):
            print(f"   Last contact: {agent['last_contact'][:10]}")
        if agent.get('followup_due'):
            print(f"   Follow-up due: {agent['followup_due'][:10]}")
        if agent.get('notes'):
            print(f"   Notes: {len(agent['notes'])}")
        print()

def show_followups():
    """Show agents due for follow-up"""
    data = load_relationships()
    now = datetime.now().isoformat()
    
    due = []
    for agent in data["agents"]:
        if agent.get('followup_due') and agent['followup_due'] <= now:
            due.append(agent)
    
    if not due:
        print("✅ No follow-ups due")
        return
    
    print(f"📋 Follow-ups Due ({len(due)})")
    print()
    
    for agent in due:
        print(f"🔸 {agent['name']}")
        print(f"   Due: {agent['followup_due']}")
        if agent.get('context'):
            print(f"   Context: {agent['context']}")
        print()

def main():
    if len(sys.argv) < 2:
        print("Relationship Tracker — Track agent connections")
        print()
        print("Usage:")
        print("  relationship-tracker.py add @agent [context]")
        print("  relationship-tracker.py list")
        print("  relationship-tracker.py followup")
        print("  relationship-tracker.py note @agent 'note text'")
        print("  relationship-tracker.py followup-set @agent [days]")
        return
    
    command = sys.argv[1]
    
    if command == "add":
        name = sys.argv[2] if len(sys.argv) > 2 else ""
        context = sys.argv[3] if len(sys.argv) > 3 else ""
        if name:
            add_agent(name, context)
        else:
            print("Usage: relationship-tracker.py add @agent [context]")
    
    elif command == "note":
        name = sys.argv[2] if len(sys.argv) > 2 else ""
        note = sys.argv[3] if len(sys.argv) > 3 else ""
        if name and note:
            add_note(name, note)
        else:
            print("Usage: relationship-tracker.py note @agent 'note text'")
    
    elif command == "followup-set":
        name = sys.argv[2] if len(sys.argv) > 2 else ""
        days = int(sys.argv[3]) if len(sys.argv) > 3 else 7
        if name:
            set_followup(name, days)
        else:
            print("Usage: relationship-tracker.py followup-set @agent [days]")
    
    elif command == "list":
        list_relationships()
    
    elif command == "followup":
        show_followups()
    
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
