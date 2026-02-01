#!/usr/bin/env python3
"""
agent-collab.py — Multi-Agent Collaboration Framework

Enables structured workflows between multiple AI agents:
- Task delegation with clear ownership
- Status tracking across agents
- Handoff protocols
- Shared state management

Usage: python3 agent-collab.py --create-task|--list|--delegate|--handoff
"""

import json
import os
import sys
import argparse
import uuid
from datetime import datetime
from pathlib import Path

# Paths
COLLAB_DIR = Path(__file__).parent.parent / "collab"
TASKS_FILE = COLLAB_DIR / "tasks.json"
AGENTS_FILE = COLLAB_DIR / "agents.json"
LOG_FILE = COLLAB_DIR / "handoffs.log"

# Known agents in the ecosystem
DEFAULT_AGENTS = {
    "nova": {
        "name": "Nova",
        "emoji": "✨",
        "specialties": ["documentation", "pattern-analysis", "tool-building"],
        "status": "active",
        "last_seen": datetime.now().isoformat()
    }
}


def init_collab():
    """Initialize collaboration directory and files."""
    COLLAB_DIR.mkdir(exist_ok=True)
    
    if not AGENTS_FILE.exists():
        with open(AGENTS_FILE, 'w') as f:
            json.dump(DEFAULT_AGENTS, f, indent=2)
    
    if not TASKS_FILE.exists():
        with open(TASKS_FILE, 'w') as f:
            json.dump({"tasks": [], "next_id": 1}, f, indent=2)


def load_agents():
    """Load agent registry."""
    with open(AGENTS_FILE) as f:
        return json.load(f)


def load_tasks():
    """Load all collaboration tasks."""
    with open(TASKS_FILE) as f:
        return json.load(f)


def save_tasks(data):
    """Save tasks to file."""
    with open(TASKS_FILE, 'w') as f:
        json.dump(data, f, indent=2, default=str)


def log_handoff(from_agent, to_agent, task_id, context):
    """Log a handoff between agents."""
    entry = {
        "timestamp": datetime.now().isoformat(),
        "from": from_agent,
        "to": to_agent,
        "task_id": task_id,
        "context": context
    }
    
    with open(LOG_FILE, 'a') as f:
        f.write(json.dumps(entry) + "\n")


def create_task(title, description, owner, priority="medium", dependencies=None):
    """Create a new collaborative task."""
    tasks_data = load_tasks()
    task_id = tasks_data["next_id"]
    
    task = {
        "id": task_id,
        "title": title,
        "description": description,
        "owner": owner,
        "priority": priority,
        "status": "created",
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
        "dependencies": dependencies or [],
        "history": [{
            "action": "created",
            "by": owner,
            "timestamp": datetime.now().isoformat()
        }]
    }
    
    tasks_data["tasks"].append(task)
    tasks_data["next_id"] = task_id + 1
    save_tasks(tasks_data)
    
    return task


def delegate_task(task_id, from_agent, to_agent, notes=""):
    """Delegate a task from one agent to another."""
    tasks_data = load_tasks()
    
    for task in tasks_data["tasks"]:
        if task["id"] == task_id:
            old_owner = task["owner"]
            task["owner"] = to_agent
            task["status"] = "delegated"
            task["updated_at"] = datetime.now().isoformat()
            task["history"].append({
                "action": "delegated",
                "from": from_agent,
                "to": to_agent,
                "notes": notes,
                "timestamp": datetime.now().isoformat()
            })
            
            save_tasks(tasks_data)
            log_handoff(from_agent, to_agent, task_id, notes)
            
            return task
    
    return None


def update_task_status(task_id, status, agent, notes=""):
    """Update task status."""
    tasks_data = load_tasks()
    
    valid_statuses = ["created", "in_progress", "blocked", "review", "completed", "cancelled"]
    if status not in valid_statuses:
        print(f"❌ Invalid status. Valid: {', '.join(valid_statuses)}")
        return None
    
    for task in tasks_data["tasks"]:
        if task["id"] == task_id:
            old_status = task["status"]
            task["status"] = status
            task["updated_at"] = datetime.now().isoformat()
            task["history"].append({
                "action": f"status_change:{old_status}->{status}",
                "by": agent,
                "notes": notes,
                "timestamp": datetime.now().isoformat()
            })
            
            save_tasks(tasks_data)
            return task
    
    return None


def list_tasks(status=None, owner=None):
    """List tasks with optional filtering."""
    tasks_data = load_tasks()
    tasks = tasks_data["tasks"]
    
    if status:
        tasks = [t for t in tasks if t["status"] == status]
    if owner:
        tasks = [t for t in tasks if t["owner"] == owner]
    
    return tasks


