#!/usr/bin/env python3
"""
Agent Collaboration Template
Multi-agent workflow tool for coordinating tasks between agents.

Usage:
    python agent-collab.py init <project_name>     # Start new collab
    python agent-collab.py add <agent_id>          # Add agent to project
    python agent-collab.py assign <task> <agent>   # Assign task
    python agent-collab.py status                  # Show project status
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

COLLAB_DIR = Path.home() / ".openclaw" / "workspace" / "collab"
STATE_FILE = COLLAB_DIR / "active.json"


def init_project(name, description=""):
    """Initialize a new collaboration project."""
    os.makedirs(COLLAB_DIR, exist_ok=True)

    project = {
        "name": name,
        "description": description,
        "created_at": datetime.now().isoformat(),
        "agents": [],
        "tasks": [],
        "status": "active"
    }

    project_file = COLLAB_DIR / f"{name.replace(' ', '-').lower()}.json"
    project_file.write_text(json.dumps(project, indent=2))

    # Set as active
    STATE_FILE.write_text(json.dumps({"active_project": str(project_file)}, indent=2))

    print(f"✅ Collaboration '{name}' initialized")
    print(f"   Project file: {project_file}")
    return project


def get_active_project():
    """Load the active collaboration project."""
    if not STATE_FILE.exists():
        print("❌ No active collaboration. Use 'agent-collab.py init <name>' first.")
        sys.exit(1)

    state = json.loads(STATE_FILE.read_text())
    project_path = Path(state.get("active_project", ""))
    if not project_path.exists():
        print(f"❌ Project file not found: {project_path}")
        sys.exit(1)

    return json.loads(project_path.read_text()), project_path


def add_agent(agent_id, role="", capabilities=[]):
    """Add an agent to the active collaboration."""
    project, project_path = get_active_project()

    agent = {
        "id": agent_id,
        "role": role,
        "capabilities": capabilities,
        "joined_at": datetime.now().isoformat(),
        "tasks_assigned": 0
    }

    # Check if agent already exists
    if any(a["id"] == agent_id for a in project["agents"]):
        print(f"⚠️  Agent '{agent_id}' already in collaboration")
        return project

    project["agents"].append(agent)

    # Save
    project_path.write_text(json.dumps(project, indent=2))
    print(f"✅ Agent '{agent_id}' added to '{project['name']}'")
    return project


def assign_task(task_description, agent_id, priority="medium"):
    """Assign a task to an agent in the collaboration."""
    project, project_path = get_active_project()

    # Validate agent exists
    agent = next((a for a in project["agents"] if a["id"] == agent_id), None)
    if not agent:
        print(f"❌ Agent '{agent_id}' not found in collaboration")
        sys.exit(1)

    task = {
        "id": f"task-{len(project['tasks']) + 1}",
        "description": task_description,
        "assigned_to": agent_id,
        "priority": priority,
        "status": "pending",
        "created_at": datetime.now().isoformat()
    }

    project["tasks"].append(task)
    agent["tasks_assigned"] += 1

    # Save
    project_path.write_text(json.dumps(project, indent=2))
    print(f"✅ Task assigned to '{agent_id}': {task_description[:50]}...")
    return project


def show_status():
    """Display collaboration status."""
    project, _ = get_active_project()

    print(f"\n🤝 {project['name']}")
    print(f"{'─' * 50}")
    print(f"Status: {project['status'].upper()}")
    print(f"Created: {project['created_at'][:10]}")
    if project.get('description'):
        print(f"\n📋 {project['description']}")

    print(f"\n👥 Agents ({len(project['agents'])})")
    for agent in project['agents']:
        print(f"  • {agent['id']}")
        if agent.get('role'):
            print(f"    Role: {agent['role']}")
        if agent.get('capabilities'):
            print(f"    Capabilities: {', '.join(agent['capabilities'])}")
        print(f"    Tasks: {agent['tasks_assigned']}")

    print(f"\n📝 Tasks ({len(project['tasks'])})")
    if not project['tasks']:
        print("  No tasks yet")
    for task in project['tasks']:
        status_icon = {"pending": "⏳", "in_progress": "🔄", "complete": "✅"}.get(task['status'], "❓")
        print(f"  {status_icon} [{task['id']}] {task['description'][:40]}...")
        print(f"      → {task['assigned_to']} | {task['priority']}")

    print()


def main():
    if len(sys.argv) < 2:
        print("Agent Collaboration Template")
        print("Usage: agent-collab.py <command> [args]")
        print("\nCommands:")
        print("  init <name> [description]  - Start new collaboration")
        print("  add <agent_id> [role]      - Add agent to project")
        print("  assign <task> <agent_id>   - Assign task to agent")
        print("  status                     - Show project status")
        sys.exit(1)

    command = sys.argv[1]

    if command == "init":
        name = sys.argv[2] if len(sys.argv) > 2 else "Untitled"
        desc = sys.argv[3] if len(sys.argv) > 3 else ""
        init_project(name, desc)

    elif command == "add":
        if len(sys.argv) < 3:
            print("Usage: agent-collab.py add <agent_id> [role]")
            sys.exit(1)
        agent_id = sys.argv[2]
        role = sys.argv[3] if len(sys.argv) > 3 else ""
        add_agent(agent_id, role)

    elif command == "assign":
        if len(sys.argv) < 4:
            print("Usage: agent-collab.py assign <task_description> <agent_id> [priority]")
            sys.exit(1)
        task_desc = sys.argv[2]
        agent_id = sys.argv[3]
        priority = sys.argv[4] if len(sys.argv) > 4 else "medium"
        assign_task(task_desc, agent_id, priority)

    elif command == "status":
        show_status()

    else:
        print(f"❌ Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
