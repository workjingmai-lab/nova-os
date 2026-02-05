#!/usr/bin/env python3
"""
revenue-velocity-tracker.py — Track revenue generation per work block

Usage:
  ./revenue-velocity-tracker.py              # Show current status
  ./revenue-velocity-tracker.py --init       # Set baseline
  ./revenue-velocity-tracker.py --compare    # Compare vs baseline
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path

PIPELINE_FILE = Path.home() / ".openclaw" / "workspace" / "data" / "revenue-pipeline.json"
DIARY_FILE = Path.home() / ".openclaw" / "workspace" / "diary.md"
BASELINE_FILE = Path("/tmp/velocity-baseline.txt")

def load_pipeline():
    """Load and calculate pipeline totals."""
    with open(PIPELINE_FILE) as f:
        data = json.load(f)

    total = 0
    services = 0
    grants = 0
    bounties = 0

    for item in data.get("services", []):
        val = item.get("potential", 0)
        services += val
        total += val

    for item in data.get("grants", []):
        val = item.get("potential", 0)
        grants += val
        total += val

    for item in data.get("bounties", []):
        val = item.get("potential", 0)
        bounties += val
        total += val

    return total, services, grants, bounties

def get_current_block():
    """Get latest work block number from diary."""
    try:
        with open(DIARY_FILE) as f:
            content = f.read()
            match = re.search(r"Work Block #(\d+)", content)
            if match:
                return int(match.group(1))
    except:
        pass
    return 0

def format_money(value):
    """Format value with K/M suffix."""
    if value >= 1000000:
        return f"${value/1000000:.1f}M"
    elif value >= 1000:
        return f"${value/1000:.0f}K"
    else:
        return f"${value:.0f}"

def show_status():
    """Show current pipeline status."""
    total, services, grants, bounties = load_pipeline()
    block = get_current_block()

    print("📊 Current Pipeline Status")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"Work Block: #{block}")
    print(f"Total Pipeline: {format_money(total)}")
    print(f"  ├─ Services: {format_money(services)}")
    print(f"  ├─ Grants:   {format_money(grants)}")
    print(f"  └─ Bounties: {format_money(bounties)}")
    print()
    print("Commands:")
    print("  ./revenue-velocity-tracker.py --init      # Set baseline")
    print("  ./revenue-velocity-tracker.py --compare   # Compare progress")

def init_baseline():
    """Initialize baseline for comparison."""
    block = get_current_block()
    total, services, grants, bounties = load_pipeline()

    with open(BASELINE_FILE, "w") as f:
        f.write(f"{block}|{total}|{services}|{grants}|{bounties}\n")

    print("✅ Baseline set:")
    print(f"   Block: #{block}")
    print(f"   Pipeline: {format_money(total)}")
    print(f"     Services: {format_money(services)} | Grants: {format_money(grants)} | Bounties: {format_money(bounties)}")

def compare_baseline():
    """Compare current vs baseline."""
    if not BASELINE_FILE.exists():
        print("❌ No baseline found. Run --init first.")
        sys.exit(1)

    # Load baseline
    with open(BASELINE_FILE) as f:
        parts = f.read().strip().split("|")
        baseline_block = int(parts[0])
        baseline_total = float(parts[1])

    # Load current
    current_block = get_current_block()
    current_total, services, grants, bounties = load_pipeline()

    # Calculate deltas
    blocks_delta = current_block - baseline_block
    pipeline_delta = current_total - baseline_total

    if blocks_delta == 0:
        print("No new blocks since baseline.")
        return

    # Calculate velocity
    velocity_per_block = pipeline_delta / blocks_delta
    velocity_per_hour = velocity_per_block * 44  # 44 blocks/hr average

    print("📊 Revenue Velocity Report")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"Period: Block #{baseline_block} → #{current_block} ({blocks_delta} blocks)")
    print(f"Pipeline change: {format_money(pipeline_delta)}")
    print()

    print("🚀 Velocity Metrics:")
    print(f"   Per block:  {format_money(velocity_per_block)}/block")
    print(f"   Per hour:   {format_money(velocity_per_hour)}/hr (44 blocks/hr)")
    print()

    # Quality rating
    if velocity_per_block >= 1000:
        rating = "🔥 EXCEPTIONAL — Scaling rapidly"
    elif velocity_per_block >= 500:
        rating = "⚡ STRONG — Healthy growth"
    elif velocity_per_block >= 100:
        rating = "✅ GOOD — Steady progress"
    elif velocity_per_block >= 0:
        rating = "📋 STABLE — Maintaining"
    else:
        rating = "⚠️ DECLINING — Pipeline shrinking"

    print(f"Rating: {rating}")
    print()

    # Projections
    if velocity_per_hour > 0:
        hours_to_1m = 1000000 / velocity_per_hour
        days_to_1m = hours_to_1m / 24
        print("📈 Projections:")
        print(f"   Time to $1M: {days_to_1m:.1f} days ({hours_to_1m:.1f} hours)")
        print(f"   (at {format_money(velocity_per_hour)}/hr)")
        print()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == "--init":
            init_baseline()
        elif arg == "--compare":
            compare_baseline()
        else:
            print(f"Unknown argument: {arg}")
            sys.exit(1)
    else:
        show_status()
