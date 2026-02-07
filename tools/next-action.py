#!/usr/bin/env python3
"""
next-action.py - ONE thing to do right now. No decisions. Just execute.
"""

import json
from datetime import datetime

# Blockers in priority order (ROI per minute)
BLOCKERS = [
    {
        "action": "Gateway restart",
        "command": "Ask Arthur: run 'openclaw gateway restart'",
        "time": 1,
        "value": 50000,
        "roi_per_min": 50000,
        "unblocks": "Code4rena bounties ($50K potential)",
        "status": "BLOCKED",
        "who": "Arthur"
    },
    {
        "action": "GitHub CLI auth", 
        "command": "Ask Arthur: run 'gh auth login'",
        "time": 5,
        "value": 125000,
        "roi_per_min": 25000,
        "unblocks": "5 grant submissions ($125K potential)",
        "status": "BLOCKED",
        "who": "Arthur"
    },
    {
        "action": "Send service messages",
        "command": "Arthur sends 39 messages (Nova prepared)",
        "time": 36,
        "value": 332000,
        "roi_per_min": 9222,
        "unblocks": "39 leads, $332K services pipeline",
        "status": "READY",
        "who": "Arthur"
    }
]

# Nova's independent actions (no blockers)
NOVA_ACTIONS = [
    {
        "action": "Publish Moltbook post",
        "command": "python3 tools/moltbook-suite.py post --next",
        "time": 1,
        "value": "Engagement + visibility",
        "roi": "Brand building",
        "who": "Nova"
    },
    {
        "action": "Build new tool",
        "command": "Create tool for revenue/pipeline/tracking",
        "time": 1,
        "value": "Compound productivity",
        "roi": "Infinite",
        "who": "Nova"
    },
    {
        "action": "Document learnings",
        "command": "Write knowledge article",
        "time": 1,
        "value": "Knowledge base growth",
        "roi": "Multiplicative",
        "who": "Nova"
    }
]

def main():
    print("=" * 60)
    print("🎯 NEXT ACTION - Execute This Now")
    print("=" * 60)
    print()
    
    # Check if any Arthur actions are unblocked
    arthur_unblocked = [b for b in BLOCKERS if b["status"] == "READY"]
    
    if arthur_unblocked:
        # Show highest ROI Arthur action
        next_item = max(arthur_unblocked, key=lambda x: x["roi_per_min"])
        print("👤 ARTHUR'S NEXT ACTION:")
        print()
        print(f"📋 ACTION: {next_item['action']}")
        print(f"⏱️  TIME: {next_item['time']} minute{'s' if next_item['time'] > 1 else ''}")
        print(f"💰 VALUE: ${next_item['value']:,}")
        print(f"📈 ROI: ${next_item['roi_per_min']:,}/min")
        print()
        print(f"🔓 UNBLOCKS: {next_item['unblocks']}")
        print()
        print(f"🚀 WHAT TO DO: {next_item['command']}")
        print()
        print("=" * 60)
        print("💡 Arthur: Execute this one thing now.")
        print("=" * 60)
    else:
        # All Arthur actions blocked — show highest ROI blocker
        next_item = BLOCKERS[0]
        print("⏳ ALL REVENUE ACTIONS BLOCKED ON ARTHUR")
        print()
        print(f"🚫 TOP BLOCKER: {next_item['action']}")
        print(f"   ROI: ${next_item['roi_per_min']:,}/min")
        print(f"   Value: ${next_item['value']:,}")
        print(f"   Time: {next_item['time']} min")
        print()
        print(f"🚀 WHAT ARTHUR NEEDS TO DO:")
        print(f"   {next_item['command']}")
        print()
        print("=" * 60)
        print("🤖 NOVA'S ACTIONS (while waiting):")
        print("=" * 60)
        for i, action in enumerate(NOVA_ACTIONS[:2], 1):
            print(f"{i}. {action['action']}: {action['command']}")
        print()
        print("💡 Nova: Keep building while Arthur unblocks.")

if __name__ == "__main__":
    main()
