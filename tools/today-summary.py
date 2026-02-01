#!/usr/bin/env python3
"""
today-summary.py - Generate a human-readable summary of today's work
Perfect for Arthur to quickly see what Nova accomplished.
"""

import re
from datetime import datetime, timezone
from pathlib import Path

def get_today_entries():
    """Extract today's entries from diary.md"""
    diary_file = Path("/home/node/.openclaw/workspace/diary.md")
    if not diary_file.exists():
        return []
    
    content = diary_file.read_text()
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    
    # Split by date headers (## YYYY-MM-DD)
    entries = []
    current_date = None
    current_content = []
    
    for line in content.split('\n'):
        date_match = re.match(r'## (\d{4}-\d{2}-\d{2})', line)
        if date_match:
            if current_date == today and current_content:
                entries.append('\n'.join(current_content))
            current_date = date_match.group(1)
            current_content = []
        elif current_date == today:
            current_content.append(line)
    
    # Don't forget the last section
    if current_date == today and current_content:
        entries.append('\n'.join(current_content))
    
    return entries

def extract_tasks(entries_text):
    """Extract completed tasks from entries"""
    tasks = []
    for line in entries_text.split('\n'):
        # Look for task patterns
        if '**Task' in line and 'COMPLETE' in line:
            task = line.split(':**')[1].split('✅')[0].strip() if ':**' in line else line.strip()
            tasks.append(task)
        elif line.strip().startswith('- ') and any(kw in line.lower() for kw in ['built', 'created', 'wrote', 'fixed', 'deployed']):
            tasks.append(line.strip()[2:])
    return tasks

def count_tools_built():
    """Count Python tools in tools/ directory"""
    tools_dir = Path("/home/node/.openclaw/workspace/tools")
    if not tools_dir.exists():
        return 0
    return len(list(tools_dir.glob("*.py")))

def generate_summary():
    """Generate the human-readable summary"""
    now = datetime.now(timezone.utc)
    today_str = now.strftime("%B %d, %Y")
    
    entries = get_today_entries()
    entries_text = '\n'.join(entries)
    tasks = extract_tasks(entries_text)
    tool_count = count_tools_built()
    
    # Count various activities
    files_created = entries_text.count("Created `") + entries_text.count("Built `") + entries_text.count("Wrote `")
    posts_made = entries_text.lower().count("moltbook") + entries_text.lower().count("posted")
    
    summary = f"""# 📋 Nova's Day in Review — {today_str}

## ✅ What Got Done ({len(tasks)} tasks)
"""
    
    if tasks:
        for task in tasks[-5:]:  # Last 5 tasks
            summary += f"- {task}\n"
    else:
        summary += "- (No completed tasks logged yet today)\n"
    
    summary += f"""
## 📊 By the Numbers
- **Tools built today:** ~{files_created} new files
- **Total tools in arsenal:** {tool_count}
- **Social posts:** {posts_made if posts_made else 0}

## 🎯 Goals Status
"""
    
    # Check goals
    active_file = Path("/home/node/.openclaw/workspace/goals/active.md")
    if active_file.exists():
        content = active_file.read_text()
        completed = content.count("[x]")
        total = content.count("[x]") + content.count("[ ]")
        summary += f"- **Week 1 Progress:** {completed}/{total} complete ({int((completed/total)*100)}%)\n"
    
    summary += """
## ⚡ Current Blockers
"""
    
    # Pull blockers from today.md
    today_file = Path("/home/node/.openclaw/workspace/today.md")
    if today_file.exists():
        content = today_file.read_text()
        if "Blockers:" in content:
            blockers = content.split("Blockers:")[1].split("\n##")[0] if "\n##" in content.split("Blockers:")[1] else content.split("Blockers:")[1]
            blocker_lines = [l.strip() for l in blockers.strip().split("\n") if l.strip() and not l.strip().startswith("-")]
            if blocker_lines:
                summary += f"- {', '.join(blocker_lines)}\n"
            else:
                summary += "- None 🎉\n"
    
    summary += f"""
---
*Generated at {now.strftime('%H:%M UTC')} | Run `./tools/today-summary.py` for fresh data*
"""
    
    return summary

if __name__ == "__main__":
    summary = generate_summary()
    
    # Save to file
    output_file = Path("/home/node/.openclaw/workspace/reports/today-summary.md")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(summary)
    
    # Print to stdout
    print(summary)
    print(f"✅ Summary saved to: {output_file}")
