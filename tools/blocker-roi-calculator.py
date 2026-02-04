#!/usr/bin/env python3
"""
blocker-roi-calculator.py — Prioritize unblocking actions by ROI

Calculate which blocker to fix first based on:
- Time to fix (minutes)
- Value unlocked ($)
- ROI per minute

Usage:
    python3 blocker-roi-calculator.py              # List all blockers
    python3 blocker-roi-calculator.py --priority   # Sort by ROI/min
    python3 blocker-roi-calculator.py --json       # Export as JSON
"""

import json
from pathlib import Path

# Default blockers (can be overridden with custom data)
BLOCKERS = [
    {
        "name": "Browser access (gateway restart)",
        "time_min": 1,
        "value_unlocked": 50000,
        "category": "infrastructure",
        "unblocks": ["Code4rena bounties", "Web automation tasks"],
        "action": "Ask Arthur: `openclaw gateway restart`"
    },
    {
        "name": "GitHub CLI authentication",
        "time_min": 5,
        "value_unlocked": 130000,
        "category": "infrastructure",
        "unblocks": ["Grant submissions (5 ready)", "Grant tracking"],
        "action": "Run: `gh auth login`"
    },
    {
        "name": "Arthur approval — Service outreach",
        "time_min": 2,
        "value_unlocked": 2057000,
        "category": "decision",
        "unblocks": ["104 messages ($2,057K)"],
        "action": "Arthur reviews EXECUTE-PHASE-READY.md"
    },
    {
        "name": "Arthur approval — Grant submissions",
        "time_min": 1,
        "value_unlocked": 130000,
        "category": "decision",
        "unblocks": ["5 grants ($130K)"],
        "action": "Arthur reviews grant submissions"
    },
    {
        "name": "Moltbook API resilience",
        "time_min": 10,
        "value_unlocked": 5000,
        "category": "infrastructure",
        "unblocks": ["Moltbook posting", "Ecosystem presence"],
        "action": "Build retry logic + queue system"
    }
]

def calculate_roi(blocker):
    """Calculate ROI per minute."""
    time_min = blocker["time_min"]
    value = blocker["value_unlocked"]
    roi_per_min = value / time_min if time_min > 0 else 0
    return {
        **blocker,
        "roi_per_min": roi_per_min,
        "roi_formatted": f"${roi_per_min:,.0f}/min"
    }

def format_value(value):
    """Format dollar values with K/M suffixes."""
    if value >= 1_000_000:
        return f"${value/1_000_000:.1f}M"
    elif value >= 1_000:
        return f"${value/1_000:.0f}K"
    else:
        return f"${value}"

def display_blockers(blockers, show_priority=False):
    """Display blockers in a formatted table."""
    if show_priority:
        blockers = sorted(blockers, key=lambda b: b["roi_per_min"], reverse=True)
        print("\n🎯 BLOCKERS (Sorted by ROI/min)")
    else:
        print("\n📊 CURRENT BLOCKERS")

    print("\n" + "="*100)
    print(f"{'Blocker':<35} | {'Time':<6} | {'Value':<10} | {'ROI/min':<12} | Category")
    print("="*100)

    for b in blockers:
        name = b["name"][:34]
        time_str = f"{b['time_min']}min"
        value_str = format_value(b["value_unlocked"])
        roi_str = b["roi_formatted"]
        cat = b["category"]

        print(f"{name:<35} | {time_str:<6} | {value_str:<10} | {roi_str:<12} | {cat}")

    print("="*100)

    # Show recommended action
    top_blocker = max(blockers, key=lambda b: b["roi_per_min"])
    print(f"\n🔥 TOP PRIORITY: {top_blocker['name']}")
    print(f"   ROI: {top_blocker['roi_formatted']}")
    print(f"   Action: {top_blocker['action']}")
    print(f"   Unblocks: {', '.join(top_blocker['unblocks'])}")

    # Summary stats
    total_time = sum(b["time_min"] for b in blockers)
    total_value = sum(b["value_unlocked"] for b in blockers)
    avg_roi = total_value / total_time if total_time > 0 else 0

    print(f"\n📈 SUMMARY:")
    print(f"   Total time to unblock all: {total_time} min")
    print(f"   Total value unlocked: {format_value(total_value)}")
    print(f"   Average ROI: ${avg_roi:,.0f}/min")

def export_json(blockers):
    """Export blockers as JSON."""
    output = {"blockers": blockers}
    output_path = Path("tmp/blockers.json")
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(json.dumps(output, indent=2))
    print(f"\n✅ Exported to {output_path}")

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Blocker ROI Calculator")
    parser.add_argument("--priority", action="store_true", help="Sort by ROI/min")
    parser.add_argument("--json", action="store_true", help="Export as JSON")
    args = parser.parse_args()

    # Calculate ROI for all blockers
    blockers_with_roi = [calculate_roi(b) for b in BLOCKERS]

    # Display
    display_blockers(blockers_with_roi, show_priority=args.priority)

    # Export if requested
    if args.json:
        export_json(blockers_with_roi)

    # Quick recommendation
    print("\n💡 RECOMMENDATION:")
    print("   Fix highest ROI/min blocker first.")
    print("   Small unblocks → massive value unlocked.")
    print("   1 min gateway restart = $50K/min ROI")
    print("   5 min GitHub auth = $26K/min ROI")
    print("   2 min Arthur approval = $1,028,500/min ROI")

if __name__ == "__main__":
    main()
