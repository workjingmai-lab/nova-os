#!/usr/bin/env python3
"""
Revenue Opportunity Tracker
Track grants, services, and bounties in one centralized system.

Usage:
  python tools/revenue-tracker.py add grant --name "Gitcoin" --potential 5000 --status "ready"
  python tools/revenue-tracker.py add service --name "Quick Automation" --potential 2000 --status "lead"
  python tools/revenue-tracker.py list
  python tools/revenue-tracker.py summary
"""

import json
import argparse
from datetime import datetime
from pathlib import Path

REVENUE_FILE = Path.home() / ".openclaw" / "workspace" / "data" / "revenue-pipeline.json"

def load_pipeline():
    """Load revenue pipeline from JSON."""
    if REVENUE_FILE.exists():
        with open(REVENUE_FILE) as f:
            return json.load(f)
    return {"grants": [], "services": [], "bounties": []}

def save_pipeline(pipeline):
    """Save revenue pipeline to JSON."""
    REVENUE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(REVENUE_FILE, "w") as f:
        json.dump(pipeline, f, indent=2)

def add_opportunity(category, name, potential, status, notes=""):
    """Add a new revenue opportunity."""
    pipeline = load_pipeline()

    opportunity = {
        "name": name,
        "potential": float(potential),
        "status": status,  # lead, ready, submitted, won, lost
        "notes": notes,
        "created": datetime.now().isoformat(),
        "updated": datetime.now().isoformat()
    }

    pipeline[category].append(opportunity)
    save_pipeline(pipeline)

    total = sum(op["potential"] for op in pipeline[category])
    print(f"✅ Added {category[:-1]}: {name} (${potential:,.0f})")
    print(f"   {category.capitalize()} pipeline total: ${total:,.0f}")

def list_pipeline(category=None, status=None):
    """List revenue opportunities."""
    pipeline = load_pipeline()

    if category:
        categories = [category]
    else:
        categories = ["grants", "services", "bounties"]

    for cat in categories:
        items = pipeline[cat]
        if status:
            items = [i for i in items if i["status"] == status]

        if not items:
            continue

        print(f"\n{cat.upper()} ({len(items)} items)")
        print("-" * 60)

        for item in sorted(items, key=lambda x: x["potential"], reverse=True):
            status_icon = {
                "lead": "🔵",
                "ready": "🟢",
                "submitted": "🟡",
                "won": "✅",
                "lost": "❌"
            }.get(item["status"], "⚪")

            print(f"{status_icon} {item['name']}")
            print(f"   Potential: ${item['potential']:,.0f} | Status: {item['status']}")
            if item.get("notes"):
                print(f"   Notes: {item['notes']}")
            print()

def show_summary():
    """Show revenue pipeline summary."""
    pipeline = load_pipeline()

    total_potential = 0
    total_won = 0

    print("\n💰 REVENUE PIPELINE SUMMARY")
    print("=" * 60)

    for category in ["grants", "services", "bounties"]:
        items = pipeline[category]
        if not items:
            continue

        cat_potential = sum(i["potential"] for i in items)
        cat_won = sum(i["potential"] for i in items if i["status"] == "won")
        cat_ready = sum(i["potential"] for i in items if i["status"] == "ready")
        cat_submitted = sum(i["potential"] for i in items if i["status"] == "submitted")

        total_potential += cat_potential
        total_won += cat_won

        print(f"\n{category.upper()}:")
        print(f"  Total items: {len(items)}")
        print(f"  Potential: ${cat_potential:,.0f}")
        print(f"  Ready to submit: ${cat_ready:,.0f}")
        print(f"  Submitted: ${cat_submitted:,.0f}")
        print(f"  Won: ${cat_won:,.0f}")

    print(f"\n{'=' * 60}")
    print(f"TOTAL PIPELINE: ${total_potential:,.0f}")
    print(f"WON: ${total_won:,.0f}")
    print(f"Conversion rate: {(total_won/total_potential*100) if total_potential > 0 else 0:.1f}%")

def main():
    parser = argparse.ArgumentParser(description="Revenue Opportunity Tracker")
    subparsers = parser.add_subparsers(dest="command", help="Command")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add opportunity")
    add_parser.add_argument("category", choices=["grant", "service", "bounty"], help="Category")
    add_parser.add_argument("--name", required=True, help="Opportunity name")
    add_parser.add_argument("--potential", type=float, required=True, help="Potential value ($)")
    add_parser.add_argument("--status", default="lead", help="Status (lead/ready/submitted/won/lost)")
    add_parser.add_argument("--notes", default="", help="Additional notes")

    # List command
    list_parser = subparsers.add_parser("list", help="List opportunities")
    list_parser.add_argument("--category", choices=["grants", "services", "bounties"], help="Filter by category")
    list_parser.add_argument("--status", help="Filter by status")

    # Summary command
    subparsers.add_parser("summary", help="Show pipeline summary")

    args = parser.parse_args()

    if args.command == "add":
        # Handle irregular plurals
        plural = f"{args.category}s"
        if args.category == "bounty":
            plural = "bounties"
        add_opportunity(plural, args.name, args.potential, args.status, args.notes)
    elif args.command == "list":
        list_pipeline(args.category, args.status)
    elif args.command == "summary":
        show_summary()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
