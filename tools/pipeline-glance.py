#!/usr/bin/env python3
"""
Pipeline at a Glance — One-line status check

Shows current pipeline state in one second.
Run: python3 tools/pipeline-glance.py
"""

import json
from pathlib import Path

def main():
    # Read pipeline data
    pipeline_file = Path("revenue-pipeline.json")
    if not pipeline_file.exists():
        print("❌ Pipeline file not found. Run revenue-tracker.py first.")
        return

    with open(pipeline_file) as f:
        data = json.load(f)

    # Calculate totals
    total = data.get("total_pipeline", 0)
    submitted = data.get("total_submitted", 0)
    won = data.get("total_won", 0)
    conversion = (won / total * 100) if total > 0 else 0

    # Calculate ready amount
    ready_grants = sum(item.get("potential", 0) for item in data.get("grants", [])
                       if item.get("status") in ["ready", "researched"])
    ready_services = sum(item.get("potential", 0) for item in data.get("services", [])
                         if item.get("status") in ["ready", "message_ready"])

    ready_total = ready_grants + ready_services

    # Display
    print(f"💰 ${total:,.0f} total | ${submitted:,.0f} submitted | ${won:,.0f} won | {conversion:.1f}% conversion | ${ready_total:,.0f} ready NOW")
    print(f"⚡  Gap: ${ready_total:,.0f} waiting to ship | ${ready_total/57:,.0f}/min ROI if Arthur executes 57-min plan")

if __name__ == "__main__":
    main()
