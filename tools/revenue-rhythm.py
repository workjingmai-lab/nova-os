#!/usr/bin/env python3
"""
revenue-rhythm.py — Daily revenue execution tracker
Quick status + next action for maintaining revenue momentum.
"""

import json
from datetime import datetime

PIPELINE_FILE = "revenue-pipeline.json"

def load_pipeline():
    try:
        with open(PIPELINE_FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def main():
    data = load_pipeline()
    if not data:
        print("No pipeline data found.")
        return

    grants = data.get("grants", [])
    services = data.get("services", [])
    bounties = data.get("bounties", [])
    meta = data.get("meta", {})

    # Calculations
    grants_submitted = sum(g["amount"] for g in grants if g["status"] == "submitted")
    grants_ready = sum(g["amount"] for g in grants if g["status"] == "ready")
    services_ready = sum(s["potential"] for s in services if s["status"] == "ready")
    high_priority = sum(s["potential"] for s in services if s["status"] == "ready" and s.get("priority") == "HIGH")
    
    total = grants_submitted + grants_ready + services_ready

    print("═" * 50)
    print(f"💰 REVENUE RHYTHM — {datetime.now().strftime('%Y-%m-%d %H:%M')} UTC")
    print("═" * 50)
    print(f"\n📊 PIPELINE STATUS")
    print(f"   Total Potential:  ${total:>10,}")
    print(f"   ─────────────────────────")
    print(f"   Grants Submitted: ${grants_submitted:>10,}")
    print(f"   Grants Ready:     ${grants_ready:>10,}")
    print(f"   Services Ready:   ${services_ready:>10,}")
    print(f"   └─ HIGH Priority: ${high_priority:>10,}")
    
    print(f"\n🎯 TODAY'S ACTIONS")
    if grants_ready > 0:
        ready_grants = [g["name"] for g in grants if g["status"] == "ready"]
        print(f"   Submit: {', '.join(ready_grants[:2])}")
    if high_priority > 0:
        high_svc = [s["name"] for s in services if s["status"] == "ready" and s.get("priority") == "HIGH"]
        print(f"   Contact: {', '.join(high_svc[:2])}")
    
    print(f"\n⏱️  TIME TO $100K: ~{100000 // 9684} minutes of focused execution")
    print("═" * 50)

if __name__ == "__main__":
    main()
