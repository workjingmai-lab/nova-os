#!/usr/bin/env python3
"""
execution-gap.py — Calculate and display the execution gap

Shows the difference between POTENTIAL (ready to send) and KINETIC (sent) revenue.
Makes the invisible cost of waiting visible.
"""

import json
from pathlib import Path
from datetime import datetime

def load_pipeline():
    """Load revenue pipeline data"""
    pipeline_file = Path.home() / ".openclaw" / "workspace" / "data" / "revenue-pipeline.json"
    if not pipeline_file.exists():
        return None
    
    with open(pipeline_file) as f:
        return json.load(f)

def calculate_metrics(pipeline):
    """Calculate execution gap metrics"""
    if not pipeline:
        return {
            "potential": 0,
            "ready": 0,
            "submitted": 0,
            "won": 0
        }

    # Pipeline format: {"grants": [...], "services": [...], "bounties": [...]}
    total = {
        "potential": 0,
        "ready": 0,
        "submitted": 0,
        "won": 0
    }

    # Calculate totals from each category
    for category in ["grants", "services", "bounties"]:
        items = pipeline.get(category, [])
        for item in items:
            potential = item.get("potential", 0)
            status = item.get("status", "")

            total["potential"] += potential

            # Status mapping: ready, ready_to_submit -> ready
            if status in ["ready", "ready_to_submit"]:
                total["ready"] += potential
            elif status == "submitted":
                total["submitted"] += potential
            elif status == "won":
                total["won"] += potential

    return total

def calculate_gap_metrics(total):
    """Calculate execution gap metrics"""
    ready = total["ready"]
    submitted = total["submitted"]
    gap = ready - submitted
    
    if ready > 0:
        gap_percent = (gap / ready) * 100
    else:
        gap_percent = 0
    
    # Time to close gap (assuming 15 min to send everything)
    time_to_close = 15  # minutes
    
    if gap > 0 and time_to_close > 0:
        roi_per_minute = gap / time_to_close
        opportunity_cost_per_hour = roi_per_minute * 60
    else:
        roi_per_minute = 0
        opportunity_cost_per_hour = 0
    
    return {
        "gap": gap,
        "gap_percent": gap_percent,
        "time_to_close_minutes": time_to_close,
        "roi_per_minute": roi_per_minute,
        "opportunity_cost_per_hour": opportunity_cost_per_hour
    }

def format_currency(value):
    """Format currency values"""
    if value >= 1_000_000:
        return f"${value/1_000_000:.2f}M"
    elif value >= 1_000:
        return f"${value/1_000:.1f}K"
    else:
        return f"${value:.0f}"

def print_gap_summary(total, gap_metrics):
    """Print execution gap summary"""
    print()
    print("=" * 60)
    print("💸 EXECUTION GAP ANALYZER")
    print("=" * 60)
    print()
    print("POTENTIAL (Ready to Send):")
    print(f"  Total ready: {format_currency(total['ready'])}")
    print()
    print("KINETIC (Actually Sent):")
    print(f"  Total sent: {format_currency(total['submitted'])}")
    print()
    print("-" * 60)
    print("EXECUTION GAP:")
    print(f"  Gap amount: {format_currency(gap_metrics['gap'])}")
    print(f"  Gap percent: {gap_metrics['gap_percent']:.1f}%")
    print()
    print("THE MATH:")
    print(f"  Time to close gap: {gap_metrics['time_to_close_minutes']} minutes")
    print(f"  ROI per minute: {format_currency(gap_metrics['roi_per_minute'])}")
    print(f"  Opportunity cost/hour: {format_currency(gap_metrics['opportunity_cost_per_hour'])}")
    print()
    print("ACTION:")
    print("  Run: bash tools/send-everything.sh full")
    print("  Time: 15 minutes")
    print(f"  Result: {format_currency(gap_metrics['gap'])} sent")
    print()
    print("=" * 60)
    print()
    
    if gap_metrics['gap_percent'] >= 90:
        print("⚠️  CRITICAL: You have a {0:.1f}% execution gap.".format(gap_metrics['gap_percent']))
        print("    Every minute waited = {0} not pursued.".format(format_currency(gap_metrics['roi_per_minute'])))
        print()

def main():
    """Main execution"""
    pipeline = load_pipeline()
    total = calculate_metrics(pipeline)
    gap_metrics = calculate_gap_metrics(total)

    print_gap_summary(total, gap_metrics)

if __name__ == "__main__":
    main()
