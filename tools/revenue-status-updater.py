#!/usr/bin/env python3
"""
Revenue Status Updater — Quick CLI to update pipeline item statuses

Updates data/revenue-pipeline.json with new status for specific items.
Prevents revenue leakage by keeping pipeline current.

Usage:
    python3 tools/revenue-status-updater.py --id 3 --status submitted
    python3 tools/revenue-status-updater.py --id "EF-40K" --status follow_up
    python3 tools/revenue-status-updater.py --list
    python3 tools/revenue-status-updater.py --pending  # Show ready items
"""

import json
import sys
from datetime import datetime
from pathlib import Path

# Configuration
PIPELINE_FILE = Path("/home/node/.openclaw/workspace/data/revenue-pipeline.json")
VALID_STATUSES = ["lead", "ready", "submitted", "follow_up", "won", "lost"]


def load_pipeline():
    """Load pipeline from JSON file."""
    if not PIPELINE_FILE.exists():
        print(f"❌ Pipeline file not found: {PIPELINE_FILE}")
        sys.exit(1)

    with open(PIPELINE_FILE, "r") as f:
        return json.load(f)


def save_pipeline(pipeline):
    """Save pipeline to JSON file."""
    with open(PIPELINE_FILE, "w") as f:
        json.dump(pipeline, f, indent=2)


def list_items(pipeline, status=None, category=None):
    """List pipeline items with optional filters."""
    items = pipeline.get("items", [])

    if status:
        items = [i for i in items if i.get("status") == status]
    if category:
        items = [i for i in items if i.get("category") == category]

    if not items:
        print("No items found.")
        return

    print(f"\n📊 Pipeline Items ({len(items)}):\n")

    for item in items:
        status_emoji = {
            "lead": "🔍",
            "ready": "✅",
            "submitted": "📤",
            "follow_up": "🔔",
            "won": "💰",
            "lost": "❌",
        }.get(item.get("status", ""), "❓")

        print(f"{status_emoji} [{item.get('id', 'N/A')}] {item.get('name', 'Unknown')}")
        print(f"   Category: {item.get('category', 'N/A')}")
        print(f"   Value: ${item.get('value', 0):,.0f}")
        print(f"   Status: {item.get('status', 'N/A')}")
        if item.get("notes"):
            print(f"   Notes: {item['notes']}")
        print()


def update_status(pipeline, item_id, new_status, notes=None):
    """Update status for a specific item."""
    items = pipeline.get("items", [])

    # Find item by id
    item = next((i for i in items if i.get("id") == item_id), None)

    if not item:
        # Try numeric index
        try:
            idx = int(item_id) - 1
            if 0 <= idx < len(items):
                item = items[idx]
            else:
                print(f"❌ Item not found: {item_id}")
                return False
        except ValueError:
            print(f"❌ Invalid item ID: {item_id}")
            return False

    old_status = item.get("status")

    if new_status not in VALID_STATUSES:
        print(f"❌ Invalid status: {new_status}")
        print(f"   Valid statuses: {', '.join(VALID_STATUSES)}")
        return False

    # Update item
    item["status"] = new_status
    item["updated"] = datetime.now().isoformat()

    if notes:
        item["notes"] = notes

    # Update pipeline metrics
    pipeline["updated"] = datetime.now().isoformat()

    # Recalculate totals
    total_value = sum(i.get("value", 0) for i in items)
    status_breakdown = {}
    for s in VALID_STATUSES:
        status_breakdown[s] = sum(
            i.get("value", 0) for i in items if i.get("status") == s
        )

    pipeline["total_value"] = total_value
    pipeline["status_breakdown"] = status_breakdown

    # Save
    save_pipeline(pipeline)

    print(f"✅ Status updated: [{item.get('id')}] {item.get('name')}")
    print(f"   {old_status} → {new_status}")
    print(f"   Value: ${item.get('value', 0):,.0f}")

    return True


def show_pending(pipeline):
    """Show items ready for next action."""
    items = pipeline.get("items", [])

    ready = [i for i in items if i.get("status") == "ready"]
    submitted = [i for i in items if i.get("status") == "submitted"]

    print(f"\n📋 Pending Actions:\n")

    if ready:
        total_ready = sum(i.get("value", 0) for i in ready)
        print(f"✅ Ready to send ({len(ready)} items, ${total_ready:,.0f}):")
        for item in ready:
            print(f"   - [{item.get('id')}] {item.get('name')} (${item.get('value', 0):,.0f})")
        print()

    if submitted:
        total_submitted = sum(i.get("value", 0) for i in submitted)
        print(f"📤 Awaiting response ({len(submitted)} items, ${total_submitted:,.0f}):")
        for item in submitted[:5]:  # Show first 5
            print(f"   - [{item.get('id')}] {item.get('name')} (${item.get('value', 0):,.0f})")
        if len(submitted) > 5:
            print(f"   ... and {len(submitted) - 5} more")
        print()


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Update revenue pipeline item statuses",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --list                           # List all items
  %(prog)s --list --status ready            # List ready items
  %(prog)s --pending                        # Show pending actions
  %(prog)s --id 3 --status submitted        # Update item 3 to submitted
  %(prog)s --id "EF-40K" --status follow_up  # Update custom ID
        """,
    )

    parser.add_argument("--list", action="store_true", help="List all pipeline items")
    parser.add_argument("--pending", action="store_true", help="Show pending actions")
    parser.add_argument("--id", help="Item ID to update (numeric or custom)")
    parser.add_argument("--status", help="New status (lead/ready/submitted/follow_up/won/lost)")
    parser.add_argument("--notes", help="Optional notes for the update")
    parser.add_argument("--category", help="Filter by category (grant/service/bounty)")

    args = parser.parse_args()

    # Load pipeline
    pipeline = load_pipeline()

    # Execute action
    if args.list:
        list_items(pipeline, status=args.status, category=args.category)
    elif args.pending:
        show_pending(pipeline)
    elif args.id and args.status:
        update_status(pipeline, args.id, args.status, args.notes)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
