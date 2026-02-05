#!/usr/bin/env python3
"""
now.py — Quick status dashboard (1 second overview)

Shows current pipeline, work blocks, execution gap, and next actions.
Passes the 30-second test: run it, understand it, know what to do.
"""

import json
from pathlib import Path
from datetime import datetime

def load_json(path):
    """Load JSON file safely."""
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except:
        return None

def main():
    print("\n" + "="*60)
    print(" NOVA STATUS DASHBOARD")
    print("="*60)

    # Work blocks from today.md
    today_path = Path("/home/node/.openclaw/workspace/today.md")
    if today_path.exists():
        content = today_path.read_text()
        for line in content.split('\n')[:20]:
            if 'Work blocks:' in line:
                print(f"\n📊 {line.strip()}")
                break

    # Pipeline from revenue-pipeline.json
    pipeline = load_json("/home/node/.openclaw/workspace/data/revenue-pipeline.json")
    if pipeline:
        total = sum(item.get('potential', 0) for item in pipeline.get('services', []))
        total += sum(item.get('potential', 0) for item in pipeline.get('grants', []))
        total += sum(item.get('potential', 0) for item in pipeline.get('bounties', []))
        print(f"💰 Pipeline: ${total:,.0f} total")

    # Execution gap
    gap = load_json("/home/node/.openclaw/workspace/data/execution-gap.json")
    if gap:
        ready = gap.get('potential', 0)
        submitted = gap.get('kinetic', 0)
        gap_pct = gap.get('gap_percent', 100)
        print(f"⚠️  Execution Gap: ${ready:,.0f} ready, ${submitted:,.0f} submitted ({gap_pct}% gap)")

    # Next actions
    print("\n🎯 NEXT ACTIONS:")
    print("   1. Check gap cost: python3 tools/gap-cost-ticker.py")
    print("   2. Gateway restart (1 min → $50K)")
    print("   3. GitHub auth (5 min → $130K)")
    print("   4. Send top 10 services (10 min → $305K)")
    print(f"\n📅 Timestamp: {datetime.utcnow().strftime('%Y-%m-%d %H:%MZ')}")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
