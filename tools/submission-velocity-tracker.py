#!/usr/bin/env python3
"""
Submission Velocity Tracker

Track submission velocity over time.
Key metric: submissions per day (not pipeline items).

Usage:
    python3 submission-velocity-tracker.py          # Show velocity
    python3 submission-velocity-tracker.py --add    # Add submission
    python3 submission-velocity-tracker.py --week   # Weekly breakdown
"""

import json
from datetime import datetime, timedelta
from pathlib import Path

DATA_FILE = Path.home() / ".openclaw/workspace/data/submissions.json"

def load_data():
    """Load submission data."""
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"submissions": []}

def save_data(data):
    """Save submission data."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_submission(category="service"):
    """Add a new submission."""
    data = load_data()
    submission = {
        "timestamp": datetime.now().isoformat(),
        "category": category,  # service | grant | bounty
        "value": 0  # Can add value tracking later
    }
    data["submissions"].append(submission)
    save_data(data)
    print(f"✓ Submission added ({category})")

def get_velocity(days=7):
    """Calculate submissions per day over last N days."""
    data = load_data()
    submissions = data["submissions"]

    if not submissions:
        return {"days": days, "total": 0, "per_day": 0.0, "breakdown": {}}

    cutoff = datetime.now() - timedelta(days=days)
    recent = [s for s in submissions if datetime.fromisoformat(s["timestamp"]) > cutoff]

    total = len(recent)
    per_day = total / days

    breakdown = {}
    for s in recent:
        cat = s.get("category", "unknown")
        breakdown[cat] = breakdown.get(cat, 0) + 1

    return {
        "days": days,
        "total": total,
        "per_day": round(per_day, 1),
        "breakdown": breakdown
    }

def show_weekly():
    """Show weekly breakdown."""
    print("📊 Weekly Submission Velocity")
    print("=" * 50)

    for days in [1, 7, 30]:
        v = get_velocity(days)
        print(f"\nLast {days} day(s): {v['total']} submissions ({v['per_day']}/day)")
        if v['breakdown']:
            for cat, count in v['breakdown'].items():
                print(f"  • {cat}: {count}")

def main():
    import sys

    if "--add" in sys.argv:
        category = sys.argv[2] if len(sys.argv) > 2 else "service"
        add_submission(category)
    elif "--week" in sys.argv or "--weekly" in sys.argv:
        show_weekly()
    else:
        v = get_velocity(7)
        print(f"📊 Submission Velocity (Last 7 days)")
        print(f"  Total: {v['total']}")
        print(f"  Per day: {v['per_day']}/day")
        if v['breakdown']:
            print(f"  Breakdown:")
            for cat, count in v['breakdown'].items():
                print(f"    • {cat}: {count}")

        if v['per_day'] < 5:
            print(f"\n⚠️  Velocity low! Target: 10 submissions/day")
        elif v['per_day'] >= 10:
            print(f"\n✅ Velocity on track! ≥10 submissions/day")
        else:
            print(f"\n→ Building velocity...")

if __name__ == "__main__":
    main()
