#!/usr/bin/env python3
"""
Gap Reminder — Shows what you're leaving on the table

Run this daily to remind yourself of the execution gap.

Usage:
    python3 gap-reminder.py
"""

import json
from pathlib import Path
from datetime import datetime

PIPELINE_FILE = Path.home() / ".openclaw/workspace/data/revenue-pipeline.json"

def load_pipeline():
    with open(PIPELINE_FILE) as f:
        return json.load(f)

def calculate_gap():
    pipeline = load_pipeline()

    total = 0
    ready = 0
    submitted = 0

    for category in ["grants", "services", "bounties"]:
        for item in pipeline.get(category, []):
            potential = item.get("potential", 0)
            status = item.get("status", "lead")
            total += potential

            if status in ["ready", "ready_to_submit", "messages_ready", "outreach-ready"]:
                ready += potential
            elif status == "submitted":
                submitted += potential
                ready += potential

    gap = ready - submitted

    return {
        "total": total,
        "ready": ready,
        "submitted": submitted,
        "gap": gap
    }

def main():
    metrics = calculate_gap()

    print("\n" + "="*60)
    print("⏰ " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " UTC")
    print("="*60)

    print(f"\n💰 You have ${metrics['ready']:,.0f} ready to send.")
    print(f"📤 You've only sent ${metrics['submitted']:,.0f}.")
    print(f"\n🚨 ** You're leaving ${metrics['gap']:,.0f} on the table. **")

    if metrics['gap'] > 500_000:
        print(f"\n⚠️  At $10K/min, that's {metrics['gap']/10000:.0f} minutes of work.")
        print(f"⚠️  Why haven't you hit send yet?")
    elif metrics['gap'] > 100_000:
        print(f"\n📈 At $10K/min, that's {metrics['gap']/10000:.0f} minutes to close the gap.")
        print(f"📈 What are you waiting for?")
    else:
        print(f"\n✅ Gap is manageable. Keep executing.")

    print(f"\n💡 Reminder: Execution beats planning every time.")
    print(f"💡 Hit send. Then optimize.")

    # Action items
    print(f"\n📋 Quick wins:")
    print(f"   1. Run: python3 tools/execution-gap-visualizer.py")
    print(f"   2. Check: outreach/messages/ for ready messages")
    print(f"   3. Execute: ARTHUR-57-MIN-QUICK-REF.md")

    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    main()
