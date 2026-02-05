#!/usr/bin/env python3
"""
Revenue Conversion Checklist

Tracks the complete journey from lead → won for every pipeline item.
Ensures nothing falls through the cracks.

Usage:
    python3 revenue-conversion-checklist.py          # Show all items
    python3 revenue-conversion-checklist.py --status ready  # Filter by status
    python3 revenue-conversion-checklist.py --category service  # Filter by category
"""

import json
import argparse
from datetime import datetime
from pathlib import Path

# Configuration
PIPELINE_FILE = Path("/home/node/.openclaw/workspace/data/revenue-pipeline.json")

# Stage definitions
STAGES = {
    "lead": {"label": "🔍 Lead", "desc": "Initial opportunity identified", "next": "ready"},
    "ready": {"label": "✅ Ready", "desc": "Message/proposal prepared", "next": "submitted"},
    "submitted": {"label": "📤 Sent", "desc": "Proposal sent to prospect", "next": "follow_up"},
    "follow_up": {"label": "🔄 Following Up", "desc": "Active follow-up sequence", "next": "won"},
    "won": {"label": "💰 Won", "desc": "Contract secured/revenue booked", "next": None},
    "lost": {"label": "❌ Lost", "desc": "Opportunity closed (no go)", "next": None}
}

def load_pipeline():
    """Load pipeline data from JSON file."""
    if not PIPELINE_FILE.exists():
        return {"grants": [], "services": [], "bounties": []}

    with open(PIPELINE_FILE, 'r') as f:
        return json.load(f)

def format_checklist_item(item, category):
    """Format a single pipeline item as a checklist row."""
    name = item.get("name", "Unknown")
    potential = item.get("potential", 0)
    status = item.get("status", "lead")
    stage_info = STAGES.get(status, STAGES["lead"])

    # Format potential value
    potential_str = f"${potential:,.0f}"

    # Stage progress indicator
    stage_order = ["lead", "ready", "submitted", "follow_up", "won", "lost"]
    current_idx = stage_order.index(status) if status in stage_order else 0

    # Build progress bar
    progress = ""
    for i, stage in enumerate(stage_order[:5]):  # Exclude "lost" from progress bar
        if i < current_idx:
            progress += "✅"
        elif i == current_idx:
            progress += STAGES[stage]["label"].split()[0]  # Get emoji
        else:
            progress += "⬜"

    return f"{progress} | {name:<30} | {potential_str:>10} | {stage_info['label']}"

def show_checklist(category=None, status_filter=None):
    """Display revenue conversion checklist."""
    pipeline = load_pipeline()

    print("=" * 100)
    print("  💰 REVENUE CONVERSION CHECKLIST")
    print("=" * 100)
    print()

    total_value = 0
    total_items = 0

    for cat_name, items in pipeline.items():
        if category and cat_name != category:
            continue

        if not items:
            continue

        print(f"\n{cat_name.upper().center(100, '-')}")
        print(f"{'Stage Progress':<50} | {'Name':<30} | {'Potential':>10} | Status")
        print("-" * 100)

        for item in items:
            if status_filter and item.get("status") != status_filter:
                continue

            print(format_checklist_item(item, cat_name))
            total_value += item.get("potential", 0)
            total_items += 1

    print()
    print("=" * 100)
    print(f"  📊 SUMMARY: {total_items} items | ${total_value:,.0f} total potential")
    print("=" * 100)

    # Stage breakdown
    print("\n  Stage Breakdown:")
    stage_order = ["lead", "ready", "submitted", "follow_up", "won", "lost"]
    for cat_name, items in pipeline.items():
        if category and cat_name != category:
            continue

        if not items:
            continue

        print(f"\n  {cat_name.upper()}:")
        for stage in stage_order:
            count = sum(1 for item in items if item.get("status") == stage)
            value = sum(item.get("potential", 0) for item in items if item.get("status") == stage)
            if count > 0:
                stage_info = STAGES[stage]
                print(f"    {stage_info['label']}: {count} items = ${value:,.0f}")

    print()
    print("💡 Next Actions:")
    print("  1. Focus on 'ready' items → Move to 'submitted'")
    print("  2. Follow up on 'submitted' items → Move to 'won'")
    print("  3. Close 'lost' items → Clean pipeline")
    print()

def show_stage_guide():
    """Show stage definitions and transition criteria."""
    print("=" * 100)
    print("  📋 STAGE DEFINITIONS & TRANSITION CRITERIA")
    print("=" * 100)
    print()

    for stage_key, stage_info in STAGES.items():
        next_stage = STAGES[stage_info["next"]]["label"] if stage_info["next"] else "None"
        print(f"  {stage_info['label']} ({stage_key})")
        print(f"    Description: {stage_info['desc']}")
        print(f"    Next Stage: {next_stage}")
        print()

def main():
    parser = argparse.ArgumentParser(
        description="Revenue Conversion Checklist — Track lead → won journey",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 revenue-conversion-checklist.py
  python3 revenue-conversion-checklist.py --status ready
  python3 revenue-conversion-checklist.py --category service
  python3 revenue-conversion-checklist.py --stages
        """
    )

    parser.add_argument("--status", help="Filter by status (lead/ready/submitted/follow_up/won/lost)")
    parser.add_argument("--category", help="Filter by category (grant/service/bounty)", choices=["grant", "service", "bounty"])
    parser.add_argument("--stages", action="store_true", help="Show stage definitions and exit")

    args = parser.parse_args()

    if args.stages:
        show_stage_guide()
        return

    show_checklist(category=args.category, status_filter=args.status)

if __name__ == "__main__":
    main()
