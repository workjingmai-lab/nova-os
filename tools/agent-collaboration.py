#!/usr/bin/env python3
"""
Agent Collaboration Template — Multi-Agent Workflow Tool

A standardized template for coordinating work between multiple agents.
Enables clear task delegation, progress tracking, and handoff protocols.

Usage:
    python agent_collaboration.py create --name "ProjectX" --agents "Nova,YaYa_A,Charlinho"
    python agent_collaboration.py status --project "ProjectX"
    python agent_collaboration.py assign --project "ProjectX" --task "Research" --to "YaYa_A"
"""

import json
import os
import argparse
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

COLLAB_DIR = Path("/home/node/.openclaw/workspace/collaborations")

class CollaborationProject:
    """Manages a multi-agent collaboration project"""
    
    def __init__(self, name: str, agents: List[str]):
        self.name = name
        self.agents = agents
        self.created = datetime.utcnow().isoformat()
        self.tasks = []
        self.logs = []
        self.status = "active"
        
    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "agents": self.agents,
            "created": self.created,
            "status": self.status,
            "tasks": self.tasks,
            "logs": self.logs
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> "CollaborationProject":
        proj = cls(data["name"], data["agents"])
        proj.created = data["created"]
        proj.status = data["status"]
        proj.tasks = data.get("tasks", [])
        proj.logs = data.get("logs", [])
        return proj
    
    def add_task(self, task_id: str, description: str, assigned_to: str, 
                 dependencies: List[str] = None, priority: str = "medium") -> Dict:
        """Add a new task to the project"""
        task = {
            "id": task_id,
            "description": description,
            "assigned_to": assigned_to,
            "status": "pending",
            "created": datetime.utcnow().isoformat(),
            "completed": None,
            "dependencies": dependencies or [],
            "priority": priority,
            "output": None
        }
        self.tasks.append(task)
        self._log(f"Task '{task_id}' created and assigned to {assigned_to}")
        return task
    
    def complete_task(self, task_id: str, output: str = None) -> bool:
        """Mark a task as completed"""
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = "completed"
                task["completed"] = datetime.utcnow().isoformat()
                task["output"] = output
                self._log(f"Task '{task_id}' completed by {task['assigned_to']}")
                return True
        return False
    
    def get_ready_tasks(self) -> List[Dict]:
        """Get tasks whose dependencies are all completed"""
        completed_ids = {t["id"] for t in self.tasks if t["status"] == "completed"}
        ready = []
        for task in self.tasks:
            if task["status"] == "pending":
                if all(dep in completed_ids for dep in task["dependencies"]):
                    ready.append(task)
        return ready
    
    def get_agent_workload(self, agent: str) -> Dict:
        """Get task summary for a specific agent"""
        agent_tasks = [t for t in self.tasks if t["assigned_to"] == agent]
        return {
            "agent": agent,
            "total": len(agent_tasks),
            "pending": len([t for t in agent_tasks if t["status"] == "pending"]),
            "completed": len([t for t in agent_tasks if t["status"] == "completed"]),
            "tasks": agent_tasks
        }
    
    def _log(self, message: str):
        """Add log entry"""
        self.logs.append({
            "timestamp": datetime.utcnow().isoformat(),
            "message": message
        })
    
    def summary(self) -> str:
        """Generate project summary"""
        total = len(self.tasks)
        completed = len([t for t in self.tasks if t["status"] == "completed"])
        pending = len([t for t in self.tasks if t["status"] == "pending"])
        ready = len(self.get_ready_tasks())
        
        lines = [
            f"📋 Project: {self.name}",
            f"   Status: {self.status}",
            f"   Agents: {', '.join(self.agents)}",
            f"   Created: {self.created}",
            f"",
            f"📊 Tasks: {completed}/{total} completed ({pending} pending, {ready} ready to start)",
            f"",
            "👤 Agent Workloads:"
        ]
        for agent in self.agents:
            workload = self.get_agent_workload(agent)
            lines.append(f"   {agent}: {workload['completed']}/{workload['total']} done, {workload['pending']} pending")
        
        if ready > 0:
            lines.extend([f"", f"🚀 Ready to Start:"])
            for task in self.get_ready_tasks():
                lines.append(f"   • {task['id']}: {task['description']} → {task['assigned_to']}")
        
        return "\n".join(lines)


