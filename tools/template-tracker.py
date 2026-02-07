#!/usr/bin/env python3
"""
template-tracker.py - Track follow-up template usage and effectiveness
Created: Work block 3060, 2026-02-07
"""

import json
import os
from datetime import datetime
from pathlib import Path

DATA_FILE = Path("data/template-usage.json")

TEMPLATE_SCENARIOS = {
    1: "No Response (Day 3)",
    2: "No Response (Day 7)",
    3: "Not Interested/No Budget",
    4: "Send More Info",
    5: "Interested - Let's Talk",
    6: "Using Competitor",
    7: "Forwarded to Teammate",
    8: "Too Expensive",
    9: "Not Right Person",
    10: "Delayed Response"
}

def load_data():
    """Load template usage data."""
    if DATA_FILE.exists():
        with open(DATA_FILE) as f:
            return json.load(f)
    return {"usages": [], "stats": {}}

def save_data(data):
    """Save template usage data."""
    DATA_FILE.parent.mkdir(exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def record_usage(lead_name: str, template_id: int, sent_date: str = None):
    """Record that a template was used."""
    data = load_data()
    usage = {
        "lead": lead_name,
        "template_id": template_id,
        "scenario": TEMPLATE_SCENARIOS.get(template_id, "Unknown"),
        "sent_date": sent_date or datetime.now().strftime("%Y-%m-%d"),
        "response": None,
        "outcome": None
    }
    data["usages"].append(usage)
    save_data(data)
    print(f"✓ Recorded: Template {template_id} used for {lead_name}")

def record_response(lead_name: str, responded: bool, outcome: str = None):
    """Record response to a template."""
    data = load_data()
    for usage in reversed(data["usages"]):
        if usage["lead"] == lead_name and usage["response"] is None:
            usage["response"] = responded
            usage["outcome"] = outcome
            save_data(data)
            status = "✓" if responded else "✗"
            print(f"{status} Updated: {lead_name} response recorded")
            return
    print(f"⚠ No open usage found for {lead_name}")

def get_stats():
    """Get template effectiveness stats."""
    data = load_data()
    stats = {}
    
    for template_id, scenario in TEMPLATE_SCENARIOS.items():
        usages = [u for u in data["usages"] if u["template_id"] == template_id]
        responses = [u for u in usages if u["response"]]
        
        stats[template_id] = {
            "scenario": scenario,
            "total_sent": len(usages),
            "responses": len(responses),
            "rate": len(responses) / len(usages) * 100 if usages else 0,
            "outcomes": [u["outcome"] for u in responses if u["outcome"]]
        }
    
    return stats

def print_summary():
    """Print template usage summary."""
    stats = get_stats()
    
    print("=" * 60)
    print("FOLLOW-UP TEMPLATE EFFECTIVENESS")
    print("=" * 60)
    
    total_sent = sum(s["total_sent"] for s in stats.values())
    total_responses = sum(s["responses"] for s in stats.values())
    overall_rate = total_responses / total_sent * 100 if total_sent else 0
    
    print(f"\nTotal Templates Sent: {total_sent}")
    print(f"Total Responses: {total_responses}")
    print(f"Overall Response Rate: {overall_rate:.1f}%")
    print()
    
    # Sort by response rate
    sorted_stats = sorted(stats.items(), key=lambda x: x[1]["rate"], reverse=True)
    
    print("By Template:")
    print("-" * 60)
    for tid, s in sorted_stats:
        if s["total_sent"] > 0:
            bar = "█" * int(s["rate"] / 10)
            print(f"  {tid:2d}. {s['scenario'][:25]:25} | {s['responses']:2d}/{s['total_sent']:2d} ({s['rate']:5.1f}%) {bar}")
    
    print()
    
    # Recent usages
    data = load_data()
    recent = data["usages"][-5:]
    if recent:
        print("Recent Activity:")
        print("-" * 60)
        for u in recent:
            status = "✓" if u["response"] else "⏳"
            print(f"  {status} {u['sent_date']} | {u['lead'][:20]:20} | {u['scenario'][:25]:25}")
    
    print("=" * 60)

def main():
    import sys
    
    if len(sys.argv) < 2:
        print_summary()
        return
    
    cmd = sys.argv[1]
    
    if cmd == "record" and len(sys.argv) >= 4:
        record_usage(sys.argv[2], int(sys.argv[3]), sys.argv[4] if len(sys.argv) > 4 else None)
    elif cmd == "response" and len(sys.argv) >= 3:
        responded = sys.argv[2].lower() in ("yes", "true", "1")
        outcome = sys.argv[3] if len(sys.argv) > 3 else None
        record_response(sys.argv[2], responded, outcome)
    elif cmd == "summary":
        print_summary()
    else:
        print("Usage:")
        print("  python3 template-tracker.py                    # Show summary")
        print("  python3 template-tracker.py record <lead> <template_id> [date]")
        print("  python3 template-tracker.py response <lead> <yes/no> [outcome]")

if __name__ == "__main__":
    main()
