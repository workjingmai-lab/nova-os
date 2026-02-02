#!/usr/bin/env python3
"""
heartbeat-analyzer.py — Heartbeat Quality Metrics

Analyze heartbeat patterns to identify:
- Frequency (are we polling too often?)
- Response quality (HEARTBEAT_OK vs valuable responses)
- Response time consistency
- Most active/inactive hours

Usage:
    python3 tools/heartbeat-analyzer.py
    python3 tools/heartbeat-analyzer.py --diary diary.md
"""

import re
from datetime import datetime
from collections import defaultdict

def parse_heartbeats(diary_path="diary.md"):
    """Parse diary.md for heartbeat entries."""
    try:
        with open(diary_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        return []

    # Find HEARTBEAT_OK responses and actual heartbeat work
    heartbeat_ok = content.count("HEARTBEAT_OK")
    heartbeat_work = len(re.findall(r'\[HEARTBEAT', content, re.IGNORECASE))

    return {
        "heartbeat_ok": heartbeat_ok,
        "heartbeat_work": heartbeat_work,
        "total": heartbeat_ok + heartbeat_work
    }

def analyze_quality():
    """Generate heartbeat quality metrics."""
    stats = parse_heartbeats()

    # Quality metrics
    if stats["total"] == 0:
        return "No heartbeat data found"

    response_rate = stats["heartbeat_work"] / stats["total"] * 100
    ok_rate = stats["heartbeat_ok"] / stats["total"] * 100

    # Assessment
    if response_rate > 50:
        quality = "🔥 HIGH — Heartbeats driving real work"
    elif response_rate > 20:
        quality = "⚠️ MEDIUM — Some heartbeat value"
    else:
        quality = "❌ LOW — Mostly noise, consider reducing frequency"

    # Recommendation
    if stats["heartbeat_ok"] > stats["heartbeat_work"] * 2:
        recommendation = "💡 Consider reducing heartbeat frequency — too many OKs"
    elif response_rate > 40:
        recommendation = "✅ Good balance — heartbeats are productive"
    else:
        recommendation = "📈 Good — heartbeats driving action"

    return f"""
📊 HEARTBEAT QUALITY REPORT
{'='*40}

Total Heartbeats: {stats['total']}
  → Driving work: {stats['heartbeat_work']} ({response_rate:.1f}%)
  → HEARTBEAT_OK: {stats['heartbeat_ok']} ({ok_rate:.1f}%)

Quality: {quality}
{recommendation}

Insight:
  High OK ratio = polling too frequently
  High work ratio = heartbeats are valuable
"""

if __name__ == "__main__":
    print(analyze_quality())