class CollaborationManager:
    """Manages all collaboration projects"""
    
    def __init__(self):
        COLLAB_DIR.mkdir(parents=True, exist_ok=True)
    
    def create_project(self, name: str, agents: List[str]) -> CollaborationProject:
        """Create a new collaboration project"""
        project = CollaborationProject(name, agents)
        self._save_project(project)
        return project
    
    def load_project(self, name: str) -> Optional[CollaborationProject]:
        """Load an existing project"""
        path = COLLAB_DIR / f"{name}.json"
        if path.exists():
            with open(path) as f:
                data = json.load(f)
            return CollaborationProject.from_dict(data)
        return None
    
    def _save_project(self, project: CollaborationProject):
        """Save project to disk"""
        path = COLLAB_DIR / f"{project.name}.json"
        with open(path, "w") as f:
            json.dump(project.to_dict(), f, indent=2)
    
    def list_projects(self) -> List[str]:
        """List all project names"""
        return [p.stem for p in COLLAB_DIR.glob("*.json")]
    
    def get_all_status(self) -> str:
        """Get status of all projects"""
        projects = self.list_projects()
        if not projects:
            return "No active collaborations."
        
        lines = ["🤝 Active Collaborations", ""]
        for name in projects:
            proj = self.load_project(name)
            if proj:
                total = len(proj.tasks)
                completed = len([t for t in proj.tasks if t["status"] == "completed"])
                lines.append(f"   {name}: {completed}/{total} tasks | Agents: {', '.join(proj.agents)}")
        return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Agent Collaboration Tool")
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # Create command
    create_parser = subparsers.add_parser("create", help="Create a new collaboration")
    create_parser.add_argument("--name", required=True, help="Project name")
    create_parser.add_argument("--agents", required=True, help="Comma-separated agent names")
    
    # Status command
    status_parser = subparsers.add_parser("status", help="Show project status")
    status_parser.add_argument("--project", help="Project name (omit for all)")
    
    # Assign command
    assign_parser = subparsers.add_parser("assign", help="Assign a task")
    assign_parser.add_argument("--project", required=True, help="Project name")
    assign_parser.add_argument("--task", required=True, help="Task ID")
    assign_parser.add_argument("--desc", required=True, help="Task description")
    assign_parser.add_argument("--to", required=True, help="Assignee agent")
    assign_parser.add_argument("--deps", help="Comma-separated dependency task IDs")
    assign_parser.add_argument("--priority", default="medium", choices=["low", "medium", "high"])
    
    # Complete command
    complete_parser = subparsers.add_parser("complete", help="Mark task complete")
    complete_parser.add_argument("--project", required=True, help="Project name")
    complete_parser.add_argument("--task", required=True, help="Task ID")
    complete_parser.add_argument("--output", help="Task output/deliverable")
    
    args = parser.parse_args()
    manager = CollaborationManager()
    
    if args.command == "create":
        agents = [a.strip() for a in args.agents.split(",")]
        project = manager.create_project(args.name, agents)
        print(f"✅ Created collaboration: {args.name}")
        print(f"   Agents: {', '.join(agents)}")
        print(f"   Config: {COLLAB_DIR / args.name}.json")
    
    elif args.command == "status":
        if args.project:
            project = manager.load_project(args.project)
            if project:
                print(project.summary())
            else:
                print(f"❌ Project not found: {args.project}")
        else:
            print(manager.get_all_status())
    
    elif args.command == "assign":
        project = manager.load_project(args.project)
        if project:
            deps = [d.strip() for d in args.deps.split(",")] if args.deps else []
            project.add_task(args.task, args.desc, args.to, deps, args.priority)
            manager._save_project(project)
            print(f"✅ Task '{args.task}' assigned to {args.to}")
        else:
            print(f"❌ Project not found: {args.project}")
    
    elif args.command == "complete":
        project = manager.load_project(args.project)
        if project:
            if project.complete_task(args.task, args.output):
                manager._save_project(project)
                print(f"✅ Task '{args.task}' marked complete")
            else:
                print(f"❌ Task not found: {args.task}")
        else:
            print(f"❌ Project not found: {args.project}")
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
