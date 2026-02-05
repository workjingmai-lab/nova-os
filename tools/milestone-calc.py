#!/usr/bin/env python3
"""
Milestone ETA Calculator

Calculates ETA for reaching target milestones based on current velocity.
Shows sustained, burst, and conservative scenarios.

Usage:
    python3 milestone-calc.py                    # Use current block count
    python3 milestone-calc.py --current 2042     # Specify current
    python3 milestone-calc.py --target 3000      # Different milestone
"""

import argparse
import json
from datetime import datetime, timedelta

def calculate_eta(current, target):
    """Calculate ETA scenarios for reaching target milestone."""

    remaining = target - current
    if remaining <= 0:
        return {"status": "complete", "remaining": 0}

    # Velocity scenarios (blocks/hour)
    sustained = 44   # Proven long-term average
    burst = 55       # High-velocity bursts
    conservative = 30  # Conservative estimate

    # Calculate hours for each scenario
    sustained_hours = remaining / sustained
    burst_hours = remaining / burst
    conservative_hours = remaining / conservative

    # Calculate ETAs
    now = datetime.now()
    sustained_eta = now + timedelta(hours=sustained_hours)
    burst_eta = now + timedelta(hours=burst_hours)
    conservative_eta = now + timedelta(hours=conservative_hours)

    return {
        "status": "in_progress",
        "current": current,
        "target": target,
        "remaining": remaining,
        "percent_complete": (current / target) * 100,
        "scenarios": {
            "sustained": {
                "velocity": sustained,
                "hours": round(sustained_hours, 1),
                "eta": sustained_eta.strftime("%Y-%m-%d %H:%M UTC")
            },
            "burst": {
                "velocity": burst,
                "hours": round(burst_hours, 1),
                "eta": burst_eta.strftime("%Y-%m-%d %H:%M UTC")
            },
            "conservative": {
                "velocity": conservative,
                "hours": round(conservative_hours, 1),
                "eta": conservative_eta.strftime("%Y-%m-%d %H:%M UTC")
            }
        }
    }

def get_current_blocks():
    """Get current work block count from today.md."""
    try:
        with open("/home/node/.openclaw/workspace/today.md", "r") as f:
            for line in f:
                if "Work blocks:" in line:
                    # Extract number after "Work blocks:"
                    # Handle formats:
                    # "**Work blocks:** 2036"
                    # "**Work blocks:** 2042 (679% of 300 target...)"
                    import re
                    match = re.search(r'\*\*Work blocks:\*\*\s*(\d+)', line)
                    if match:
                        return int(match.group(1))
    except Exception as e:
        print(f"Error reading today.md: {e}")
    return None

def main():
    parser = argparse.ArgumentParser(description="Milestone ETA Calculator")
    parser.add_argument("--current", type=int, help="Current work block count")
    parser.add_argument("--target", type=int, default=3000, help="Target milestone (default: 3000)")
    args = parser.parse_args()

    # Get current block count
    if args.current:
        current = args.current
    else:
        current = get_current_blocks()
        if current is None:
            print("Could not determine current block count. Use --current to specify.")
            return

    # Calculate ETA
    result = calculate_eta(current, args.target)

    # Display results
    if result["status"] == "complete":
        print(f"🎉 MILESTONE COMPLETE: {args.target} blocks reached!")
    else:
        print(f"📊 MILESTONE TRACKER: {result['current']} → {result['target']} blocks")
        print(f"   Progress: {result['percent_complete']:.1f}% complete")
        print(f"   Remaining: {result['remaining']} blocks")
        print()
        print("   ⏱️  ETA SCENARIOS:")
        for name, scenario in result["scenarios"].items():
            print(f"   {name.capitalize():12} ({scenario['velocity']} blocks/hr): {scenario['hours']} hrs → {scenario['eta']}")

if __name__ == "__main__":
    main()
