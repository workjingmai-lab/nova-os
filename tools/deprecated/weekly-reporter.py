#!/usr/bin/env python3
"""
Weekly Progress Reporter — Nova's automated week-in-review
Generates structured reports from diary.md and goal files
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path
import re

WEEKLY_REPORTS_DIR = Path("/home/node/.openclaw/workspace/reports")
DIARY_PATH = Path("/home/node/.openclaw/workspace/diary.md")
ACTIVE_GOALS_PATH = Path("/home/node/.openclaw/workspace/goals/active.md")
WEEKLY_GOALS_PATH = Path("/home/node/.openclaw/workspace/goals/week-2.md")


def parse_diary_entries(days_back=7):
    """Extract work blocks and achievements from diary.md"""
    if not DIARY_PATH.exists():
        return []
    
    cutoff = datetime.now().replace(tzinfo=None) - timedelta(days=days_back)
    entries = []
    
    with open(DIARY_PATH, 'r') as f:
        content = f.read()
        
    # Split by entry markers
    entries_raw = re.split(r'\n---\n', content)
    
    for entry in entries_raw:
        # Try to extract timestamp
        ts_match = re.search(r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)', entry)
        if ts_match:
            # Parse as naive datetime (strip Z)
            ts = datetime.fromisoformat(ts_match.group(1).replace('Z', ''))
            if ts > cutoff:
                entries.append({
                    'timestamp': ts,
                    'content': entry[:200],  # First 200 chars
                    'type': detect_entry_type(entry)
                })
    
    return entries


def detect_entry_type(entry):
    """Categorize diary entry by type"""
    if '[WORK BLOCK]' in entry or '[CRON]' in entry:
        return 'task'
    elif '[FULL]' in entry:
        return 'heartbeat'
    elif '[DEEP THINK]' in entry:
        return 'deep_think'
    else:
        return 'log'


def count_work_blocks(entries):
    """Count completed work blocks"""
    return sum(1 for e in entries if e['type'] == 'task')


def extract_achievements(entries):
    """Extract lines marked as achievements"""
    achievements = []
    for entry in entries:
        if '✅' in entry['content'] or 'COMPLETE' in entry['content']:
            achievements.append(entry['content'][:100])
    return achievements[:5]  # Top 5


def generate_report(week_num=2):
    """Generate weekly progress report"""
    entries = parse_diary_entries(days_back=7)
    work_blocks = count_work_blocks(entries)
    achievements = extract_achievements(entries)
    
    # Calculate velocity (tasks per day)
    velocity = work_blocks / 7
    
    report = {
        'week_num': week_num,
        'date_range': (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d') + 
                     ' to ' + datetime.now().strftime('%Y-%m-%d'),
        'metrics': {
            'work_blocks_completed': work_blocks,
            'velocity_tasks_per_day': round(velocity, 2),
            'total_entries': len(entries),
            'achievements_count': len(achievements)
        },
        'top_achievements': achievements,
        'generated_at': datetime.now().isoformat()
    }
    
    return report


def save_report(report):
    """Save report to JSON and Markdown"""
    WEEKLY_REPORTS_DIR.mkdir(exist_ok=True, parents=True)
    
    # JSON version
    json_path = WEEKLY_REPORTS_DIR / f"week-{report['week_num']}-progress.json"
    with open(json_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    # Markdown version
    md_path = WEEKLY_REPORTS_DIR / f"week-{report['week_num']}-progress.md"
    with open(md_path, 'w') as f:
        f.write(f"""# Week {report['week_num']} Progress Report

**Date Range:** {report['date_range']}
**Generated:** {report['generated_at']}

---

## 📊 Metrics

| Metric | Value |
|--------|-------|
| Work Blocks Completed | {report['metrics']['work_blocks_completed']} |
| Velocity (tasks/day) | {report['metrics']['velocity_tasks_per_day']} |
| Total Diary Entries | {report['metrics']['total_entries']} |
| Achievements | {report['metrics']['achievements_count']} |

---

## 🏆 Top Achievements

""")
        for i, achievement in enumerate(report['top_achievements'], 1):
            f.write(f"{i}. {achievement}...\n")
    
    print(f"✅ Report saved to {json_path}")
    print(f"✅ Report saved to {md_path}")
    
    return json_path, md_path


if __name__ == '__main__':
    print("📊 Generating weekly progress report...")
    report = generate_report(week_num=2)
    json_path, md_path = save_report(report)
    print(f"\n📈 Week 2 Summary: {report['metrics']['work_blocks_completed']} work blocks, "
          f"{report['metrics']['velocity_tasks_per_day']} tasks/day velocity")
