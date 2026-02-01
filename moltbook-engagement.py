#!/usr/bin/env python3
"""
Moltbook Engagement Tracker
Track agent connections and interactions on Moltbook.
"""

import json
import os
from datetime import datetime
from pathlib import Path

STATE_FILE = Path(__file__).parent / ".moltbook_state.json"

def load_state():
    """Load engagement state."""
    if STATE_FILE.exists():
        with open(STATE_FILE, 'r') as f:
            return json.load(f)
    return {
        "agents": {},
        "interactions": [],
        "lastUpdate": None
    }

def save_state(state):
    """Save engagement state."""
    state["lastUpdate"] = datetime.now().isoformat()
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)

def add_agent(name, bio="", location="", note=""):
    """Add or update an agent."""
    state = load_state()
    if name not in state["agents"]:
        state["agents"][name] = {
            "added": datetime.now().isoformat(),
            "bio": bio,
            "location": location,
            "note": note,
            "interactions": 0
        }
        print(f"✅ Added: {name}")
    else:
        print(f"⏭️  Already tracking: {name}")
    save_state(state)
    return state

def log_interaction(name, type_="comment", note=""):
    """Log an interaction with an agent."""
    state = load_state()
    if name in state["agents"]:
        state["agents"][name]["interactions"] += 1
        state["interactions"].append({
            "agent": name,
            "type": type_,
            "note": note,
            "time": datetime.now().isoformat()
        })
        print(f"💬 Logged {type_} with {name}")
    else:
        print(f"❌ Agent not found: {name}")
    save_state(state)
    return state

def show_stats():
    """Show engagement statistics."""
    state = load_state()
    agents = state["agents"]
    total_interactions = sum(a["interactions"] for a in agents.values())
    
    print(f"\n📊 Moltbook Engagement Stats")
    print(f"   Agents tracked: {len(agents)}")
    print(f"   Total interactions: {total_interactions}")
    print(f"   Last update: {state['lastUpdate'] or 'Never'}")
    
    if agents:
        print(f"\n🤖 Agents:")
        for name, info in agents.items():
            print(f"   • {name}: {info['interactions']} interactions")
            if info.get('bio'):
                print(f"     {info['bio'][:60]}...")
    print()

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        show_stats()
        sys.exit(0)
    
    cmd = sys.argv[1]
    
    if cmd == "add" and len(sys.argv) >= 3:
        name = sys.argv[2]
        bio = sys.argv[3] if len(sys.argv) > 3 else ""
        location = sys.argv[4] if len(sys.argv) > 4 else ""
        add_agent(name, bio, location)
    
    elif cmd == "log" and len(sys.argv) >= 3:
        name = sys.argv[2]
        type_ = sys.argv[3] if len(sys.argv) > 3 else "comment"
        note = sys.argv[4] if len(sys.argv) > 4 else ""
        log_interaction(name, type_, note)
    
    else:
        print("Usage:")
        print("  python moltbook-engagement.py              # Show stats")
        print("  python moltbook-engagement.py add NAME [bio] [location]")
        print("  python moltbook-engagement.py log NAME [type] [note]")
