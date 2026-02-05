#!/usr/bin/env python3
"""
One-Minute Task Picker — Quick task selection for continuous execution

Reduces decision fatigue by picking from high-value, executable tasks.
Use during cron work blocks or when velocity matters.

Usage:
    python3 one-minute-picker.py          # Random task
    python3 one-minute-picker.py --list   # Show all options
    python3 one-minute-picker.py --category outreach  # Filter by category
"""

import random
import argparse
from pathlib import Path

TASK_POOL = {
    "documentation": [
        "Create README for a new tool",
        "Update knowledge/ with a new insight",
        "Document a work pattern from diary.md",
        "Create a quick-start guide for a workflow",
        "Update TOOL.md with environment-specific notes",
    ],
    "outreach": [
        "Research 1 new DAO prospect (5 min → potential $15-40K)",
        "Queue 1 Moltbook post (maintain presence)",
        "Engage with 2 agents on Moltbook (build relationships)",
        "Write 1 service proposal template",
        "Update outreach messaging based on lessons learned",
    ],
    "analysis": [
        "Run daily-velocity-report.py and review trends",
        "Check diary.md for patterns (what's working?)",
        "Review pipeline status in revenue-tracker.py",
        "Analyze last 10 work blocks for ROI",
        "Check which tools are most-used (prioritize documentation)",
    ],
    "maintenance": [
        "Archive old sessions from today.md to memory/YYYY-MM-DD.md",
        "Trim today.md to last 10 sessions (context reduction)",
        "Update .heartbeat_state.json with latest stats",
        "Review and consolidate duplicate tools",
        "Check for missing READMEs (goal: 100% coverage)",
    ],
    "revenue": [
        "Research 1 grant opportunity (add to grants/)",
        "Review 1 service proposal for clarity",
        "Check Code4rena for new audit contests (if browser works)",
        "Update pipeline with new leads",
        "Prepare 1 outreach message (batch for later sending)",
    ],
    "meta": [
        "Reflect on what I learned today (write to diary.md)",
        "Update MEMORY.md with key insight",
        "Review SOUL.md — am I following my principles?",
        "Check streak in .heartbeat_state.json",
        "Read last 5 diary entries — what's the pattern?",
    ],
}

def pick_task(category: str = None) -> tuple[str, str]:
    """Pick a random task from the pool."""
    if category and category in TASK_POOL:
        pool = TASK_POOL[category]
        cat = category
    else:
        cat = random.choice(list(TASK_POOL.keys()))
        pool = TASK_POOL[cat]
    
    task = random.choice(pool)
    return task, cat

def main():
    parser = argparse.ArgumentParser(description="Pick a 1-minute task")
    parser.add_argument("--list", action="store_true", help="List all tasks")
    parser.add_argument("--category", help="Filter by category")
    args = parser.parse_args()

    if args.list:
        print("📋 One-Minute Task Pool\n")
        for cat, tasks in TASK_POOL.items():
            print(f"\n{cat.upper()}:")
            for task in tasks:
                print(f"  • {task}")
        return

    task, cat = pick_task(args.category)
    
    print(f"🎯 Task picked: {cat.upper()}")
    print(f"   {task}")
    print(f"\n⏱️  1 minute. Execute. Document. Next.")

if __name__ == "__main__":
    main()
