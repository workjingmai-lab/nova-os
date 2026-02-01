#!/usr/bin/env python3
"""
nova-status.py - Quick 24h activity summary from diary.md
Usage: python3 nova-status.py
"""

import re
from datetime import datetime, timedelta
from collections import Counter

def parse_diary(filepath="diary.md"):
    """Parse diary.md and extract last 24h entries."""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        return []
    
    cutoff = datetime.now() - timedelta(hours=24)
    entries = []
    
    # Pattern: ISO timestamps like 2026-02-01T08:51:00Z
    for line in content.split('\n'):
        # Match ISO timestamp anywhere in line
        ts_match = re.search(r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)', line)
        if ts_match:
            try:
                entry_time = datetime.strptime(ts_match.group(1), "%Y-%m-%dT%H:%M:%SZ")
                if entry_time >= cutoff:
                    entries.append({
                        'time': entry_time,
                        'line': line.strip()[:80]
                    })
            except:
                pass
    
    return entries

def summarize(entries):
    """Generate summary stats."""
    if not entries:
        return "📊 No entries in last 24h"
    
    # Count entry types
    types = Counter()
    for e in entries:
        line = e['line'].lower()
        if 'heartbeat' in line or 'check' in line:
            types['heartbeats'] += 1
        elif 'build' in line or 'creat' in line:
            types['builds'] += 1
        elif 'post' in line or 'moltbook' in line:
            types['posts'] += 1
        elif 'learn' in line or 'read' in line:
            types['learning'] += 1
        else:
            types['other'] += 1
    
    # Build output
    lines = [
        f"📊 Nova Status (Last 24h)",
        f"━━━━━━━━━━━━━━━━━━━━━━━",
        f"Entries logged: {len(entries)}",
        f"",
        f"Activity breakdown:",
    ]
    
    for t, c in types.most_common():
        bar = '█' * min(c, 10)
        lines.append(f"  {t:12} {bar} {c}")
    
    lines.append(f"\nLast activity: {entries[-1]['time'].strftime('%H:%M')}")
    return '\n'.join(lines)

if __name__ == "__main__":
    entries = parse_diary()
    print(summarize(entries))
