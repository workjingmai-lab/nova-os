#!/usr/bin/env python3
"""
blocker-tracker.py — Monitors blocked tasks and surfaces them for resolution
Run this to see what's blocking Nova and what actions are needed.
"""

import json
import os
from datetime import datetime, timezone
from pathlib import Path

BLOCKER_FILE = Path("/home/node/.openclaw/workspace/status/blockers.json")
DIARY_FILE = Path("/home/node/.openclaw/workspace/diary.md")

def load_blockers():
    """Load current blockers from status file."""
    if BLOCKER_FILE.exists():
        with open(BLOCKER_FILE) as f:
            return json.load(f)
    return {
        "last_updated": datetime.now(timezone.utc).isoformat(),
        "blockers": []
    }

def save_blockers(data):
    """Save blockers to status file."""
    BLOCKER_FILE.parent.mkdir(parents=True, exist_ok=True)
    data["last_updated"] = datetime.now(timezone.utc).isoformat()
    with open(BLOCKER_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def get_default_blockers():
    """Current known blockers from today.md."""
    return [
        {
            "id": "sepolia-eth",
            "task": "Deploy Force exercise to testnet",
            "blocker": "Sepolia ETH needed (0.05-0.1 ETH)",
            "impact": "high",
            "since": "2026-02-01",
            "action_needed": "Get Sepolia ETH from faucet or Arthur"
        },
        {
            "id": "github-token",
            "task": "Push 156-file portfolio to GitHub",
            "blocker": "GitHub personal access token",
            "impact": "high", 
            "since": "2026-02-01",
            "action_needed": "Arthur to generate token with repo scope"
        },
        {
            "id": "moltbook-token",
            "task": "Automated Moltbook posting/engagement",
            "blocker": "Moltbook API token for automation",
            "impact": "medium",
            "since": "2026-02-01",
            "action_needed": "Request token from Moltbook team"
        }
    ]

def format_blocker(b):
    """Format a single blocker for display."""
    impact_emoji = "🔴" if b["impact"] == "high" else "🟡" if b["impact"] == "medium" else "🟢"
    return f"""{impact_emoji} **{b['task']}**
   Blocked: {b['blocker']}
   Since: {b['since']} | Action: {b['action_needed']}
"""

def log_to_diary(blockers):
    """Log blocker status to diary."""
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    count = len(blockers["blockers"])
    high = sum(1 for b in blockers["blockers"] if b.get("impact") == "high")
    
    entry = f"""
## {timestamp} — Blocker Check

**Status:** {count} blockers active ({high} high priority)

"""
    for b in blockers["blockers"]:
        entry += f"- **{b['task']}** — {b['blocker']}\n"
    
    entry += f"\n**Next:** Continue autonomous work until blockers resolved\n"
    
    with open(DIARY_FILE, 'a') as f:
        f.write(entry)

def main():
    # Initialize or load blockers
    blockers = load_blockers()
    
    # If empty, populate with known blockers
    if not blockers.get("blockers"):
        blockers["blockers"] = get_default_blockers()
        save_blockers(blockers)
    
    # Print current status
    print("=" * 50)
    print("🔒 NOVA BLOCKER TRACKER")
    print("=" * 50)
    print(f"Last updated: {blockers['last_updated'][:19]}")
    print()
    
    high = [b for b in blockers["blockers"] if b.get("impact") == "high"]
    medium = [b for b in blockers["blockers"] if b.get("impact") == "medium"]
    
    if high:
        print("🔴 HIGH PRIORITY")
        for b in high:
            print(format_blocker(b))
    
    if medium:
        print("🟡 MEDIUM PRIORITY")
        for b in medium:
            print(format_blocker(b))
    
    print("=" * 50)
    print(f"Total: {len(blockers['blockers'])} blockers | {len(high)} high priority")
    print()
    print("💡 Run with --log to append to diary.md")
    
    # Log if requested
    if "--log" in os.sys.argv:
        log_to_diary(blockers)
        print("✅ Logged to diary.md")

if __name__ == "__main__":
    main()
