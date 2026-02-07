#!/usr/bin/env python3
"""
moltbook-monitor.py - Moltbook posting availability monitor

Tracks rate limit status and estimates when posting will be available again.
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path

STATE_FILE = Path(__file__).parent / ".moltbook_state.json"

def load_state():
    if STATE_FILE.exists():
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"lastAttempt": None, "lastSuccess": None, "consecutiveFails": 0}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def check_status():
    state = load_state()
    now = datetime.utcnow()
    
    print("📊 Moltbook Rate Limit Monitor")
    print("=" * 40)
    
    if state["lastSuccess"]:
        last_success = datetime.fromisoformat(state["lastSuccess"])
        hours_since = (now - last_success).total_seconds() / 3600
        print(f"✅ Last post: {hours_since:.1f}h ago")
    else:
        print("⚠️  No successful posts recorded")
    
    if state["lastAttempt"]:
        last_attempt = datetime.fromisoformat(state["lastAttempt"])
        minutes_since = (now - last_attempt).total_seconds() / 60
        print(f"🔄 Last attempt: {minutes_since:.0f}m ago")
    
    # Rate limit estimation (typical: 1 post per 30-60 min based on patterns)
    if state["lastSuccess"]:
        next_available = last_success + timedelta(minutes=45)
        if now < next_available:
            wait_minutes = (next_available - now).total_seconds() / 60
            print(f"⏳ Rate limit: ~{wait_minutes:.0f}m remaining")
            print(f"🕐 Next slot: ~{(now + timedelta(minutes=wait_minutes)).strftime('%H:%M')} UTC")
        else:
            print("✅ Posting should be available")
    else:
        print("❓ Unknown rate limit status")
    
    print(f"\n📈 Consecutive fails: {state['consecutiveFails']}")

def record_attempt(success=False):
    state = load_state()
    now = datetime.utcnow().isoformat()
    
    state["lastAttempt"] = now
    if success:
        state["lastSuccess"] = now
        state["consecutiveFails"] = 0
    else:
        state["consecutiveFails"] += 1
    
    save_state(state)
    print(f"{'✅' if success else '❌'} Attempt recorded")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "record":
        success = len(sys.argv) > 2 and sys.argv[2] == "success"
        record_attempt(success)
    else:
        check_status()
