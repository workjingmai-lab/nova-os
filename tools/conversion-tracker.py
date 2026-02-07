#!/usr/bin/env python3
"""
conversion-tracker.py — Track outreach conversion rates
Week 4: Optimize conversion, not just pipeline
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path

DATA_FILE = "data/conversions.json"

# Conversion funnel stages
STAGES = ["sent", "opened", "replied", "call_booked", "proposal_sent", "closed_won", "closed_lost"]

def init_data():
    """Initialize conversion data structure."""
    return {
        "version": "1.0",
        "last_updated": datetime.utcnow().isoformat(),
        "leads": [],
        "totals": {stage: 0 for stage in STAGES},
        "rates": {}
    }

def load_data():
    """Load conversion data from file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            return json.load(f)
    return init_data()

def save_data(data):
    """Save conversion data to file."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    data["last_updated"] = datetime.utcnow().isoformat()
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_lead(lead_id, name, source, value, message_type):
    """Add a new lead to tracking."""
    data = load_data()
    lead = {
        "id": lead_id,
        "name": name,
        "source": source,
        "value": value,
        "message_type": message_type,
        "stage": "sent",
        "sent_at": datetime.utcnow().isoformat(),
        "history": [{"stage": "sent", "at": datetime.utcnow().isoformat()}]
    }
    data["leads"].append(lead)
    data["totals"]["sent"] += 1
    save_data(data)
    print(f"✅ Added lead: {name} (${value:,})")

def update_stage(lead_id, new_stage):
    """Update lead to new stage."""
    if new_stage not in STAGES:
        print(f"❌ Invalid stage: {new_stage}")
        print(f"Valid stages: {', '.join(STAGES)}")
        return
    
    data = load_data()
    for lead in data["leads"]:
        if lead["id"] == lead_id:
            old_stage = lead["stage"]
            lead["stage"] = new_stage
            lead["history"].append({"stage": new_stage, "at": datetime.utcnow().isoformat()})
            data["totals"][new_stage] += 1
            save_data(data)
            print(f"🔄 {lead['name']}: {old_stage} → {new_stage}")
            return
    print(f"❌ Lead not found: {lead_id}")

def calculate_rates(data):
    """Calculate conversion rates between stages."""
    totals = data["totals"]
    rates = {}
    
    # Funnel rates
    if totals["sent"] > 0:
        rates["sent_to_replied"] = (totals["replied"] / totals["sent"]) * 100
        rates["sent_to_closed_won"] = (totals["closed_won"] / totals["sent"]) * 100
    
    if totals["replied"] > 0:
        rates["replied_to_call"] = (totals["call_booked"] / totals["replied"]) * 100
    
    if totals["call_booked"] > 0:
        rates["call_to_close"] = (totals["closed_won"] / totals["call_booked"]) * 100
    
    return rates

def show_status():
    """Display current conversion status."""
    data = load_data()
    rates = calculate_rates(data)
    
    print("=" * 50)
    print("📊 CONVERSION FUNNEL STATUS")
    print("=" * 50)
    print(f"Last updated: {data['last_updated'][:19]}")
    print()
    
    # Funnel visualization
    print("🔄 FUNNEL:")
    for stage in STAGES:
        count = data["totals"][stage]
        bar = "█" * count + "░" * (20 - min(count, 20))
        print(f"  {stage:15} │{bar}│ {count}")
    
    print()
    print("📈 CONVERSION RATES:")
    if "sent_to_replied" in rates:
        print(f"  Response rate:    {rates['sent_to_replied']:.1f}% (target: 10%+)")
    if "replied_to_call" in rates:
        print(f"  Call booked rate: {rates['replied_to_call']:.1f}%")
    if "call_to_close" in rates:
        print(f"  Close rate:       {rates['call_to_close']:.1f}% (target: 5%+)")
    
    print()
    print(f"💰 PIPELINE VALUE:")
    total_value = sum(l["value"] for l in data["leads"])
    won_value = sum(l["value"] for l in data["leads"] if l["stage"] == "closed_won")
    print(f"  Total sent:  ${total_value:,.0f}")
    print(f"  Closed won:  ${won_value:,.0f}")
    
    print()
    print("📋 RECENT LEADS:")
    for lead in data["leads"][-5:]:
        print(f"  {lead['name'][:20]:20} │ {lead['stage']:12} │ ${lead['value']:,.0f}")

def show_help():
    """Display help message."""
    print("""
conversion-tracker.py — Track outreach conversion rates

USAGE:
  python3 conversion-tracker.py status           Show funnel status
  python3 conversion-tracker.py add <id> <name> <source> <value> <type>
                                                 Add new lead
  python3 conversion-tracker.py update <id> <stage>
                                                 Update lead stage
  python3 conversion-tracker.py help             Show this help

STAGES:
  sent → opened → replied → call_booked → proposal_sent → closed_won/lost

EXAMPLES:
  python3 conversion-tracker.py add ef01 "EF Support" grant 40000 standard
  python3 conversion-tracker.py update ef01 replied
  python3 conversion-tracker.py update ef01 call_booked

TARGETS:
  Response rate: 10%+
  Close rate: 5%+
""")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        show_status()
    elif sys.argv[1] == "status":
        show_status()
    elif sys.argv[1] == "add" and len(sys.argv) >= 7:
        add_lead(sys.argv[2], sys.argv[3], sys.argv[4], float(sys.argv[5]), sys.argv[6])
    elif sys.argv[1] == "update" and len(sys.argv) >= 4:
        update_stage(sys.argv[2], sys.argv[3])
    else:
        show_help()
