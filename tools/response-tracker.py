#!/usr/bin/env python3
"""
Response Tracker — Track sent messages and conversion rates

Tracks the journey from: Sent → Response → Call → Won/Lost

Usage:
    python3 tools/response-tracker.py status          # Show conversion funnel
    python3 tools/response-tracker.py add             # Add new response
    python3 tools/response-tracker.py list            # List all responses
    python3 tools/response-tracker.py export          # Export to JSON
"""

import json
import os
from datetime import datetime
from pathlib import Path

TRACKER_FILE = "/home/node/.openclaw/workspace/conversion-funnel.json"

def load_tracker():
    """Load conversion funnel data"""
    if os.path.exists(TRACKER_FILE):
        with open(TRACKER_FILE, 'r') as f:
            return json.load(f)
    return {
        "created": datetime.now().isoformat(),
        "lastUpdated": datetime.now().isoformat(),
        "funnel": {
            "sent": 0,
            "responses": 0,
            "calls": 0,
            "won": 0,
            "lost": 0
        },
        "responses": []
    }

def save_tracker(data):
    """Save conversion funnel data"""
    data["lastUpdated"] = datetime.now().isoformat()
    with open(TRACKER_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def show_status():
    """Show conversion funnel status"""
    data = load_tracker()
    funnel = data["funnel"]

    print("\n📊 Conversion Funnel Status")
    print("=" * 50)

    # Calculate rates
    response_rate = (funnel["responses"] / funnel["sent"] * 100) if funnel["sent"] > 0 else 0
    call_rate = (funnel["calls"] / funnel["responses"] * 100) if funnel["responses"] > 0 else 0
    close_rate = (funnel["won"] / funnel["calls"] * 100) if funnel["calls"] > 0 else 0
    overall_rate = (funnel["won"] / funnel["sent"] * 100) if funnel["sent"] > 0 else 0

    print(f"📤 Sent:        {funnel['sent']:>6} messages")
    print(f"💬 Responses:   {funnel['responses']:>6} ({response_rate:.1f}%)")
    print(f"📞 Calls:       {funnel['calls']:>6} ({call_rate:.1f}% of responses)")
    print(f"✅ Won:         {funnel['won']:>6} (${funnel['won'] * 10000:>10,} est.)")  # Avg $10K/deal
    print(f"❌ Lost:        {funnel['lost']:>6}")
    print()
    print(f"📈 Conversion Rates:")
    print(f"   Response rate:  {response_rate:.1f}%")
    print(f"   Call rate:      {call_rate:.1f}%")
    print(f"   Close rate:     {close_rate:.1f}%")
    print(f"   Overall rate:   {overall_rate:.1f}%")
    print()

    # Pipeline value
    if funnel["sent"] > 0:
        pipeline_value = funnel["sent"] * 25000  # Avg $25K per message
        print(f"💰 Pipeline value: ${pipeline_value:>10,}")
        print(f"💵 Revenue won:    ${funnel['won'] * 10000:>10,}")
        print(f"📊 Gap:            ${pipeline_value - (funnel['won'] * 10000):>10,}")

def add_response():
    """Add a new response"""
    print("\n📝 Add New Response")
    print("-" * 50)

    target = input("Target organization: ").strip()
    stage = input("Stage (response/call/won/lost): ").strip().lower()
    value = input("Deal value ($): ").strip() if stage in ["won", "lost"] else "0"
    notes = input("Notes: ").strip()

    response = {
        "target": target,
        "stage": stage,
        "value": int(value) if value.isdigit() else 0,
        "notes": notes,
        "timestamp": datetime.now().isoformat()
    }

    data = load_tracker()
    data["responses"].append(response)

    # Update funnel counts
    if stage == "response":
        data["funnel"]["responses"] += 1
    elif stage == "call":
        data["funnel"]["calls"] += 1
    elif stage == "won":
        data["funnel"]["won"] += 1
    elif stage == "lost":
        data["funnel"]["lost"] += 1

    save_tracker(data)
    print(f"\n✅ Response added: {target} → {stage}")

def list_responses():
    """List all responses"""
    data = load_tracker()
    responses = data["responses"]

    if not responses:
        print("\n📭 No responses yet")
        return

    print(f"\n📋 All Responses ({len(responses)} total)")
    print("=" * 50)

    for resp in reversed(responses[-20:]):  # Show last 20
        date = datetime.fromisoformat(resp["timestamp"]).strftime("%Y-%m-%d")
        emoji = {"response": "💬", "call": "📞", "won": "✅", "lost": "❌"}.get(resp["stage"], "📌")
        print(f"{emoji} {date} | {resp['target']:<30} | {resp['stage']}")
        if resp.get("notes"):
            print(f"   └─ {resp['notes']}")
        if resp.get("value", 0) > 0:
            print(f"   └─ Value: ${resp['value']:,}")

def export_data():
    """Export to JSON"""
    data = load_tracker()
    export_file = "/home/node/.openclaw/workspace/conversion-funnel-export.json"

    with open(export_file, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\n📤 Exported to: {export_file}")

def main():
    import sys

    if len(sys.argv) < 2:
        show_status()
        return

    command = sys.argv[1]

    if command == "status":
        show_status()
    elif command == "add":
        add_response()
    elif command == "list":
        list_responses()
    elif command == "export":
        export_data()
    else:
        print(f"Unknown command: {command}")
        print("Usage: response-tracker.py [status|add|list|export]")

if __name__ == "__main__":
    main()
