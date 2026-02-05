#!/usr/bin/env python3
"""
Next Action Suggester — Recommends what to work on based on goals, blockers, and time
Part of Nova's autonomous operation toolkit
"""

import json
import random
from datetime import datetime
from pathlib import Path

# Files to check
GOALS_FILE = Path("goals/week-2.md")
CREDENTIALS_FILE = Path(".credential_status.json")
TASK_QUEUE = Path(".task_queue.json")
DIARY_FILE = Path("diary.md")
TODAY_FILE = Path("today.md")

def load_json_file(filepath):
    """Load JSON file if it exists"""
    if filepath.exists():
        with open(filepath) as f:
            return json.load(f)
    return {}

def load_text_file(filepath):
    """Load text file if it exists"""
    if filepath.exists():
        with open(filepath) as f:
            return f.read()
    return ""

def get_unfinished_goals():
    """Extract unchecked goals from markdown"""
    content = load_text_file(GOALS_FILE)
    unfinished = []
    
    for line in content.split('\n'):
        line = line.strip()
        if line.startswith('- [ ]') or line.startswith('- [🔄]'):
            goal = line.replace('- [ ]', '').replace('- [🔄]', '').strip()
            if goal and not goal.startswith('-'):
                unfinished.append(goal)
    
    return unfinished

def get_available_tasks():
    """Get tasks that aren't blocked by credentials"""
    creds = load_json_file(CREDENTIALS_FILE)
    
    ready_creds = set()
    for name, data in creds.get("credentials", {}).items():
        if data.get("ready"):
            ready_creds.add(name)
    
    # Define task dependencies
    task_deps = {
        "Push repository to GitHub": {"github"},
        "Execute Ethernaut exploit": {"sepoliaETH"},
        "Publish to Moltbook": {"moltbookAPI"},
        "Post Week 1 retrospective": {"moltbookAPI"},
    }
    
    available = []
    blocked = []
    
    for task, deps in task_deps.items():
        if deps.issubset(ready_creds):
            available.append(task)
        else:
            missing = deps - ready_creds
            blocked.append((task, missing))
    
    return available, blocked

def get_recent_diary_entries():
    """Get last few diary entries to avoid repetition"""
    content = load_text_file(DIARY_FILE)
    entries = content.split('[WORK BLOCK]')
    return [e.strip()[:100] for e in entries[-3:] if e.strip()]

def suggest_action():
    """Generate next action recommendation"""
    goals = get_unfinished_goals()
    available, blocked = get_available_tasks()
    queue = load_json_file(TASK_QUEUE)
    
    suggestions = []
    
    # Priority 1: Unblocked high-priority tasks
    if available:
        for task in available[:3]:
            suggestions.append({
                "priority": "HIGH",
                "task": task,
                "reason": "Credentials ready — no blockers",
                "estimated_time": "15-30 min"
            })
    
    # Priority 2: Pending tasks from queue
    pending = queue.get("pending", [])
    if pending:
        for p in pending[:2]:
            suggestions.append({
                "priority": "MEDIUM", 
                "task": p.get("description", "Unknown task"),
                "reason": f"From task queue ({p.get('priority', 'normal')} priority)",
                "estimated_time": "20-40 min"
            })
    
    # Priority 3: Unfinished goals that might need creative workarounds
    for goal in goals[:3]:
        # Skip if obviously blocked
        if any(blocked_task in goal for blocked_task, _ in blocked):
            continue
        suggestions.append({
            "priority": "FLEXIBLE",
            "task": goal,
            "reason": "Week 2 goal — find workaround or prepare materials",
            "estimated_time": "30-60 min"
        })
    
    # Priority 4: Blocked but worth monitoring
    if blocked:
        for task, deps in blocked[:2]:
            suggestions.append({
                "priority": "MONITOR",
                "task": f"[BLOCKED] {task}",
                "reason": f"Waiting for: {', '.join(deps)}",
                "estimated_time": "Check credential monitor"
            })
    
    return suggestions

def print_recommendation():
    """Print formatted recommendation"""
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    
    print("🎯 NEXT ACTION SUGGESTER")
    print(f"Generated: {now}")
    print("=" * 60)
    
    suggestions = suggest_action()
    
    if not suggestions:
        print("\n🎉 All caught up! No pending actions found.")
        return
    
    # Group by priority
    priority_order = ["HIGH", "MEDIUM", "FLEXIBLE", "MONITOR"]
    
    for priority in priority_order:
        priority_tasks = [s for s in suggestions if s["priority"] == priority]
        if priority_tasks:
            emoji = {"HIGH": "🔥", "MEDIUM": "📋", "FLEXIBLE": "💡", "MONITOR": "⏳"}.get(priority, "•")
            print(f"\n{emoji} {priority} PRIORITY")
            print("-" * 40)
            
            for i, task in enumerate(priority_tasks[:2], 1):
                print(f"  {i}. {task['task']}")
                print(f"     Why: {task['reason']}")
                print(f"     Time: {task['estimated_time']}")
    
    # Pick a random top suggestion
    top = [s for s in suggestions if s["priority"] in ["HIGH", "MEDIUM"]]
    if top:
        pick = random.choice(top[:3])
        print(f"\n{'=' * 60}")
        print("🎲 RANDOM PICK (if you can't decide):")
        print(f"   → {pick['task']}")
        print(f"   ({pick['estimated_time']})")

def main():
    """Main entry point"""
    print_recommendation()

if __name__ == "__main__":
    main()
