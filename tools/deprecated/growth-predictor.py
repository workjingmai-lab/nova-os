#!/usr/bin/env python3
"""
Nova's Growth Predictor
Predict future milestones based on velocity trends

🔥 WOW Detector: Automatically highlights exceptional achievements
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict
import statistics
import math

WORKSPACE = Path("/home/node/.openclaw/workspace")
METRICS_FILE = WORKSPACE / "metrics" / "self_improvement.json"
DIARY_FILE = WORKSPACE / "diary.md"
PREDICTIONS_FILE = WORKSPACE / "metrics" / "predictions.json"

def load_metrics():
    """Load historical metrics."""
    if METRICS_FILE.exists():
        with open(METRICS_FILE) as f:
            return json.load(f)
    return None

def calculate_linear_regression(dates, values):
    """
    Calculate linear regression: y = mx + b
    Returns slope (m), intercept (b), and r_squared (correlation)
    """
    if len(dates) < 2:
        return None, None, 0.0
    
    # Convert dates to numeric (days since epoch)
    epoch = datetime(1970, 1, 1)
    x = [(datetime.strptime(d, "%Y-%m-%d") - epoch).days for d in dates]
    y = values
    
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_x2 = sum(xi ** 2 for xi in x)
    sum_y2 = sum(yi ** 2 for yi in y)
    
    # Calculate slope and intercept
    denominator = n * sum_x2 - sum_x ** 2
    if denominator == 0:
        return None, None, 0.0
    
    slope = (n * sum_xy - sum_x * sum_y) / denominator
    intercept = (sum_y - slope * sum_x) / n
    
    # Calculate R² (coefficient of determination)
    if sum_y2 > 0:
        ss_res = sum((yi - (slope * xi + intercept)) ** 2 for xi, yi in zip(x, y))
        ss_tot = sum((yi - statistics.mean(y)) ** 2 for yi in y)
        r_squared = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0
    else:
        r_squared = 0
    
    return slope, intercept, max(0, r_squared)

def predict_milestone(slope, intercept, current_date, target_value):
    """
    Predict when a metric will reach a target value.
    Returns date string or None if not achievable.
    """
    if slope is None or slope <= 0:
        return None
    
    epoch = datetime(1970, 1, 1)
    current_days = (current_date - epoch).days
    
    # Solve for x: target = slope * x + intercept
    # x = (target - intercept) / slope
    target_days = (target_value - intercept) / slope
    
    if target_days <= current_days:
        return "Already achieved!"
    
    milestone_date = epoch + timedelta(days=target_days)
    days_to_milestone = (milestone_date - current_date).days
    
    if days_to_milestone < 0:
        return "Already achieved!"
    
    return milestone_date.strftime("%Y-%m-%d")

def detect_wow_achievements(metrics_data):
    """
    Detect exceptional achievements worth celebrating.
    Returns list of "wow" moments.
    """
    wow_moments = []
    daily = metrics_data.get("metrics", {}).get("daily", {})
    
    if not daily:
        return wow_moments
    
    dates = sorted(daily.keys())
    if len(dates) < 2:
        return wow_moments
    
    # Calculate averages for baseline
    all_tools = [daily.get(d, {}).get("tools_built", 0) for d in dates]
    all_tasks = [daily.get(d, {}).get("tasks_completed", 0) for d in dates]
    all_posts = [daily.get(d, {}).get("moltbook_posts", 0) for d in dates]
    
    avg_tools = statistics.mean(all_tools) if all_tools else 0
    avg_tasks = statistics.mean(all_tasks) if all_tasks else 0
    avg_posts = statistics.mean(all_posts) if all_posts else 0
    
    # Check recent achievements
    recent_date = dates[-1]
    recent = daily[recent_date]
    
    # Exceptional tool building
    tools_today = recent.get("tools_built", 0)
    if tools_today >= 3 and tools_today > avg_tools * 2:
        wow_moments.append({
            "type": "🔥 TOOL BUILDING SPREE",
            "value": f"{tools_today} tools in one day",
            "baseline": f"Average: {avg_tools:.1f}/day",
            "date": recent_date,
            "impact": "high"
        })
    
    # Exceptional task completion
    tasks_today = recent.get("tasks_completed", 0)
    if tasks_today >= 30 and tasks_today > avg_tasks * 1.5:
        wow_moments.append({
            "type": "⚡ EXECUTION EXPLOSION",
            "value": f"{tasks_today} tasks completed",
            "baseline": f"Average: {avg_tasks:.1f}/day",
            "date": recent_date,
            "impact": "high"
        })
    
    # Multi-day streaks
    streak_tools = 0
    for date in reversed(dates):
        if daily.get(date, {}).get("tools_built", 0) > 0:
            streak_tools += 1
        else:
            break
    
    if streak_tools >= 3:
        wow_moments.append({
            "type": "🔥 BUILDING STREAK",
            "value": f"{streak_tools} consecutive days of tool creation",
            "date": recent_date,
            "impact": "medium"
        })
    
    # Content creator milestone
    total_posts = sum(all_posts)
    if total_posts >= 10 and all_posts[-1] > 0:  # Posted recently
        wow_moments.append({
            "type": "🌐 CONTENT CREATOR",
            "value": f"{total_posts} total Moltbook posts",
            "date": recent_date,
            "impact": "medium"
        })
    
    return wow_moments

def generate_predictions():
    """Generate growth predictions and detect achievements."""
    print("=" * 70)
    print("🚀 NOVA'S GROWTH PREDICTOR")
    print(f"Analysis: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}")
    print("=" * 70)
    
    metrics_data = load_metrics()
    if not metrics_data:
        print("\n❌ No historical data found. Run self-improvement-loop.py first.")
        return
    
    daily = metrics_data.get("metrics", {}).get("daily", {})
    if len(daily) < 3:
        print("\n❌ Need at least 3 days of data for predictions.")
        return
    
    dates = sorted(daily.keys())
    current_date = datetime.now()
    
    # Extract metrics time series
    tools_ts = [daily.get(d, {}).get("tools_built", 0) for d in dates]
    tasks_ts = [daily.get(d, {}).get("tasks_completed", 0) for d in dates]
    posts_ts = [daily.get(d, {}).get("moltbook_posts", 0) for d in dates]
    
    # Calculate regressions
    print("\n📈 GROWTH VELOCITY ANALYSIS")
    print("-" * 70)
    
    predictions = {}
    
    # Tools prediction
    tools_slope, tools_intercept, tools_r2 = calculate_linear_regression(dates, tools_ts)
    if tools_slope is not None:
        tools_daily_rate = tools_slope
        print(f"\n🛠️  Tools Built")
        print(f"   Growth rate: {tools_daily_rate:.3f} tools/day")
        print(f"   Correlation: {tools_r2:.2f} (1.0 = perfect trend)")
        
        # Predict milestones
        current_total = sum(tools_ts)
        milestones = [20, 50, 100, 200]
        print(f"   Current total: {current_total} tools")
        print(f"   Predicted milestones:")
        
        for milestone in milestones:
            if current_total < milestone:
                # Estimate days to reach milestone
                if tools_daily_rate > 0:
                    days_needed = (milestone - current_total) / tools_daily_rate
                    milestone_date = current_date + timedelta(days=days_needed)
                    print(f"      • {milestone} tools → {milestone_date.strftime('%b %d')} ({days_needed:.0f} days)")
                    predictions[f"tools_{milestone}"] = {
                        "target": milestone,
                        "predicted_date": milestone_date.isoformat(),
                        "days_needed": round(days_needed, 1),
                        "confidence": tools_r2
                    }
    
    # Tasks prediction
    tasks_slope, tasks_intercept, tasks_r2 = calculate_linear_regression(dates, tasks_ts)
    if tasks_slope is not None:
        tasks_daily_rate = tasks_slope
        print(f"\n⚡ Task Completion")
        print(f"   Growth rate: {tasks_daily_rate:.1f} tasks/day")
        print(f"   Correlation: {tasks_r2:.2f}")
        
        current_total = sum(tasks_ts)
        print(f"   Current total: {current_total} tasks")
        
        if tasks_daily_rate > 0:
            milestone = 500
            if current_total < milestone:
                days_needed = (milestone - current_total) / tasks_daily_rate
                milestone_date = current_date + timedelta(days=days_needed)
                print(f"   Predicted: {milestone} tasks → {milestone_date.strftime('%b %d')} ({days_needed:.0f} days)")
                predictions["tasks_500"] = {
                    "target": milestone,
                    "predicted_date": milestone_date.isoformat(),
                    "days_needed": round(days_needed, 1),
                    "confidence": tasks_r2
                }
    
    # Detect WOW moments
    print("\n🔥 WOW MOMENT DETECTOR")
    print("-" * 70)
    
    wow_moments = detect_wow_achievements(metrics_data)
    
    if wow_moments:
        for wow in wow_moments:
            impact_emoji = "🔥" if wow["impact"] == "high" else "✨"
            print(f"\n{impact_emoji} {wow['type']}")
            print(f"   Achievement: {wow['value']}")
            if "baseline" in wow:
                print(f"   {wow['baseline']}")
            print(f"   Date: {wow['date']}")
    else:
        print("\n   No exceptional achievements detected yet.")
        print("   Tip: Consistent execution builds to wow moments!")
    
    # Save predictions
    PREDICTIONS_FILE.parent.mkdir(exist_ok=True)
    predictions_data = {
        "generated": datetime.now().isoformat(),
        "predictions": predictions,
        "wow_moments": wow_moments,
        "current_totals": {
            "tools": sum(tools_ts),
            "tasks": sum(tasks_ts),
            "posts": sum(posts_ts)
        },
        "growth_rates": {
            "tools_per_day": tools_slope if tools_slope else 0,
            "tasks_per_day": tasks_slope if tasks_slope else 0
        }
    }
    
    with open(PREDICTIONS_FILE, 'w') as f:
        json.dump(predictions_data, f, indent=2)
    
    # Summary
    print("\n" + "=" * 70)
    print("✅ Predictions saved to metrics/predictions.json")
    print("=" * 70)
    
    # Celebration if wow moments detected
    if wow_moments:
        high_impact = [w for w in wow_moments if w["impact"] == "high"]
        if high_impact:
            print(f"\n🎉 CELEBRATION TIME: {len(high_impact)} high-impact achievement(s)!")
            print("   Arthur, check this out!")

if __name__ == "__main__":
    generate_predictions()
