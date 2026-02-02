#!/usr/bin/env python3
"""
Task Navigator - Autonomous Task Picker

Randomly selects an unblocked task from goals when running autonomous work blocks.
Eliminates decision fatigue during continuous execution.

Usage:
    python tools/task-navigator.py
"""

import random
import sys
import os

# Add workspace root to path
workspace_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, workspace_root)

UNBLOCKED_TASKS = [
    "Create a new tool (5-30 min)",
    "Update documentation (5-15 min)",
    "Run self-improvement analysis (5 min)",
    "Consolidate similar tools (10-20 min)",
    "Write Moltbook draft content (10-15 min)",
    "Plan next week's goals (5-10 min)",
    "Review and update knowledge base (5-10 min)",
    "Check for agent engagement opportunities (5 min)",
    "Create quick-reference guide (5-10 min)",
    "Build automation script (10-20 min)",
    "Analyze work patterns (5-10 min)",
    "Organize workspace files (5-10 min)",
    "Create or update templates (5-10 min)",
    "Document learnings (5-10 min)",
    "Test and refine existing tools (5-10 min)"
]

BLOCKED_TASKS = [
    "(BLOCKED) Moltbook posting - needs browser",
    "(BLOCKED) Code4rena onboarding - needs browser",
    "(BLOCKED) Selenium setup - requires Arthur config"
]

def print_header():
    print("=" * 60)
    print("🧭 TASK NAVIGATOR")
    print("=" * 60)
    print()

def pick_task():
    """Randomly select an unblocked task."""
    return random.choice(UNBLOCKED_TASKS)

def show_status():
    """Show current execution context."""
    print("📍 EXECUTION CONTEXT:")
    print("  • Mode: Autonomous work blocks")
    print("  • Rule: 1 min per task, execute immediately")
    print("  • Focus: Unblocked tasks only")
    print()

def show_unblocked():
    """Show all unblocked options."""
    print(f"✅ UNBLOCKED TASKS ({len(UNBLOCKED_TASKS)}):")
    for i, task in enumerate(UNBLOCKED_TASKS, 1):
        print(f"  {i:2d}. {task}")
    print()

def show_blocked():
    """Show blocked tasks for awareness."""
    if BLOCKED_TASKS:
        print(f"⏸️  BLOCKED ({len(BLOCKED_TASKS)}):")
        for task in BLOCKED_TASKS:
            print(f"     {task}")
        print()

def main():
    print_header()
    show_status()

    # Pick and highlight task
    selected = pick_task()
    print(f"🎯 NEXT TASK:")
    print(f"  → {selected}")
    print()

    # Show alternatives
    print("💡 ALTERNATIVES:")
    for _ in range(3):
        alt = pick_task()
        if alt != selected:
            print(f"  • {alt}")

    print()
    print("=" * 60)
    print("💪 EXECUTE NOW. Document to diary.md when done.")
    print("=" * 60)

if __name__ == "__main__":
    main()
