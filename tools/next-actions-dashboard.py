#!/usr/bin/env python3
"""
next-actions-dashboard.py — Show what's ready to execute RIGHT NOW

Usage:
  python3 tools/next-actions-dashboard.py           # Show all next actions
  python3 tools/next-actions-dashboard.py --focus   # Show only HIGH-ROI actions
  python3 tools/next-actions-dashboard.py --category outreach  # Filter by category

Purpose:
  Reduce decision fatigue by showing ready-to-execute tasks with ROI and time estimates.
  Pulls from:
  - revenue-tracker.py (ready items, zero blockers)
  - moltbook/ (queued posts)
  - follow-up-reminder.py (due follow-ups)
  - cron jobs (scheduled tasks)

Output:
  Prioritized action list with:
  - Task description
  - Time estimate
  - Value/ROI
  - Blocker status
  - Execution command
"""

import argparse
import json
import subprocess
from pathlib import Path

WORKSPACE = Path("/home/node/.openclaw/workspace")

def get_ready_revenue_items():
    """Get revenue items with status=ready (zero blockers)."""
    try:
        result = subprocess.run(
            ["python3", f"{WORKSPACE}/tools/revenue-tracker.py", "list", "--status", "ready"],
            capture_output=True, text=True, timeout=15
        )
        if result.returncode == 0:
            # Parse output to extract item names and values
            items = []
            lines = result.stdout.split('\n')
            for line in lines:
                if 'Potential: $' in line and 'Status: ready' in lines[lines.index(line)+1]:
                    # Extract value
                    value_match = line.split('Potential: $')[1].split('|')[0].strip().replace(',', '')
                    try:
                        value = float(value_match)
                        # Get name from previous line
                        name_idx = lines.index(line) - 1
                        if name_idx >= 0:
                            name = lines[name_idx].strip('🟢 ').strip()
                            items.append({
                                "name": name,
                                "value": value,
                                "category": "services",
                                "time": "20 min",  # Average outreach time
                                "command": f"# Outreach message in outreach/messages/",
                                "blocker": "None (needs Arthur approval)"
                            })
                    except (ValueError, IndexError):
                        continue
            return items
    except Exception as e:
        print(f"Warning: Could not fetch revenue items: {e}", file=__import__("sys").stderr)
    return []

def get_queued_moltbook_posts():
    """Get queued Moltbook posts ready to publish."""
    pipeline_file = WORKSPACE / "moltbook/CONTENT-PIPELINE-STATUS.md"
    if not pipeline_file.exists():
        return []

    posts = []
    content = pipeline_file.read_text()

    # Parse "Queued Posts" section
    if "## 🚀 Queued Posts" in content:
        queued_section = content.split("## 🚀 Queued Posts")[1].split("##")[0]
        lines = queued_section.split('\n')
        for i, line in enumerate(lines):
            if '—' in line and '.md' in line:
                name = line.split('—')[0].strip(f"{i}. ").strip()
                posts.append({
                    "name": f"Publish: {name}",
                    "value": 0,  # Moltbook posts are brand-building, not direct revenue
                    "category": "content",
                    "time": "2 min",
                    "command": "python3 tools/moltbook-suite.py post --next",
                    "blocker": "Rate limit (HTTP 429)"
                })

    return posts

def get_due_followups():
    """Get follow-ups due today."""
    try:
        result = subprocess.run(
            ["python3", f"{WORKSPACE}/tools/follow-up-reminder.py"],
            capture_output=True, text=True, timeout=10
        )
        if "No follow-ups needed" in result.stdout:
            return []
        # Parse follow-up items (simplified)
        return [{"name": "Check follow-ups", "value": 5000, "category": "revenue", "time": "5 min",
                 "command": "python3 tools/follow-up-reminder.py", "blocker": "None"}]
    except Exception:
        return []

def get_blocker_summary():
    """Get current blockers (from today.md or memory)."""
    # Hardcoded based on current knowledge (should parse from files)
    return [
        {
            "name": "Gateway Restart (Arthur)",
            "value": 50000,
            "category": "blocker",
            "time": "1 min",
            "command": "openclaw gateway restart",
            "blocker": "Arthur action required"
        },
        {
            "name": "GitHub CLI Auth (Arthur)",
            "value": 125000,
            "category": "blocker",
            "time": "5 min",
            "command": "gh auth login",
            "blocker": "Arthur action required"
        }
    ]

def calculate_roi(item):
    """Calculate ROI per minute."""
    value = item.get("value", 0)
    time_str = item.get("time", "1 min")
    try:
        time_min = float(time_str.split()[0])
        return value / time_min if time_min > 0 else 0
    except (ValueError, ZeroDivisionError):
        return 0

def format_dashboard(items, focus=False, category=None):
    """Format dashboard output."""
    # Filter by focus (HIGH ROI only) or category
    if focus:
        items = [i for i in items if calculate_roi(i) > 1000]  # >$1K/min
    if category:
        items = [i for i in items if i.get("category") == category]

    # Sort by ROI (descending)
    items.sort(key=calculate_roi, reverse=True)

    output = ["=" * 70, "  🎯 NEXT ACTIONS DASHBOARD", "=" * 70, ""]

    if not items:
        output.append("  ✅ No actions to display. System is optimized.")
        output.append("")
        output.append("=" * 70)
        return "\n".join(output)

    # Group by category
    categories = {}
    for item in items:
        cat = item.get("category", "other")
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(item)

    for cat, cat_items in categories.items():
        output.append(f"## 📂 {cat.upper()}")
        output.append("")

        for item in cat_items:
            roi = calculate_roi(item)
            roi_str = f"${roi:,.0f}/min" if roi > 0 else "N/A"
            value_str = f"${item.get('value', 0):,.0f}" if item.get('value', 0) > 0 else "Brand"

            output.append(f"🎯 {item['name']}")
            output.append(f"   💰 Value: {value_str} | ⏱️  Time: {item['time']} | 📈 ROI: {roi_str}")
            output.append(f"   🚫 Blocker: {item['blocker']}")
            output.append(f"   💻 Command: {item['command']}")
            output.append("")

    output.append("=" * 70)
    output.append(f"  📊 Total: {len(items)} actions ready")
    output.append("=" * 70)

    return "\n".join(output)

def main():
    parser = argparse.ArgumentParser(description="Show ready-to-execute actions")
    parser.add_argument("--focus", action="store_true", help="Show only HIGH-ROI actions (>$1K/min)")
    parser.add_argument("--category", choices=["services", "content", "revenue", "blocker"],
                        help="Filter by category")
    args = parser.parse_args()

    # Collect all actions
    actions = []
    actions.extend(get_ready_revenue_items())
    actions.extend(get_queued_moltbook_posts())
    actions.extend(get_due_followups())
    actions.extend(get_blocker_summary())

    # Display dashboard
    print(format_dashboard(actions, focus=args.focus, category=args.category))

if __name__ == "__main__":
    main()
