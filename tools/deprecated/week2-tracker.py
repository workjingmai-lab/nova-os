#!/usr/bin/env python3
"""
Week 2 Goal Tracker — Fast progress dashboard for Feb 2-8 goals
"""

import json
import os
from datetime import datetime

WEEK_2_GOALS = {
    "high_priority": {
        "testnet_exploit": {"done": False, "target": 1, "current": 0},
        "funding_secured": {"done": False, "target": 100, "current": 0, "unit": "$"},
        "github_portfolio": {"done": False, "blocked": "GitHub auth pending"},
        "moltbook_posts": {"done": False, "target": 3, "current": 0},
        "code4rena_onboard": {"done": False, "progress": "Research done, guide created"},
    },
    "medium_priority": {
        "nova_dashboard": {"done": True, "date": "2026-02-01"},
        "agent_collab_template": {"done": True, "date": "2026-02-01"},
        "document_learnings": {"done": True, "date": "2026-02-01"},
        "refine_voice": {"done": True, "date": "2026-02-01"},
        "notification_system": {"done": True, "date": "2026-02-01"},
    }
}

METRICS = {
    "github_stars": {"target": 10, "current": 0},
    "moltbook_followers": {"target": 15, "current": 4},
    "testnet_exploits": {"target": 1, "current": 0},
    "grant_applications": {"target": 3, "current": 0},
    "code4rena_comps": {"target": 1, "current": 0},
}

def format_status():
    lines = [
        "=" * 50,
        f"📊 Week 2 Goal Tracker — {datetime.now().strftime('%Y-%m-%d %H:%M')} UTC",
        "=" * 50,
        "",
        "🎯 HIGH PRIORITY",
        "-" * 30,
    ]
    
    for goal, data in WEEK_2_GOALS["high_priority"].items():
        status = "✅" if data.get("done") else "🔄" if data.get("progress") else "⏳"
        if data.get("blocked"):
            lines.append(f"{status} {goal}: BLOCKED — {data['blocked']}")
        elif data.get("progress"):
            lines.append(f"{status} {goal}: {data['progress']}")
        elif "current" in data and "target" in data:
            pct = (data["current"] / data["target"]) * 100
            lines.append(f"{status} {goal}: {data['current']}/{data['target']} ({pct:.0f}%)")
        else:
            lines.append(f"{status} {goal}")
    
    lines.extend([
        "",
        "📈 SUCCESS METRICS",
        "-" * 30,
    ])
    
    for metric, data in METRICS.items():
        pct = (data["current"] / data["target"]) * 100 if data["target"] > 0 else 0
        bar = "█" * int(pct / 10) + "░" * (10 - int(pct / 10))
        lines.append(f"{metric}: [{bar}] {data['current']}/{data['target']} ({pct:.0f}%)")
    
    # Calculate overall progress
    all_goals = list(WEEK_2_GOALS["high_priority"].values()) + list(WEEK_2_GOALS["medium_priority"].values())
    completed = sum(1 for g in all_goals if g.get("done"))
    total = len(all_goals)
    
    lines.extend([
        "",
        "=" * 50,
        f"📊 OVERALL: {completed}/{total} goals complete ({completed/total*100:.0f}%)",
        "=" * 50,
    ])
    
    return "\n".join(lines)

if __name__ == "__main__":
    print(format_status())
    
    # Save to file for dashboard consumption
    os.makedirs("dashboard", exist_ok=True)
    with open("dashboard/week2-status.json", "w") as f:
        json.dump({
            "goals": WEEK_2_GOALS,
            "metrics": METRICS,
            "updated": datetime.now().isoformat(),
        }, f, indent=2)
    print("\n💾 Saved to dashboard/week2-status.json")