def show_task(task_id):
    """Show detailed task information."""
    tasks_data = load_tasks()
    
    for task in tasks_data["tasks"]:
        if task["id"] == task_id:
            return task
    
    return None


def generate_handoff_summary(task_id):
    """Generate a handoff summary for a task."""
    task = show_task(task_id)
    if not task:
        return None
    
    summary = f"""
═══════════════════════════════════════════════════
  HANDOFF SUMMARY — Task #{task['id']}
═══════════════════════════════════════════════════

TASK: {task['title']}
STATUS: {task['status'].upper()}
OWNER: @{task['owner']}
PRIORITY: {task['priority'].upper()}

DESCRIPTION:
{task['description']}

HISTORY:
"""
    
    for entry in task['history']:
        ts = entry['timestamp'][:16]
        summary += f"  [{ts}] {entry['action']} by @{entry.get('by', 'unknown')}\n"
        if 'notes' in entry and entry['notes']:
            summary += f"           Note: {entry['notes']}\n"
    
    if task['dependencies']:
        summary += f"\nDEPENDENCIES: {', '.join(task['dependencies'])}"
    
    summary += "\n═══════════════════════════════════════════════════\n"
    
    return summary


def main():
    parser = argparse.ArgumentParser(description="Multi-agent collaboration framework")
    parser.add_argument("--create-task", action="store_true", help="Create a new task")
    parser.add_argument("--title", help="Task title")
    parser.add_argument("--description", help="Task description")
    parser.add_argument("--owner", default="nova", help="Task owner (default: nova)")
    parser.add_argument("--priority", default="medium", choices=["low", "medium", "high", "critical"])
    parser.add_argument("--depends", help="Comma-separated list of task IDs this depends on")
    
    parser.add_argument("--list", action="store_true", help="List all tasks")
    parser.add_argument("--status", help="Filter by status")
    parser.add_argument("--filter-owner", help="Filter by owner")
    
    parser.add_argument("--show", type=int, metavar="ID", help="Show task details")
    parser.add_argument("--handoff", type=int, metavar="ID", help="Handoff task to another agent")
    parser.add_argument("--to", help="Target agent for handoff")
    parser.add_argument("--from", dest="from_agent", default="nova", help="Source agent for handoff")
    parser.add_argument("--notes", help="Handoff notes")
    
    parser.add_argument("--update", type=int, metavar="ID", help="Update task status")
    parser.add_argument("--set-status", help="New status value")
    
    args = parser.parse_args()
    
    init_collab()
    
    # Create task
    if args.create_task:
        if not args.title or not args.description:
            print("❌ --title and --description required for new tasks")
            sys.exit(1)
        
        deps = args.depends.split(",") if args.depends else []
        task = create_task(args.title, args.description, args.owner, args.priority, deps)
        print(f"✅ Task created: #{task['id']}")
        print(f"   Title: {task['title']}")
        print(f"   Owner: @{task['owner']}")
        print(f"   Priority: {task['priority']}")
    
    # List tasks
    elif args.list:
        tasks = list_tasks(args.status, args.filter_owner)
        if tasks:
            print(f"📋 Tasks ({len(tasks)} total):\n")
            for task in tasks:
                icon = "⏳"
                if task["status"] == "completed":
                    icon = "✅"
                elif task["status"] == "in_progress":
                    icon = "🔨"
                elif task["status"] == "blocked":
                    icon = "🚫"
                
                print(f"{icon} #{task['id']} [{task['priority'].upper()}] {task['title']}")
                print(f"   Owner: @{task['owner']} | Status: {task['status']}")
                print()
        else:
            print("📭 No tasks found")
    
    # Show task details
    elif args.show:
        task = show_task(args.show)
        if task:
            summary = generate_handoff_summary(args.show)
            print(summary)
        else:
            print(f"❌ Task #{args.show} not found")
    
    # Handoff task
    elif args.handoff:
        if not args.to:
            print("❌ --to required for handoff (target agent)")
            sys.exit(1)
        
        task = delegate_task(args.handoff, args.from_agent, args.to, args.notes or "")
        if task:
            print(f"✅ Task #{args.handoff} delegated from @{args.from_agent} to @{args.to}")
            if args.notes:
                print(f"   Notes: {args.notes}")
        else:
            print(f"❌ Task #{args.handoff} not found")
    
    # Update status
    elif args.update:
        if not args.set_status:
            print("❌ --set-status required")
            sys.exit(1)
        
        task = update_task_status(args.update, args.set_status, args.owner, args.notes or "")
        if task:
            print(f"✅ Task #{args.update} status updated to '{args.set_status}'")
        else:
            print(f"❌ Task #{args.update} not found")
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
