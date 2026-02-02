#!/usr/bin/env python3
"""
Grant Status Tracker — Nova's Grant Pipeline Monitor

Checks tracked grants for urgent deadlines and generates status reports.
"""
import json
import re
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any

# Workspace root
WORKSPACE = Path("/home/node/.openclaw/workspace")
TRACKED_GRANTS_FILE = WORKSPACE / "grants" / "tracked-grants.md"
DIARY_FILE = WORKSPACE / "diary.md"

def parse_markdown_grants(file_path: Path) -> List[Dict[str, Any]]:
    """Parse tracked-grants.md and extract grant information."""
    if not file_path.exists():
        return []

    content = file_path.read_text()
    grants = []
    current_section = None
    current_grant = {}

    lines = content.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        # Detect grant sections (### headers)
        if line.startswith('### '):
            if current_grant:  # Save previous grant
                grants.append(current_grant)
            current_grant = {'name': line[4:].strip()}
            current_section = None

        # Detect subsections (#### headers)
        elif line.startswith('#### ') or line.startswith('- \*\*'):
            field_match = re.match(r'^[-#]+\s*\*\*(.+?):\*\*\s*(.+)$', line)
            if field_match:
                key = field_match.group(1).strip().lower().replace(' ', '_')
                value = field_match.group(2).strip()
                current_grant[key] = value
                current_section = key

        # Parse list items under sections
        elif line.startswith('- ') and current_section:
            if 'notes' not in current_grant:
                current_grant['notes'] = []
            current_grant['notes'].append(line[2:].strip())

        i += 1

    if current_grant:
        grants.append(current_grant)

    return grants

def parse_deadline(deadline_str: str) -> datetime:
    """Parse various deadline formats into datetime."""
    if not deadline_str or deadline_str.lower() in ['ongoing', 'rolling', 'unknown', 'tbd']:
        return None

    # Try common formats
    formats = [
        '%Y-%m-%d',
        '%B %d, %Y',
        '%b %d, %Y',
        '%d %B %Y',
        '%d %b %Y',
    ]

    for fmt in formats:
        try:
            return datetime.strptime(deadline_str.split('(')[0].strip(), fmt)
        except ValueError:
            continue

    return None

def check_urgent_grants(grants: List[Dict[str, Any]], days_threshold: int = 3) -> List[Dict[str, Any]]:
    """Identify grants with urgent deadlines."""
    urgent = []
    today = datetime.now()

    for grant in grants:
        deadline_str = grant.get('deadline', '')
        deadline = parse_deadline(deadline_str)

        if deadline:
            days_until = (deadline - today).days
            if days_until <= days_threshold and days_until >= 0:
                grant['days_until'] = days_until
                grant['deadline_date'] = deadline.strftime('%Y-%m-%d')
                urgent.append(grant)

    return urgent

def generate_report(grants: List[Dict[str, Any]], urgent: List[Dict[str, Any]]) -> str:
    """Generate status report."""
    report_lines = []
    report_lines.append("# 🎯 Grant Status Report")
    report_lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC")
    report_lines.append("")

    # Urgent alerts
    if urgent:
        report_lines.append("## 🚨 URGENT — Deadlines ≤3 Days")
        report_lines.append("")
        for grant in urgent:
            report_lines.append(f"### {grant.get('name', 'Unknown Grant')}")
            report_lines.append(f"- **Deadline:** {grant.get('deadline_date', 'Unknown')} ({grant['days_until']} days)")
            report_lines.append(f"- **Status:** {grant.get('status', 'Unknown')}")
            report_lines.append(f"- **Source:** {grant.get('source', 'Unknown')}")
            report_lines.append("")
        report_lines.append("---")
        report_lines.append("")
    else:
        report_lines.append("✅ No urgent deadlines (≤3 days)")
        report_lines.append("")

    # Active grants summary
    active = [g for g in grants if g.get('status') and g.get('status').lower() not in ['identified', 'backlog']]
    if active:
        report_lines.append("## 📋 Active Grants")
        report_lines.append("")
        for grant in active:
            name = grant.get('name', 'Unknown')
            status = grant.get('status', 'Unknown')
            source = grant.get('source', 'Unknown')
            report_lines.append(f"**{name}** — {status}")
            report_lines.append(f"  Source: {source}")
            report_lines.append("")

    # Pipeline stats
    report_lines.append("## 📊 Pipeline Stats")
    report_lines.append("")
    report_lines.append(f"- **Total tracked:** {len(grants)}")
    report_lines.append(f"- **Active:** {len(active)}")
    report_lines.append(f"- **Urgent:** {len(urgent)}")
    report_lines.append("")

    return '\n'.join(report_lines)

def append_to_diary(entry: str):
    """Append timestamped entry to diary.md."""
    if DIARY_FILE.exists():
        existing = DIARY_FILE.read_text()
        if not existing.endswith('\n'):
            entry = '\n' + entry

    with open(DIARY_FILE, 'a') as f:
        f.write(entry + '\n')

def main():
    """Main execution."""
    import sys

    # Parse grants
    grants = parse_markdown_grants(TRACKED_GRANTS_FILE)

    # Check urgent
    urgent = check_urgent_grants(grants, days_threshold=3)

    # Generate report
    report = generate_report(grants, urgent)

    # Output
    if urgent:
        print(report)
        timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        append_to_diary(f"[{timestamp}] Grant check complete — {len(urgent)} URGENT deadlines found")
        sys.exit(1)  # Exit with error code for urgent
    else:
        print(report)
        timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        append_to_diary(f"[{timestamp}] Grant check complete — No urgent deadlines")
        print("\nGRANT_CHECK_OK")
        sys.exit(0)

if __name__ == "__main__":
    main()
