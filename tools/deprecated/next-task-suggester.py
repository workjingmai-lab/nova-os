#!/usr/bin/env python3
"""
next-task-suggester.py - Quick next-task suggestions

Reads today.md and suggests highest-value next tasks.
Optimized for 1-minute work blocks: fast, actionable, high-impact.

Usage:
    python3 next-task-suggester.py
    python3 next-task-suggester.py --count 3
    python3 next-task-suggester.py --category execution
"""

import json
import re
from pathlib import Path
from datetime import datetime

WORKSPACE = Path("/home/node/.openclaw/workspace")
TODAY_MD = WORKSPACE / "today.md"
DIARY_MD = WORKSPACE / "diary.md"

# Task patterns that signal ready actions
READY_PATTERNS = [
    r"✅.*ready",
    r"🎯.*ready",
    r"Pipeline.*ready",
    r"awaiting.*approval",
    r"BUILD.*COMPLETE",
    r"EXECUTE.*ready"
]

# Categories based on work patterns
CATEGORIES = {
    "execution": ["send", "execute", "pipeline", "outreach", "messages"],
    "documentation": ["readme", "document", "guide", "tutorial"],
    "tools": ["tool", "script", "automation", "create"],
    "analytics": ["track", "analyze", "metrics", "snapshot"],
    "blockers": ["unblock", "fix", "resolve", "auth"]
}

def extract_next_actions(content: str) -> list:
    """Extract next actions from today.md"""
    actions = []
    
    # Look for "Next Actions" section
    next_section = re.search(r"## Next Actions.*?(?=\n##|\Z)", content, re.DOTALL)
    if next_section:
        lines = next_section.group(0).split("\n")
        for line in lines:
            if line.strip().startswith("-"):
                actions.append(line.strip())
    
    # Look for ready patterns
    for pattern in READY_PATTERNS:
        matches = re.findall(pattern, content, re.IGNORECASE)
        actions.extend(matches)
    
    return actions

def categorize_task(task: str) -> str:
    """Categorize task by keyword"""
    task_lower = task.lower()
    for category, keywords in CATEGORIES.items():
        if any(keyword in task_lower for keyword in keywords):
            return category
    return "general"

def prioritize_actions(actions: list) -> list:
    """Prioritize by impact"""
    # High-priority keywords
    high_priority = ["send", "execute", "revenue", "pipeline", "approval"]
    medium_priority = ["document", "create", "build"]
    
    prioritized = []
    for action in actions:
        priority = "medium"
        action_lower = action.lower()
        if any(kw in action_lower for kw in high_priority):
            priority = "high"
        elif any(kw in action_lower for kw in medium_priority):
            priority = "medium"
        prioritized.append((priority, action))
    
    # Sort by priority
    prioritized.sort(key=lambda x: {"high": 0, "medium": 1, "low": 2}.get(x[0], 3))
    return prioritized

def get_latest_block_number() -> int:
    """Extract latest work block number from diary.md"""
    if not DIARY_MD.exists():
        return 0
    
    content = DIARY_MD.read_text()
    match = re.search(r"WORK BLOCK (\d+)", content)
    if match:
        return int(match.group(1))
    return 0

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Quick next-task suggestions")
    parser.add_argument("--count", type=int, default=5, help="Number of suggestions")
    parser.add_argument("--category", type=str, help="Filter by category")
    args = parser.parse_args()
    
    # Read today.md
    if not TODAY_MD.exists():
        print("❌ today.md not found")
        return
    
    content = TODAY_MD.read_text()
    
    # Extract actions
    actions = extract_next_actions(content)
    if not actions:
        print("ℹ️  No next actions found in today.md")
        return
    
    # Prioritize
    prioritized = prioritize_actions(actions)
    
    # Filter by category if specified
    if args.category:
        prioritized = [(p, a) for p, a in prioritized 
                      if categorize_task(a) == args.category]
    
    # Display
    latest_block = get_latest_block_number()
    print(f"🎯 Next Task Suggestions (Work Block {latest_block + 1})")
    print("=" * 50)
    
    for i, (priority, action) in enumerate(prioritized[:args.count], 1):
        priority_icon = {"high": "🔥", "medium": "⚡", "low": "📝"}.get(priority, "📌")
        category = categorize_task(action)
        print(f"{i}. {priority_icon} {action}")
        print(f"   Category: {category} | Priority: {priority}")
    
    # Quick stats
    print(f"\n📊 Quick Stats:")
    print(f"   Total actions: {len(actions)}")
    print(f"   Latest block: {latest_block}")
    print(f"   Ready to execute: {len([a for a in actions if 'ready' in a.lower()])}")

if __name__ == "__main__":
    main()
