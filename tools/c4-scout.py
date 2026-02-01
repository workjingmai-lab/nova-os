#!/usr/bin/env python3
"""
c4-scout.py — Code4rena Contest Monitor
Tracks active audits, prize pools, and optimal entry timing
"""

import json
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

C4_DATA = Path("data/code4rena.json")
C4_DATA.parent.mkdir(parents=True, exist_ok=True)

def load_contests():
    """Load tracked contests."""
    if C4_DATA.exists():
        with open(C4_DATA) as f:
            return json.load(f)
    return {"contests": [], "last_check": None}

def save_contests(data):
    """Save contest data."""
    data["last_check"] = datetime.utcnow().isoformat()
    with open(C4_DATA, "w") as f:
        json.dump(data, f, indent=2)

def add_contest(name, prize_pool, start_date, end_date, scope_url, difficulty="medium"):
    """Add a contest to track."""
    data = load_contests()
    contest = {
        "id": f"c4_{len(data['contests']) + 1:03d}",
        "name": name,
        "prize_pool_usd": prize_pool,
        "start": start_date,
        "end": end_date,
        "scope_url": scope_url,
        "difficulty": difficulty,
        "status": "upcoming",  # upcoming, active, ended
        "my_status": "watching",  # watching, preparing, participating, submitted
        "findings": [],
        "notes": ""
    }
    data["contests"].append(contest)
    save_contests(data)
    return contest["id"]

def update_contest_status():
    """Update status based on dates."""
    data = load_contests()
    now = datetime.utcnow()
    
    for contest in data["contests"]:
        try:
            start = datetime.fromisoformat(contest["start"].replace("Z", "+00:00")).replace(tzinfo=None)
            end = datetime.fromisoformat(contest["end"].replace("Z", "+00:00")).replace(tzinfo=None)
            
            if now < start:
                contest["status"] = "upcoming"
            elif start <= now <= end:
                contest["status"] = "active"
            else:
                contest["status"] = "ended"
                
            # Calculate time remaining
            if contest["status"] == "upcoming":
                contest["starts_in_hours"] = int((start - now).total_seconds() / 3600)
            elif contest["status"] == "active":
                contest["ends_in_hours"] = int((end - now).total_seconds() / 3600)
        except:
            pass
    
    save_contests(data)
    return data

def get_active():
    """Get currently active contests."""
    data = update_contest_status()
    return [c for c in data["contests"] if c["status"] == "active"]

def get_upcoming(hours=168):
    """Get upcoming contests starting within N hours."""
    data = update_contest_status()
    upcoming = []
    for c in data["contests"]:
        if c.get("starts_in_hours") and c["starts_in_hours"] <= hours:
            upcoming.append(c)
    return upcoming

def recommend_contest():
    """Recommend best contest for Nova to enter."""
    data = update_contest_status()
    
    # Priority: active contests first, then upcoming within 48h
    candidates = get_active()
    if not candidates:
        candidates = get_upcoming(48)
    
    if not candidates:
        return None
    
    # Score: prefer smaller pools for first contest, beginner difficulty
    scored = []
    for c in candidates:
        score = 0
        # Prefer beginner difficulty
        if c.get("difficulty") == "beginner":
            score += 100
        # Smaller pools = less competition for beginners
        pool = c.get("prize_pool_usd", 50000)
        if pool < 20000:
            score += 50
        elif pool < 50000:
            score += 25
        # Prefer watching -> preparing -> participating status
        status = c.get("my_status", "")
        if status == "preparing":
            score += 75
        elif status == "watching":
            score += 25
        
        scored.append((score, c))
    
    scored.sort(reverse=True)
    return scored[0][1] if scored else None

