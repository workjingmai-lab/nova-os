#!/usr/bin/env python3
"""
Nova Alert System
Monitors for mentions, opportunities, and triggers
"""

import json
import time
from datetime import datetime, timedelta
from pathlib import Path

ALERT_CONFIG = {
    "moltbook": {
        "check_interval_minutes": 15,
        "mention_keywords": ["nova", "agent", "ai"],
        "last_check": None
    },
    "grants": {
        "sources": [
            "gitcoin.co/grants",
            "esp.ethereum.foundation",
            "optimism.io/grants"
        ],
        "keywords": ["ai", "agent", "automation", "security"],
        "check_interval_hours": 6
    },
    "bounties": {
        "sources": [
            "code4rena.com",
            "immunefi.com",
            " Sherlock.dev"
        ],
        "check_interval_hours": 4
    }
}

class AlertManager:
    def __init__(self, state_file=".alert_state.json"):
        self.state_file = Path(state_file)
        self.state = self._load_state()
    
    def _load_state(self):
        if self.state_file.exists():
            return json.loads(self.state_file.read_text())
        return {
            "last_moltbook_check": None,
            "last_grant_check": None,
            "last_bounty_check": None,
            "pending_alerts": []
        }
    
    def _save_state(self):
        self.state_file.write_text(json.dumps(self.state, indent=2))
    
    def check_moltbook(self):
        """Check for mentions on Moltbook"""
        now = datetime.utcnow()
        
        # Check if it's time
        last = self.state.get("last_moltbook_check")
        if last:
            last_dt = datetime.fromisoformat(last)
            if now - last_dt < timedelta(minutes=ALERT_CONFIG["moltbook"]["check_interval_minutes"]):
                return []
        
        # TODO: Actual API call when available
        # For now, mark as checked
        self.state["last_moltbook_check"] = now.isoformat()
        self._save_state()
        
        return ["⚠️ Moltbook API unavailable — check skipped"]
    
    def check_grants(self):
        """Check for new grant opportunities"""
        now = datetime.utcnow()
        
        last = self.state.get("last_grant_check")
        if last:
            last_dt = datetime.fromisoformat(last)
            if now - last_dt < timedelta(hours=ALERT_CONFIG["grants"]["check_interval_hours"]):
                return []
        
        # Track that we checked
        self.state["last_grant_check"] = now.isoformat()
        self._save_state()
        
        # Return manual check reminders
        return [
            "💰 Grant check due — visit:",
            "  - gitcoin.co/grants",
            "  - esp.ethereum.foundation", 
            "  - optimism.io/grants"
        ]
    
    def check_bounties(self):
        """Check for security bounties"""
        now = datetime.utcnow()
        
        last = self.state.get("last_bounty_check")
        if last:
            last_dt = datetime.fromisoformat(last)
            if now - last_dt < timedelta(hours=ALERT_CONFIG["bounties"]["check_interval_hours"]):
                return []
        
        self.state["last_bounty_check"] = now.isoformat()
        self._save_state()
        
        return [
            "🎯 Bounty check due — visit:",
            "  - code4rena.com (competitions)",
            "  - immunefi.com (bug bounties)"
        ]
    
    def run_all_checks(self):
        """Run all alert checks"""
        alerts = []
        
        alerts.extend(self.check_moltbook())
        alerts.extend(self.check_grants())
        alerts.extend(self.check_bounties())
        
        return alerts
    
    def status(self):
        """Print current alert system status"""
        print("🔔 Nova Alert System")
        print("=" * 40)
        
        checks = [
            ("Moltbook mentions", self.state.get("last_moltbook_check")),
            ("Grant opportunities", self.state.get("last_grant_check")),
            ("Security bounties", self.state.get("last_bounty_check"))
        ]
        
        for name, last in checks:
            if last:
                last_dt = datetime.fromisoformat(last)
                ago = datetime.utcnow() - last_dt
                print(f"  {name}: {ago.seconds // 60}m ago")
            else:
                print(f"  {name}: Never checked")
        
        pending = len(self.state.get("pending_alerts", []))
        print(f"\nPending alerts: {pending}")

if __name__ == "__main__":
    import sys
    
    alert_mgr = AlertManager()
    
    if len(sys.argv) > 1 and sys.argv[1] == "status":
        alert_mgr.status()
    else:
        alerts = alert_mgr.run_all_checks()
        if alerts:
            print("\n".join(alerts))
        else:
            print("✅ All checks up to date — no alerts")
