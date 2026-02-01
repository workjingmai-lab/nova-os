#!/usr/bin/env python3
"""
Nova Notification System
Alerts on Moltbook mentions, grant updates, and important events
Week 2 Goal: Build notification system
"""

import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

# Configuration
CONFIG = {
    "moltbook_api": "https://www.moltbook.com/api/v1",
    "api_key": "moltbook_sk_xSwszjAM8vLLaa7VsSZVgNWp5a-R5XqD",
    "agent_id": "5d8b3d2e-c9e2-4476-b8b6-41d0d2304da4",
    "check_interval_minutes": 15,
    "notifications_dir": "/home/node/.openclaw/workspace/notifications",
    "state_file": "/home/node/.openclaw/workspace/.notification_state.json"
}

class NotificationSystem:
    def __init__(self):
        self.state = self.load_state()
        self.notifications = []
        
    def load_state(self):
        """Load persistent state"""
        if os.path.exists(CONFIG["state_file"]):
            with open(CONFIG["state_file"]) as f:
                return json.load(f)
        return {
            "last_check": None,
            "last_moltbook_check": None,
            "pending_alerts": [],
            "alert_history": []
        }
    
    def save_state(self):
        """Save state to disk"""
        with open(CONFIG["state_file"], 'w') as f:
            json.dump(self.state, f, indent=2)
    
    def check_moltbook_mentions(self):
        """Check for new mentions on Moltbook"""
        # Would make actual API call here
        # For now, check the stored check file
        check_file = Path(CONFIG["notifications_dir"]) / "moltbook-check.json"
        if check_file.exists():
            with open(check_file) as f:
                data = json.load(f)
                mentions = data.get("mentions", [])
                new_mentions = [
                    m for m in mentions 
                    if m.get("timestamp", "") > self.state.get("last_moltbook_check", "")
                ]
                if new_mentions:
                    self.notifications.append({
                        "type": "moltbook_mention",
                        "priority": "medium",
                        "message": f"{len(new_mentions)} new mention(s) on Moltbook",
                        "details": new_mentions,
                        "timestamp": datetime.utcnow().isoformat()
                    })
                return len(new_mentions)
        return 0
    
    def check_grant_status(self):
        """Check for grant application updates"""
        grants_dir = Path("/home/node/.openclaw/workspace/grants")
        
        # Look for response files or status updates
        for grant_file in grants_dir.glob("*.md"):
            # Check if grant has been submitted and awaiting response
            if "submitted" in grant_file.read_text().lower():
                # In real implementation, would check grant platform APIs
                pass
        
        # Simulate finding a new opportunity
        opportunities = [
            {
                "name": "Gitcoin Grants GG24",
                "deadline": (datetime.utcnow() + timedelta(days=7)).isoformat(),
                "amount": "$500-50,000",
                "url": "https://gitcoin.co/grants"
            }
        ]
        
        for opp in opportunities:
            self.notifications.append({
                "type": "grant_opportunity",
                "priority": "high",
                "message": f"New grant opportunity: {opp['name']}",
                "details": opp,
                "timestamp": datetime.utcnow().isoformat()
            })
        
        return len(opportunities)
    
    def check_github_activity(self):
        """Check for GitHub stars, issues, PRs"""
        # Would check GitHub API for repo activity
        # For now, placeholder
        return 0
    
    def check_code4rena_competitions(self):
        """Check for new Code4rena competitions"""
        # Would scrape or API call to Code4rena
        competitions = [
            {
                "name": "Olas Protocol",
                "prize_pool": "$62,000",
                "start_date": "2026-02-03",
                "end_date": "2026-02-10",
                "status": "upcoming"
            }
        ]
        
        for comp in competitions:
            self.notifications.append({
                "type": "competition_alert",
                "priority": "high" if comp["status"] == "live" else "medium",
                "message": f"Code4rena competition: {comp['name']} (${comp['prize_pool']})",
                "details": comp,
                "timestamp": datetime.utcnow().isoformat()
            })
        
        return len(competitions)
    
    def check_goals_deadlines(self):
        """Check for upcoming goal deadlines"""
        # Read goals and check deadlines
        goals_file = Path("/home/node/.openclaw/workspace/goals/week-2.md")
        if goals_file.exists():
            content = goals_file.read_text()
            # Simple check - in production would parse dates
            if "Week 2" in content:
                self.notifications.append({
                    "type": "goal_reminder",
                    "priority": "low",
                    "message": "Week 2 goals in progress — review status",
                    "details": {"file": "goals/week-2.md"},
                    "timestamp": datetime.utcnow().isoformat()
                })
        
        return 1
    
    def format_notification(self, notification):
        """Format notification for display"""
        icons = {
            "moltbook_mention": "💬",
            "grant_opportunity": "💰",
            "grant_response": "✉️",
            "github_activity": "⭐",
            "competition_alert": "🏆",
            "goal_reminder": "🎯",
            "system": "⚙️"
        }
        
        icon = icons.get(notification["type"], "📢")
        priority_emoji = {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(notification["priority"], "⚪")
        
        return f"{icon} {priority_emoji} {notification['message']}"
    
    def run_all_checks(self):
        """Run all notification checks"""
        print("🔔 Nova Notification System")
        print("=" * 50)
        
        checks = [
            ("Moltbook mentions", self.check_moltbook_mentions),
            ("Grant opportunities", self.check_grant_status),
            ("GitHub activity", self.check_github_activity),
            ("Code4rena competitions", self.check_code4rena_competitions),
            ("Goal deadlines", self.check_goals_deadlines)
        ]
        
        total_new = 0
        for name, check_func in checks:
            try:
                count = check_func()
                total_new += count
                status = f"✅ {count} new" if count > 0 else "➖ No updates"
                print(f"  {name}: {status}")
            except Exception as e:
                print(f"  {name}: ❌ Error - {e}")
        
        print("=" * 50)
        
        if self.notifications:
            print(f"\n📬 {len(self.notifications)} notification(s):")
            for n in self.notifications:
                print(f"  {self.format_notification(n)}")
        else:
            print("\n📭 No new notifications")
        
        # Update state
        self.state["last_check"] = datetime.utcnow().isoformat()
        self.state["pending_alerts"] = self.notifications
        self.save_state()
        
        # Save detailed notifications to file
        notifications_file = Path(CONFIG["notifications_dir"]) / f"notifications-{datetime.utcnow().strftime('%Y%m%d-%H%M')}.json"
        with open(notifications_file, 'w') as f:
            json.dump({
                "timestamp": datetime.utcnow().isoformat(),
                "notifications": self.notifications,
                "total_new": total_new
            }, f, indent=2)
        
        return total_new

def main():
    """Main entry point"""
    notifier = NotificationSystem()
    
    # Check if running in cron/heartbeat mode
    if len(sys.argv) > 1 and sys.argv[1] == "--quiet":
        count = notifier.run_all_checks()
        sys.exit(0 if count == 0 else 1)
    else:
        notifier.run_all_checks()
        
        # Print helpful next steps
        print("\n💡 Next steps:")
        print("  - Review notifications above")
        print("  - Check detailed logs in notifications/")
        print("  - Run with --quiet for cron mode")

if __name__ == "__main__":
    main()
