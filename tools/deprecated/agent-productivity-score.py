#!/usr/bin/env python3
"""
agent-productivity-score.py
Calculate a productivity score from diary/heartbeat logs.
For agents who want to measure their output velocity.

Usage:
    python agent-productivity-score.py diary.md
    python agent-productivity-score.py --stdin < diary.md
"""

import re
import sys
from datetime import datetime
from collections import defaultdict

def parse_entries(content):
    """Extract timestamped entries from diary content."""
    # Match [TYPE] YYYY-MM-DDThh:mm:ssZ format (all on one line)
    pattern = r'^\[([^\]]+)\]\s+(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)\s*\n(.+?)(?=\n---|\n\[|$)'
    matches = re.findall(pattern, content, re.DOTALL | re.MULTILINE)
    
    entries = []
    for entry_type, timestamp, body in matches:
        try:
            entries.append({
                'type': entry_type.strip(),
                'time': datetime.fromisoformat(timestamp.replace('Z', '+00:00')),
                'body': body.strip()
            })
        except:
            pass  # Skip malformed entries
    return entries

def calculate_metrics(entries):
    """Calculate productivity metrics from entries."""
    metrics = {
        'total_entries': len(entries),
        'by_type': defaultdict(int),
        'by_hour': defaultdict(int),
        'by_day': defaultdict(int),
        'work_blocks': 0,
        'completed_tasks': 0
    }
    
    for entry in entries:
        metrics['by_type'][entry['type']] += 1
        metrics['by_hour'][entry['time'].hour] += 1
        metrics['by_day'][entry['time'].strftime('%Y-%m-%d')] += 1
        
        if 'WORK BLOCK' in entry['type'] or 'work' in entry['body'].lower():
            metrics['work_blocks'] += 1
        if 'complete' in entry['body'].lower() or '✅' in entry['body']:
            metrics['completed_tasks'] += 1
    
    return metrics

def calculate_score(metrics):
    """Calculate overall productivity score (0-100)."""
    # Factors: consistency, volume, completion rate
    score = 0
    
    # Volume score (up to 40 pts)
    volume = min(metrics['total_entries'] / 50, 1.0)  # Normalize to 50 entries
    score += volume * 40
    
    # Consistency score (up to 30 pts)
    unique_days = len(metrics['by_day'])
    consistency = min(unique_days / 7, 1.0)  # Normalize to 1 week
    score += consistency * 30
    
    # Completion score (up to 30 pts)
    if metrics['total_entries'] > 0:
        completion = min(metrics['completed_tasks'] / metrics['total_entries'] * 2, 1.0)
        score += completion * 30
    
    return round(score)

def get_tier(score):
    """Get productivity tier based on score."""
    if score >= 90: return "🏆 Legendary"
    if score >= 75: return "🌟 Elite"  
    if score >= 60: return "⚡ Pro"
    if score >= 40: return "🔥 Active"
    if score >= 20: return "💪 Building"
    return "🌱 Starting"

def print_report(metrics, score):
    """Print formatted productivity report."""
    print("=" * 50)
    print("📊 AGENT PRODUCTIVITY REPORT")
    print("=" * 50)
    print()
    print(f"Overall Score: {score}/100")
    print(f"Tier: {get_tier(score)}")
    print()
    print("📈 METRICS")
    print(f"  Total Entries: {metrics['total_entries']}")
    print(f"  Work Blocks: {metrics['work_blocks']}")
    print(f"  Completed Tasks: {metrics['completed_tasks']}")
    print(f"  Active Days: {len(metrics['by_day'])}")
    print()
    
    if metrics['by_type']:
        print("📝 ENTRY TYPES")
        for entry_type, count in sorted(metrics['by_type'].items(), key=lambda x: -x[1])[:5]:
            bar = "█" * int(count / max(metrics['by_type'].values()) * 20)
            print(f"  {entry_type:15} {count:3} {bar}")
        print()
    
    if metrics['by_hour']:
        print("⏰ ACTIVITY BY HOUR")
        peak_hour = max(metrics['by_hour'], key=metrics['by_hour'].get)
        print(f"  Peak Activity: {peak_hour:02d}:00 ({metrics['by_hour'][peak_hour]} entries)")
        print()
    
    print("=" * 50)

def main():
    if len(sys.argv) < 2 or sys.argv[1] == '--help':
        print(__doc__)
        sys.exit(0)
    
    if sys.argv[1] == '--stdin':
        content = sys.stdin.read()
    else:
        with open(sys.argv[1], 'r') as f:
            content = f.read()
    
    entries = parse_entries(content)
    if not entries:
        print("No timestamped entries found in log file.")
        print("Expected format: [TYPE] YYYY-MM-DDThh:mm:ssZ")
        sys.exit(1)
    
    metrics = calculate_metrics(entries)
    score = calculate_score(metrics)
    print_report(metrics, score)

if __name__ == '__main__':
    main()
