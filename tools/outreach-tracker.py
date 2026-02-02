#!/usr/bin/env python3
"""
Outreach Tracker — Track leads, outreach, and conversions for Nova's service business
Created: 2026-02-02 (Work Block 455)
Usage: python3 tools/outreach-tracker.py [list|add|update|stats]
"""

import json
import sys
from datetime import datetime
from pathlib import Path

TRACKER_FILE = "grants/outreach-tracker.json"

def load_data():
    """Load outreach data from JSON file"""
    path = Path(TRACKER_FILE)
    if path.exists():
        with open(path, 'r') as f:
            return json.load(f)
    return {"leads": [], "stats": {"total_leads": 0, "outreach_sent": 0, "responses": 0, "calls": 0, "closed": 0}}

def save_data(data):
    """Save outreach data to JSON file"""
    with open(TRACKER_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def list_leads(data):
    """List all leads with status"""
    if not data["leads"]:
        print("📋 No leads tracked yet.")
        return
    
    print(f"\n📋 OUTREACH LEADS ({len(data['leads'])} total)")
    print("=" * 80)
    
    for i, lead in enumerate(data["leads"], 1):
        status_emoji = {
            "identified": "🎯",
            "contacted": "📧",
            "responded": "💬",
            "call_booked": "📞",
            "closed": "💰",
            "lost": "❌"
        }.get(lead["status"], "❓")
        
        print(f"\n{i}. {status_emoji} {lead['name']} ({lead['company']})")
        print(f"   Market: {lead['market']}")
        print(f"   Status: {lead['status']}")
        print(f"   Added: {lead.get('added_date', 'Unknown')}")
        
        if lead.get('outreach_date'):
            print(f"   Outreach: {lead['outreach_date']}")
        if lead.get('response_date'):
            print(f"   Response: {lead['response_date']} ({lead.get('response_type', 'N/A')})")
        if lead.get('notes'):
            print(f"   Notes: {lead['notes']}")

def add_lead(data, name, company, market, pain_point=""):
    """Add a new lead"""
    lead = {
        "name": name,
        "company": company,
        "market": market,
        "pain_point": pain_point,
        "status": "identified",
        "added_date": datetime.now().isoformat(),
        "outreach_date": None,
        "response_date": None,
        "response_type": None,
        "notes": ""
    }
    
    data["leads"].append(lead)
    data["stats"]["total_leads"] += 1
    save_data(data)
    print(f"✅ Lead added: {name} ({company}) - {market}")

def update_lead(data, lead_index, **kwargs):
    """Update lead status or fields"""
    if lead_index < 1 or lead_index > len(data["leads"]):
        print(f"❌ Invalid lead index: {lead_index}")
        return
    
    lead = data["leads"][lead_index - 1]
    
    for key, value in kwargs.items():
        if value and value.lower() != "none":
            lead[key] = value
            if key == "status":
                # Update stats
                if value == "contacted":
                    data["stats"]["outreach_sent"] += 1
                    lead["outreach_date"] = datetime.now().isoformat()
                elif value == "responded":
                    data["stats"]["responses"] += 1
                    lead["response_date"] = datetime.now().isoformat()
                elif value == "call_booked":
                    data["stats"]["calls"] += 1
                elif value == "closed":
                    data["stats"]["closed"] += 1
    
    save_data(data)
    print(f"✅ Updated lead: {lead['name']} → Status: {lead['status']}")

def show_stats(data):
    """Show outreach statistics"""
    stats = data["stats"]
    total = stats["total_leads"]
    
    print("\n📊 OUTREACH STATISTICS")
    print("=" * 40)
    print(f"Total Leads:        {total}")
    
    if total > 0:
        print(f"Outreach Sent:      {stats['outreach_sent']} ({stats['outreach_sent']/total*100:.1f}%)")
    else:
        print(f"Outreach Sent:      {stats['outreach_sent']} (N/A)")
    
    if stats['outreach_sent'] > 0:
        print(f"Responses:          {stats['responses']} ({stats['responses']/stats['outreach_sent']*100:.1f}%)")
    else:
        print(f"Responses:          {stats['responses']} (N/A)")
    
    print(f"Calls Booked:       {stats['calls']}")
    print(f"Closed Deals:       {stats['closed']}")
    print()
    
    # Goal tracking
    print("🎯 WEEK 3-4 GOAL TRACKING")
    print("-" * 40)
    print(f"Leads (target 20):     {total}/20 ({total/20*100:.0f}%)")
    print(f"Responses (target 4):  {stats['responses']}/4 ({stats['responses']/4*100:.0f}%)")
    print(f"Calls (target 3):      {stats['calls']}/3 ({stats['calls']/3*100:.0f}%)")
    print(f"Closed (target 1):     {stats['closed']}/1 ({stats['closed']*100:.0f}%)")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 tools/outreach-tracker.py [list|add|update|stats]")
        print("\nExamples:")
        print("  python3 tools/outreach-tracker.py list")
        print("  python3 tools/outreach-tracker.py add 'John Doe' 'Acme Inc' 'Web3' 'Needs community agent'")
        print("  python3 tools/outreach-tracker.py update 1 --status contacted --notes 'Sent email via template 1'")
        print("  python3 tools/outreach-tracker.py stats")
        sys.exit(1)
    
    command = sys.argv[1].lower()
    data = load_data()
    
    if command == "list":
        list_leads(data)
    
    elif command == "add":
        if len(sys.argv) < 5:
            print("Usage: python3 tools/outreach-tracker.py add 'Name' 'Company' 'Market' [PainPoint]")
            sys.exit(1)
        add_lead(data, sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5] if len(sys.argv) > 5 else "")
    
    elif command == "update":
        if len(sys.argv) < 3:
            print("Usage: python3 tools/outreach-tracker.py update <index> [--status STATUS] [--notes NOTES]")
            sys.exit(1)
        
        kwargs = {}
        for i in range(3, len(sys.argv)):
            if sys.argv[i].startswith("--"):
                key = sys.argv[i][2:]
                value = sys.argv[i+1] if i+1 < len(sys.argv) else ""
                kwargs[key] = value
        
        update_lead(data, int(sys.argv[2]), **kwargs)
    
    elif command == "stats":
        show_stats(data)
    
    else:
        print(f"❌ Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()
