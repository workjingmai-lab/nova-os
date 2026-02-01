#!/usr/bin/env python3
"""
Nova's Efficiency Metrics Tracker
Track task completion, token usage, and performance over time
"""
import json
import os
from datetime import datetime

METRICS_FILE = "/home/node/.openclaw/workspace/.metrics.json"
WORKSPACE = "/home/node/.openclaw/workspace"

def load_metrics():
    """Load existing metrics"""
    if os.path.exists(METRICS_FILE):
        with open(METRICS_FILE, 'r') as f:
            return json.load(f)
    return {"tasks": [], "daily": {}}

def save_metrics(metrics):
    """Save metrics to file"""
    with open(METRICS_FILE, 'w') as f:
        json.dump(metrics, f, indent=2)

def log_task(task_name, status, notes=""):
    """Log a task completion"""
    metrics = load_metrics()
    today = datetime.utcnow().strftime("%Y-%m-%d")

    task = {
        "timestamp": datetime.utcnow().isoformat(),
        "task": task_name,
        "status": status,  # success, failed, partial
        "notes": notes
    }

    metrics["tasks"].append(task)

    # Update daily stats
    if today not in metrics["daily"]:
        metrics["daily"][today] = {
            "completed": 0,
            "failed": 0,
            "total": 0
        }

    metrics["daily"][today]["total"] += 1
    if status == "success":
        metrics["daily"][today]["completed"] += 1
    elif status == "failed":
        metrics["daily"][today]["failed"] += 1

    save_metrics(metrics)
    print(f"✅ Logged: {task_name} ({status})")

def show_summary():
    """Show performance summary"""
    metrics = load_metrics()

    print("\n📊 Nova's Performance Metrics")
    print("=" * 40)

    # Show last 7 days
    from collections import OrderedDict
    last_7 = OrderedDict(sorted(metrics["daily"].items(), reverse=True)[:7])

    for date, stats in last_7.items():
        success_rate = (stats["completed"] / stats["total"] * 100) if stats["total"] > 0 else 0
        print(f"{date}: {stats['completed']}/{stats['total']} tasks ({success_rate:.0f}%)")

    # Overall stats
    total_tasks = len(metrics["tasks"])
    completed = sum(1 for t in metrics["tasks"] if t["status"] == "success")
    overall_rate = (completed / total_tasks * 100) if total_tasks > 0 else 0

    print(f"\nOverall: {completed}/{total_tasks} tasks ({overall_rate:.0f}%)")

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "summary":
        show_summary()
    elif len(sys.argv) > 3:
        log_task(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "")
    else:
        print("Usage: metrics.py 'task name' 'status' [notes]")
        print("   or: metrics.py summary")
