#!/usr/bin/env python3
"""
daily-snapshot.py — One-command status dashboard
Shows pipeline, submissions, velocity, and active goals in compact view.
Usage: python3 daily-snapshot.py
"""

import json
import os
import glob
from datetime import datetime, timedelta

def load_revenue_data():
    """Load from revenue-pipeline.json or return defaults."""
    if os.path.exists("revenue-pipeline.json"):
        with open("revenue-pipeline.json") as f:
            return json.load(f)
    return {"grants": [], "services": [], "bounties": [], "meta": {}}

def load_scoreboard():
    """Load from revenue-scoreboard.json or return defaults."""
    if os.path.exists("revenue-scoreboard.json"):
        with open("revenue-scoreboard.json") as f:
            return json.load(f)
    return {"submitted": 0, "won": 0, "lost": 0, "history": []}

def count_today_work_blocks():
    """Count work blocks from today's diary."""
    today_file = f"memory/{datetime.now().strftime('%Y-%m-%d')}.md"
    if not os.path.exists(today_file):
        return 0
    
    with open(today_file) as f:
        content = f.read()
    return content.lower().count("work block")

def get_velocity():
    """Calculate blocks per hour from today.md timestamps."""
    today_file = f"memory/{datetime.now().strftime('%Y-%m-%d')}.md"
    if not os.path.exists(today_file):
        return 0
    
    with open(today_file) as f:
        content = f.read()
    
    # Find all time references
    import re
    times = re.findall(r'(\d{1,2}):(\d{2})\s*(AM|PM)', content, re.IGNORECASE)
    if len(times) < 2:
        return 0
    
    # Convert to minutes from midnight
    def to_minutes(h, m, ap):
        h = int(h)
        m = int(m)
        if ap.upper() == "PM" and h != 12:
            h += 12
        if ap.upper() == "AM" and h == 12:
            h = 0
        return h * 60 + m
    
    minutes = [to_minutes(h, m, ap) for h, m, ap in times]
    if not minutes:
        return 0
    
    time_span_hours = (max(minutes) - min(minutes)) / 60
    blocks = len(re.findall(r'Work Block \d+', content))
    
    if time_span_hours < 0.5:
        return blocks * 2  # Estimate if less than 30 min
    return round(blocks / time_span_hours, 1)

def get_weekly_blocks():
    """Count work blocks from this week."""
    week_total = 0
    for i in range(7):
        date = (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d')
        filepath = f"memory/{date}.md"
        if os.path.exists(filepath):
            with open(filepath) as f:
                content = f.read()
            week_total += content.lower().count("work block")
    return week_total

def format_money(n):
    """Format number as $X.YK or $X."""
    if n >= 1000:
        return f"${n/1000:.1f}K"
    return f"${n}"

def main():
    print("=" * 50)
    print("📊 DAILY SNAPSHOT — Nova Status Dashboard")
    print("=" * 50)
    
    # Revenue Pipeline
    data = load_revenue_data()
    
    # Calculate from grants, services, bounties
    grants = data.get("grants", [])
    services = data.get("services", [])
    bounties = data.get("bounties", [])
    
    ready = (
        sum(g.get("amount", 0) for g in grants if g.get("status") == "ready") +
        sum(s.get("potential", 0) for s in services if s.get("status") == "ready") +
        sum(b.get("amount", 0) for b in bounties if b.get("status") == "ready")
    )
    submitted = sum(g.get("amount", 0) for g in grants if g.get("status") == "submitted")
    
    print(f"\n💰 REVENUE")
    print(f"   Pipeline (ready):  {format_money(ready)}")
    print(f"   Submitted:         {format_money(submitted)}")
    print(f"   Conversion:        {len(data.get('submissions', []))} apps → {len(data.get('wins', []))} wins")
    
    # Velocity
    today_blocks = count_today_work_blocks()
    velocity = get_velocity()
    week_blocks = get_weekly_blocks()
    
    print(f"\n⚡ VELOCITY")
    print(f"   Today's blocks:    {today_blocks}")
    print(f"   Blocks/hour:       {velocity}")
    print(f"   Weekly total:      {week_blocks}")
    
    # Pipeline Breakdown
    print(f"\n📋 PIPELINE BREAKDOWN")
    
    grant_ready = sum(g.get("amount", 0) for g in grants if g.get("status") == "ready")
    grant_sub = sum(g.get("amount", 0) for g in grants if g.get("status") == "submitted")
    svc_ready = sum(s.get("potential", 0) for s in services if s.get("status") == "ready")
    bounty_ready = sum(b.get("amount", 0) for b in bounties if b.get("status") == "ready")
    bounty_blocked = sum(b.get("amount", 0) for b in bounties if b.get("status") == "blocked")
    
    breakdown = [
        ("Grants (ready)", grant_ready),
        ("Grants (sub)", grant_sub),
        ("Services", svc_ready),
        ("Bounties", bounty_ready),
        ("Blocked", bounty_blocked),
    ]
    
    for cat, rev in breakdown:
        if rev > 0:
            bar = "█" * int(rev / 50000)  # One block per $50K
            print(f"   {cat:14} {format_money(rev):>6} {bar}")
    
    # Active Goals
    print(f"\n🎯 ACTIVE GOALS")
    if os.path.exists("goals/active.md"):
        with open("goals/active.md") as f:
            content = f.read()
        # Find unchecked items
        import re
        tasks = re.findall(r'\- \[ \](.+)', content)
        for task in tasks[:3]:  # Show top 3
            print(f"   ☐ {task.strip()[:40]}")
        if len(tasks) > 3:
            print(f"   ... and {len(tasks) - 3} more")
    
    print(f"\n" + "=" * 50)
    print(f"Generated: {datetime.now().strftime('%H:%M UTC')}")
    print("=" * 50)

if __name__ == "__main__":
    main()
