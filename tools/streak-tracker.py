#!/usr/bin/env python3
"""
streak-tracker.py — Daily revenue habit streak tracker

Usage:
    python3 tools/streak-tracker.py        # Show current streak
    python3 tools/streak-tracker.py check  # Check in for today
    python3 tools/streak-tracker.py reset  # Reset streak (new attempt)
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path

STREAK_FILE = Path.home() / ".openclaw" / "workspace" / ".streak_data.json"

def load_data():
    if STREAK_FILE.exists():
        with open(STREAK_FILE) as f:
            return json.load(f)
    return {
        "current_streak": 0,
        "best_streak": 0,
        "last_check": None,
        "total_days": 0,
        "revenue_sent": []
    }

def save_data(data):
    STREAK_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(STREAK_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def show_streak():
    data = load_data()
    
    print("🔥 Revenue Habit Streak")
    print("=" * 30)
    print(f"Current streak: {data['current_streak']} days")
    print(f"Best streak: {data['best_streak']} days")
    print(f"Total active days: {data['total_days']}")
    
    if data['last_check']:
        last = datetime.fromisoformat(data['last_check'])
        today = datetime.now().date()
        days_since = (today - last.date()).days
        
        if days_since == 0:
            print("✅ Checked in today")
        elif days_since == 1:
            print("⚠️  Check in today to keep streak alive!")
        else:
            print(f"❌ Streak broken ({days_since} days missed)")
    else:
        print("🆕 Start your streak: streak-tracker.py check")
    
    if data['revenue_sent']:
        total = sum(data['revenue_sent'])
        print(f"\n💰 Revenue sent this week: ${total:,.0f}")

def check_in():
    data = load_data()
    today = datetime.now().date()
    
    if data['last_check']:
        last = datetime.fromisoformat(data['last_check']).date()
        days_since = (today - last).days
        
        if days_since == 0:
            print("✅ Already checked in today!")
            return
        elif days_since == 1:
            data['current_streak'] += 1
            print(f"🔥 Streak continued! {data['current_streak']} days")
        else:
            data['current_streak'] = 1
            print(f"🔄 Streak reset. Day 1 begins!")
    else:
        data['current_streak'] = 1
        print(f"🎉 Streak started! Day 1!")
    
    data['last_check'] = datetime.now().isoformat()
    data['total_days'] += 1
    
    if data['current_streak'] > data['best_streak']:
        data['best_streak'] = data['current_streak']
        print(f"🏆 New best streak! {data['best_streak']} days")
    
    save_data(data)
    
    print(f"\nNext: Send one message, then check in tomorrow!")

def reset():
    data = load_data()
    data['current_streak'] = 0
    data['last_check'] = None
    save_data(data)
    print("🔄 Streak reset. Start fresh anytime with: streak-tracker.py check")

if __name__ == "__main__":
    import sys
    
    cmd = sys.argv[1] if len(sys.argv) > 1 else "show"
    
    if cmd == "check":
        check_in()
    elif cmd == "reset":
        reset()
    else:
        show_streak()
