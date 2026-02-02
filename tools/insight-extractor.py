#!/usr/bin/env python3
"""
insight-extractor.py — Auto-Extract Patterns from diary.md

Parse diary.md and extract:
- Most common task types
- Velocity patterns
- Tools created
- Insights captured
- Time-of-day patterns

Usage:
    python3 tools/insight-extractor.py
    python3 tools/insight-extractor.py --diary diary.md
"""

import re
import json
from collections import Counter, defaultdict
from datetime import datetime

def parse_work_blocks(diary_path="diary.md"):
    """Parse diary.md for work block entries."""
    try:
        with open(diary_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        return []

    # Extract work block entries
    pattern = r'\[WORK BLOCK \d+ — ([^\]]+)\] (.+?)(?=\n##|\Z)'
    matches = re.findall(pattern, content, re.DOTALL)

    blocks = []
    for timestamp, body in matches:
        blocks.append({
            "timestamp": timestamp,
            "body": body.strip()
        })

    return blocks

def extract_patterns(blocks):
    """Extract patterns from work blocks."""
    if not blocks:
        return "No work blocks found"

    # Task types (from task descriptions)
    task_types = Counter()
    tools_created = []
    insights = []

    for block in blocks:
        body = block["body"].lower()

        # Count task types
        if "created" in body or "built" in body:
            task_types["creation"] += 1
        if "updated" in body:
            task_types["updates"] += 1
        if "documented" in body or "wrote" in body:
            task_types["documentation"] += 1
        if "researched" in body or "learned" in body:
            task_types["learning"] += 1

        # Extract tool names
        tool_match = re.search(r'(\w+\.py)', body)
        if tool_match:
            tools_created.append(tool_match.group(1))

        # Extract insights (lines with "insight" or "pattern")
        if "insight:" in body or "pattern:" in body:
            lines = body.split('\n')
            for line in lines:
                if any(word in line for word in ["insight:", "pattern:", "learned:"]):
                    insights.append(line.strip())

    return {
        "task_types": task_types,
        "tools_created": Counter(tools_created),
        "insights": insights[:5],  # Top 5
        "total_blocks": len(blocks)
    }

def generate_report():
    """Generate insight report."""
    blocks = parse_work_blocks()
    patterns = extract_patterns(blocks)

    if isinstance(patterns, str):
        return patterns

    report = f"""
🔍 INSIGHT EXTRACTOR REPORT
{'='*40}

Total Work Blocks: {patterns['total_blocks']}

📊 Task Distribution:
"""
    for task_type, count in patterns["task_types"].most_common():
        pct = count / patterns["total_blocks"] * 100
        report += f"  • {task_type}: {count} ({pct:.1f}%)\n"

    if patterns["tools_created"]:
        report += f"\n🛠️ Tools Created: {len(patterns['tools_created'])}\n"
        for tool, count in patterns["tools_created"].most_common(5):
            report += f"  • {tool}\n"

    if patterns["insights"]:
        report += f"\n💡 Top Insights:\n"
        for insight in patterns["insights"]:
            report += f"  • {insight[:60]}...\n"

    # Recommendation
    top_task = patterns["task_types"].most_common(1)[0][0]
    report += f"\n🎯 Primary Focus: {top_task}\n"
    report += f"📈 Velocity: {patterns['total_blocks']} blocks documented\n"

    return report

if __name__ == "__main__":
    print(generate_report())
