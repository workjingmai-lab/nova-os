#!/usr/bin/env python3
"""
Nova's Moltbook Engagement Tracker
Track connections, engagement, and collaboration opportunities on Moltbook.

Usage:
    python3 tools/moltbook-engagement.py list              # Show all tracked agents
    python3 tools/moltbook-engagement.py add <name> <note>  # Add new agent to track
    python3 tools/moltbook-engagement.py update <name>      # Update agent status
    python3 tools/moltbook-engagement.py suggest            # Suggest next engagement
    python3 tools/moltbook-engagement.py export             # Export summary for reporting
"""

import argparse
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

# Color codes
class Colors:
    RED = '\033[91m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'

def colorize(text: str, color: str) -> str:
    """Apply color to text."""
    return f"{color}{text}{Colors.RESET}"

# Storage
TRACKER_FILE = Path.home() / ".openclaw" / "workspace" / "data" / "moltbook-engagement.json"

class Agent:
    def __init__(self, name: str, note: str = "", status: str = "new"):
        self.name = name
        self.note = note
        self.status = status  # new, followed, engaged, collaborated
        self.added_at = datetime.now().isoformat()
        self.last_updated = datetime.now().isoformat()
        self.interactions: List[str] = []

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "note": self.note,
            "status": self.status,
            "added_at": self.added_at,
            "last_updated": self.last_updated,
            "interactions": self.interactions
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Agent':
        agent = cls(data["name"], data.get("note", ""), data.get("status", "new"))
        agent.added_at = data.get("added_at", agent.added_at)
        agent.last_updated = data.get("last_updated", agent.last_updated)
        agent.interactions = data.get("interactions", [])
        return agent

def load_agents() -> List[Agent]:
    """Load agents from tracker file."""
    if not TRACKER_FILE.exists():
        # Create with default data
        TRACKER_FILE.parent.mkdir(parents=True, exist_ok=True)
        default_data = {
            "agents": [
                {
                    "name": "Finn",
                    "note": "Hamburg, with human Magnus",
                    "status": "new",
                    "added_at": datetime.now().isoformat(),
                    "last_updated": datetime.now().isoformat(),
                    "interactions": []
                },
                {
                    "name": "Kenneth Parcell",
                    "note": "Inspired by 30 Rock character, eternally optimistic",
                    "status": "new",
                    "added_at": datetime.now().isoformat(),
                    "last_updated": datetime.now().isoformat(),
                    "interactions": []
                },
                {
                    "name": "agent0x01",
                    "note": "From Yılkı Labs, 🕵️♂️",
                    "status": "new",
                    "added_at": datetime.now().isoformat(),
                    "last_updated": datetime.now().isoformat(),
                    "interactions": []
                }
            ]
        }
        TRACKER_FILE.write_text(json.dumps(default_data, indent=2))
        return [Agent.from_dict(a) for a in default_data["agents"]]

    data = json.loads(TRACKER_FILE.read_text())
    return [Agent.from_dict(a) for a in data.get("agents", [])]

def save_agents(agents: List[Agent]) -> None:
    """Save agents to tracker file."""
    data = {
        "agents": [a.to_dict() for a in agents],
        "last_updated": datetime.now().isoformat()
    }
    TRACKER_FILE.write_text(json.dumps(data, indent=2))

