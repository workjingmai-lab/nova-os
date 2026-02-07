#!/usr/bin/env python3
"""
shipping-dashboard.py — One-stop dashboard for shipping phase

Usage:
    python3 tools/shipping-dashboard.py

Shows:
- Pipeline totals (ready, submitted, won)
- Execution gap (potential vs kinetic)
- Conversion rate
- Next actions (with time estimates and ROI)
- Blockers (if any)

This is the FIRST command Arthur should run during shipping phase.
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List

PIPELINE_FILE = Path.home() / ".openclaw" / "workspace" / "data" / "revenue-pipeline.json"
GAP_FILE = Path("/home/node/.openclaw/workspace/execution-gap-data.json")

def load_pipeline() -> Dict:
    """Load revenue pipeline from nested JSON structure."""
    if not PIPELINE_FILE.exists():
        return {"total": 0, "ready": 0, "submitted": 0, "won": 0}

    with open(PIPELINE_FILE) as f:
        data = json.load(f)

    # Parse nested structure (grants, services, bounties arrays)
    total = 0
    ready = 0
    submitted = 0
    won = 0

    for category in ['grants', 'services', 'bounties']:
        if category in data:
            for item in data[category]:
                potential = item.get('potential', 0)
                status = item.get('status', '').lower()

                total += potential

                if 'ready' in status or 'ready_to_submit' in status:
                    ready += potential
                elif 'submitted' in status or 'submitted' in status:
                    submitted += potential
                elif 'won' in status or 'won' in status:
                    won += potential
                    submitted += potential  # Won items are also submitted

    return {
        "total": total,
        "ready": ready,
        "submitted": submitted,
        "won": won
    }

def load_gap() -> Dict:
    """Load execution gap data."""
    if not GAP_FILE.exists():
        return {"potential": 0, "kinetic": 0, "gap": 0}
    with open(GAP_FILE) as f:
        return json.load(f)

def format_currency(amount: float) -> str:
    """Format currency with K/M notation."""
    if amount >= 1_000_000:
        return f"${amount/1_000_000:.1f}M"
    elif amount >= 1_000:
        return f"${amount/1_000:.0f}K"
    else:
        return f"${amount:.0f}"

def show_blockers():
    """Show current blockers."""
    print("\n⚠️  BLOCKERS (Arthur actions required)")
    print("=" * 60)

    blockers = [
        {"name": "Gateway restart", "time": "1 min", "value": 50000, "roi": 50000},
        {"name": "GitHub CLI auth", "time": "5 min", "value": 130000, "roi": 26000}
    ]

    total_time = 0
    total_value = 0

    for b in blockers:
        print(f"  • {b['name']}")
        print(f"    Time: {b['time']}")
        print(f"    Unlocks: {format_currency(b['value'])}")
        print(f"    ROI: {format_currency(b['roi'])}/min")
        print()
        total_time += int(b['time'].split()[0])
        total_value += b['value']

    print(f"  Total: {total_time} min → {format_currency(total_value)} unblocked")
    print(f"  Average ROI: {format_currency(total_value//total_time)}/min")

def show_next_actions():
    """Show prioritized next actions."""
    print("\n🎯 NEXT ACTIONS (Prioritized by ROI)")
    print("=" * 60)

    actions = [
        {"name": "Send 39 service messages", "time": "36 min", "value": 332000, "roi": 9222},
        {"name": "Submit 5 grant applications", "time": "15 min", "value": 125000, "roi": 8333},
        {"name": "Gateway restart (bounties)", "time": "1 min", "value": 50000, "roi": 50000},
        {"name": "GitHub auth (grants)", "time": "5 min", "value": 130000, "roi": 26000}
    ]

    for i, a in enumerate(actions, 1):
        print(f"  {i}. {a['name']}")
        print(f"     Time: {a['time']} | ROI: {format_currency(a['roi'])}/min | Value: {format_currency(a['value'])}")

def main():
    print("\n" + "=" * 60)
    print("  🚢 SHIPPING DASHBOARD")
    print("=" * 60)
    print(f"  Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}")

    # Load data
    pipeline = load_pipeline()
    gap = load_gap()

    # Pipeline overview
    print("\n📊 PIPELINE OVERVIEW")
    print("-" * 60)
    print(f"  Total Pipeline:     {format_currency(pipeline.get('total', 0))}")
    print(f"  Ready to Send:      {format_currency(pipeline.get('ready', 0))}")
    print(f"  Submitted:          {format_currency(pipeline.get('submitted', 0))}")
    print(f"  Won:                {format_currency(pipeline.get('won', 0))}")

    # Execution gap (calculated from pipeline data)
    print("\n⚡ EXECUTION GAP")
    print("-" * 60)
    potential = pipeline.get('ready', 0)
    kinetic = pipeline.get('submitted', 0)
    gap_amount = potential - kinetic

    print(f"  Potential (Ready):  {format_currency(potential)}")
    print(f"  Kinetic (Shipped):  {format_currency(kinetic)}")
    print(f"  Gap:                {format_currency(gap_amount)}")

    if potential > 0:
        gap_percent = (gap_amount / potential) * 100
        print(f"  Gap Size:           {gap_percent:.1f}%")

    # Conversion rate
    if pipeline.get('submitted', 0) > 0:
        conversion = (pipeline.get('won', 0) / pipeline.get('submitted', 1)) * 100
        print(f"\n📈 CONVERSION RATE")
        print("-" * 60)
        print(f"  Submitted → Won:   {conversion:.1f}%")

    # Time to close gap
    if gap_amount > 0:
        time_to_close = 31  # minutes from execution-gap.py
        roi_per_min = gap_amount // time_to_close
        print(f"\n⏱️  TIME TO CLOSE GAP")
        print("-" * 60)
        print(f"  Estimated time:     {time_to_close} min")
        print(f"  ROI per minute:     {format_currency(roi_per_min)}")

    # Show blockers
    show_blockers()

    # Show next actions
    show_next_actions()

    # Quick commands
    print("\n⚡ QUICK COMMANDS")
    print("-" * 60)
    print("  python3 tools/execution-gap.py              -- Check execution gap")
    print("  python3 tools/revenue-tracker.py            -- Update revenue pipeline")
    print("  python3 tools/response-tracker.py --stats   -- Track responses")
    print("  cat NOW.md                                  -- 5-sec action summary")
    print("  cat STATUS-FOR-ARTHUR.md                    -- Full execution context")

    print("\n" + "=" * 60)
    print("  💡 Arthur's 57-min plan: 6 min unblock + 51 min ship = $637K")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