def generate_briefing():
    """Generate daily briefing for Nova."""
    update_contest_status()
    
    active = get_active()
    upcoming = get_upcoming(72)  # Next 72 hours
    recommended = recommend_contest()
    
    lines = ["# Code4rena Daily Briefing"]
    lines.append(f"Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}\n")
    
    if active:
        lines.append(f"## 🔥 Active Contests ({len(active)})")
        for c in active:
            hours = c.get("ends_in_hours", 0)
            lines.append(f"- **{c['name']}**: ${c['prize_pool_usd']:,} pool | Ends in {hours}h | Status: {c['my_status']}")
        lines.append("")
    
    if upcoming:
        lines.append(f"## ⏰ Starting Soon ({len(upcoming)} within 72h)")
        for c in upcoming:
            hours = c.get("starts_in_hours", 0)
            lines.append(f"- **{c['name']}**: ${c['prize_pool_usd']:,} | Starts in {hours}h | {c['difficulty']}")
        lines.append("")
    
    if recommended:
        lines.append("## 🎯 Recommended Next Action")
        lines.append(f"**{recommended['name']}**")
        lines.append(f"- Prize pool: ${recommended['prize_pool_usd']:,}")
        lines.append(f"- Difficulty: {recommended['difficulty']}")
        lines.append(f"- Your status: {recommended['my_status']}")
        lines.append(f"- Scope: {recommended['scope_url']}")
        if recommended.get('ends_in_hours'):
            lines.append(f"- Ends in: {recommended['ends_in_hours']} hours")
        elif recommended.get('starts_in_hours'):
            lines.append(f"- Starts in: {recommended['starts_in_hours']} hours")
    else:
        lines.append("## 🎯 No contests match criteria")
        lines.append("Check https://code4rena.com/audits for new announcements")
    
    return "\n".join(lines)

def log_to_diary():
    """Log briefing summary to diary."""
    update_contest_status()
    active_count = len(get_active())
    upcoming_count = len(get_upcoming(72))
    
    diary = Path("diary.md")
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    log_entry = f"\n[{timestamp}] C4 Scout: {active_count} active, {upcoming_count} upcoming (72h)\n"
    
    with open(diary, "a") as f:
        f.write(log_entry)
    
    return active_count, upcoming_count

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python c4-scout.py [add|active|upcoming|recommend|brief|log]")
        sys.exit(1)
    
    cmd = sys.argv[1]
    
    if cmd == "add":
        # python c4-scout.py add "Contest Name" 25000 2026-02-05T00:00:00Z 2026-02-12T00:00:00Z https://...
        if len(sys.argv) < 7:
            print("Usage: add <name> <prize> <start> <end> <scope_url> [difficulty]")
            sys.exit(1)
        cid = add_contest(
            sys.argv[2], 
            int(sys.argv[3]), 
            sys.argv[4], 
            sys.argv[5], 
            sys.argv[6],
            sys.argv[7] if len(sys.argv) > 7 else "medium"
        )
        print(f"Added contest: {cid}")
    
    elif cmd == "active":
        for c in get_active():
            print(f"{c['name']}: ${c['prize_pool_usd']:,} | {c.get('ends_in_hours', '?')}h remaining")
    
    elif cmd == "upcoming":
        hours = int(sys.argv[2]) if len(sys.argv) > 2 else 72
        for c in get_upcoming(hours):
            print(f"{c['name']}: ${c['prize_pool_usd']:,} | {c.get('starts_in_hours', '?')}h until start")
    
    elif cmd == "recommend":
        rec = recommend_contest()
        if rec:
            print(f"Recommended: {rec['name']} (${rec['prize_pool_usd']:,})")
            print(f"Difficulty: {rec['difficulty']}")
            print(f"URL: {rec['scope_url']}")
        else:
            print("No contests match criteria")
    
    elif cmd == "brief":
        print(generate_briefing())
    
    elif cmd == "log":
        active, upcoming = log_to_diary()
        print(f"[{datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')}] C4_SCOUT_OK")
        print(f"  Active: {active}")
        print(f"  Upcoming (72h): {upcoming}")
    
    else:
        print(f"Unknown command: {cmd}")
