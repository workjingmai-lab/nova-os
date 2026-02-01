#!/usr/bin/env python3
"""
Nova Notification System
Monitors external services and alerts on important events.
Week 2 Goal: Build notification system for Moltbook mentions, grants, etc.
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

class NotificationSystem:
    """Simple notification manager with persistence."""
    
    def __init__(self, state_file: str = ".notification_state.json"):
        self.state_file = Path(state_file)
        self.state = self._load_state()
        self.notifications = []
    
    def _load_state(self) -> dict:
        """Load persistent state."""
        if self.state_file.exists():
            return json.loads(self.state_file.read_text())
        return {
            "last_check": {},
            "dismissed": [],
            "created_at": datetime.now().isoformat()
        }
    
    def _save_state(self):
        """Save persistent state."""
        self.state_file.write_text(json.dumps(self.state, indent=2))
    
    def check_moltbook_mentions(self) -> list:
        """Check for new mentions on Moltbook (placeholder for API)."""
        # TODO: Implement actual Moltbook API call
        # For now, return mock data structure
        return []
    
    def check_grants(self) -> list:
        """Check for new grant opportunities."""
        grants = []
        
        # Check Gitcoin grants (placeholder)
        # TODO: Implement actual scraping or API
        
        # Check Web3 Foundation (placeholder)
        # TODO: Implement
        
        return grants
    
    def check_github_stars(self, repo: str) -> int:
        """Check for new GitHub stars."""
        # TODO: Implement GitHub API call
        return 0
    
    def check_system_health(self) -> dict:
        """Check local system health."""
        import shutil
        
        disk = shutil.disk_usage("/")
        health = {
            "disk_percent": (disk.used / disk.total) * 100,
            "disk_ok": (disk.used / disk.total) < 0.9,
            "timestamp": datetime.now().isoformat()
        }
        
        if not health["disk_ok"]:
            self.add_notification(
                level="warning",
                source="system",
                message=f"Disk usage at {health['disk_percent']:.1f}%"
            )
        
        return health
    
    def add_notification(self, level: str, source: str, message: str, 
                         action: Optional[str] = None):
        """Add a new notification."""
        notification = {
            "id": f"{source}_{datetime.now().timestamp()}",
            "level": level,  # info, warning, urgent
            "source": source,  # moltbook, github, system, grants
            "message": message,
            "action": action,  # Optional action URL or command
            "created_at": datetime.now().isoformat(),
            "read": False
        }
        self.notifications.append(notification)
        return notification
    
    def get_unread(self, min_level: str = "info") -> list:
        """Get unread notifications at or above level."""
        levels = {"info": 0, "warning": 1, "urgent": 2}
        min_val = levels.get(min_level, 0)
        
        return [
            n for n in self.notifications 
            if not n["read"] and levels.get(n["level"], 0) >= min_val
        ]
    
    def mark_read(self, notification_id: str):
        """Mark a notification as read."""
        for n in self.notifications:
            if n["id"] == notification_id:
                n["read"] = True
                break
        self._save_state()
    
    def run_all_checks(self) -> list:
        """Run all monitoring checks."""
        # System health
        self.check_system_health()
        
        # External services (when APIs available)
        # self.check_moltbook_mentions()
        # self.check_grants()
        # self.check_github_stars("nova-agent")
        
        self._save_state()
        return self.get_unread()
    
    def format_digest(self) -> str:
        """Format unread notifications as text digest."""
        unread = self.get_unread()
        if not unread:
            return "No new notifications."
        
        lines = [f"📬 {len(unread)} Notification(s)", "─" * 30]
        
        for n in unread:
            emoji = {"info": "ℹ️", "warning": "⚠️", "urgent": "🚨"}.get(n["level"], "•")
            lines.append(f"{emoji} [{n['source'].upper()}] {n['message']}")
        
        return "\n".join(lines)


def main():
    """CLI entry point."""
    import sys
    
    notifier = NotificationSystem()
    
    if len(sys.argv) > 1 and sys.argv[1] == "check":
        # Run all checks and output digest
        notifier.run_all_checks()
        print(notifier.format_digest())
    else:
        # Default: show status
        unread = notifier.get_unread()
        print(f"Notification system ready. {len(unread)} unread.")
        print(f"State file: {notifier.state_file}")


if __name__ == "__main__":
    main()
