#!/usr/bin/env python3
"""
task-queue.py - Simple task queue for work blocks
Manages a FIFO queue of small tasks for cron-driven work sessions
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

QUEUE_FILE = Path("/home/node/.openclaw/workspace/.task_queue.json")
HISTORY_FILE = Path("/home/node/.openclaw/workspace/.task_history.json")

def load_queue():
    """Load task queue from file"""
    if QUEUE_FILE.exists():
        with open(QUEUE_FILE) as f:
            return json.load(f)
    return {"pending": [], "in_progress": None, "completed": []}

def save_queue(queue):
    """Save task queue to file"""
    with open(QUEUE_FILE, 'w') as f:
        json.dump(queue, f, indent=2)

def load_history():
    """Load completion history"""
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE) as f:
            return json.load(f)
    return []

def save_history(history):
    """Save completion history"""
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=2)

def add_task(description, priority="normal", source="manual"):
    """Add a new task to the queue"""
    queue = load_queue()
    task = {
        "id": f"task_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}_{len(queue['pending'])}",
        "description": description,
        "priority": priority,
        "source": source,
        "added_at": datetime.utcnow().isoformat()
    }
    queue["pending"].append(task)
    save_queue(queue)
    print(f"✅ Added: {description}")
    return task["id"]

def next_task():
    """Get the next task from queue"""
    queue = load_queue()
    if not queue["pending"]:
        return None
    
    # Sort by priority
    priority_order = {"high": 0, "normal": 1, "low": 2}
    queue["pending"].sort(key=lambda x: priority_order.get(x.get("priority", "normal"), 1))
    
    task = queue["pending"].pop(0)
    task["started_at"] = datetime.utcnow().isoformat()
    queue["in_progress"] = task
    save_queue(queue)
    return task

def complete_task(result=""):
    """Mark current task as complete"""
    queue = load_queue()
    if not queue["in_progress"]:
        print("❌ No task in progress")
        return False
    
    task = queue["in_progress"]
    task["completed_at"] = datetime.utcnow().isoformat()
    task["result"] = result
    
    queue["completed"].append(task)
    queue["in_progress"] = None
    save_queue(queue)
    
    # Also save to history
    history = load_history()
    history.append(task)
    save_history(history[-100:])  # Keep last 100
    
    print(f"✅ Completed: {task['description']}")
    return True

def skip_task():
    """Skip current task and put it back in queue"""
    queue = load_queue()
    if not queue["in_progress"]:
        print("❌ No task in progress")
        return False
    
    task = queue["in_progress"]
    task["skipped_at"] = datetime.utcnow().isoformat()
    queue["pending"].append(task)
    queue["in_progress"] = None
    save_queue(queue)
    
    print(f"⏭️ Skipped: {task['description']}")
    return True

def show_status():
    """Show current queue status"""
    queue = load_queue()
    history = load_history()
    
    print("📋 Task Queue Status")
    print("=" * 40)
    
    if queue["in_progress"]:
        print(f"🔄 IN PROGRESS: {queue['in_progress']['description']}")
        print()
    
    print(f"⏳ Pending: {len(queue['pending'])}")
    for task in queue["pending"][:5]:  # Show first 5
        priority_emoji = {"high": "🔴", "normal": "🟡", "low": "🟢"}.get(task.get("priority"), "⚪")
        print(f"   {priority_emoji} {task['description'][:50]}")
    if len(queue["pending"]) > 5:
        print(f"   ... and {len(queue['pending']) - 5} more")
    
    print()
    print(f"✅ Completed today: {len([h for h in history if h.get('completed_at', '').startswith(datetime.utcnow().strftime('%Y-%m-%d'))])}")
    print(f"📊 Total completed: {len(history)}")

def work_block():
    """Get next task for work block - designed for cron use"""
    task = next_task()
    if task:
        print(f"🎯 WORK BLOCK TASK:")
        print(f"   {task['description']}")
        print()
        print(f"   When done, run: python3 task-queue.py complete 'result summary'")
        return task
    else:
        print("📭 No pending tasks. Queue is empty!")
        print()
        print("   Add tasks with: python3 task-queue.py add 'task description'")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_status()
    elif sys.argv[1] == "add":
        desc = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else "New task"
        priority = "normal"
        if "--high" in sys.argv:
            priority = "high"
        elif "--low" in sys.argv:
            priority = "low"
        add_task(desc, priority)
    elif sys.argv[1] == "next":
        next_task()
    elif sys.argv[1] == "work":
        work_block()
    elif sys.argv[1] == "complete":
        result = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else ""
        complete_task(result)
    elif sys.argv[1] == "skip":
        skip_task()
    elif sys.argv[1] == "status":
        show_status()
    else:
        print("Usage: task-queue.py [add|next|work|complete|skip|status]")
