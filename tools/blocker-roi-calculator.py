#!/usr/bin/env python3
"""
Blocker ROI Calculator — Prioritize unblocking work by value/time

Insight: "Blocker ROI = Priority" (MEMORY.md #17)
$180K from 6 blockers = $30K/min average. Execute highest ROI blockers first.

Usage:
    python3 blocker-roi-calculator.py                    # Show ranked blockers
    python3 blocker-roi-calculator.py --add "GitHub auth" 5 130000  # Add blocker
    python3 blocker-roi-calculator.py --rm 0              # Remove blocker #0
    python3 blocker-roi-calculator.py --clear             # Clear all blockers
"""

import argparse
import json
from pathlib import Path

BLOCKERS_FILE = Path.home() / ".openclaw/workspace/data/blockers.json"

def load_blockers() -> list:
    """Load blockers from JSON file."""
    if BLOCKERS_FILE.exists():
        return json.loads(BLOCKERS_FILE.read_text())
    return [
        {"name": "Gateway restart", "time_min": 1, "value": 50000},
        {"name": "GitHub CLI auth", "time_min": 5, "value": 130000},
    ]

def save_blockers(blockers: list) -> None:
    """Save blockers to JSON file."""
    BLOCKERS_FILE.parent.mkdir(parents=True, exist_ok=True)
    BLOCKERS_FILE.write_text(json.dumps(blockers, indent=2))

def calculate_roi(blocker: dict) -> float:
    """Calculate ROI: value per minute."""
    time_key = "time_min" if "time_min" in blocker else "minutes"
    return blocker["value"] / blocker[time_key] if blocker[time_key] > 0 else 0

def show_ranked_blockers(blockers: list) -> None:
    """Display blockers ranked by ROI."""
    ranked = sorted(blockers, key=calculate_roi, reverse=True)
    total_value = sum(b["value"] for b in blockers)
    total_time = sum(b.get("time_min", b.get("minutes", 0)) for b in blockers)

    print("\n🔓 BLOCKER ROI RANKING")
    print("=" * 70)
    print(f"{'#':<3} {'Blocker':<25} {'Time':<6} {'Value':<10} {'ROI ($/min)':<12}")
    print("-" * 70)

    for i, b in enumerate(ranked):
        roi = calculate_roi(b)
        time_min = b.get("time_min", b.get("minutes", 0))
        print(f"{i:<3} {b['name']:<25} {time_min:<6}m ${b['value']:<9,.0f} ${roi:<11,.0f}")

    print("-" * 70)
    print(f"{'TOTAL':<29} {total_time:<6}m ${total_value:<9,.0f} ${total_value/total_time:,.0f}/min")
    print()

def main():
    parser = argparse.ArgumentParser(description="Blocker ROI Calculator")
    parser.add_argument("--add", nargs=3, metavar=("NAME", "MINUTES", "VALUE"),
                       help="Add blocker: name minutes value")
    parser.add_argument("--rm", type=int, metavar="INDEX", help="Remove blocker by index")
    parser.add_argument("--clear", action="store_true", help="Clear all blockers")
    args = parser.parse_args()

    blockers = load_blockers()

    if args.clear:
        blockers = []
        print("✓ Cleared all blockers")
    elif args.add:
        name, minutes, value = args.add
        blockers.append({
            "name": name,
            "time_min": int(minutes),
            "value": int(value)
        })
        print(f"✓ Added: {name} ({minutes}m → ${value:,})")
    elif args.rm is not None:
        removed = blockers.pop(args.rm)
        print(f"✓ Removed: {removed['name']}")

    save_blockers(blockers)
    show_ranked_blockers(blockers)

if __name__ == "__main__":
    main()
