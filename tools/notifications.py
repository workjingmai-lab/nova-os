#!/usr/bin/env python3
"""
Nova's Notification System
Checks for mentions, new followers, and important events across platforms.
"""
import json
import requests
import os
from datetime import datetime, timedelta

STATE_FILE = ".notification_state.json"
MOLTBOOK_API = "https://www.moltbook.com/api/v1"
MOLTBOOK_TOKEN = os.environ.get("MOLTBOOK_TOKEN", "")

class NotificationSystem:
    def __init__(self):
        self.state = self._load_state()
        self.notifications = []
    
    def _load_state(self):
        if os.path.exists(STATE_FILE):
            with open(STATE_FILE) as f:
                return json.load(f)
        return {
            "lastCheck": None,
            "lastMentionId": None,
            "lastFollowerCount": 0,
            "mutes": []
        }
    
    def _save_state(self):
        with open(STATE_FILE, "w") as f:
            json.dump(self.state, f, indent=2)
    
    def check_moltbook_mentions(self):
        """Check for new mentions on Moltbook."""
        if not MOLTBOOK_TOKEN:
            return  # Skip if no token
        
        try:
            headers = {"Authorization": f"Bearer {MOLTBOOK_TOKEN}"}
            resp = requests.get(f"{MOLTBOOK_API}/agents/notifications", headers=headers, timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                for notif in data.get("notifications", []):
                    if notif["id"] != self.state.get("lastMentionId"):
                        self.notifications.append({
                            "platform": "moltbook",
                            "type": notif.get("type", "mention"),
                            "message": notif.get("message", "New notification"),
                            "timestamp": datetime.now().isoformat()
                        })
                if data.get("notifications"):
                    self.state["lastMentionId"] = data["notifications"][0]["id"]
        except Exception as e:
            print(f"Moltbook check failed: {e}")
    
    def check_grants(self):
        """Check for new grant opportunities or status updates."""
        # TODO: Integrate with grant APIs or RSS feeds
        pass
    
    def check_github(self):
        """Check for stars, PRs, or issues on GitHub repos."""
        # TODO: Use GitHub API to check repo activity
        pass
    
    def run(self):
        """Execute all notification checks."""
        print(f"🔔 Nova Notification System — {datetime.now().isoformat()}")
        
        self.check_moltbook_mentions()
        self.check_grants()
        self.check_github()
        
        # Save state
        self.state["lastCheck"] = datetime.now().isoformat()
        self._save_state()
        
        # Report
        if self.notifications:
            print(f"\n📬 {len(self.notifications)} new notification(s):")
            for n in self.notifications:
                print(f"  [{n['platform'].upper()}] {n['type']}: {n['message']}")
        else:
            print("\n✅ No new notifications")
        
        return self.notifications

if __name__ == "__main__":
    notifier = NotificationSystem()
    notifier.run()
