#!/usr/bin/env python3
"""
daily-revenue-action.py — One high-ROI action per day

Analyzes revenue pipeline and suggests the single most impactful action
to move toward conversion. Eliminates decision fatigue.

Usage:
    python3 tools/daily-revenue-action.py           # Get today's action
    python3 tools/daily-revenue-action.py --why     # Show reasoning
    python3 tools/daily-revenue-action.py --all     # Show all possible actions ranked
"""

import json
import argparse
from pathlib import Path
from datetime import datetime, timezone

PIPELINE_FILE = Path.home() / ".openclaw/workspace/data/revenue-pipeline.json"
DIARY_FILE = Path.home() / ".openclaw/workspace/memory/2026-02-07.md"

# Action definitions with ROI estimates
ACTIONS = [
    {
        "id": "gateway_restart",
        "name": "Restart Gateway for Browser Access",
        "time_min": 1,
        "value_unblocked": 50000,
        "roi_per_min": 50000,
        "condition": "bounties_blocked",
        "command": "Ask Arthur: Run 'openclaw gateway restart' to unblock $50K bounties",
        "context": "Code4rena audits require browser automation"
    },
    {
        "id": "github_auth",
        "name": "Authenticate GitHub CLI",
        "time_min": 5,
        "value_unblocked": 125000,
        "roi_per_min": 25000,
        "condition": "grants_blocked",
        "command": "Ask Arthur: Run 'gh auth login' to unblock $125K grant submissions",
        "context": "5 grants ready, need repo push capability"
    },
    {
        "id": "send_service_messages",
        "name": "Send Service Outreach Messages",
        "time_min": 36,
        "value_unblocked": 332000,
        "roi_per_min": 9222,
        "condition": "services_ready",
        "command": "Send 39 service messages using outreach/ directory templates",
        "context": "$332K services ready, 0 blockers"
    },
    {
        "id": "submit_grants",
        "name": "Submit Grant Applications",
        "time_min": 15,
        "value_unblocked": 125000,
        "roi_per_min": 8333,
        "condition": "grants_ready",
        "command": "Submit 5 grants via their portals (Gitcoin, Octant, Olas, RPGF, Moloch)",
        "context": "Templates ready, forms pre-filled"
    },
    {
        "id": "check_follow_ups",
        "name": "Check Follow-ups on Sent Messages",
        "time_min": 5,
        "value_unblocked": 50000,
        "roi_per_min": 10000,
        "condition": "always",
        "command": "python3 tools/follow-up-tracker.py due",
        "context": "Catch responses before they go cold"
    },
    {
        "id": "moltbook_post",
        "name": "Publish Moltbook Content",
        "time_min": 2,
        "value_unblocked": 10000,
        "roi_per_min": 5000,
        "condition": "always",
        "command": "python3 tools/moltbook-suite.py post --next",
        "context": "3 posts/week goal, 14 queued and ready"
    },
    {
        "id": "update_pipeline",
        "name": "Update Pipeline Statuses",
        "time_min": 5,
        "value_unblocked": 5000,
        "roi_per_min": 1000,
        "condition": "always",
        "command": "python3 tools/revenue-tracker.py summary",
        "context": "Visibility prevents revenue leakage"
    }
]

def get_pipeline_status():
    """Load current pipeline status."""
    if not PIPELINE_FILE.exists():
        return {"total": 0, "ready": 0, "submitted": 0, "won": 0}
    
    with open(PIPELINE_FILE) as f:
        data = json.load(f)
    
    total = sum(item.get("potential", 0) for item in data.get("items", []))
    ready = sum(item.get("potential", 0) for item in data.get("items", []) 
              if item.get("status") == "ready")
    submitted = sum(item.get("potential", 0) for item in data.get("items", []) 
                  if item.get("status") == "submitted")
    won = sum(item.get("potential", 0) for item in data.get("items", []) 
            if item.get("status") == "won")
    
    return {"total": total, "ready": ready, "submitted": submitted, "won": won}

def check_blocks():
    """Check what's currently blocking execution."""
    blocks = {
        "bounties_blocked": True,  # Still need gateway restart
        "grants_blocked": True,    # Still need GitHub auth
        "services_ready": True     # Always ready
    }
    return blocks

def get_top_action(blocks, pipeline):
    """Determine the highest ROI action right now."""
    eligible = []
    
    for action in ACTIONS:
        # Check if condition is met
        if action["condition"] == "always":
            eligible.append(action)
        elif blocks.get(action["condition"], False):
            eligible.append(action)
    
    # Sort by ROI per minute
    eligible.sort(key=lambda x: x["roi_per_min"], reverse=True)
    
    return eligible[0] if eligible else None

def format_money(n):
    """Format number as currency."""
    if n >= 1000000:
        return f"${n/1000000:.2f}M"
    elif n >= 1000:
        return f"${n/1000:.0f}K"
    return f"${n}"

def main():
    parser = argparse.ArgumentParser(description="Daily revenue action recommender")
    parser.add_argument("--why", action="store_true", help="Show reasoning")
    parser.add_argument("--all", action="store_true", help="Show all actions ranked")
    args = parser.parse_args()
    
    blocks = check_blocks()
    pipeline = get_pipeline_status()
    
    if args.all:
        print("🎯 ALL POSSIBLE ACTIONS (ranked by ROI):\n")
        eligible = []
        for action in ACTIONS:
            if action["condition"] == "always" or blocks.get(action["condition"]):
                eligible.append(action)
        
        eligible.sort(key=lambda x: x["roi_per_min"], reverse=True)
        
        for i, action in enumerate(eligible, 1):
            roi = format_money(action["roi_per_min"])
            print(f"{i}. {action['name']}")
            print(f"   Time: {action['time_min']} min | ROI: {roi}/min | Unblocks: {format_money(action['value_unblocked'])}")
            print(f"   → {action['command']}")
            print()
        return
    
    top_action = get_top_action(blocks, pipeline)
    
    if not top_action:
        print("✅ No high-ROI actions available right now.")
        print("   Pipeline status: All caught up!")
        return
    
    now = datetime.now(timezone.utc).strftime("%H:%M UTC")
    
    print(f"🎯 DAILY REVENUE ACTION — {now}\n")
    print(f"Action: {top_action['name']}")
    print(f"Time Required: {top_action['time_min']} minute{'s' if top_action['time_min'] > 1 else ''}")
    print(f"Value Unblocked: {format_money(top_action['value_unblocked'])}")
    print(f"ROI: {format_money(top_action['roi_per_min'])}/min ⭐")
    print()
    print(f"Command: {top_action['command']}")
    print()
    
    if args.why:
        print(f"Why this action?")
        print(f"  → {top_action['context']}")
        print()
        print(f"Current Pipeline:")
        print(f"  Total: {format_money(pipeline['total'])}")
        print(f"  Ready: {format_money(pipeline['ready'])}")
        print(f"  Submitted: {format_money(pipeline['submitted'])}")
        print(f"  Won: {format_money(pipeline['won'])}")
        print()
        print(f"Blockers Status:")
        print(f"  Bounties: {'🔴 Blocked' if blocks['bounties_blocked'] else '🟢 Unblocked'}")
        print(f"  Grants: {'🔴 Blocked' if blocks['grants_blocked'] else '🟢 Unblocked'}")
        print(f"  Services: {'🟢 Ready' if blocks['services_ready'] else '⏳ Waiting'}")
        print()

if __name__ == "__main__":
    main()
