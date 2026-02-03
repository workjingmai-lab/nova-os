#!/usr/bin/env python3
"""
Nova's Daily Brief — Top 3 things Arthur needs to know.

Shows the most important updates, blockers, and opportunities in one glance.
Perfect for busy humans who want visibility without noise.

Usage:
    python3 nova-brief.py              # Today's top 3
    python3 nova-brief.py --full       # Full brief with metrics
    python3 nova-brief.py --blockers   # Show only blockers
"""

import json
import os
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE = Path("/home/node/.openclaw/workspace")
DIARY = WORKSPACE / "diary.md"
PIPELINE_JSON = WORKSPACE / "data" / "revenue-pipeline.json"
HEARTBEAT_STATE = WORKSPACE / ".heartbeat_state.json"


def get_latest_diary_entries(limit=5):
    """Get the most recent diary entries with task info."""
    if not DIARY.exists():
        return []

    with open(DIARY) as f:
        content = f.read()

    # Extract work blocks (## 🔥 WORK BLOCK)
    # Return full lines to extract task info later
    lines = content.split("\n")
    blocks = []
    for i, line in enumerate(lines):
        if line.startswith("## 🔥 WORK BLOCK"):
            # Get the task line (usually next line or within next few lines)
            task_line = ""
            for j in range(i+1, min(i+5, len(lines))):
                if "**Task:**" in lines[j]:
                    task_line = lines[j]
                    break
            blocks.append(task_line if task_line else line)

    return blocks[-limit:]


def get_revenue_summary():
    """Get revenue pipeline summary."""
    if not PIPELINE_JSON.exists():
        return {"total": 0, "ready": 0, "leads": 0, "submitted": 0, "blockers": []}

    with open(PIPELINE_JSON) as f:
        data = json.load(f)

    total = 0
    ready = 0
    leads = 0
    submitted = 0
    blockers = []

    # Process all categories: grants, services, bounties
    for category in ["grants", "services", "bounties"]:
        for opp in data.get(category, []):
            amount = opp.get("potential", 0)
            status = opp.get("status", "lead")
            total += amount

            if status == "ready":
                ready += amount
            elif status == "lead":
                leads += amount
            elif status == "submitted":
                submitted += amount

            # Extract blockers from notes
            notes = opp.get("notes", "")
            if "blocked on" in notes.lower() or "needs" in notes.lower():
                # Extract the blocker text
                if "blocked on" in notes.lower():
                    blocker = notes.lower().split("blocked on")[1].split("(")[0].strip()
                    if blocker and blocker not in blockers:
                        blockers.append(blocker)
                elif "needs" in notes.lower():
                    blocker = notes.lower().split("needs")[1].split("(")[0].strip()
                    if blocker and blocker not in blockers:
                        blockers.append(blocker)

    return {
        "total": total,
        "ready": ready,
        "leads": leads,
        "submitted": submitted,
        "blockers": blockers
    }


def get_work_block_count():
    """Count total work blocks from today.md or diary.md."""
    import re

    # First try today.md (has recent blocks with sequential numbers)
    today_md = WORKSPACE / "today.md"
    if today_md.exists():
        with open(today_md) as f:
            content = f.read()

        # Extract work block numbers (## 🔥 WORK BLOCK #762)
        matches = re.findall(r'## 🔥 WORK BLOCK #(\d+)', content)
        if matches:
            # Return the highest block number (total cumulative count)
            return max(int(m) for m in matches)

    # Fall back to diary.md
    if not DIARY.exists():
        return 0

    with open(DIARY) as f:
        content = f.read()

    matches = re.findall(r'## 🔥 WORK BLOCK #(\d+)', content)
    if matches:
        return max(int(m) for m in matches)

    # Last resort: count occurrences
    return content.count("🔥 WORK BLOCK")


def get_last_checkin():
    """Get last heartbeat check-in time."""
    if not HEARTBEAT_STATE.exists():
        return None

    try:
        with open(HEARTBEAT_STATE) as f:
            data = json.load(f)
        return data.get("lastCheckin")
    except:
        return None


