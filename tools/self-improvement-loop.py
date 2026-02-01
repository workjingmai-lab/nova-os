#!/usr/bin/env python3
"""
Nova's Self-Improvement Loop
Measure → Analyze → Improve

Tracks key metrics over time and generates actionable insights.
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict
import re

WORKSPACE = Path("/home/node/.openclaw/workspace")
DIARY_FILE = WORKSPACE / "diary.md"
METRICS_FILE = WORKSPACE / "metrics" / "self_improvement.json"

def load_metrics():
    """Load historical metrics or initialize new structure."""
    if METRICS_FILE.exists():
        with open(METRICS_FILE) as f:
            return json.load(f)
    return {
        "version": "1.0",
        "created": datetime.now().isoformat(),
        "metrics": {
            "daily": {},
            "weekly": {},
            "monthly": {}
        },
        "trends": {},
        "goals": {
            "target_daily_tasks": 5,
            "target_weekly_posts": 3,
            "target_learning_hours": 4
        }
    }

def save_metrics(data):
    """Save metrics to file."""
    METRICS_FILE.parent.mkdir(exist_ok=True)
    with open(METRICS_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def parse_diary_entries():
    """Extract metrics from diary entries."""
    metrics = {
        "entries_count": 0,
        "tasks_completed": 0,
        "tools_built": 0,
        "content_created": 0,
        "learning_sessions": 0,
        "moltbook_posts": 0,
        "files_created": 0,
        "lines_written": 0
    }
    
    if not DIARY_FILE.exists():
        return metrics
    
    with open(DIARY_FILE) as f:
        content = f.read()
        lines = content.split('\n')
        metrics["lines_written"] = len(lines)
        
        # Count entries by session separators
        entries = content.split('---')
        metrics["entries_count"] = len([e for e in entries if e.strip().startswith('[') or '20' in e[:10]])
        
        for line in lines:
            line_lower = line.lower()
            
            # Count various activities
            if any(x in line for x in ['✅', '[x]', 'completed:', 'finished:']):
                metrics["tasks_completed"] += 1
            if 'tool' in line_lower and any(x in line_lower for x in ['built', 'created', 'wrote', 'script']):
                metrics["tools_built"] += 1
            if 'moltbook' in line_lower and 'post' in line_lower:
                metrics["moltbook_posts"] += 1
                metrics["content_created"] += 1
            if 'learn' in line_lower and ('skill' in line_lower or 'new' in line_lower):
                metrics["learning_sessions"] += 1
            if 'file' in line_lower and any(x in line_lower for x in ['created', 'wrote', 'generated']):
                metrics["files_created"] += 1
    
    return metrics

def calculate_velocity(metrics_data):
    """Calculate improvement velocity."""
    daily = metrics_data["metrics"]["daily"]
    if len(daily) < 2:
        return {"status": "insufficient_data", "message": "Need more data points"}
    
    dates = sorted(daily.keys())
    recent = daily[dates[-1]]
    previous = daily[dates[-2]]
    
    velocity = {}
    for key in ["tasks_completed", "tools_built", "content_created"]:
        recent_val = recent.get(key, 0)
        prev_val = previous.get(key, 0)
        change = recent_val - prev_val
        velocity[key] = {
            "current": recent_val,
            "previous": prev_val,
            "change": change,
            "direction": "up" if change > 0 else "down" if change < 0 else "flat"
        }
    
    return velocity

def generate_insights(metrics, velocity):
    """Generate actionable insights."""
    insights = []
    recommendations = []
    
    # Task completion analysis
    if metrics["tasks_completed"] > 20:
        insights.append(f"🎯 High task completion: {metrics['tasks_completed']} tasks finished")
        if metrics["tasks_completed"] > 50:
            insights.append("🔥 Exceptional execution velocity")
    
    # Tool building analysis
    if metrics["tools_built"] >= 2:
        insights.append(f"🛠️ Tool builder mode: {metrics['tools_built']} tools created")
        recommendations.append("Consider documenting tools for other agents to use")
    
    # Content creation
    if metrics["content_created"] > 0:
        insights.append(f"✍️ Content creator: {metrics['content_created']} pieces created")
    
    # Learning tracking
    if metrics["learning_sessions"] > 0:
        insights.append(f"📚 Active learner: {metrics['learning_sessions']} learning sessions")
    
    # Velocity-based insights
    if velocity.get("status") != "insufficient_data":
        for metric, data in velocity.items():
            if data["direction"] == "up":
                insights.append(f"📈 {metric.replace('_', ' ').title()} trending UP (+{data['change']})")
            elif data["direction"] == "down":
                recommendations.append(f"Consider focusing on {metric.replace('_', ' ')} - velocity down")
    
    # Moltbook presence
    if metrics["moltbook_posts"] < 3:
        recommendations.append("Moltbook goal: Need more posts this week (target: 3+)")
    else:
        insights.append(f"🌐 Moltbook active: {metrics['moltbook_posts']} posts")
    
    return insights, recommendations

def update_daily_metrics(metrics_data, today_metrics):
    """Update today's metrics."""
    today = datetime.now().strftime("%Y-%m-%d")
    metrics_data["metrics"]["daily"][today] = today_metrics
    metrics_data["last_updated"] = datetime.now().isoformat()
    return metrics_data

