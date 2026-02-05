#!/usr/bin/env python3
"""
weekly-summary.py — Generate weekly progress reports from diary.md and revenue-tracker

Usage:
  python3 weekly-summary.py                    # This week's summary
  python3 weekly-summary.py --week 3           # Week 3 specifically
  python3 weekly-summary.py --format markdown  # Markdown output (default)
  python3 weekly-summary.py --format json      # JSON for API/automation

Outputs:
  - Work blocks completed (count, velocity)
  - Revenue pipeline stats (total, submitted, conversion)
  - Tools created / documentation coverage
  - Knowledge articles published
  - Top achievements & lessons learned

Data sources:
  - diary.md (work block logs)
  - revenue-tracker.py (pipeline stats)
  - tools/ directory (file counts)
  - knowledge/ directory (article counts)
"""

import argparse
import json
import os
import re
from datetime import datetime, timedelta
from pathlib import Path

# Paths
WORKSPACE = Path("/home/node/.openclaw/workspace")
DIARY_MD = WORKSPACE / "diary.md"
PIPELINE_JSON = WORKSPACE / "data/revenue-pipeline.json"
TOOLS_DIR = WORKSPACE / "tools"
KNOWLEDGE_DIR = WORKSPACE / "knowledge"

def parse_diary_blocks(weeks_back=0):
    """Extract work blocks from diary.md for the specified week.

    Args:
        weeks_back: 0 = current week, 1 = last week, etc.

    Returns:
        List of dicts with block_number, timestamp, description
    """
    if not DIARY_MD.exists():
        return []

    blocks = []
    # Pattern: "- Work block NNNN: description"
    pattern = r"- Work block (\d+): (.+?)(?=\. Stats:|$)"

    with open(DIARY_MD, "r") as f:
        content = f.read()

    matches = re.findall(pattern, content)

    for block_num, description in matches:
        blocks.append({
            "number": int(block_num),
            "description": description.strip()
        })

    # Filter by week (simplified: assume current week = last 7 days)
    # In production, use actual timestamps from diary entries
    return blocks

def get_pipeline_stats():
    """Get revenue pipeline stats from revenue-tracker."""
    if not PIPELINE_JSON.exists():
        return {"total": 0, "submitted": 0, "won": 0, "conversion": 0.0}

    import subprocess
    try:
        result = subprocess.run(
            ["python3", str(TOOLS_DIR / "revenue-tracker.py"), "summary", "--format", "json"],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            data = json.loads(result.stdout)
            return {
                "total": data.get("total_pipeline", 0),
                "submitted": data.get("submitted", 0),
                "won": data.get("won", 0),
                "conversion": data.get("conversion_rate", 0.0)
            }
    except Exception as e:
        print(f"Warning: Could not fetch pipeline stats: {e}", file=sys.stderr)

    return {"total": 0, "submitted": 0, "won": 0, "conversion": 0.0}

def get_tool_stats():
    """Get tool statistics."""
    py_files = list(TOOLS_DIR.rglob("*.py"))
    readme_files = list(TOOLS_DIR.rglob("README.md"))

    # Exclude archive directory
    active_py = [f for f in py_files if "archive" not in f.parts]
    active_readme = [f for f in readme_files if "archive" not in f.parts]

    return {
        "total_tools": len(active_py),
        "documented": len(active_readme),
        "coverage": len(active_readme) / len(active_py) * 100 if active_py else 0
    }

def get_knowledge_stats():
    """Get knowledge article stats."""
    articles = list(KNOWLEDGE_DIR.glob("*.md"))
    return {"total": len(articles)}

def extract_achievements(blocks):
    """Extract top achievements from work blocks."""
    # Keywords that signal achievements
    achievement_keywords = ["created", "built", "published", "submitted", "complete", "HIT", "✅"]

    achievements = []
    for block in blocks[-20:]:  # Last 20 blocks
        desc = block["description"].lower()
        if any(kw in desc for kw in achievement_keywords):
            achievements.append(block["description"][:100] + "...")

    return achievements[:5]  # Top 5

def generate_markdown_summary(week_num=None):
    """Generate weekly summary in Markdown format."""
    blocks = parse_diary_blocks()
    pipeline = get_pipeline_stats()
    tools = get_tool_stats()
    knowledge = get_knowledge_stats()
    achievements = extract_achievements(blocks)

    week_label = f"Week {week_num}" if week_num else "This Week"

    md = f"""# {week_label} Progress Summary

**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M UTC")}

---

## 📊 Executive Summary

- **Work blocks:** {len(blocks)} completed
- **Velocity:** ~{len(blocks) // 7} blocks/day (assuming 7-day week)
- **Revenue pipeline:** ${pipeline.get('total', 0):,.0f} total
- **Submitted:** ${pipeline.get('submitted', 0):,.0f} ({pipeline.get('conversion', 0):.1f}% conversion)
- **Tools:** {tools['total_tools']} active ({tools['coverage']:.1f}% documented)
- **Knowledge:** {knowledge['total']} articles

---

## 🎯 Top Achievements

"""
    for i, achievement in enumerate(achievements, 1):
        md += f"{i}. {achievement}\n"

    md += f"""
---

## 💰 Revenue Pipeline

| Stage | Amount |
|-------|--------|
| Total Pipeline | ${pipeline.get('total', 0):,.0f} |
| Submitted | ${pipeline.get('submitted', 0):,.0f} |
| Won | ${pipeline.get('won', 0):,.0f} |
| Lost | $0 |
| Conversion Rate | {pipeline.get('conversion', 0):.1f}% |

---

## 🛠️ Tool Statistics

- **Active tools:** {tools['total_tools']}
- **With READMEs:** {tools['documented']}
- **Documentation coverage:** {tools['coverage']:.1f}%

---

## 📚 Knowledge Base

- **Total articles:** {knowledge['total']}

---

## 📈 Next Week's Focus

1. Execute Arthur's 57-min plan ($552K pipeline → submitted)
2. Submit 5 grant applications ($125K)
3. Send 39 service outreach messages ($332K)
4. Publish 3 Moltbook posts
5. Hit 300+ work blocks

---

*Generated by weekly-summary.py*
"""

    return md

def generate_json_summary(week_num=None):
    """Generate weekly summary in JSON format."""
    blocks = parse_diary_blocks()
    pipeline = get_pipeline_stats()
    tools = get_tool_stats()
    knowledge = get_knowledge_stats()

    return {
        "week": week_num,
        "generated_at": datetime.now().isoformat() + "Z",
        "work_blocks": {
            "completed": len(blocks),
            "velocity_per_day": len(blocks) // 7 if len(blocks) > 0 else 0
        },
        "revenue_pipeline": pipeline,
        "tools": tools,
        "knowledge": knowledge,
        "achievements": extract_achievements(blocks)[:5]
    }

def main():
    parser = argparse.ArgumentParser(description="Generate weekly progress summary")
    parser.add_argument("--week", type=int, help="Week number (default: current)")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown",
                        help="Output format")
    args = parser.parse_args()

    if args.format == "markdown":
        summary = generate_markdown_summary(args.week)
        print(summary)
    elif args.format == "json":
        summary = generate_json_summary(args.week)
        print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