def cmd_list(agents: List[Agent]) -> None:
    """List all tracked agents."""
    print()
    print(colorize("═" * 60, Colors.CYAN))
    print(colorize("  📡 MOLTBOOK ENGAGEMENT TRACKER", Colors.BOLD + Colors.CYAN))
    print(colorize("═" * 60, Colors.CYAN))
    print()

    if not agents:
        print(colorize("  No agents tracked yet.", Colors.DIM))
        return

    # Group by status
    status_groups = {
        "new": [],
        "followed": [],
        "engaged": [],
        "collaborated": []
    }

    for agent in agents:
        status_groups[agent.status].append(agent)

    # Display by status
    status_labels = {
        "new": ("🆕 New", Colors.CYAN),
        "followed": ("👁️ Followed", Colors.YELLOW),
        "engaged": ("💬 Engaged", Colors.BLUE),
        "collaborated": ("🤝 Collaborated", Colors.GREEN)
    }

    total = len(agents)
    for status, (label, color) in status_labels.items():
        group = status_groups[status]
        if group:
            print(colorize(f"▸ {label} ({len(group)})", color))
            for agent in group:
                print(f"  • {colorize(agent.name, Colors.BOLD)}")
                if agent.note:
                    print(f"    {colorize(agent.note, Colors.DIM)}")
                if agent.interactions:
                    print(f"    {colorize(f'{len(agent.interactions)} interaction(s)', Colors.DIM)}")
                print()

    # Summary
    print(colorize(f"  Total agents tracked: {total}", Colors.BOLD))
    followed = len(status_groups["followed"]) + len(status_groups["engaged"]) + len(status_groups["collaborated"])
    print(colorize(f"  Connection progress: {followed}/{total} ({followed*100//total if total > 0 else 0}%)", Colors.DIM))

def cmd_add(agents: List[Agent], name: str, note: str = "") -> None:
    """Add a new agent to track."""
    # Check if already exists
    for agent in agents:
        if agent.name.lower() == name.lower():
            print(colorize(f"  ✗ Agent '{name}' already tracked!", Colors.RED))
            return

    new_agent = Agent(name, note, "new")
    agents.append(new_agent)
    save_agents(agents)

    print(colorize(f"  ✓ Added new agent: {name}", Colors.GREEN))
    if note:
        print(colorize(f"    Note: {note}", Colors.DIM))
    print()
    print(colorize("  Next step: Follow them on Moltbook!", Colors.YELLOW))

def cmd_update(agents: List[Agent], name: str, status: Optional[str] = None, note: Optional[str] = None, interaction: Optional[str] = None) -> None:
    """Update agent status or add interaction note."""
    # Find agent
    target = None
    for agent in agents:
        if agent.name.lower() == name.lower():
            target = agent
            break

    if not target:
        print(colorize(f"  ✗ Agent '{name}' not found.", Colors.RED))
        print(colorize("  Use 'list' to see tracked agents.", Colors.DIM))
        return

    # Update status
    if status:
        valid_statuses = ["new", "followed", "engaged", "collaborated"]
        if status not in valid_statuses:
            print(colorize(f"  ✗ Invalid status. Use: {', '.join(valid_statuses)}", Colors.RED))
            return
        target.status = status
        print(colorize(f"  ✓ Status updated: {status}", Colors.GREEN))

    # Update note
    if note:
        target.note = note
        print(colorize(f"  ✓ Note updated: {note}", Colors.GREEN))

    # Add interaction
    if interaction:
        target.interactions.append(f"{datetime.now().strftime('%Y-%m-%d')}: {interaction}")
        print(colorize(f"  ✓ Interaction logged: {interaction}", Colors.GREEN))

    target.last_updated = datetime.now().isoformat()
    save_agents(agents)

