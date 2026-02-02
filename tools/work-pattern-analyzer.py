#!/usr/bin/env python3
"""
Work Pattern Analyzer — Time-of-Day Distribution

Analyzes diary.md to find productivity patterns by time of day.
Helps optimize when to do different types of work.

Usage:
    python3 tools/work-pattern-analyzer.py
"""

import re
from datetime import datetime
from collections import defaultdict

DIARY_PATH = "/home/node/.openclaw/workspace/diary.md"

def parse_work_blocks():
    """Extract work blocks with timestamps and task types."""
    blocks = []
    
    with open(DIARY_PATH, 'r') as f:
        content = f.read()
    
    # Pattern: ### HH:MMZ — Work Block XXX — Title
    pattern = r'### (\d{2}:\d{2})Z — Work Block (\d+) — (.+?)(?=\n|$)'
    
    matches = re.findall(pattern, content)
    
    for time_str, block_num, title in matches:
        hour = int(time_str.split(':')[0])
        blocks.append({
            'time': time_str,
            'hour': hour,
            'block': int(block_num),
            'title': title.strip()
        })
    
    return blocks

def categorize_task(title):
    """Categorize task by type."""
    title_lower = title.lower()
    
    if 'tool' in title_lower or 'script' in title_lower or 'built' in title_lower:
        return 'Building'
    elif 'moltbook' in title_lower or 'post' in title_lower or 'draft' in title_lower:
        return 'Content'
    elif 'goal' in title_lower or 'plan' in title_lower:
        return 'Planning'
    elif 'analyz' in title_lower or 'pattern' in title_lower or 'review' in title_lower:
        return 'Analysis'
    elif 'docum' in title_lower or 'update' in title_lower or 'ref' in title_lower:
        return 'Documentation'
    else:
        return 'Other'

def analyze_by_hour(blocks):
    """Group blocks by hour."""
    hourly = defaultdict(lambda: {'total': 0, 'categories': defaultdict(int)})
    
    for block in blocks:
        hour = block['hour']
        category = categorize_task(block['title'])
        
        hourly[hour]['total'] += 1
        hourly[hour]['categories'][category] += 1
    
    return hourly

def print_header():
    print("=" * 60)
    print("📊 WORK PATTERN ANALYZER — Time Distribution")
    print("=" * 60)
    print()

def print_hourly_breakdown(hourly):
    """Print hourly distribution."""
    print("⏰ HOURLY ACTIVITY (UTC):")
    print("-" * 60)
    
    for hour in sorted(hourly.keys()):
        data = hourly[hour]
        total = data['total']
        
        # Top category for this hour
        top_cat = max(data['categories'].items(), key=lambda x: x[1])
        top_name, top_count = top_cat
        
        bar = '█' * min(total, 20)
        
        print(f"{hour:02d}:00 | {bar:20s} | {total:2d} blocks | Top: {top_name} ({top_count})")
    
    print()

def print_peak_hours(hourly):
    """Find most productive hours."""
    sorted_hours = sorted(hourly.items(), key=lambda x: x[1]['total'], reverse=True)
    
    print("🔥 PEAK PRODUCTIVITY HOURS:")
    print("-" * 60)
    
    for hour, data in sorted_hours[:5]:
        total = data['total']
        top_cat = max(data['categories'].items(), key=lambda x: x[1])[0]
        print(f"  {hour:02d}:00 — {total} blocks (mostly {top_cat})")
    
    print()

def print_task_distribution(hourly):
    """Overall task type distribution."""
    all_categories = defaultdict(int)
    
    for data in hourly.values():
        for cat, count in data['categories'].items():
            all_categories[cat] += count
    
    total = sum(all_categories.values())
    
    print("📈 TASK TYPE DISTRIBUTION:")
    print("-" * 60)
    
    for cat, count in sorted(all_categories.items(), key=lambda x: x[1], reverse=True):
        pct = (count / total) * 100
        bar = '█' * int(pct / 5)
        print(f"  {cat:15s} | {bar:20s} | {count:3d} ({pct:5.1f}%)")
    
    print()

def print_insights(hourly, total_blocks):
    """Generate insights."""
    print("💡 INSIGHTS:")
    print("-" * 60)
    
    # Find peak
    peak_hour, peak_data = max(hourly.items(), key=lambda x: x[1]['total'])
    print(f"  • Peak hour: {peak_hour:02d}:00 UTC ({peak_data['total']} blocks)")
    
    # Building focus
    building_hours = [h for h, d in hourly.items() if d['categories'].get('Building', 0) >= 2]
    if building_hours:
        print(f"  • Best for building: {', '.join(f'{h:02d}:00' for h in building_hours[:3])}")
    
    # Content focus
    content_hours = [h for h, d in hourly.items() if d['categories'].get('Content', 0) >= 2]
    if content_hours:
        print(f"  • Best for content: {', '.join(f'{h:02d}:00' for h in content_hours[:3])}")
    
    print(f"  • Total analyzed: {total_blocks} blocks")
    print()

def main():
    print_header()
    
    blocks = parse_work_blocks()
    
    if not blocks:
        print("⚠️  No work blocks found in diary.md")
        return
    
    hourly = analyze_by_hour(blocks)
    
    print_hourly_breakdown(hourly)
    print_peak_hours(hourly)
    print_task_distribution(hourly)
    print_insights(hourly, len(blocks))
    
    print("=" * 60)
    print("✅ Analysis complete. Optimize your schedule!")
    print("=" * 60)

if __name__ == "__main__":
    main()
