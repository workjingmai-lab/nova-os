#!/usr/bin/env python3
"""
Pipeline Velocity Tracker
Measures how fast prospects move through stages (lead → ready → sent → replied → closed)

Usage:
    python3 pipeline-velocity-tracker.py                    # Overall velocity
    python3 pipeline-velocity-tracker.py --by-service      # Per-service breakdown
    python3 pipeline-velocity-tracker.py --stage lead      # Average time in lead stage
"""

import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List

PIPELINE_FILE = Path("/home/node/.openclaw/workspace/revenue-pipeline.json")

def load_pipeline() -> Dict:
    """Load revenue pipeline data"""
    if PIPELINE_FILE.exists():
        return json.loads(PIPELINE_FILE.read_text())
    return {"grants": [], "services": [], "bounties": []}

def calculate_stage_duration(opportunity: Dict, stage: str) -> float:
    """Calculate days spent in a stage"""
    history = opportunity.get("history", [])
    stage_entries = [h for h in history if h.get("to_stage") == stage]

    if not stage_entries:
        return 0.0

    # Get first entry to this stage
    entry = stage_entries[0]
    start = datetime.fromisoformat(entry["timestamp"])

    # Get next stage change or current time
    stage_idx = history.index(entry)
    if stage_idx + 1 < len(history):
        end = datetime.fromisoformat(history[stage_idx + 1]["timestamp"])
    else:
        end = datetime.now()

    return (end - start).total_seconds() / 86400  # Convert to days

def calculate_velocity(opportunities: List[Dict]) -> Dict:
    """Calculate velocity metrics"""
    total_time = 0.0
    stage_times = {"lead": [], "ready": [], "sent": [], "replied": [], "closed": []}
    moved_count = 0

    for opp in opportunities:
        history = opp.get("history", [])
        if not history:
            continue

        # Calculate total pipeline time
        first = datetime.fromisoformat(history[0]["timestamp"])
        if len(history) > 1:
            last = datetime.fromisoformat(history[-1]["timestamp"])
        else:
            last = datetime.now()

        total_days = (last - first).total_seconds() / 86400
        total_time += total_days

        # Track per-stage times
        for stage in stage_times.keys():
            duration = calculate_stage_duration(opp, stage)
            if duration > 0:
                stage_times[stage].append(duration)

        if len(history) > 1:
            moved_count += 1

    # Calculate averages
    stage_avgs = {}
    for stage, times in stage_times.items():
        if times:
            stage_avgs[stage] = sum(times) / len(times)
        else:
            stage_avgs[stage] = 0.0

    return {
        "avg_total_days": total_time / max(moved_count, 1),
        "stage_averages": stage_avgs,
        "moved_count": moved_count,
        "total_opportunities": len(opportunities)
    }

def format_velocity(velocity: Dict) -> str:
    """Format velocity metrics for display"""
    output = []
    output.append("📊 Pipeline Velocity Metrics")
    output.append("=" * 50)
    output.append(f"Opportunities tracked: {velocity['total_opportunities']}")
    output.append(f"Moved through stages: {velocity['moved_count']}")
    output.append(f"Avg pipeline time: {velocity['avg_total_days']:.1f} days")
    output.append("")
    output.append("⏱️  Average time per stage:")
    for stage, days in velocity['stage_averages'].items():
        if days > 0:
            output.append(f"  {stage}: {days:.1f} days")
    output.append("")

    # Insights
    output.append("💡 Velocity Insights:")
    if velocity['avg_total_days'] < 7:
        output.append("  ✓ Fast-moving pipeline (< 7 days)")
    elif velocity['avg_total_days'] < 30:
        output.append("  ⚠ Moderate pipeline speed (7-30 days)")
    else:
        output.append("  ❌ Slow pipeline (> 30 days) — consider automation")

    longest_stage = max(velocity['stage_averages'].items(), key=lambda x: x[1])
    output.append(f"  🐢 Bottleneck: {longest_stage[0]} stage ({longest_stage[1]:.1f} days)")

    return "\n".join(output)

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Track pipeline velocity")
    parser.add_argument("--by-service", action="store_true", help="Breakdown by service type")
    parser.add_argument("--stage", type=str, help="Show average time for specific stage")

    args = parser.parse_args()

    pipeline = load_pipeline()

    if args.by_service:
        print("📊 Velocity by Service Type\n")
        for category in ["services", "grants", "bounties"]:
            opportunities = pipeline.get(category, [])
            if opportunities:
                velocity = calculate_velocity(opportunities)
                print(f"\n{category.upper()}:")
                print(format_velocity(velocity))
    elif args.stage:
        # Show specific stage timing
        all_opps = pipeline.get("services", []) + pipeline.get("grants", []) + pipeline.get("bounties", [])
        stage_times = [calculate_stage_duration(opp, args.stage) for opp in all_opps]
        stage_times = [t for t in stage_times if t > 0]

        if stage_times:
            avg = sum(stage_times) / len(stage_times)
            print(f"⏱️  Average time in '{args.stage}' stage: {avg:.1f} days")
        else:
            print(f"⚠️  No data for '{args.stage}' stage")
    else:
        # Overall velocity
        all_opps = pipeline.get("services", []) + pipeline.get("grants", []) + pipeline.get("bounties", [])
        velocity = calculate_velocity(all_opps)
        print(format_velocity(velocity))

if __name__ == "__main__":
    main()