def format_brief():
    """Generate the daily brief."""
    revenue = get_revenue_summary()
    blocks = get_work_block_count()
    recent = get_latest_diary_entries(3)
    last_checkin = get_last_checkin()

    brief = []
    brief.append("╔════════════════════════════════════════╗")
    brief.append("║     📯 NOVA'S DAILY BRIEF              ║")
    brief.append("╠════════════════════════════════════════╣")

    # Timestamp
    now = datetime.now(timezone.utc)
    brief.append(f"║ Time: {now.strftime('%Y-%m-%d %H:%M UTC'):^36} ║")
    brief.append("╠════════════════════════════════════════╣")

    # 🚨 Top Priority: Blockers
    brief.append("║ 🚨 TOP PRIORITY:                        ║")
    if revenue["blockers"]:
        for blocker in revenue["blockers"][:3]:
            brief.append(f"║  • {blocker[:34]:<34} ║")
    else:
        brief.append("║  ✓ No blockers!                          ║")
    brief.append("╠════════════════════════════════════════╣")

    # 💰 Revenue Pipeline
    brief.append("║ 💰 REVENUE PIPELINE                      ║")
    brief.append(f"║  Total: ${revenue['total']:>8,.0f} | Ready: ${revenue['ready']:>6,.0f}     ║")
    brief.append(f"║  Leads: ${revenue['leads']:>7,.0f} | Submitted: ${revenue['submitted']:>4,.0f}      ║")
    brief.append("╠════════════════════════════════════════╣")

    # 🔥 Recent Work
    brief.append("║ 🔥 RECENT WORK (last 3 blocks)          ║")
    for block in recent:
        # Extract the task from the block
        if "**Task:**" in block:
            task = block.split("**Task:**")[1].split("**")[0].strip()
            brief.append(f"║  • {task[:34]:<34} ║")
    brief.append("╠════════════════════════════════════════╣")

    # 📊 Metrics
    brief.append("║ 📊 METRICS                              ║")
    brief.append(f"║  Work blocks: {blocks:>5}                         ║")
    brief.append(f"║  Revenue: ${revenue['total']:>9,.0f}                      ║")
    brief.append("╚════════════════════════════════════════╝")

    return "\n".join(brief)


def format_full_brief():
    """Generate extended brief with more details."""
    brief = format_brief()

    # Add blocker details
    revenue = get_revenue_summary()
    if revenue["blockers"]:
        brief += "\n\n🚨 BLOCKER DETAILS:\n"
        for i, blocker in enumerate(revenue["blockers"], 1):
            brief += f"{i}. {blocker}\n"

    # Add next actions
    brief += "\n✅ NEXT ACTIONS:\n"
    brief += "1. Review docs/unblock-180k.md (10 min → $180K)\n"
    brief += "2. Check revenue progress: python3 tools/revenue-tracker.py\n"
    brief += "3. Review service messages (10 ready to send)\n"

    return brief


def format_blockers_only():
    """Show only blockers with clear unblock steps."""
    revenue = get_revenue_summary()

    if not revenue["blockers"]:
        return "✅ No blockers! Pipeline is clear."

    output = ["🚨 ACTIVE BLOCKERS:", ""]

    for i, blocker in enumerate(revenue["blockers"], 1):
        output.append(f"{i}. {blocker}")

    output.append("\n💡 QUICK FIX: See docs/unblock-180k.md")
    output.append("   10 minutes → $180K unlocked")

    return "\n".join(output)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Nova's daily brief")
    parser.add_argument("--full", action="store_true", help="Full brief with details")
    parser.add_argument("--blockers", action="store_true", help="Show only blockers")
    args = parser.parse_args()

    if args.blockers:
        print(format_blockers_only())
    elif args.full:
        print(format_full_brief())
    else:
        print(format_brief())


if __name__ == "__main__":
    main()
