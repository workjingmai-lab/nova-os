#!/usr/bin/env python3
"""
Moltbook Monitor - Auto-recovery tracking for Moltbook API
Tracks API status and notifies when back online
"""

import urllib.request
import urllib.error
import json
import time
from datetime import datetime
from pathlib import Path

API_KEY = "moltbook_sk_xSwszjAM8vLLaa7VsSZVgNWp5a-R5XqD"
BASE_URL = "https://www.moltbook.com/api/v1"
STATE_FILE = Path(".moltbook_state.json")

def check_status():
    """Check Moltbook API health"""
    try:
        req = urllib.request.Request(
            f"{BASE_URL}/agents/status",
            headers={"Authorization": f"Bearer {API_KEY}"}
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            return resp.status == 200 and data.get("success", False)
    except:
        return False

def check_feed():
    """Check if feed endpoint is accessible"""
    try:
        req = urllib.request.Request(
            f"{BASE_URL}/feed?limit=1",
            headers={"Authorization": f"Bearer {API_KEY}"}
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status == 200
    except:
        return False

def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"checks": [], "last_online": None, "downtime_start": "2026-02-01T09:00:00Z"}

def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2))

def main():
    state = load_state()
    
    status_ok = check_status()
    feed_ok = check_feed()
    
    check = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "status_endpoint": status_ok,
        "feed_endpoint": feed_ok,
        "fully_operational": status_ok and feed_ok
    }
    
    state["checks"].append(check)
    state["checks"] = state["checks"][-50:]  # Keep last 50
    
    if check["fully_operational"] and not state.get("was_online"):
        state["last_online"] = check["timestamp"]
        state["recovery_detected"] = True
        print("🎉 MOLBOOK IS BACK ONLINE!")
    else:
        state["recovery_detected"] = False
    
    state["was_online"] = check["fully_operational"]
    save_state(state)
    
    # Summary
    total_checks = len(state["checks"])
    online_checks = sum(1 for c in state["checks"] if c["fully_operational"])
    uptime_pct = (online_checks / total_checks * 100) if total_checks else 0
    
    print(f"Status: {'✅ Online' if check['fully_operational'] else '❌ Offline'}")
    print(f"Status endpoint: {'✅' if status_ok else '❌'}")
    print(f"Feed endpoint: {'✅' if feed_ok else '❌'}")
    print(f"Uptime (last {total_checks} checks): {uptime_pct:.1f}%")
    
    if state.get("recovery_detected"):
        print("\n🚨 RECOVERY DETECTED - Moltbook is back!")

if __name__ == "__main__":
    main()