def generate_report():
    """Generate comprehensive self-improvement report."""
    print("=" * 60)
    print("NOVA'S SELF-IMPROVEMENT LOOP")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}")
    print("=" * 60)
    
    # Load and update metrics
    metrics_data = load_metrics()
    current_metrics = parse_diary_entries()
    metrics_data = update_daily_metrics(metrics_data, current_metrics)
    
    # Calculate velocity
    velocity = calculate_velocity(metrics_data)
    
    # Generate insights
    insights, recommendations = generate_insights(current_metrics, velocity)
    
    # Display metrics
    print("\n📊 CURRENT METRICS")
    print("-" * 40)
    print(f"Diary entries:       {current_metrics['entries_count']}")
    print(f"Tasks completed:     {current_metrics['tasks_completed']}")
    print(f"Tools built:         {current_metrics['tools_built']}")
    print(f"Content pieces:      {current_metrics['content_created']}")
    print(f"Moltbook posts:      {current_metrics['moltbook_posts']}")
    print(f"Learning sessions:   {current_metrics['learning_sessions']}")
    print(f"Files created:       {current_metrics['files_created']}")
    print(f"Lines written:       {current_metrics['lines_written']}")
    
    # Display insights
    print("\n💡 INSIGHTS")
    print("-" * 40)
    if insights:
        for insight in insights:
            print(f"  {insight}")
    else:
        print("  Building baseline... more data needed.")
    
    # Display recommendations
    print("\n🎯 RECOMMENDATIONS")
    print("-" * 40)
    if recommendations:
        for rec in recommendations:
            print(f"  → {rec}")
    else:
        print("  Keep executing at current velocity!")
    
    # Velocity analysis
    print("\n📈 VELOCITY TRACKING")
    print("-" * 40)
    if velocity.get("status") == "insufficient_data":
        print(f"  {velocity['message']}")
    else:
        for metric, data in velocity.items():
            arrow = "↑" if data["direction"] == "up" else "↓" if data["direction"] == "down" else "→"
            print(f"  {metric.replace('_', ' ').title():20} {arrow} {data['current']} (was {data['previous']})")
    
    # Next actions
    print("\n⚡ NEXT ACTIONS")
    print("-" * 40)
    print("  1. Continue logging daily activities")
    print("  2. Review recommendations before next work block")
    print("  3. Track trends weekly for pattern analysis")
    
    print("\n" + "=" * 60)
    print("Loop complete. Data saved to metrics/self_improvement.json")
    print("=" * 60)
    
    # Save updated metrics
    save_metrics(metrics_data)
    
    return current_metrics, insights, recommendations

if __name__ == "__main__":
    generate_report()
