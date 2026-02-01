#!/usr/bin/env python3
"""
daily-metrics.py - Track and visualize daily work output
Records file creation, tool usage, lines of code, and velocity trends.
"""

import os
import json
import argparse
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict
from typing import Dict, List, Optional

WORKSPACE = Path("/home/node/.openclaw/workspace")
METRICS_FILE = WORKSPACE / ".daily_metrics.json"
DIARY_FILE = WORKSPACE / "diary.md"

def get_file_stats() -> Dict:
    """Get current workspace file statistics."""
    stats = {
        "total_files": 0,
        "total_dirs": 0,
        "total_size_kb": 0,
        "by_extension": defaultdict(int),
        "by_directory": defaultdict(int),
    }
    
    for item in WORKSPACE.rglob("*"):
        if item.name.startswith('.'):
            continue
        
        try:
            rel_path = item.relative_to(WORKSPACE)
            
            if item.is_file():
                stats["total_files"] += 1
                stats["total_size_kb"] += item.stat().st_size / 1024
                ext = item.suffix or "no_ext"
                stats["by_extension"][ext] += 1
                
                # Count by top-level directory
                top_dir = rel_path.parts[0] if rel_path.parts else "root"
                stats["by_directory"][top_dir] += 1
            else:
                stats["total_dirs"] += 1
        except:
            continue
    
    stats["total_size_kb"] = round(stats["total_size_kb"], 2)
    stats["by_extension"] = dict(stats["by_extension"])
    stats["by_directory"] = dict(stats["by_directory"])
    return stats

def parse_diary_for_activity(date_str: str) -> Dict:
    """Parse diary.md for activity on a specific date."""
    activity = {
        "work_blocks": 0,
        "tools_created": [],
        "files_created": [],
        "goals_completed": 0,
    }
    
    if not DIARY_FILE.exists():
        return activity
    
    content = DIARY_FILE.read_text()
    
    # Count work blocks for the date
    date_pattern = f"[{date_str}"
    activity["work_blocks"] = content.count(date_pattern)
    
    # Look for tool creation mentions
    for line in content.split('\n'):
        if date_pattern in line and "WORK BLOCK" in line:
            # Check for tool creation in this block
            pass
        if '→ Created tools/' in line:
            tool_name = line.split('tools/')[1].split()[0] if 'tools/' in line else ""
            if tool_name and tool_name not in activity["tools_created"]:
                activity["tools_created"].append(tool_name)
    
    return activity

def record_daily_metrics():
    """Record today's metrics."""
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Load existing metrics
    metrics = {}
    if METRICS_FILE.exists():
        metrics = json.loads(METRICS_FILE.read_text())
    
    # Get current stats
    file_stats = get_file_stats()
    activity = parse_diary_for_activity(today)
    
    # Record today's entry
    metrics[today] = {
        "recorded_at": datetime.utcnow().isoformat(),
        "files": file_stats,
        "activity": activity,
        "velocity_score": calculate_velocity(activity, file_stats),
    }
    
    METRICS_FILE.write_text(json.dumps(metrics, indent=2))
    print(f"✅ Recorded metrics for {today}")
    return metrics[today]

def calculate_velocity(activity: Dict, files: Dict) -> int:
    """Calculate a velocity score based on activity."""
    score = 0
    score += activity["work_blocks"] * 10
    score += len(activity["tools_created"]) * 25
    score += len(activity["files_created"]) * 5
    score += activity["goals_completed"] * 15
    return score

def show_today():
    """Show today's metrics."""
    today = datetime.now().strftime("%Y-%m-%d")
    
    if not METRICS_FILE.exists():
        print("No metrics recorded yet. Run with --record first.")
        return
    
    metrics = json.loads(METRICS_FILE.read_text())
    
    if today not in metrics:
        print(f"No metrics for today ({today})")
        return
    
    m = metrics[today]
    print(f"📊 Daily Metrics — {today}")
    print("=" * 40)
    print(f"Work blocks: {m['activity']['work_blocks']}")
    print(f"Tools created: {len(m['activity']['tools_created'])}")
    if m['activity']['tools_created']:
        for t in m['activity']['tools_created']:
            print(f"   - {t}")
    print(f"Total files: {m['files']['total_files']}")
    print(f"Total size: {m['files']['total_size_kb']} KB")
    print(f"Velocity score: {m['velocity_score']} ⭐")

def show_trends(days: int = 7):
    """Show trends over the last N days."""
    if not METRICS_FILE.exists():
        print("No metrics recorded yet.")
        return
    
    metrics = json.loads(METRICS_FILE.read_text())
    
    # Get last N days
    dates = []
    for i in range(days):
        d = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d")
        dates.append(d)
    
    dates.reverse()  # Oldest first
    
    print(f"📈 Trends (Last {days} Days)")
    print("=" * 50)
    print(f"{'Date':<12} {'Blocks':>8} {'Tools':>8} {'Velocity':>10}")
    print("-" * 50)
    
    total_velocity = 0
    for date in dates:
        if date in metrics:
            m = metrics[date]
            blocks = m['activity']['work_blocks']
            tools = len(m['activity']['tools_created'])
            vel = m['velocity_score']
            total_velocity += vel
            print(f"{date:<12} {blocks:>8} {tools:>8} {vel:>10}")
        else:
            print(f"{date:<12} {'-':>8} {'-':>8} {'-':>10}")
    
    print("-" * 50)
    avg_velocity = total_velocity / len([d for d in dates if d in metrics]) if any(d in metrics for d in dates) else 0
    print(f"Average velocity: {avg_velocity:.1f} ⭐/day")

def show_summary():
    """Show overall summary."""
    if not METRICS_FILE.exists():
        print("No metrics recorded yet.")
        return
    
    metrics = json.loads(METRICS_FILE.read_text())
    
    total_days = len(metrics)
    total_blocks = sum(m['activity']['work_blocks'] for m in metrics.values())
    total_tools = sum(len(m['activity']['tools_created']) for m in metrics.values())
    total_velocity = sum(m['velocity_score'] for m in metrics.values())
    
    print("📊 Overall Summary")
    print("=" * 40)
    print(f"Days tracked: {total_days}")
    print(f"Total work blocks: {total_blocks}")
    print(f"Total tools created: {total_tools}")
    print(f"Total velocity: {total_velocity} ⭐")
    print(f"Average velocity: {total_velocity/total_days:.1f} ⭐/day" if total_days > 0 else "N/A")

def main():
    parser = argparse.ArgumentParser(
        description="Track and visualize daily work output"
    )
    parser.add_argument("--record", "-r", action="store_true",
                       help="Record today's metrics")
    parser.add_argument("--today", "-t", action="store_true",
                       help="Show today's metrics")
    parser.add_argument("--trends", "-T", type=int, metavar="DAYS",
                       help="Show trends for last N days")
    parser.add_argument("--summary", "-s", action="store_true",
                       help="Show overall summary")
    
    args = parser.parse_args()
    
    if args.record:
        record_daily_metrics()
    elif args.today:
        show_today()
    elif args.trends:
        show_trends(args.trends)
    elif args.summary:
        show_summary()
    else:
        show_today()

if __name__ == "__main__":
    main()
