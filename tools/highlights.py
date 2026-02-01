#!/usr/bin/env python3
"""
highlights.py — Extract key highlights from diary.md
Usage: python3 tools/highlights.py [today]
"""

import re
from datetime import datetime, timedelta
from pathlib import Path

def extract_highlights(diary_path="diary.md", days_back=1):
    """Extract key insights, files created, and completed work blocks"""
    content = Path(diary_path).read_text()

    # Parse today's date header
    today = datetime.utcnow().date()
    target_date = today - timedelta(days=days_back)
    date_header = target_date.strftime("%Y-%m-%d")

    # Find today's section (more flexible search)
    pattern = f"## {date_header}"
    if pattern not in content:
        return {"error": f"No entries found for {date_header}"}

    # Get all sections for this date
    sections = content.split(pattern)
    if len(sections) < 2:
        return {"error": f"No entries found for {date_header}"}

    # Combine all sections for this date (skip first which is before first match)
    today_section = "".join(sections[1:])

    # Extract work blocks
    blocks = re.findall(r"Work Block (\d+)", today_section)
    total_blocks = len(set(blocks))
    total_blocks = len(set(blocks))

    # Extract insights
    insights = re.findall(r"\*\*Key Insight:\*\* (.+)", today_section)

    # Extract files created
    files = re.findall(r"Files Created: (.+)", today_section)

    # Extract session completes
    sessions = re.findall(r"SESSION COMPLETE", today_section)

    # Extract values (why it matters)
    values = re.findall(r"\*\*Value:\*\* (.+)", today_section)

    return {
        "date": str(target_date),
        "work_blocks": total_blocks,
        "insights": insights,
        "files_created": files,
        "sessions_completed": len(sessions),
        "values_delivered": values
    }

def format_highlights(data):
    """Format highlights for display"""
    if "error" in data:
        return f"❌ {data['error']}"

    output = [f"📅 {data['date']} — Daily Highlights"]
    output.append("=" * 50)
    output.append(f"\n🎯 Work Blocks: {data['work_blocks']}")
    output.append(f"✅ Sessions Complete: {data['sessions_completed']}")

    if data['insights']:
        output.append("\n💡 Key Insights:")
        for insight in data['insights'][:5]:  # Max 5
            output.append(f"  • {insight[:80]}...")

    if data['files_created']:
        output.append(f"\n📁 Files Created: {len(data['files_created'])}")
        for f in data['files_created'][:5]:
            output.append(f"  • {f}")

    if data['values_delivered']:
        output.append("\n✨ Values Delivered:")
        for v in data['values_delivered'][:3]:
            output.append(f"  • {v[:80]}...")

    return "\n".join(output)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Extract daily highlights from diary.md")
    parser.add_argument("--days", "-d", type=int, default=1, help="Days back (default: 1=today)")
    args = parser.parse_args()

    data = extract_highlights(days_back=args.days)
    print(format_highlights(data))
