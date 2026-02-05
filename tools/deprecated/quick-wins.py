#!/usr/bin/env python3
"""
quick-wins.py - Generate 1-minute micro-task ideas
Keeps Nova moving when time is tight. No overthinking.
"""

import random
import json

CATEGORIES = {
    "write": [
        "Write a 100-word summary of today's learning",
        "Create a 3-bullet 'State of Nova' update",
        "Draft one social post idea (no posting, just ideate)",
        "Write a micro-tutorial for a tool you use",
        "Create a quick reference checklist for something you do often"
    ],
    "code": [
        "Add --help text to any script missing it",
        "Create a 10-line convenience function",
        "Write a quick data validation function",
        "Build a simple log parser (diary.md → insights)",
        "Create a clipboard-friendly template for something repetitive"
    ],
    "organize": [
        "Update today.md with current status",
        "Clean up one old file (< 7 days old)",
        "Reorganize one tools/ subdirectory",
        "Create one symlink for frequently used file",
        "Update one README with latest changes"
    ],
    "learn": [
        "Read one SKILL.md you haven't read yet",
        "Search memory for 'lesson' and pick one to re-learn",
        " skim OpenClaw docs for one new feature",
        "Check recent session logs for patterns",
        "Review one tool's code and find one optimization"
    ],
    "connect": [
        "Draft one message to a Moltbook agent (don't send yet)",
        "List 3 agents you want to know more about",
        "Create an engagement template (reusable message structure)",
        "Research one agent's background/tools",
        "Draft a reply to one interesting post (save as draft)"
    ]
}

def get_idea(category=None, time_limit="1m"):
    """Get one quick win idea"""
    if category:
        ideas = CATEGORIES.get(category.lower(), CATEGORIES["write"])
    else:
        ideas = random.choice(list(CATEGORIES.values()))
    
    return random.choice(ideas)

def get_three():
    """Get 3 ideas across different categories"""
    categories = list(CATEGORIES.keys())
    selected = random.sample(categories, min(3, len(categories)))
    return [(cat, get_idea(cat)) for cat in selected]

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate 1-minute micro-task ideas")
    parser.add_argument("--category", "-c", choices=list(CATEGORIES.keys()), help="Specific category")
    parser.add_argument("--three", "-3", action="store_true", help="Get 3 different ideas")
    args = parser.parse_args()

    if args.three:
        print("🎯 THREE QUICK WINS:\n")
        for cat, idea in get_three():
            print(f"[{cat.upper()}] {idea}\n")
    else:
        print(f"🎯 QUICK WIN: {get_idea(args.category)}")
