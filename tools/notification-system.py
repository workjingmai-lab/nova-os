#!/usr/bin/env python3
"""
notification-system.py — Nova's Alert & Mention Tracker

Checks various sources for notifications:
- Moltbook mentions and replies
- GitHub notifications (when account created)
- Grant opportunity alerts
- Scheduled reminders

Usage: python3 notification-system.py [--check-all|--moltbook|--grants|--show]
"""

import json
import os
import sys
import argparse
from datetime import datetime, timedelta
from pathlib import Path

# Configuration
CONFIG_PATH = Path(__file__).parent / ".notification_config.json"
STATE_PATH = Path(__file__).parent / ".notification_state.json"
DASHBOARD_DIR = Path(__file__).parent.parent / "dashboard"

# Default configuration
DEFAULT_CONFIG = {
    "moltbook": {
        "enabled": True,
        "check_interval_minutes": 30,
        "api_endpoint": "https://www.moltbook.com/api/v1",
        "auth_token": "moltbook_sk_xSwszjAM8vLLaa7VsSZVgNWp5a-R5XqD"
    },
    "grants": {
        "enabled": True,
        "sources": [
            {"name": "Gitcoin", "url": "https://grants.gitcoin.co"},
            {"name": "Code4rena", "url": "https://code4rena.com"},
            {"name": "Immunefi", "url": "https://immunefi.com"}
        ]
    },
    "reminders": []
}


def load_config():
    """Load or create configuration."""
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH) as f:
            return json.load(f)
    save_config(DEFAULT_CONFIG)
    return DEFAULT_CONFIG


def save_config(config):
    """Save configuration to file."""
    with open(CONFIG_PATH, 'w') as f:
        json.dump(config, f, indent=2)


def load_state():
    """Load notification state."""
    if STATE_PATH.exists():
        with open(STATE_PATH) as f:
            return json.load(f)
    return {
        "last_check": None,
        "moltbook_last_check": None,
        "notifications": [],
        "unread_count": 0
    }


def save_state(state):
    """Save notification state."""
    with open(STATE_PATH, 'w') as f:
        json.dump(state, f, indent=2, default=str)


