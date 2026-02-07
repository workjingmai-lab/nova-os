#!/usr/bin/env python3
"""
revenue-scoreboard.py — Daily Revenue Conversion Tracker
Makes the invisible visible. Every submission tracked.
"""

import json
import os
from datetime import datetime, timedelta

PIPELINE_FILE = "revenue-pipeline.json"
SCOREBOARD_FILE = "revenue-scoreboard.json"

def load_json(path):
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return {}

def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def get_scoreboard():
    """Get or initialize scoreboard."""
    return load_json(SCOREBOARD_FILE) or {
        "created": datetime.now().isoformat(),
        "daily": {},
        "totals": {"submitted": 0, "won": 0, "lost": 0}
    }

def update_daily_entry(scoreboard, submitted=0, won=0, lost=0):
    """Update today's entry."""
    today = datetime.now().strftime("%Y-%m-%d")
    
    if today not in scoreboard["daily"]:
        scoreboard["daily"][today] = {"submitted": 0, "won": 0, "lost": 0}
    
    scoreboard["daily"][today]["submitted"] += submitted
    scoreboard["daily"][today]["won"] += won
    scoreboard["daily"][today]["lost"] += lost
    
    scoreboard["totals"]["submitted"] += submitted
    scoreboard["totals"]["won"] += won
    scoreboard["totals"]["lost"] += lost
    
    return scoreboard

def display_scoreboard():
    """Display the revenue conversion scoreboard."""
    pipeline = load_json(PIPELINE_FILE)
    scoreboard = get_scoreboard()
    
    today = datetime.now().strftime("%Y-%m-%d")
    today_data = scoreboard["daily"].get(today, {"submitted": 0, "won": 0, "lost": 0})
    
    ready = pipeline.get("totals", {}).get("ready", 0)
    submitted_total = scoreboard["totals"]["submitted"]
    won_total = scoreboard["totals"]["won"]
    
    # Calculate conversion rate
    if submitted_total > 0:
        conversion_rate = (won_total / submitted_total) * 100
    else:
        conversion_rate = 0
    
    # Progress bar calculation
    total_pipeline = ready + submitted_total
    if total_pipeline > 0:
        submitted_pct = min(50, int((submitted_total / total_pipeline) * 50))
        ready_pct = min(50, int((ready / total_pipeline) * 50))
    else:
        submitted_pct = 0
        ready_pct = 50
    
    bar_submitted = "█" * submitted_pct
    bar_ready = "░" * ready_pct
    
    print()
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║           NOVA'S REVENUE CONVERSION SCOREBOARD               ║")
    print(f"║              {datetime.now().strftime('%A, %B %d, %Y')}                    ║")
    print("╠══════════════════════════════════════════════════════════════╣")
    print()
    print(f"  TODAY'S PROGRESS:")
    print(f"  ┌─────────────────────────────────────────────────────────┐")
    print(f"  │  Submitted: ${today_data['submitted']:>10,}  Won: ${today_data['won']:>8,}  │")
    print(f"  └─────────────────────────────────────────────────────────┘")
    print()
    print(f"  PIPELINE STATUS:")
    print(f"  ┌─────────────────────────────────────────────────────────┐")
    print(f"  │  Ready:     ${ready:>10,}  [{bar_ready:<50}] │")
    print(f"  │  Submitted: ${submitted_total:>10,}  [{bar_submitted:<50}] │")
    print(f"  │  Won:       ${won_total:>10,}  [{'█' * int(conversion_rate/2):<50}] │")
    print(f"  └─────────────────────────────────────────────────────────┘")
    print(f"                              Conversion: {conversion_rate:.1f}%")
    print()
    print(f"  ALL-TIME TOTALS:")
    print(f"  ┌─────────────────────────────────────────────────────────┐")
    print(f"  │  Total Submitted: ${scoreboard['totals']['submitted']:>12,}                   │")
    print(f"  │  Total Won:       ${scoreboard['totals']['won']:>12,}                   │")
    print(f"  │  Total Lost:      ${scoreboard['totals']['lost']:>12,}                   │")
    print(f"  └─────────────────────────────────────────────────────────┘")
    print()
    print("╚══════════════════════════════════════════════════════════════╝")
    print()
    
    if ready > 0 and submitted_total == 0:
        print("  ⚡  EXECUTION GAP: $" + f"{ready:,}" + " ready but not submitted!")
        print("  💡  Run: python3 service-outreach-execution-guide.md")
        print()

def record_submission(amount, category="service"):
    """Record a new submission."""
    scoreboard = get_scoreboard()
    scoreboard = update_daily_entry(scoreboard, submitted=amount)
    save_json(SCOREBOARD_FILE, scoreboard)
    print(f"✅ Recorded ${amount:,} {category} submission!")

def record_win(amount):
    """Record a won deal."""
    scoreboard = get_scoreboard()
    scoreboard = update_daily_entry(scoreboard, won=amount)
    save_json(SCOREBOARD_FILE, scoreboard)
    print(f"🎉 Recorded ${amount:,} WIN!")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        display_scoreboard()
    elif sys.argv[1] == "submit" and len(sys.argv) >= 3:
        category = sys.argv[3] if len(sys.argv) >= 4 else "service"
        record_submission(int(sys.argv[2]), category)
    elif sys.argv[1] == "win" and len(sys.argv) >= 3:
        record_win(int(sys.argv[2]))
    elif sys.argv[1] == "reset":
        if input("Reset scoreboard? Type 'yes': ") == "yes":
            save_json(SCOREBOARD_FILE, {
                "created": datetime.now().isoformat(),
                "daily": {},
                "totals": {"submitted": 0, "won": 0, "lost": 0}
            })
            print("Scoreboard reset.")
    else:
        print("Usage:")
        print("  python3 revenue-scoreboard.py              # Display scoreboard")
        print("  python3 revenue-scoreboard.py submit 5000  # Record $5K submission")
        print("  python3 revenue-scoreboard.py win 10000    # Record $10K win")
