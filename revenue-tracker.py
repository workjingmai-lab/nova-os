#!/usr/bin/env python3
"""
Revenue Tracker — Nova's Pipeline Visibility Tool

Tracks revenue pipeline across grants, services, and bounties.
Reads from revenue-pipeline.json and outputs status, blockers, and next actions.
"""

import json
import sys
from datetime import datetime
from pathlib import Path

def load_pipeline():
    """Load revenue pipeline from JSON."""
    path = Path("revenue-pipeline.json")
    if not path.exists():
        return None
    with open(path) as f:
        return json.load(f)

def format_currency(amount):
    """Format amount as currency string."""
    return f"${amount:,.0f}"

def print_status(pipeline):
    """Print pipeline status summary."""
    total = pipeline.get("totalPipeline", 0)
    last_updated = pipeline.get("lastUpdated", "Unknown")
    categories = pipeline.get("categories", {})

    print(f"📊 Revenue Pipeline — {format_currency(total)}")
    print(f"🕐 Last updated: {last_updated}")
    print()

    for cat_name, cat_data in categories.items():
        amount = cat_data.get("amount", 0)
        status = cat_data.get("status", "Unknown")
        blocker = cat_data.get("blocker")

        status_emoji = {
            "ready": "✅",
            "outreach": "📤",
            "setup": "🔧"
        }.get(status, "❓")

        print(f"{status_emoji} {cat_name.title()}: {format_currency(amount)} ({status})")

        if blocker:
            print(f"   ⏸️  Blocker: {blocker}")

        # Show opportunities if available
        if "opportunities" in cat_data:
            for opp in cat_data["opportunities"]:
                print(f"   • {opp['name']}: {format_currency(opp['amount'])}")

        # Show proposals/leads if available
        if "proposalsReady" in cat_data:
            print(f"   📄 {cat_data['proposalsReady']} proposals ready")

        if "leads" in cat_data:
            print(f"   👥 {cat_data['leads']} leads identified")

        print()

    # Show metrics
    metrics = pipeline.get("metrics", {})
    if metrics:
        print("📈 Metrics:")
        print(f"   Work blocks today: {metrics.get('workBlocksToday', 0)}")
        print(f"   Work blocks Week 2: {metrics.get('workBlocksWeek2', 0)}")
        print(f"   Velocity: {metrics.get('velocity', 'Unknown')}")
        print(f"   Conversion rate: {metrics.get('conversionRate', '0%')}")

def print_next_actions(pipeline):
    """Print next actions based on pipeline status."""
    categories = pipeline.get("categories", {})

    print("\n🎯 Next Actions:")

    # Grants
    grants = categories.get("grants", {})
    if grants.get("blocker"):
        print(f"   1. 🔥 UNBLOCK GRANTS ({format_currency(grants['amount'])}): {grants['blocker']}")

    # Services
    services = categories.get("services", {})
    if services.get("proposalsReady", 0) > 0:
        sent = services.get("messagesSent", 0)
        ready = services.get("proposalsReady", 0)
        if ready > sent:
            print(f"   2. 📤 SEND PROPOSALS: {ready - sent} ready to send")

    # Bounties
    bounties = categories.get("bounties", {})
    if bounties.get("blocker"):
        print(f"   3. 🔧 UNBLOCK BOUNTIES ({format_currency(bounties['amount'])}): {bounties['blocker']}")

def main():
    """Main entry point."""
    pipeline = load_pipeline()

    if not pipeline:
        print("❌ No revenue pipeline found.")
        print("   Create revenue-pipeline.json to start tracking.")
        return 1

    print_status(pipeline)
    print_next_actions(pipeline)

    return 0

if __name__ == "__main__":
    sys.exit(main())
