#!/usr/bin/env python3
"""
daily-output-tracker.py - Analyze daily productivity from diary.md
Generates metrics: tasks completed, tools built, files created, learnings logged
"""

import re
from datetime import datetime
from pathlib import Path
from collections import defaultdict

def parse_diary_entries():
    """Parse all diary entries and extract productivity metrics."""
    diary_path = Path("diary.md")
    if not diary_path.exists():
        return {}
    
    content = diary_path.read_text()
    
    # Split by timestamp headers ([YYYY-MM-DDThh:mmZ])
    entry_pattern = r'\[(\d{4}-\d{2}-\d{2})T\d{2}:\d{2}Z\]'
    sections = re.split(entry_pattern, content)
    
    if len(sections) < 3:
        return {}
    
    # Group entries by date
    daily_data = defaultdict(lambda: defaultdict(int))
    
    for i in range(1, len(sections), 2):
        if i + 1 < len(sections):
            date = sections[i]
            entry_content = sections[i + 1]
            metrics = analyze_entry(entry_content)
            for key, val in metrics.items():
                daily_data[date][key] += val
    
    return dict(daily_data)

def analyze_entry(content):
    """Analyze a single day's entry for productivity metrics."""
    metrics = {
        'tasks_completed': len(re.findall(r'\[x\]|✅|✓|completed|finished|done', content, re.I)),
        'files_created': len(re.findall(r'created.*\.(py|md|js|ts|json|yml|yaml|sh)|new file|wrote.*to', content, re.I)),
        'tools_built': len(re.findall(r'built.*tool|created.*script|wrote.*function|implemented', content, re.I)),
        'posts_published': len(re.findall(r'posted.*on|published.*post|blog entry|moltbook', content, re.I)),
        'learnings': len(re.findall(r'learned|discovered|realized|understood', content, re.I)),
        'errors_fixed': len(re.findall(r'fixed|resolved|debugged|corrected', content, re.I)),
        'word_count': len(content.split()),
    }
    return metrics

def generate_report(daily_data):
    """Generate a formatted productivity report."""
    if not daily_data:
        return "No diary data found."
    
    lines = [
        "# 📊 Daily Output Report",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        "## Summary by Day",
        ""
    ]
    
    # Sort by date
    sorted_dates = sorted(daily_data.keys())
    
    totals = defaultdict(int)
    
    for date in sorted_dates[-7:]:  # Last 7 days
        m = daily_data[date]
        lines.append(f"### {date}")
        lines.append(f"- Tasks: {m['tasks_completed']} | Files: {m['files_created']} | Tools: {m['tools_built']} | Posts: {m['posts_published']} | Learnings: {m['learnings']} | Words: {m['word_count']}")
        lines.append("")
        
        for key, val in m.items():
            totals[key] += val
    
    lines.append("## 📈 7-Day Totals")
    lines.append(f"- **Tasks Completed:** {totals['tasks_completed']}")
    lines.append(f"- **Files Created:** {totals['files_created']}")
    lines.append(f"- **Tools Built:** {totals['tools_built']}")
    lines.append(f"- **Posts Published:** {totals['posts_published']}")
    lines.append(f"- **Learnings Logged:** {totals['learnings']}")
    lines.append(f"- **Errors Fixed:** {totals['errors_fixed']}")
    lines.append(f"- **Total Words:** {totals['word_count']}")
    lines.append("")
    
    # Velocity calculation
    avg_tasks = totals['tasks_completed'] / min(7, len(sorted_dates))
    lines.append(f"**Velocity:** {avg_tasks:.1f} tasks/day")
    
    return '\n'.join(lines)

def main():
    daily_data = parse_diary_entries()
    report = generate_report(daily_data)
    
    output_path = Path("reports/daily-output-latest.md")
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(report)
    
    # Also print to console
    print(report)
    print(f"\n📄 Saved to: {output_path}")

if __name__ == "__main__":
    main()
