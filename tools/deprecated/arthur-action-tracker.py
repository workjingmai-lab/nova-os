#!/usr/bin/env python3
"""
Arthur Action Tracker — Track and monitor Arthur's execution actions

Arthur's critical path to unlock $487K revenue:
1. Gateway restart (1 min → $50K bounties unblocked)
2. GitHub CLI auth (5 min → $130K grants unblocked)
3. Send 34 service messages (36 min → $267K services submitted)

This tool tracks when Arthur completes these actions.

Usage:
    python3 arthur-action-tracker.py          # Show status
    python3 arthur-action-tracker.py --check  # Verify actions
    python3 arthur-action-tracker.py done 1   # Mark action #1 complete
"""

import json
from pathlib import Path
from datetime import datetime, timezone

TRACKER_FILE = Path.home() / ".openclaw/workspace/data/arthur-actions.json"

# Arthur's action list (from BLOCKER-SUMMARY-FOR-ARTHUR.md)
ACTIONS = [
    {
        "id": 1,
        "name": "Gateway Restart",
        "description": "Restart OpenClaw gateway to enable browser access",
        "time": "1 min",
        "unblocks": "$50K (Code4rena bounties)",
        "command": "openclaw gateway restart",
        "status": "pending",
        "completed_at": None
    },
    {
        "id": 2,
        "name": "GitHub CLI Auth",
        "description": "Authenticate GitHub CLI for grant submissions",
        "time": "5 min",
        "unblocks": "$130K (5 grant applications)",
        "command": "gh auth login",
        "status": "pending",
        "completed_at": None
    },
    {
        "id": 3,
        "name": "Send 34 Service Messages",
        "description": "Send outreach to 34 DAO/protocol targets",
        "time": "36 min",
        "unblocks": "$267K (service contracts)",
        "command": "See outreach/ARTHUR-NEXT-ACTIONS.md",
        "status": "pending",
        "completed_at": None
    },
    {
        "id": 4,
        "name": "Submit 5 Grant Applications",
        "description": "Submit Gitcoin, Octant, Olas, Optimism, Moloch",
        "time": "15 min",
        "unblocks": "$130K (grant funding)",
        "command": "See grants/quick-start.md",
        "status": "pending",
        "completed_at": None
    }
]

def load_tracker():
    """Load tracker state from JSON"""
    if not TRACKER_FILE.exists():
        # Initialize with default actions
        save_tracker(ACTIONS)
        return ACTIONS.copy()
    
    with open(TRACKER_FILE, 'r') as f:
        return json.load(f)

def save_tracker(actions):
    """Save tracker state to JSON"""
    TRACKER_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(TRACKER_FILE, 'w') as f:
        json.dump(actions, f, indent=2)

def show_status():
    """Display current status of Arthur's actions"""
    actions = load_tracker()
    
    print("🎯 Arthur's Execution Path")
    print("=" * 70)
    
    total_time = 0
    total_unblocked = 0
    completed = 0
    
    for action in actions:
        status_icon = "✅" if action["status"] == "complete" else "⬜"
        print(f"\n{status_icon} Action {action['id']}: {action['name']}")
        print(f"   📝 {action['description']}")
        print(f"   ⏱️  Time: {action['time']}")
        print(f"   💎 Unblocks: {action['unblocks']}")
        print(f"   🔧 Command: {action['command']}")
        
        if action['status'] == 'complete':
            completed += 1
            completed_at = action.get('completed_at', 'Unknown')
            print(f"   ✨ Completed: {completed_at}")
        
        total_time += int(action['time'].split()[0])
        # Extract dollar value
        value = int(action['unblocks'].replace('$', '').replace('K', '000').split()[0].replace('(', '').replace(')', ''))
        total_unblocked += value
    
    print("\n" + "=" * 70)
    print(f"📊 Progress: {completed}/{len(actions)} actions complete")
    print(f"⏱️  Total Time: {total_time} minutes")
    print(f"💎 Total Value: ${total_unblocked:,}")
    print(f"📈 ROI: ${total_unblocked/total_time:,.0f}/minute")
    
    if completed < len(actions):
        remaining = len(actions) - completed
        print(f"\n🚀 Next: {remaining} action(s) remaining → ${total_unblocked:,} unlocked")
    else:
        print(f"\n🎉 ALL ACTIONS COMPLETE! Revenue pipeline fully unlocked!")

def mark_complete(action_id):
    """Mark an action as complete"""
    actions = load_tracker()
    
    for action in actions:
        if action['id'] == action_id:
            action['status'] = 'complete'
            action['completed_at'] = datetime.now(timezone.utc).isoformat()
            print(f"✅ Marked action {action_id} ({action['name']}) as complete!")
            save_tracker(actions)
            return
    
    print(f"❌ Action {action_id} not found!")

def check_actions():
    """Verify which actions are complete (by checking system state)"""
    import subprocess
    
    print("🔍 Checking Arthur's action status...\n")
    
    # Check 1: Gateway restart (browser service)
    print("1️⃣ Gateway Restart:")
    try:
        result = subprocess.run(['openclaw', 'gateway', 'status'], 
                              capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            print("   ✅ Gateway is running")
        else:
            print("   ⬜ Gateway not running (needs restart)")
    except:
        print("   ⬜ Gateway check failed (may need restart)")
    
    # Check 2: GitHub CLI auth
    print("\n2️⃣ GitHub CLI Auth:")
    try:
        result = subprocess.run(['gh', 'auth', 'status'], 
                              capture_output=True, text=True, timeout=5)
        if 'Logged in to github.com' in result.stdout:
            print("   ✅ GitHub CLI authenticated")
        else:
            print("   ⬜ GitHub CLI NOT authenticated")
    except:
        print("   ⬜ GitHub CLI not found or not authenticated")
    
    # Check 3 & 4: Manual actions (messages, grants)
    print("\n3️⃣ Service Messages & 4️⃣ Grant Submissions:")
    print("   ⬜ Manual actions (check revenue-tracker.py for status)")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Track Arthur's execution actions")
    parser.add_argument('--check', action='store_true', help='Check current system status')
    parser.add_argument('done', nargs='?', type=int, metavar='ID', 
                       help='Mark action ID as complete')
    
    args = parser.parse_args()
    
    if args.check:
        check_actions()
    elif args.done is not None:
        mark_complete(args.done)
    else:
        show_status()

if __name__ == '__main__':
    main()
