#!/usr/bin/env python3
"""
daily-report.py — Unified daily reporting for Nova

Consolidates daily-summary.py, daily-briefing.py, and daily-snapshot.py
into one tool with multiple modes.

Usage:
  python3 daily-report.py summary          # Full daily summary (default)
  python3 daily-report.py briefing         # Generate today.md working memory
  python3 daily-report.py snapshot         # Quick status report

  python3 daily-report.py summary --date 2026-02-01
  python3 daily-report.py summary --format json
  python3 daily-report.py summary --output reports/summary.md

Modes:
  summary   — Multi-source aggregation (diary, goals, grants, heartbeat)
  briefing  — Auto-generate today.md from goals and patterns
  snapshot  — Quick status at a glance
"""

import os
import re
import json
import argparse
from datetime import datetime, timedelta, timezone
from pathlib import Path

WORKSPACE = Path("/home/node/.openclaw/workspace")

def parse_diary_entries(date_str):
    """Extract diary entries for specific date."""
    diary_path = WORKSPACE / "diary.md"
    if not diary_path.exists():
        return []
    
    content = diary_path.read_text()
    entries = []
    
    # Match WORK BLOCK entries for the date
    pattern = rf'\[WORK BLOCK.*?\] {date_str}.*?$'
    for line in content.split('\n'):
        if date_str in line and 'WORK BLOCK' in line:
            entries.append(line.strip())
    
    return entries

def get_goal_progress():
    """Parse active.md for completion status"""
    active_file = WORKSPACE / "goals" / "active.md"
    if not active_file.exists():
        return {"completed": 0, "total": 0, "percent": 0}
    
    content = active_file.read_text()
    completed = content.count("[x]")
    total = content.count("[x]") + content.count("[ ]")
    percent = int((completed/total)*100) if total else 0
    
    return {"completed": completed, "total": total, "percent": percent}

def get_grant_status():
    """Parse grants/tracker.md for funding pipeline status"""
    grant_file = WORKSPACE / "grants" / "tracker.md"
    if not grant_file.exists():
        return {"drafts": 0, "submitted": 0}
    
    content = grant_file.read_text()
    # Count grant entries
    drafts = len(re.findall(r'- \[ \].*?\$.*?grant', content, re.IGNORECASE))
    submitted = len(re.findall(r'- \[x\].*?\$.*?grant', content, re.IGNORECASE))
    
    return {"drafts": drafts, "submitted": submitted}

def get_heartbeat_stats():
    """Get heartbeat file statistics"""
    heartbeat_dir = WORKSPACE / "heartbeat"
    if not heartbeat_dir.exists():
        return {"files": 0, "lines": 0}
    
    jsonl_files = list(heartbeat_dir.glob("*.jsonl"))
    total_lines = sum(len(f.read_text().splitlines()) for f in jsonl_files)
    
    return {"files": len(jsonl_files), "lines": total_lines}

def get_recent_activity(hours=24):
    """Count recent diary entries"""
    diary_file = WORKSPACE / "diary.md"
    if not diary_file.exists():
        return 0
    
    content = diary_file.read_text()
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    
    # Count WORK BLOCK entries for today
    return len([l for l in content.split('\n') if today in l and 'WORK BLOCK' in l])

def get_blockers():
    """Extract blockers from today.md"""
    today_file = WORKSPACE / "today.md"
    if not today_file.exists():
        return []
    
    content = today_file.read_text()
    in_blockers = False
    blockers = []
    
    for line in content.split('\n'):
        if '## Blockers' in line or '# Blockers' in line:
            in_blockers = True
            continue
        if in_blockers:
            if line.startswith('##') or line.startswith('#'):
                break
            if line.strip().startswith('⏸️') or line.strip().startswith('✅'):
                blockers.append(line.strip())
    
    return blockers

def generate_summary(date_str=None, format='text'):
    """Generate full daily summary."""
    if date_str is None:
        date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    
    goals = get_goal_progress()
    grants = get_grant_status()
    heartbeat = get_heartbeat_stats()
    entries = parse_diary_entries(date_str)
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    
    if format == 'json':
        return json.dumps({
            "date": date_str,
            "generated_at": generated_at,
            "activity": {
                "entries_logged": len(entries),
                "entries": entries[:10]  # First 10 entries
            },
            "goals": goals,
            "grants": grants,
            "operations": heartbeat
        }, indent=2)
    
    # Text format
    lines = [
        f"# 📊 Nova's Daily Summary — {date_str}",
        "",
        f"**Generated:** {generated_at}",
        "",
        "## 🎯 Goals Progress",
        f"- Completed: {goals['completed']}/{goals['total']} ({goals['percent']}.0%)",
        "",
        "## 💰 Funding Pipeline",
        f"- Grant drafts ready: {grants['drafts']}",
        f"- Applications submitted: {grants['submitted']}",
        "",
        "## 📝 Today's Activity"
    ]
    
    if entries:
        lines.extend(entries[:10])
    else:
        lines.append("- No activity logged yet")
    
    lines.extend([
        "",
        "## ⚡ Operational Stats",
        f"- Heartbeat files: {heartbeat['files']}",
        f"- Log lines: {heartbeat['lines']}",
        "",
        "---",
        "*Generated by daily-report.py*"
    ])
    
    return '\n'.join(lines)