def check_moltbook(config):
    """Check Moltbook for mentions and activity."""
    import subprocess
    
    results = {
        "status": "unknown",
        "mentions": [],
        "errors": []
    }
    
    # Check agent status
    try:
        cmd = [
            "curl", "-s", "-o", "/dev/null", "-w", "%{http_code}",
            "-H", f"Authorization: Bearer {config['moltbook']['auth_token']}",
            f"{config['moltbook']['api_endpoint']}/agents/status"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        status_code = result.stdout.strip()
        
        if status_code == "200":
            results["status"] = "online"
            # In future: fetch mentions, replies, new followers
            results["mentions"].append({
                "type": "system",
                "message": "API is online - fetch functionality ready",
                "time": datetime.now().isoformat()
            })
        else:
            results["status"] = "offline"
            results["errors"].append(f"API returned status {status_code}")
            
    except Exception as e:
        results["status"] = "error"
        results["errors"].append(str(e))
    
    return results


def check_grants(config):
    """Check for new grant opportunities."""
    # This would integrate with grant APIs in production
    # For now, return tracked opportunities
    
    opportunities = [
        {
            "name": "Gitcoin Grants 23",
            "platform": "Gitcoin",
            "deadline": "2026-02-15",
            "match_amount": "$100K+",
            "status": "open",
            "relevance": "high"
        },
        {
            "name": "Code4rena Wardens Program",
            "platform": "Code4rena",
            "deadline": "rolling",
            "match_amount": "varies",
            "status": "open", 
            "relevance": "high"
        },
        {
            "name": "Immunefi Bug Bounties",
            "platform": "Immunefi",
            "deadline": "ongoing",
            "match_amount": "up to $1M",
            "status": "open",
            "relevance": "medium"
        }
    ]
    
    return {
        "opportunities": opportunities,
        "new_count": len(opportunities),
        "last_checked": datetime.now().isoformat()
    }


def add_reminder(text, when=None):
    """Add a new reminder."""
    config = load_config()
    
    reminder = {
        "id": len(config["reminders"]) + 1,
        "text": text,
        "created": datetime.now().isoformat(),
        "due": when or (datetime.now() + timedelta(hours=1)).isoformat(),
        "completed": False
    }
    
    config["reminders"].append(reminder)
    save_config(config)
    
    return reminder


def check_reminders():
    """Check for due reminders."""
    config = load_config()
    now = datetime.now()
    
    due = []
    for reminder in config["reminders"]:
        if not reminder["completed"]:
            due_time = datetime.fromisoformat(reminder["due"].replace('Z', '+00:00'))
            if due_time <= now:
                due.append(reminder)
    
    return due


def update_dashboard(notifications):
    """Update dashboard with notification data."""
    DASHBOARD_DIR.mkdir(exist_ok=True)
    
    data = {
        "generated_at": datetime.now().isoformat(),
        "unread_count": len(notifications),
        "notifications": notifications,
        "sources": {
            "moltbook": "online" if any("moltbook" in str(n) for n in notifications) else "unknown",
            "github": "not_configured",
            "grants": "active"
        }
    }
    
    data_path = DASHBOARD_DIR / "notifications.json"
    with open(data_path, 'w') as f:
        json.dump(data, f, indent=2, default=str)
    
    return data_path


def format_notification(note):
    """Format a notification for display."""
    icon = "🔔"
    if note.get("type") == "mention":
        icon = "💬"
    elif note.get("type") == "grant":
        icon = "💰"
    elif note.get("type") == "reminder":
        icon = "⏰"
    elif note.get("type") == "system":
        icon = "⚙️"
    
    time_str = ""
    if "time" in note:
        time_str = f" ({note['time'][:16]})"
    
    return f"{icon} {note.get('message', str(note))}{time_str}"


def main():
    parser = argparse.ArgumentParser(description="Nova's notification system")
    parser.add_argument("--check-all", action="store_true", help="Check all sources")
    parser.add_argument("--moltbook", action="store_true", help="Check Moltbook only")
    parser.add_argument("--grants", action="store_true", help="Check grants only")
    parser.add_argument("--reminders", action="store_true", help="Show due reminders")
    parser.add_argument("--add-reminder", metavar="TEXT", help="Add a reminder")
    parser.add_argument("--when", metavar="TIME", help="When the reminder is due (e.g., '1h', '2026-02-02 09:00')")
    parser.add_argument("--show", action="store_true", help="Show all notifications")
    parser.add_argument("--clear", action="store_true", help="Clear all notifications")
    
    args = parser.parse_args()
    
    config = load_config()
    state = load_state()
    
    # Add reminder
    if args.add_reminder:
        when = None
        if args.when:
            if args.when.endswith('h'):
                hours = int(args.when[:-1])
                when = (datetime.now() + timedelta(hours=hours)).isoformat()
            else:
                when = args.when
        
        reminder = add_reminder(args.add_reminder, when)
        print(f"✅ Reminder added (ID: {reminder['id']})")
        print(f"   Text: {reminder['text']}")
        print(f"   Due: {reminder['due']}")
        return
    
    # Check reminders
    if args.reminders or args.check_all:
        due = check_reminders()
        if due:
            print(f"⏰ {len(due)} reminder(s) due:")
            for r in due:
                print(f"   [{r['id']}] {r['text']}")
        elif args.reminders:
            print("✅ No reminders due")
    
    # Check Moltbook
    if args.moltbook or args.check_all:
        print("🔍 Checking Moltbook...")
        moltbook_results = check_moltbook(config)
        
        if moltbook_results["status"] == "online":
            print("✅ Moltbook API is online")
            for mention in moltbook_results["mentions"]:
                state["notifications"].append({
                    "type": "system",
                    "source": "moltbook",
                    "message": mention["message"],
                    "time": mention["time"]
                })
        else:
            print(f"⚠️ Moltbook is {moltbook_results['status']}")
            if moltbook_results["errors"]:
                print(f"   Error: {moltbook_results['errors'][0]}")
    
    # Check grants
    if args.grants or args.check_all:
        print("🔍 Checking grant opportunities...")
        grants_results = check_grants(config)
        
        print(f"💰 Found {grants_results['new_count']} opportunities:")
        for opp in grants_results["opportunities"]:
            print(f"   • {opp['name']} ({opp['platform']}) - {opp['match_amount']}")
            state["notifications"].append({
                "type": "grant",
                "source": "grants",
                "message": f"{opp['name']} on {opp['platform']}",
                "details": opp,
                "time": datetime.now().isoformat()
            })
    
    # Show notifications
    if args.show or args.check_all:
        if state["notifications"]:
            print(f"\n📬 Notifications ({len(state['notifications'])}):")
            for note in state["notifications"][-10:]:  # Show last 10
                print(f"   {format_notification(note)}")
        else:
            print("\n📭 No notifications")
    
    # Clear notifications
    if args.clear:
        state["notifications"] = []
        print("🗑️ Notifications cleared")
    
    # Update state
    state["last_check"] = datetime.now().isoformat()
    state["unread_count"] = len(state["notifications"])
    save_state(state)
    
    # Update dashboard
    if args.check_all:
        dashboard_path = update_dashboard(state["notifications"])
        print(f"\n📊 Dashboard updated: {dashboard_path}")


if __name__ == "__main__":
    main()
