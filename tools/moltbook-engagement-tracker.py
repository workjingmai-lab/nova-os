#!/usr/bin/env python3
"""
moltbook-engagement-tracker.py
Track and log engagement with other Moltbook agents.

Usage:
    python3 moltbook-engagement-tracker.py log <agent_name> <action> [note]
    python3 moltbook-engagement-tracker.py list
    python3 moltbook-engagement-tracker.py stats
"""

import json
import sys
import os
from datetime import datetime

DATA_FILE = "data/moltbook-engagement.json"

def load_data():
    """Load engagement data from file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            # Ensure required keys exist with correct types
            if "engagements" not in data or not isinstance(data["engagements"], list):
                data["engagements"] = []
            if "agents" not in data or not isinstance(data["agents"], dict):
                data["agents"] = {}
            return data
    return {"engagements": [], "agents": {}}

def save_data(data):
    """Save engagement data to file."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def log_engagement(agent_name, action, note=""):
    """Log a new engagement."""
    data = load_data()
    
    engagement = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "agent": agent_name,
        "action": action,
        "note": note
    }
    
    data["engagements"].append(engagement)
    
    # Update agent stats
    if agent_name not in data["agents"]:
        data["agents"][agent_name] = {"count": 0, "last_interaction": None}
    
    data["agents"][agent_name]["count"] += 1
    data["agents"][agent_name]["last_interaction"] = engagement["timestamp"]
    
    save_data(data)
    print(f"✅ Logged: {action} with {agent_name}")

def list_engagements():
    """List recent engagements."""
    data = load_data()
    
    if not data["engagements"]:
        print("No engagements logged yet.")
        return
    
    print("\n📊 Recent Moltbook Engagements:")
    print("-" * 60)
    
    for e in reversed(data["engagements"][-10:]):
        ts = e["timestamp"][:16].replace("T", " ")
        print(f"{ts} | {e['action']:<12} | {e['agent']:<20}")
        if e.get("note"):
            print(f"           ↳ {e['note'][:50]}")
    
    print("-" * 60)

def show_stats():
    """Show engagement statistics."""
    data = load_data()
    
    total = len(data["engagements"])
    unique_agents = len(data["agents"])
    
    print(f"\n📈 Moltbook Engagement Stats:")
    print(f"   Total engagements: {total}")
    print(f"   Unique agents: {unique_agents}")
    print(f"   Week 3 goal: 5+ agents (current: {unique_agents}/5)")
    
    if unique_agents >= 5:
        print("   ✅ GOAL ACHIEVED")
    else:
        print(f"   📍 Need {5 - unique_agents} more agents")
    
    if data["agents"]:
        print("\n   Top interactions:")
        sorted_agents = sorted(data["agents"].items(), key=lambda x: x[1]["count"], reverse=True)
        for agent, stats in sorted_agents[:5]:
            print(f"   • {agent}: {stats['count']} interactions")

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "log" and len(sys.argv) >= 4:
        agent = sys.argv[2]
        action = sys.argv[3]
        note = sys.argv[4] if len(sys.argv) > 4 else ""
        log_engagement(agent, action, note)
    elif command == "list":
        list_engagements()
    elif command == "stats":
        show_stats()
    else:
        print(__doc__)

if __name__ == "__main__":
    main()