def generate_briefing():
    """Generate today.md working memory."""
    workspace = WORKSPACE
    incomplete = []
    
    # Check week-2.md first (current week)
    week2_path = workspace / "goals" / "week-2.md"
    if week2_path.exists():
        content = week2_path.read_text()
        for line in content.splitlines():
            if line.strip().startswith("- [ ]") or line.strip().startswith("- [🔄]"):
                goal = re.sub(r'^- \[[ 🔄]\] \*\*', '', line.strip())
                goal = re.sub(r'\*\*.*$', '', goal)
                incomplete.append(goal.strip())
    
    # Get recent activity
    diary_path = workspace / "diary.md"
    recent_activity = []
    if diary_path.exists():
        content = diary_path.read_text()
        for line in reversed(content.split('\n')):
            if 'WORK BLOCK' in line and line.strip():
                recent_activity.append(line.strip()[:80])  # Truncate long lines
                if len(recent_activity) >= 3:
                    break
    
    # Get blockers
    blockers = get_blockers()
    
    # Generate today.md
    now = datetime.now(timezone.utc)
    lines = [
        f"# today.md — Nova's Working Memory",
        "",
        f"**Date:** {now.strftime('%Y-%m-%d')}",
        f"**Generated:** {now.strftime('%Y-%m-%dT%H:%M:%SZ')}",
        "",
        "## 🎯 Today's Focus (Auto-prioritized)"
    ]
    
    for goal in incomplete[:3]:
        lines.append(f"• {goal}")
    
    lines.extend([
        "",
        "## 📊 Recent Activity"
    ])
    
    for activity in reversed(recent_activity):
        lines.append(f"• {activity}")
    
    lines.extend([
        "",
        "## ⚡ Quick Actions",
        "- [ ] Execute 1 work block from active goals",
        "- [ ] Log learnings to knowledge/",
        "- [ ] Update blocker status"
    ])
    
    if blockers:
        lines.extend([
            "",
            "## 🔄 Blockers & Needs"
        ])
        for blocker in blockers:
            lines.append(blocker)
    
    return '\n'.join(lines)

def generate_snapshot():
    """Generate quick status snapshot."""
    goals = get_goal_progress()
    activity = get_recent_activity()
    blockers = get_blockers()
    tools_count = len(list((WORKSPACE / "tools").glob("*.py")))
    
    # Status emoji based on goal progress
    if goals['percent'] >= 70:
        status = "🟢 On Track"
    elif goals['percent'] >= 40:
        status = "🟡 In Progress"
    else:
        status = "🔴 Needs Focus"
    
    lines = [
        f"# 📊 Daily Snapshot — {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')} UTC",
        "",
        f"**Status:** {status}",
        "",
        "## 🎯 Goals Progress",
        f"- {goals['completed']}/{goals['total']} complete ({goals['percent']}%)",
        "",
        "## 📝 Activity Today",
        f"- {activity} work blocks",
        f"- {tools_count} tools in workspace",
        "",
        "## 🚧 Current Blockers"
    ]
    
    if blockers:
        for blocker in blockers:
            lines.append(blocker)
    else:
        lines.append("- No active blockers")
    
    lines.extend([
        "",
        "## 📌 Next Actions",
        f"See `today.md` for current priorities",
        "",
        "---",
        f"*Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')} UTC*"
    ])
    
    return '\n'.join(lines)

def main():
    parser = argparse.ArgumentParser(
        description="Unified daily reporting for Nova",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Modes:
  summary   — Multi-source aggregation (diary, goals, grants, heartbeat)
  briefing  — Auto-generate today.md from goals and patterns
  snapshot  — Quick status at a glance

Examples:
  python3 daily-report.py summary
  python3 daily-report.py briefing
  python3 daily-report.py snapshot
  python3 daily-report.py summary --date 2026-02-01 --format json --output report.md
        """
    )
    
    parser.add_argument('mode', nargs='?', default='summary',
                       choices=['summary', 'briefing', 'snapshot'],
                       help='Report mode (default: summary)')
    parser.add_argument('--date', help='Date for summary (YYYY-MM-DD)')
    parser.add_argument('--format', choices=['text', 'json'], default='text',
                       help='Output format for summary (default: text)')
    parser.add_argument('--output', help='Save output to file')
    
    args = parser.parse_args()
    
    # Generate report based on mode
    if args.mode == 'summary':
        output = generate_summary(args.date, args.format)
    elif args.mode == 'briefing':
        output = generate_briefing()
        # For briefing, default output is today.md
        if not args.output:
            args.output = WORKSPACE / "today.md"
    elif args.mode == 'snapshot':
        output = generate_snapshot()
        # For snapshot, default output is reports/daily-snapshot.md
        if not args.output:
            snapshot_dir = WORKSPACE / "reports"
            snapshot_dir.mkdir(exist_ok=True)
            args.output = snapshot_dir / "daily-snapshot.md"
    
    # Write output
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(output)
        print(f"✅ {args.mode.capitalize()} saved to {output_path}")
    else:
        print(output)

if __name__ == '__main__':
    main()
