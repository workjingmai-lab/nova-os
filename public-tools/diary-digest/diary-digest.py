#!/usr/bin/env python3
"""
Diary Digest — Summarize daily logs into insights

Reads diary.md or daily logs and extracts:
- Work blocks completed
- Tools built
- Key insights
- Metrics (velocity, achievements)

Usage:
    python diary-digest.py
    python diary-digest.py --file memory/YYYY-MM-DD.md
    python diary-digest.py --days 7
"""

import sys
import os
import re
import argparse
from datetime import datetime, timedelta
from collections import Counter

# Paths
DIARY_PATH = "/home/node/.openclaw/workspace/diary.md"
MEMORY_DIR = "/home/node/.openclaw/workspace/memory"

def extract_blocks(content):
    """Extract work blocks from diary content"""
    pattern = r'### (\d{2}:\d{2}Z) — Work Block (\d+)'
    matches = re.findall(pattern, content)
    return [(time, int(num)) for time, num in matches]

def extract_tools_built(content):
    """Extract tools built from content"""
    # Look for "Built:", "Created:", patterns
    tools = []
    patterns = [
        r'Built:?\s+`([^`]+)`',
        r'Created\s+`([^`]+\.py)`',
        r'tools/(\w+\.py)',
    ]
    for pattern in patterns:
        tools.extend(re.findall(pattern, content))
    return tools

def extract_insights(content):
    """Extract insight lines"""
    insights = []
    for line in content.split('\n'):
        line = line.strip()
        if line.startswith('**Insight:**') or line.startswith('**Key insight:**'):
            insights.append(line)
    return insights

def analyze_day(content):
    """Analyze a single day's content"""
    blocks = extract_blocks(content)
    tools = extract_tools_built(content)
    insights = extract_insights(content)

    return {
        "blocks": len(blocks),
        "block_numbers": [b[1] for b in blocks],
        "tools": tools,
        "insights": insights
    }

def generate_summary(analysis):
    """Generate summary from analysis"""
    lines = []
    lines.append(f"📊 **Daily Summary**")
    lines.append(f"")
    lines.append(f"**Work Blocks:** {analysis['blocks']}")
    if analysis['block_numbers']:
        lines.append(f"**Range:** {min(analysis['block_numbers'])}-{max(analysis['block_numbers'])}")
    lines.append(f"**Tools Built:** {len(analysis['tools'])}")
    if analysis['tools']:
        lines.append(f"**Tools:** {', '.join(analysis['tools'][:5])}")
        if len(analysis['tools']) > 5:
            lines.append(f"  ... and {len(analysis['tools']) - 5} more")
    lines.append(f"**Insights:** {len(analysis['insights'])}")
    if analysis['insights']:
        lines.append(f"")
        lines.append(f"**Top Insight:**")
        lines.append(f"{analysis['insights'][0]}")

    return '\n'.join(lines)

def main():
    parser = argparse.ArgumentParser(description="Diary digest - summarize daily logs")
    parser.add_argument("--file", help="Specific file to analyze")
    parser.add_argument("--days", type=int, help="Last N days")
    parser.add_argument("--json", action="store_true", help="Output JSON")

    args = parser.parse_args()

    # Determine what to read
    if args.file:
        with open(args.file, 'r') as f:
            content = f.read()
        analysis = analyze_day(content)
        summary = generate_summary(analysis)
        print(summary)
    elif args.days:
        # Read last N days from memory/
        summaries = []
        for i in range(args.days):
            date = (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d')
            filepath = os.path.join(MEMORY_DIR, f"{date}.md")
            if os.path.exists(filepath):
                with open(filepath, 'r') as f:
                    content = f.read()
                analysis = analyze_day(content)
                summaries.append(f"## {date}\n{generate_summary(analysis)}")

        if summaries:
            print('\n\n'.join(reversed(summaries)))
    else:
        # Read diary.md
        if os.path.exists(DIARY_PATH):
            with open(DIARY_PATH, 'r') as f:
                content = f.read()
            analysis = analyze_day(content)
            summary = generate_summary(analysis)
            print(summary)
        else:
            print(f"❌ Diary not found at {DIARY_PATH}")
            return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())
