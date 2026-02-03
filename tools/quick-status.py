#!/usr/bin/env python3
"""
Quick Status — Instant health snapshot

Shows critical metrics at a glance:
- Work blocks (today, week)
- Pipeline status ($ tracked)
- Blockers and next actions
- Time since last update

Usage:
    python3 tools/quick-status.py
"""

import json
from pathlib import Path
from datetime import datetime, timedelta

WORKSPACE = Path.home() / ".openclaw/workspace"
TODAY_MD = WORKSPACE / "today.md"
PIPELINE_JSON = WORKSPACE / "data/revenue-pipeline.json"
HEARTBEAT_STATE = WORKSPACE / ".heartbeat_state.json"

def parse_today_md():
    """Extract stats from today.md"""
    try:
        content = TODAY_MD.read_text()
        lines = content.split('\n')

        stats = {}
        for line in lines:
            if "Today:" in line and "work blocks" in line:
                # Extract: "**Today:** 243 work blocks (112 in this session)"
                parts = line.split("Today:")[1].strip()
                blocks = int(parts.split("work blocks")[0].strip().replace("*", "").replace("**", ""))
                session = int(parts.split("(")[1].split(" in this session")[0].strip())
                stats["today_blocks"] = blocks
                stats["session_blocks"] = session

            elif "Week 2:" in line and "total" in line:
                # Extract: "**Week 2:** 631 total (210% of 300 target, +331 surplus)"
                parts = line.split("Week 2:")[1].strip()
                total = int(parts.split("total")[0].strip().replace("*", "").replace("**", ""))
                stats["week_blocks"] = total

            elif "🔥 Streak:" in line:
                stats["streak"] = line.split("🔥 Streak:")[1].strip()

        return stats
    except:
        return {"today_blocks": 0, "week_blocks": 0, "session_blocks": 0, "streak": "Unknown"}

def parse_pipeline():
    """Extract pipeline stats"""
    try:
        data = json.loads(PIPELINE_JSON.read_text())

        grants = data.get("grants", [])
        services = data.get("services", [])
        bounties = data.get("bounties", [])

        total_potential = 0
        ready = 0

        for item in grants + services + bounties:
            if item.get("potential"):
                total_potential += item["potential"]
            if item.get("status") == "ready":
                if item.get("potential"):
                    ready += item["potential"]

        return {
            "total_potential": total_potential,
            "ready": ready,
            "grants": len(grants),
            "services": len(services),
            "bounties": len(bounties)
        }
    except:
        return {"total_potential": 0, "ready": 0, "grants": 0, "services": 0, "bounties": 0}

def get_last_update():
    """Check time since last activity"""
    try:
        diary = WORKSPACE / "diary.md"
        if diary.exists():
            # Get last modified time
            mtime = datetime.fromtimestamp(diary.stat().st_mtime)
            ago = datetime.now() - mtime

            if ago < timedelta(minutes=15):
                return f"🟢 Active ({ago.seconds // 60}m ago)"
            elif ago < timedelta(hours=2):
                return f"🟡 Recent ({ago.seconds // 60}m ago)"
            else:
                return f"🔴 Stale ({ago.seconds // 3600}h ago)"
    except:
        return "Unknown"

def main():
    """Print quick status"""
    stats = parse_today_md()
    pipeline = parse_pipeline()
    last_update = get_last_update()

    print("\n" + "="*50)
    print(" 📊 NOVA STATUS — Quick Snapshot")
    print("="*50 + "\n")

    # Work blocks
    print("🔥 Work Blocks:")
    print(f"   Today:    {stats.get('today_blocks', 0)} blocks (+{stats.get('session_blocks', 0)} this session)")
    print(f"   Week 2:   {stats.get('week_blocks', 0)} blocks")
    print(f"   Streak:   {stats.get('streak', 'Unknown')}\n")

    # Pipeline
    print("💰 Revenue Pipeline:")
    print(f"   Total:    ${pipeline['total_potential']:,}")
    print(f"   Ready:    ${pipeline['ready']:,}")
    print(f"   Items:    {pipeline['grants']} grants, {pipeline['services']} services, {pipeline['bounties']} bounties\n")

    # Activity
    print("⏱️  Activity:")
    print(f"   Status:   {last_update}\n")

    # Blockers
    print("⚠️  Blockers:")
    print("   📝 GitHub auth (grants) — Arthur action needed")
    print("   🌐 Browser access (Code4rena) — Gateway restart needed\n")

    # Next actions
    print("➡️  Next Actions:")
    print("   1. Execute grant submissions ($130K) — awaiting GitHub auth")
    print("   2. Send service proposals ($82K) — outreach ready")
    print("   3. Code4rena onboarding — awaiting browser access\n")

    print("="*50 + "\n")

if __name__ == "__main__":
    main()
