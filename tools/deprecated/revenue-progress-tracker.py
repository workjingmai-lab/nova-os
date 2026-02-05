#!/usr/bin/env python3
"""
Revenue Progress Tracker
Monitor revenue pipeline execution progress after unblocking.

Usage:
  python3 tools/revenue-progress-tracker.py          # Full progress report
  python3 tools/revenue-progress-tracker.py --grants  # Grant-specific progress
  python3 tools/revenue-progress-tracker.py --watch   # Watch mode (refresh every 30s)
"""

import json
import time
import argparse
from pathlib import Path
from datetime import datetime

REVENUE_FILE = Path.home() / ".openclaw" / "workspace" / "data" / "revenue-pipeline.json"

def load_pipeline():
    """Load revenue pipeline."""
    if REVENUE_FILE.exists():
        with open(REVENUE_FILE) as f:
            return json.load(f)
    return {"grants": [], "services": [], "bounties": []}

def check_blockers():
    """Check current blocker status."""
    blockers = {
        "github_auth": False,
        "browser_access": False,
        "messages_reviewed": False
    }

    # Check GitHub auth
    try:
        import subprocess
        result = subprocess.run(["gh", "auth", "status"], capture_output=True, text=True)
        blockers["github_auth"] = result.returncode == 0
    except:
        pass

    # Check browser access (simplified - in reality would check gateway status)
    # For now, assume blocked

    # Check messages reviewed (simplified - would check approval status)
    # For now, assume not reviewed

    return blockers

def calculate_progress(pipeline):
    """Calculate execution progress percentages."""
    total = 0
    submitted = 0
    won = 0

    for category in ["grants", "services", "bounties"]:
        for item in pipeline[category]:
            total += item["potential"]
            if item["status"] in ["submitted", "won"]:
                submitted += item["potential"]
            if item["status"] == "won":
                won += item["potential"]

    return {
        "total": total,
        "submitted": submitted,
        "won": won,
        "submission_rate": (submitted / total * 100) if total > 0 else 0,
        "win_rate": (won / total * 100) if total > 0 else 0
    }

def show_progress(pipeline, category_filter=None):
    """Show progress report."""
    blockers = check_blockers()
    progress = calculate_progress(pipeline)

    print("\n" + "=" * 60)
    print("💰 REVENUE PROGRESS TRACKER")
    print("=" * 60)
    print(f"📅 Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")

    # Blocker status
    print("\n🔧 BLOCKER STATUS:")
    print(f"   GitHub Auth: {'✅ Unblocked' if blockers['github_auth'] else '⏸️ Blocked'}")
    print(f"   Browser Access: {'✅ Unblocked' if blockers['browser_access'] else '⏸️ Blocked'}")
    print(f"   Messages Reviewed: {'✅ Approved' if blockers['messages_reviewed'] else '⏸️ Pending'}")

    # Overall progress
    print(f"\n📊 OVERALL PROGRESS:")
    print(f"   Total Pipeline: ${progress['total']:,.0f}")
    print(f"   Submitted: ${progress['submitted']:,.0f} ({progress['submission_rate']:.1f}%)")
    print(f"   Won: ${progress['won']:,.0f} ({progress['win_rate']:.1f}%)")

    # Progress bar
    bar_width = 40
    submitted_bars = int(bar_width * progress['submission_rate'] / 100)
    won_bars = int(bar_width * progress['win_rate'] / 100)
    progress_bar = "█" * won_bars + "▓" * (submitted_bars - won_bars) + "░" * (bar_width - submitted_bars)
    print(f"   [{progress_bar}]")

    # Category breakdown
    if not category_filter or category_filter == "grants":
        print(f"\n🎯 GRANTS (${sum(i['potential'] for i in pipeline['grants']):,.0f})")
        for item in pipeline['grants']:
            status_icon = {
                "lead": "🔵",
                "ready": "🟢",
                "submitted": "🟡",
                "won": "✅",
                "lost": "❌"
            }.get(item['status'], "⚪")
            print(f"   {status_icon} {item['name']}: ${item['potential']:,.0f} ({item['status']})")

    if not category_filter or category_filter == "services":
        print(f"\n💼 SERVICES (${sum(i['potential'] for i in pipeline['services']):,.0f})")
        for item in pipeline['services']:
            status_icon = {
                "lead": "🔵",
                "ready": "🟢",
                "submitted": "🟡",
                "won": "✅",
                "lost": "❌"
            }.get(item['status'], "⚪")
            print(f"   {status_icon} {item['name']}: ${item['potential']:,.0f} ({item['status']})")

    if not category_filter or category_filter == "bounties":
        print(f"\n🏆 BOUNTIES (${sum(i['potential'] for i in pipeline['bounties']):,.0f})")
        for item in pipeline['bounties']:
            status_icon = {
                "lead": "🔵",
                "ready": "🟢",
                "submitted": "🟡",
                "won": "✅",
                "lost": "❌"
            }.get(item['status'], "⚪")
            print(f"   {status_icon} {item['name']}: ${item['potential']:,.0f} ({item['status']})")

    # Next actions
    print(f"\n🚀 NEXT ACTIONS:")
    if not blockers['github_auth']:
        print("   ⏸️  Run 'gh auth login' to unblock $130K grants")
    if not blockers['messages_reviewed']:
        print("   ⏸️  Review outreach/messages/ to unblock $2K services")
    if not blockers['browser_access']:
        print("   ⏸️  Restart gateway to unblock $50K bounties")
    if blockers['github_auth'] and progress['submission_rate'] < 100:
        print("   ✅ Run 'python3 tools/grant-submit.py --all' to submit grants")

    print("\n" + "=" * 60 + "\n")

def watch_mode():
    """Watch mode - refresh every 30 seconds."""
    try:
        while True:
            pipeline = load_pipeline()
            show_progress(pipeline)
            print("⏳ Refreshing in 30 seconds... (Ctrl+C to exit)")
            time.sleep(30)
    except KeyboardInterrupt:
        print("\n✅ Watch mode stopped")

def main():
    parser = argparse.ArgumentParser(description="Revenue Progress Tracker")
    parser.add_argument("--grants", action="store_true", help="Show grants only")
    parser.add_argument("--services", action="store_true", help="Show services only")
    parser.add_argument("--bounties", action="store_true", help="Show bounties only")
    parser.add_argument("--watch", action="store_true", help="Watch mode (refresh every 30s)")

    args = parser.parse_args()

    pipeline = load_pipeline()

    category = None
    if args.grants:
        category = "grants"
    elif args.services:
        category = "services"
    elif args.bounties:
        category = "bounties"

    if args.watch:
        watch_mode()
    else:
        show_progress(pipeline, category)

if __name__ == "__main__":
    main()
