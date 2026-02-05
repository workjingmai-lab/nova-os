#!/usr/bin/env python3
"""
ROI Task Prioritizer — Quick reference for highest-value tasks

Usage:
    python3 tools/roi-task-prioritizer.py

Output:
    Sorted list of tasks by $/min ROI
"""

import json
from pathlib import Path

WORKSPACE = Path("/home/node/.openclaw/workspace")

# Task catalog with ROI calculations
TASKS = [
    {
        "name": "Gateway restart",
        "category": "Unblock",
        "time_min": 1,
        "value_unblocked": 50000,
        "roi_per_min": 50000,
        "blocker": "Arthur",
        "command": "openclaw gateway restart"
    },
    {
        "name": "GitHub CLI auth",
        "category": "Unblock",
        "time_min": 5,
        "value_unblocked": 125000,
        "roi_per_min": 25000,
        "blocker": "Arthur",
        "command": "gh auth login"
    },
    {
        "name": "Send 3 HIGH priority messages",
        "category": "Execute",
        "time_min": 10,
        "value_unblocked": 115000,
        "roi_per_min": 11500,
        "blocker": None,
        "command": "See: outreach/TOP-10-READY-TO-SEND.md"
    },
    {
        "name": "Send 10 MEDIUM priority messages",
        "category": "Execute",
        "time_min": 20,
        "value_unblocked": 260000,
        "roi_per_min": 13000,
        "blocker": None,
        "command": "See: outreach/TOP-10-READY-TO-SEND.md"
    },
    {
        "name": "Send 39 service messages (all)",
        "category": "Execute",
        "time_min": 39,
        "value_unblocked": 479500,
        "roi_per_min": 12295,
        "blocker": None,
        "command": "See: outreach/TOP-10-READY-TO-SEND.md"
    },
    {
        "name": "Submit 5 grant applications",
        "category": "Execute",
        "time_min": 15,
        "value_unblocked": 125000,
        "roi_per_min": 8333,
        "blocker": "Arthur (GitHub auth)",
        "command": "See: outreach/grants/"
    },
    {
        "name": "Code4rena account setup",
        "category": "Unblock",
        "time_min": 10,
        "value_unblocked": 50000,
        "roi_per_min": 5000,
        "blocker": "Arthur (gateway restart)",
        "command": "Requires browser access"
    }
]

def format_roi(roi: int) -> str:
    """Format ROI with K suffix and dollar sign."""
    if roi >= 1000:
        return f"${roi // 1000}K"
    return f"${roi}"

def main():
    print("\n" + "=" * 60)
    print("  🎯 ROI TASK PRIORITIZER")
    print("=" * 60)
    print(f"  Sorted by: $/min ROI (highest first)")
    print(f"  Total tasks: {len(TASKS)}")
    print("=" * 60)

    # Sort by ROI per minute
    sorted_tasks = sorted(TASKS, key=lambda x: x["roi_per_min"], reverse=True)

    for rank, task in enumerate(sorted_tasks, 1):
        # Format category with emoji
        category_emoji = {
            "Unblock": "🔓",
            "Execute": "🚀"
        }.get(task["category"], "📋")

        # Format blocker status
        blocker_status = f"⚠️  {task['blocker']}" if task["blocker"] else "✅ Zero blockers"

        print(f"\n  {rank}. {task['name']}")
        print(f"     Category: {category_emoji} {task['category']}")
        print(f"     Time: {task['time_min']} min → {format_roi(task['value_unblocked'])} value")
        print(f"     ROI: {format_roi(task['roi_per_min'])}/min")
        print(f"     Status: {blocker_status}")
        if task.get("command"):
            print(f"     Command: {task['command']}")

    # Summary stats
    print("\n" + "=" * 60)
    print("  📊 SUMMARY")
    print("=" * 60)

    total_unblocked = sum(t["value_unblocked"] for t in sorted_tasks[:3])
    total_time = sum(t["time_min"] for t in sorted_tasks[:3])
    avg_roi = total_unblocked // total_time if total_time > 0 else 0

    print(f"  Top 3 tasks: {total_time} min → {format_roi(total_unblocked)} = {format_roi(avg_roi)}/min")
    print(f"  All tasks: {sum(t['time_min'] for t in sorted_tasks)} min → {format_roi(sum(t['value_unblocked'] for t in sorted_tasks))}")
    print(f"  Arthur blockers: {sum(1 for t in sorted_tasks if t['blocker'])} tasks")
    print(f"  Zero-blocker tasks: {sum(1 for t in sorted_tasks if not t['blocker'])} tasks")

    print("\n" + "=" * 60)
    print("  💡 KEY INSIGHT")
    print("=" * 60)
    print("  Unblock first (Arthur). Execute second (Nova/Arthur).")
    print("  Top 2 unblock tasks: 6 min → $175K = $29,167/min")
    print("\n  Don't think. Just execute.")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
