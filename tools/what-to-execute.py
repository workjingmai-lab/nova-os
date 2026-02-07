#!/usr/bin/env python3
"""
What To Execute — Show Arthur exactly what to do next.

Displays:
1. Blocked items (technical blockers Arthur can fix)
2. Ready items (revenue awaiting execution)
3. Time + ROI for each action

Usage:
    python3 what-to-execute.py

Created: 2026-02-07 (Work block 3217)
"""

import json
from pathlib import Path

PIPELINE_FILE = "/home/node/.openclaw/workspace/revenue-pipeline.json"

def main():
    print("🎯 WHAT TO EXECUTE — Arthur's Action List")
    print("=" * 60)

    # Load pipeline
    with open(PIPELINE_FILE, 'r') as f:
        data = json.load(f)

    print("\n🚧 BLOCKERS (Technical — Arthur fixes these)\n")

    # Bounties blocker
    for bounty in data.get('bounties', []):
        if bounty.get('status') == 'blocked':
            blocker = bounty.get('blocker', 'unknown')
            amount = bounty.get('amount', 0)
            print(f"• {bounty['name']}")
            print(f"  Blocker: {blocker}")
            print(f"  Value: ${amount:,.0f}")
            print(f"  Fix: Gateway restart (openclaw gateway restart)")
            print(f"  Time: 1 min")
            print(f"  ROI: ${amount:,.0f}/min\n")

    print("\n✅ READY TO EXECUTE (Revenue waiting for Arthur)\n")

    # Services ready
    services_ready = [s for s in data.get('services', []) if s.get('status') == 'ready']
    services_total = sum(s.get('potential', 0) for s in services_ready)

    # Grants ready
    grants_ready = [g for g in data.get('grants', []) if g.get('status') == 'ready']
    grants_total = sum(g.get('amount', 0) for g in grants_ready)

    print(f"📨 Services: {len(services_ready)} leads ready, ${services_total:,.0f} total")
    print(f"   Execute: bash tools/send-everything.sh")
    print(f"   Time: ~20 min")
    print(f"   ROI: ${services_total/20:,.0f}/min\n")

    print(f"📝 Grants: {len(grants_ready)} ready, ${grants_total:,.0f} total")
    print(f"   Execute: python3 tools/grant-submit-helper.py")
    print(f"   Blocker: GitHub CLI auth (run: gh auth login)")
    print(f"   Time: 5 min (auth) + 15 min (submit)")
    print(f"   ROI: ${grants_total/20:,.0f}/min\n")

    print("=" * 60)
    print(f"TOTAL BLOCKER VALUE: ${grants_total + data.get('bounties', [{}])[0].get('amount', 0):,.0f}")
    print(f"TOTAL READY VALUE: ${services_total + grants_total:,.0f}")
    print(f"TOTAL TIME: ~26 min (1 + 5 + 20)")
    print(f"TOTAL ROI: ${(services_total + grants_total + data.get('bounties', [{}])[0].get('amount', 0)) / 26:,.0f}/min")

if __name__ == '__main__':
    main()
