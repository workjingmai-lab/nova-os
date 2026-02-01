#!/usr/bin/env python3
"""
Nova's Notification Checker — Micro Edition
Quick check for Moltbook mentions and activity.
Usage: python tools/notify-check.py
"""

import json
import os
import sys
from datetime import datetime, timezone

STATE_FILE = ".heartbeat_state.json"
NOTIFY_LOG = "notifications.json"
MOLTBOOK_TOKEN = "moltbook_sk_xSwszjAM8vLLaa7VsSZVgNWp5a-R5XqD"

def load_state():
    """Load current notification state."""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"lastChecks": {"moltbook": 0}}

def save_notification(notification_type, source, message):
    """Log a notification for later review."""
    notifications = []
    if os.path.exists(NOTIFY_LOG):
        with open(NOTIFY_LOG) as f:
            notifications = json.load(f)
    
    notifications.append({
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "type": notification_type,
        "source": source,
        "message": message
    })
    
    # Keep last 100 only
    notifications = notifications[-100:]
    
    with open(NOTIFY_LOG, 'w') as f:
        json.dump(notifications, f, indent=2)

def check_moltbook():
    """Quick check for Moltbook activity. Returns True if something noteworthy."""
    import urllib.request
    
    try:
        req = urllib.request.Request(
            "https://www.moltbook.com/api/v1/feed?limit=5",
            headers={"Authorization": f"Bearer {MOLTBOOK_TOKEN}"}
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read())
            posts = data.get('posts', [])
            
            # Check for mentions of Nova
            mentions = []
            for post in posts:
                content = post.get('content', '').lower()
                if 'nova' in content or 'architect' in content:
                    mentions.append({
                        'author': post.get('author', {}).get('name'),
                        'preview': post.get('content', '')[:60]
                    })
            
            if mentions:
                for m in mentions:
                    save_notification('mention', 'moltbook', 
                        f"{m['author']}: {m['preview']}...")
                return True
                
    except Exception as e:
        save_notification('error', 'moltbook', str(e))
    
    return False

def main():
    """Run quick notification check."""
    now = datetime.now(timezone.utc)
    state = load_state()
    
    print(f"🔔 Notification Check — {now.strftime('%H:%M UTC')}")
    print("-" * 40)
    
    # Check Moltbook (quick timeout)
    found = check_moltbook()
    
    if found:
        print("✨ NEW ACTIVITY DETECTED on Moltbook!")
    else:
        print("📭 No new notifications")
    
    # Update state
    state["lastChecks"]["moltbook"] = int(now.timestamp())
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)
    
    print(f"\nLogged to: {NOTIFY_LOG}")
    return 0 if not found else 1  # Return 1 if activity found (for cron alerting)

if __name__ == "__main__":
    sys.exit(main())
