#!/usr/bin/env python3
"""
conversion-pulse.py — Quick conversion metrics snapshot

Post-send daily check: How many responses? Calls booked? Revenue won?

Usage:
    python3 tools/conversion-pulse.py

Output:
    Single-line conversion summary with trends
"""

import json
from pathlib import Path
from datetime import datetime, timedelta

WORKSPACE = Path("/home/node/.openclaw/workspace")
PIPELINE_FILE = WORKSPACE / "revenue-pipeline.json"
CONVERSION_FILE = WORKSPACE / "conversion-tracking.json"

def load_pipeline():
    """Load pipeline data"""
    if not PIPELINE_FILE.exists():
        return None

    with open(PIPELINE_FILE) as f:
        return json.load(f)

def load_conversion():
    """Load conversion tracking data"""
    if not CONVERSION_FILE.exists():
        return {"responses": {}, "calls": {}, "won": {}}

    with open(CONVERSION_FILE) as f:
        return json.load(f)

def calculate_metrics(pipeline, conversion):
    """Calculate conversion metrics"""
    if not pipeline:
        return None

    categories = pipeline.get("categories", {})
    total = pipeline.get("totalPipeline", 0)
    submitted = sum(c.get("submitted", 0) for c in categories.values())

    # Count conversion events
    responses = len(conversion.get("responses", {}))
    calls = len(conversion.get("calls", {}))
    won = sum(c.get("amount", 0) for c in conversion.get("won", {}).values())

    return {
        "total": total,
        "submitted": submitted,
        "responses": responses,
        "calls": calls,
        "won": won,
        "response_rate": (responses / submitted * 100) if submitted > 0 else 0,
        "call_rate": (calls / responses * 100) if responses > 0 else 0,
        "win_rate": (won / submitted * 100) if submitted > 0 else 0
    }

def format_currency(amount):
    """Format currency with K suffix"""
    if amount >= 1000:
        return f"${amount/1000:.1f}K"
    return f"${amount}"

def main():
    """Display conversion pulse"""
    print("💓 Conversion Pulse")
    print("=" * 40)

    pipeline = load_pipeline()
    conversion = load_conversion()
    metrics = calculate_metrics(pipeline, conversion)

    if not metrics:
        print("⚠️  No pipeline data found")
        print()
        print("Run: python3 tools/revenue-tracker.py summary")
        return

    # Main metrics
    print(f"Sent:      {format_currency(metrics['submitted'])}")
    print(f"Responses: {metrics['responses']} ({metrics['response_rate']:.1f}%)")
    print(f"Calls:     {metrics['calls']} ({metrics['call_rate']:.1f}% of responses)")
    print(f"Won:       {format_currency(metrics['won'])} ({metrics['win_rate']:.1f}% of sent)")
    print()

    # Funnel visualization
    if metrics['submitted'] > 0:
        print("Funnel:")
        print(f"  Sent → {metrics['submitted']} messages")
        if metrics['responses'] > 0:
            print(f"  ↓ {metrics['response_rate']:.1f}% response rate")
            print(f"  Responses → {metrics['responses']}")
        else:
            print(f"  ↓ Awaiting responses...")
        if metrics['calls'] > 0:
            print(f"  ↓ {metrics['call_rate']:.1f}% call rate")
            print(f"  Calls → {metrics['calls']}")
        if metrics['won'] > 0:
            print(f"  ↓ {metrics['win_rate']:.1f}% win rate")
            print(f"  Revenue → {format_currency(metrics['won'])}")
        print()

    # Benchmarks
    print("Benchmarks (good/healthy):")
    print(f"  Response rate: {metrics['response_rate']:.1f}% (target: 10-20%)")
    print(f"  Call rate:     {metrics['call_rate']:.1f}% (target: 30-50% of responses)")
    print(f"  Win rate:      {metrics['win_rate']:.1f}% (target: 20-40% of calls)")
    print()

    # Action items
    actions = []
    if metrics['submitted'] == 0:
        actions.append("🚀 Execute sends: bash tools/send-everything.sh")
    if metrics['responses'] == 0 and metrics['submitted'] > 50:
        actions.append("⏰ Wait 24-48h for responses (typical response time)")
    if metrics['responses'] > 0 and metrics['calls'] == 0:
        actions.append("📞 Book calls: python3 tools/follow-up-reminder.py due")

    if actions:
        print("Next actions:")
        for action in actions:
            print(f"  {action}")

if __name__ == "__main__":
    main()
