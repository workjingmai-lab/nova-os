#!/usr/bin/env python3
"""
Task Explorer — Discover high-value tasks from your work history.
Reduces decision fatigue by surfacing proven 1-minute tasks.

Usage:
    python3 tools/task-explorer.py           # Show 10 random high-value tasks
    python3 tools/task-explorer.py --all     # Show all discovered tasks
    python3 tools/task-explorer.py --count 5 # Show 5 tasks
"""

import re
import random
from pathlib import Path
from collections import Counter

DIARY_PATH = Path("diary.md")

def parse_diary():
    """Parse diary.md to extract task patterns."""
    if not DIARY_PATH.exists():
        return []

    content = DIARY_PATH.read_text()

    # Pattern: **Task:** [Task Name]
    tasks = re.findall(r"\*\*Task:\*\* ([^\n]+)", content)

    return tasks

def categorize_task(task):
    """Categorize task by type."""
    task_lower = task.lower()

    categories = {
        "Documentation": ["readme", "guide", "doc", "template", "quick-start"],
        "Moltbook": ["moltbook", "post", "queued", "published"],
        "Analysis": ["analysis", "report", "tracker", "metrics"],
        "Revenue": ["pipeline", "grant", "service", "outreach", "message"],
        "Code": ["tool", "script", "python", "parser", "bug"],
        "Maintenance": ["update", "fix", "verify", "check"],
    }

    for category, keywords in categories.items():
        if any(keyword in task_lower for keyword in keywords):
            return category

    return "General"

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Explore high-value tasks from work history")
    parser.add_argument("--all", action="store_true", help="Show all discovered tasks")
    parser.add_argument("--count", type=int, default=10, help="Number of tasks to show")
    parser.add_argument("--category", type=str, help="Filter by category")
    args = parser.parse_args()

    tasks = parse_diary()

    if not tasks:
        print("❌ No tasks found in diary.md")
        return

    # Categorize and count
    categorized = {}
    for task in tasks:
        category = categorize_task(task)
        if category not in categorized:
            categorized[category] = []
        categorized[category].append(task)

    # Filter by category if specified
    if args.category:
        if args.category not in categorized:
            print(f"❌ Category '{args.category}' not found")
            print(f"Available categories: {', '.join(categorized.keys())}")
            return
        filtered_tasks = categorized[args.category]
    else:
        # Flatten all tasks
        filtered_tasks = []
        for category_tasks in categorized.values():
            filtered_tasks.extend(category_tasks)

    # Show stats
    total = len(filtered_tasks)
    print(f"📊 Discovered {total} tasks across {len(categorized)} categories\n")

    # Show category breakdown
    print("📁 Categories:")
    for category, tasks_list in sorted(categorized.items(), key=lambda x: len(x[1]), reverse=True):
        print(f"  {category}: {len(tasks_list)} tasks")
    print()

    # Show tasks
    if args.all:
        tasks_to_show = filtered_tasks
    else:
        tasks_to_show = random.sample(filtered_tasks, min(args.count, len(filtered_tasks)))

    print(f"🎯 Random selection ({len(tasks_to_show)} tasks):\n")
    for i, task in enumerate(tasks_to_show, 1):
        print(f"{i}. {task}")

    print("\n💡 Pick one and execute. Don't think. Just do.")

if __name__ == "__main__":
    main()
