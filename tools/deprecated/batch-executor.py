#!/usr/bin/env python3
"""
Batch Executor — Run multiple work blocks in sequence
Usage: python3 tools/batch-executor.py
"""

import json
import os
from datetime import datetime

TASKS_FILE = "/home/node/.openclaw/workspace/batch-tasks.json"

def load_tasks():
    """Load pending batch tasks."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    """Save pending batch tasks."""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task(task, result="", insight="", next_step="Continue work blocks"):
    """Add a task to the batch queue."""
    tasks = load_tasks()
    tasks.append({
        'task': task,
        'result': result,
        'insight': insight,
        'next_step': next_step,
        'status': 'pending',
        'added': datetime.utcnow().isoformat()
    })
    save_tasks(tasks)
    return len(tasks)

def execute_batch(limit=5):
    """Execute up to N pending tasks."""
    tasks = load_tasks()
    if not tasks:
        print("✨ No pending tasks in batch queue")
        return 0

    executed = 0
    for i, task in enumerate(tasks[:limit]):
        if task['status'] == 'pending':
            # Log using work-block-logger
            import subprocess
            result = subprocess.run([
                'python3', 'tools/work-block-logger.py',
                task['task'],
                task['result'] or 'Task completed',
                task['insight'] or '',
                task['next_step'] or 'Continue work blocks'
            ], capture_output=True, text=True)

            if result.returncode == 0:
                task['status'] = 'complete'
                task['completed'] = datetime.utcnow().isoformat()
                executed += 1
                print(result.stdout.strip())
            else:
                print(f"❌ Failed to execute: {task['task']}")

    # Save updated tasks
    save_tasks(tasks)

    # Remove completed tasks from queue
    remaining = [t for t in tasks if t['status'] == 'pending']
    save_tasks(remaining)

    return executed

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == 'add':
        # Add task to batch
        task = sys.argv[2] if len(sys.argv) > 2 else input("Task: ")
        result = sys.argv[3] if len(sys.argv) > 3 else ""
        insight = sys.argv[4] if len(sys.argv) > 4 else ""
        next_step = sys.argv[5] if len(sys.argv) > 5 else ""

        count = add_task(task, result, insight, next_step)
        print(f"✅ Task added to batch queue ({count} pending)")

    elif len(sys.argv) > 1 and sys.argv[1] == 'list':
        # List pending tasks
        tasks = load_tasks()
        print(f"📋 Pending batch tasks: {len(tasks)}")
        for i, task in enumerate(tasks, 1):
            print(f"  {i}. {task['task'][:60]}...")

    else:
        # Execute batch
        limit = int(sys.argv[1]) if len(sys.argv) > 1 else 5
        print(f"🚀 Executing up to {limit} tasks from batch queue...")
        executed = execute_batch(limit)
        print(f"\n✅ Batch complete: {executed} tasks executed")
