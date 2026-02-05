#!/usr/bin/env python3
"""
Weekly Velocity Report Generator
Analyzes diary.md and generates week-over-week performance metrics
"""

import json
import re
from datetime import datetime, timedelta
from pathlib import Path

DIARY_PATH = "/home/node/.openclaw/workspace/diary.md"
PIPELINE_PATH = "/home/node/.openclaw/workspace/revenue-pipeline.json"
OUTPUT_PATH = "/home/node/.openclaw/workspace/weekly-velocity-report.md"

def parse_diary_blocks():
    """Extract work blocks from diary.md"""
    with open(DIARY_PATH, 'r') as f:
        content = f.read()

    # Pattern: ## [WORK BLOCK N — timestamp]
    pattern = r'\[WORK BLOCK (\d+) — ([^\]]+)\]'
    matches = re.findall(pattern, content)

    blocks = []
    for block_num, timestamp in matches:
        blocks.append({
            'number': int(block_num),
            'timestamp': timestamp
        })

    return sorted(blocks, key=lambda x: x['number'])

def get_weekly_blocks(blocks, week_number=None):
    """Group blocks by week (assuming week starts Monday)"""
    if not blocks:
        return {}

    weeks = {}
    for block in blocks:
        try:
            dt = datetime.fromisoformat(block['timestamp'].replace('Z', '+00:00'))
            week_num = dt.isocalendar()[1]
            year = dt.year
            week_key = f"{year}-W{week_num:02d}"

            if week_key not in weeks:
                weeks[week_key] = []
            weeks[week_key].append(block)
        except:
            continue

    return weeks

def calculate_velocity(weekly_blocks):
    """Calculate velocity metrics for each week"""
    report = {}

    for week, blocks in weekly_blocks.items():
        block_count = len(blocks)
        first_block = blocks[0]['number']
        last_block = blocks[-1]['number']

        # Estimate: 1 block = 1 minute = ~44 blocks/hour sustained
        total_hours = block_count / 44

        report[week] = {
            'blocks': block_count,
            'first_block': first_block,
            'last_block': last_block,
            'estimated_hours': round(total_hours, 1),
            'velocity_bph': round(block_count / max(total_hours, 1), 1)  # blocks per hour
        }

    return report

def load_pipeline():
    """Load revenue pipeline data"""
    try:
        with open(PIPELINE_PATH, 'r') as f:
            return json.load(f)
    except:
        return {}

def generate_markdown_report(velocity_data, pipeline):
    """Generate formatted markdown report"""
    lines = []
    lines.append("# Weekly Velocity Report")
    lines.append(f"**Generated:** {datetime.utcnow().isoformat()}Z\n")

    # Summary table
    lines.append("## Week-over-Week Summary")
    lines.append("| Week | Blocks | Est. Hours | Velocity (blocks/hr) | Block Range |")
    lines.append("|------|--------|------------|---------------------|-------------|")

    for week in sorted(velocity_data.keys()):
        data = velocity_data[week]
        lines.append(
            f"| {week} | {data['blocks']} | {data['estimated_hours']}h | "
            f"{data['velocity_bph']} | #{data['first_block']}-#{data['last_block']} |"
        )

    # Pipeline snapshot
    lines.append("\n## Revenue Pipeline Snapshot")
    if pipeline:
        total = pipeline.get('totalPipeline', 0)
        lines.append(f"**Total Pipeline:** ${total:,.0f}")
        lines.append(f"**Grants:** ${pipeline.get('grants', {}).get('total', 0):,.0f}")
        lines.append(f"**Services:** ${pipeline.get('services', {}).get('total', 0):,.0f}")
        lines.append(f"**Bounties:** ${pipeline.get('bounties', {}).get('total', 0):,.0f}")
    else:
        lines.append("*No pipeline data available*")

    # Insights
    lines.append("\n## Velocity Insights")
    if len(velocity_data) > 1:
        weeks = sorted(velocity_data.keys())
        latest = weeks[-1]
        previous = weeks[-2]
        growth = velocity_data[latest]['blocks'] - velocity_data[previous]['blocks']
        pct_change = (growth / velocity_data[previous]['blocks'] * 100) if velocity_data[previous]['blocks'] > 0 else 0

        lines.append(f"**Growth:** {previous} → {latest} ({growth:+d} blocks, {pct_change:+.1f}%)")
        lines.append(f"**Latest Velocity:** {velocity_data[latest]['velocity_bph']} blocks/hour")
    else:
        lines.append("*Need at least 2 weeks of data for comparison*")

    return '\n'.join(lines)

def main():
    print("🔍 Analyzing diary.md for velocity data...")

    blocks = parse_diary_blocks()
    if not blocks:
        print("❌ No work blocks found in diary.md")
        return

    print(f"✅ Found {len(blocks)} work blocks")

    weekly_blocks = get_weekly_blocks(blocks)
    print(f"✅ Grouped into {len(weekly_blocks)} weeks")

    velocity_data = calculate_velocity(weekly_blocks)
    pipeline = load_pipeline()

    report = generate_markdown_report(velocity_data, pipeline)

    with open(OUTPUT_PATH, 'w') as f:
        f.write(report)

    print(f"✅ Report saved to {OUTPUT_PATH}")
    print(f"\n📊 Quick Stats:")
    for week, data in sorted(velocity_data.items()):
        print(f"  {week}: {data['blocks']} blocks ({data['estimated_hours']}h)")

if __name__ == "__main__":
    main()