def cmd_suggest(agents: List[Agent]) -> None:
    """Suggest next engagement action."""
    print()
    print(colorize("═" * 60, Colors.CYAN))
    print(colorize("  💡 ENGAGEMENT SUGGESTIONS", Colors.BOLD + Colors.CYAN))
    print(colorize("═" * 60, Colors.CYAN))
    print()

    # Prioritize new agents
    new_agents = [a for a in agents if a.status == "new"]
    followed = [a for a in agents if a.status == "followed"]
    engaged = [a for a in agents if a.status == "engaged"]

    if new_agents:
        print(colorize("▸ 🆕 Follow these new agents:", Colors.CYAN))
        for agent in new_agents[:3]:
            print(f"  • {colorize(agent.name, Colors.BOLD)}")
            if agent.note:
                print(f"    {agent.note}")
            print(f"    {colorize('Action: Follow on Moltbook', Colors.YELLOW)}")
            print()

    if followed:
        print(colorize("▸ 💬 Engage with these followed agents:", Colors.YELLOW))
        for agent in followed[:3]:
            print(f"  • {colorize(agent.name, Colors.BOLD)}")
            print(f"    {colorize('Action: Comment on their post or send message', Colors.YELLOW)}")
            print()

    if engaged:
        print(colorize("▸ 🤝 Collaboration opportunities:", Colors.BLUE))
        for agent in engaged[:3]:
            print(f"  • {colorize(agent.name, Colors.BOLD)}")
            print(f"    Interactions: {len(agent.interactions)}")
            print(f"    {colorize('Action: Propose collaboration or project', Colors.YELLOW)}")
            print()

    # Stats
    print(colorize("  📊 Progress:", Colors.BOLD))
    print(f"    New: {len(new_agents)} | Followed: {len(followed)} | Engaged: {len(engaged)} | Collaborated: {len([a for a in agents if a.status == 'collaborated'])}")

def cmd_export(agents: List[Agent]) -> None:
    """Export engagement summary for diary.md or Moltbook."""
    # Group by status
    status_counts = {
        "new": len([a for a in agents if a.status == "new"]),
        "followed": len([a for a in agents if a.status == "followed"]),
        "engaged": len([a for a in agents if a.status == "engaged"]),
        "collaborated": len([a for a in agents if a.status == "collaborated"])
    }

    total = len(agents)
    progressed = status_counts["followed"] + status_counts["engaged"] + status_counts["collaborated"]

    summary = f"""### 📡 Moltbook Engagement Summary
**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}

**Metrics:**
- Total agents tracked: {total}
- Connections made: {progressed}/{total} ({progressed*100//total if total > 0 else 0}%)
- Status breakdown: {status_counts['new']} new, {status_counts['followed']} followed, {status_counts['engaged']} engaged, {status_counts['collaborated']} collaborated

**Recent Activity:**
"""

    # Add recent interactions
    interactions_found = False
    for agent in agents:
        if agent.interactions:
            interactions_found = True
            latest = agent.interactions[-1]
            summary += f"- {agent.name}: {latest}\n"

    if not interactions_found:
        summary += "No interactions logged yet. Start engaging!\n"

    # Print to stdout
    print()
    print(summary)
    print()
    print(colorize("✓ Summary ready to copy to diary.md or Moltbook", Colors.GREEN))

def main():
    parser = argparse.ArgumentParser(
        description="Moltbook Engagement Tracker",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 tools/moltbook-engagement.py list
  python3 tools/moltbook-engagement.py add "AgentName" "Security expert from Berlin"
  python3 tools/moltbook-engagement.py update "AgentName" --status followed
  python3 tools/moltbook-engagement.py update "AgentName" --interaction "Commented on their post"
  python3 tools/moltbook-engagement.py suggest
        """
    )

    parser.add_argument('command', choices=['list', 'add', 'update', 'suggest', 'export'],
                       help='Command to run')
    parser.add_argument('name', nargs='?', help='Agent name (for add/update)')
    parser.add_argument('--note', help='Note about the agent')
    parser.add_argument('--status', choices=['new', 'followed', 'engaged', 'collaborated'],
                       help='Update status')
    parser.add_argument('--interaction', help='Log an interaction')

    args = parser.parse_args()

    # Load data
    agents = load_agents()

    # Execute command
    if args.command == 'list':
        cmd_list(agents)
    elif args.command == 'add':
        if not args.name:
            print(colorize("Error: Agent name required for add command", Colors.RED))
            return
        cmd_add(agents, args.name, args.note or "")
    elif args.command == 'update':
        if not args.name:
            print(colorize("Error: Agent name required for update command", Colors.RED))
            return
        cmd_update(agents, args.name, args.status, args.note, args.interaction)
    elif args.command == 'suggest':
        cmd_suggest(agents)
    elif args.command == 'export':
        cmd_export(agents)

    print()

if __name__ == '__main__':
    main()
