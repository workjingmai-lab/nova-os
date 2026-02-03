#!/usr/bin/env python3
"""
⚠️ DEPRECATED — Use daily-report.py instead

This tool has been consolidated into daily-report.py (mode: snapshot).
Run: python3 daily-report.py snapshot

Keeping this file for reference. Migration date: 2026-02-02

---

[Original documentation follows]

daily-snapshot.py - Generate a quick daily status report for Arthur
Run this anytime to see Nova's current state at a glance.
"""

import json
import os
from datetime import datetime, timezone
from pathlib import Path

def get_goal_progress():
    """Parse active.md for completion status"""
    active_file = Path("/home/node/.openclaw/workspace/goals/active.md")
    if not active_file.exists():
        return {"completed": 0, "total": 0}
    
    content = active_file.read_text()
    completed = content.count("[x]")
    total = content.count("[x]") + content.count("[ ]")
    return {"completed": completed, "total": total, "percent": int((completed/total)*100) if total else 0}

def get_recent_activity(hours=24):
    """Count recent diary entries"""
    diary_file = Path("/home/node/.openclaw/workspace/diary.md")
    if not diary_file.exists():
        return 0
    
    content = diary_file.read_text()
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return content.count(today)

def get_heartbeat_stats():
    """Get basic heartbeat metrics"""
    hb_dir = Path("/home/node/.openclaw/workspace/heartbeats")
    if not hb_dir.exists():
        return {"files": 0, "lines": 0}
    
    files = list(hb_dir.glob("*.jsonl"))
    total_lines = 0
    for f in files:
        try:
            with open(f) as fp:
                total_lines += sum(1 for _ in fp)
        except:
            pass
    return {"files": len(files), "lines": total_lines}

def get_tools_count():
    """Count tools in workspace"""
    tools_dir = Path("/home/node/.openclaw/workspace/tools")
    if not tools_dir.exists():
        return 0
    return len(list(tools_dir.glob("*.py")))

def generate_snapshot():
    """Generate the daily snapshot report"""
    now = datetime.now(timezone.utc)
    
    goals = get_goal_progress()
    activity = get_recent_activity()
    hb = get_heartbeat_stats()
    tools = get_tools_count()
    
    report = f"""# 📸 Nova Daily Snapshot
**Generated:** {now.strftime("%Y-%m-%d %H:%M UTC")}

## 🎯 Goals Progress
- **Completed:** {goals['completed']}/{goals['total']} ({goals['percent']}%)
- **Status:** {"🟢 On track" if goals['percent'] >= 75 else "🟡 Making progress" if goals['percent'] >= 50 else "🔴 Needs attention"}

## 📊 Activity Today
- **Diary entries:** {activity}
- **Tools built:** {tools} total
- **Heartbeats logged:** {hb['files']:,} files, {hb['lines']:,} entries

## ⚡ Current Blockers
"""
    
    # Check today.md for blockers
    today_file = Path("/home/node/.openclaw/workspace/today.md")
    if today_file.exists():
        content = today_file.read_text()
        if "Blockers:" in content:
            blockers_section = content.split("Blockers:")[1].split("\n##")[0] if "\n##" in content.split("Blockers:")[1] else content.split("Blockers:")[1]
            for line in blockers_section.strip().split("\n"):
                line = line.strip()
                if line and not line.startswith("-"):
                    report += f"- {line}\n"
                elif line.startswith("-"):
                    report += f"{line}\n"
    
    report += f"""
## 🔄 Next Actions
See today.md for current priorities.

---
*Run `./tools/daily-snapshot.py` anytime for fresh data*
"""
    
    return report

if __name__ == "__main__":
    snapshot = generate_snapshot()
    
    # Save to file
    output_file = Path("/home/node/.openclaw/workspace/reports/daily-snapshot.md")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(snapshot)
    
    # Also print to stdout
    print(snapshot)
    print(f"\n✅ Snapshot saved to: {output_file}")
