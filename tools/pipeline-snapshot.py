#!/usr/bin/env python3
"""
pipeline-snapshot.py — Instant pipeline status view

Usage:
    python3 tools/pipeline-snapshot.py
    python3 tools/pipeline-snapshot.py --json
    python3 tools/pipeline-snapshot.py --markdown

Shows:
- Total messages, ready, sent, responded
- Pipeline value by status
- Response rate
- Top 10 by value
"""

import json
import sys
from pathlib import Path
from typing import Dict, List

PIPELINE_FILE = Path("/home/node/.openclaw/workspace/service-outreach-tracker.json")
RESPONSES_FILE = Path("/home/node/.openclaw/workspace/data/responses.json")

def load_pipeline() -> List[Dict]:
    """Load revenue pipeline."""
    if not PIPELINE_FILE.exists():
        return []
    with open(PIPELINE_FILE) as f:
        data = json.load(f)
        return data.get("messages", [])

def load_responses() -> Dict[str, Dict]:
    """Load responses, indexed by msg_id."""
    if not RESPONSES_FILE.exists():
        return {}
    with open(RESPONSES_FILE) as f:
        responses = json.load(f)
        return {r["msg_id"]: r for r in responses}

def show_snapshot(format: str = "text"):
    """Show pipeline snapshot."""
    pipeline = load_pipeline()
    responses = load_responses()

    if not pipeline:
        print("📭 No pipeline data found")
        return

    # Count by status
    status_counts = {}
    status_values = {}
    total_value = 0

    for msg in pipeline:
        status = msg.get("status", "unknown")
        value = msg.get("pipeline_value", 0)

        status_counts[status] = status_counts.get(status, 0) + 1
        status_values[status] = status_values.get(status, 0) + value
        total_value += value

    # Calculate response rate
    total_sent = status_counts.get("sent", 0)
    total_responded = len([r for r in responses.values() if r.get("status") != "no_response"])
    response_rate = (total_responded / total_sent * 100) if total_sent > 0 else 0

    # Format output
    if format == "json":
        snapshot = {
            "total_messages": len(pipeline),
            "total_value": total_value,
            "by_status": {
                "counts": status_counts,
                "values": status_values
            },
            "response_rate": response_rate,
            "responded": total_responded,
            "sent": total_sent
        }
        print(json.dumps(snapshot, indent=2))

    elif format == "markdown":
        print("## Pipeline Snapshot")
        print()
        print(f"**Total Messages:** {len(pipeline)}")
        print(f"**Total Pipeline Value:** ${total_value}K")
        print()
        print("| Status | Count | Value |")
        print("|--------|-------|-------|")
        for status in sorted(status_counts.keys()):
            count = status_counts[status]
            value = status_values[status]
            print(f"| {status} | {count} | ${value}K |")
        print()
        print(f"**Response Rate:** {response_rate:.1f}% ({total_responded}/{total_sent})")
        print()

    else:  # text
        print("📊 PIPELINE SNAPSHOT")
        print("=" * 50)
        print()
        print(f"Total messages: {len(pipeline)}")
        print(f"Total value: ${total_value}K")
        print()
        print("By status:")
        for status in sorted(status_counts.keys()):
            count = status_counts[status]
            value = status_values[status]
            print(f"  {status:15} {count:3} messages | ${value:4}K")
        print()
        if total_sent > 0:
            print(f"Response rate: {response_rate:.1f}% ({total_responded}/{total_sent})")
        print()

        # Top 5 by value
        print("Top 5 by value:")
        top5 = sorted(pipeline, key=lambda m: m.get("pipeline_value", 0), reverse=True)[:5]
        for i, msg in enumerate(top5, 1):
            value = msg.get("pipeline_value", 0)
            prospect = msg.get("prospect", "Unknown")
            status = msg.get("status", "unknown")
            print(f"  {i}. {prospect:20} ${value:3}K ({status})")
        print()

def main():
    format = "text"
    if "--json" in sys.argv:
        format = "json"
    elif "--markdown" in sys.argv:
        format = "markdown"

    show_snapshot(format)

if __name__ == "__main__":
    main()
