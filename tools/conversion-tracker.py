#!/usr/bin/env python3
"""
conversion-tracker.py - Track outreach responses and conversion rates
Logs sent messages, responses, and outcomes with follow-up automation.
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path

CONVERSION_FILE = Path(__file__).parent.parent / "data" / "conversion-log.json"

def ensure_data_dir():
    CONVERSION_FILE.parent.mkdir(parents=True, exist_ok=True)

def load_conversions():
    if CONVERSION_FILE.exists():
        with open(CONVERSION_FILE) as f:
            return json.load(f)
    return {"leads": [], "stats": {"total_sent": 0, "total_responses": 0, "total_won": 0}}

def save_conversions(data):
    ensure_data_dir()
    with open(CONVERSION_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def add_lead(name, value, channel="email"):
    """Add a new lead to track."""
    data = load_conversions()
    lead = {
        "id": len(data["leads"]) + 1,
        "name": name,
        "value": value,
        "channel": channel,
        "status": "ready",  # ready → sent → responded → called → won/lost
        "sent_at": None,
        "responded_at": None,
        "follow_up_count": 0,
        "notes": ""
    }
    data["leads"].append(lead)
    save_conversions(data)
    print(f"✅ Added lead: {name} ({value})")

def send_lead(lead_id):
    """Mark lead as sent."""
    data = load_conversions()
    for lead in data["leads"]:
        if lead["id"] == lead_id:
            lead["status"] = "sent"
            lead["sent_at"] = datetime.now().isoformat()
            data["stats"]["total_sent"] += 1
            save_conversions(data)
            print(f"📤 Marked sent: {lead['name']}")
            return
    print(f"❌ Lead {lead_id} not found")

def respond_lead(lead_id):
    """Mark lead as responded."""
    data = load_conversions()
    for lead in data["leads"]:
        if lead["id"] == lead_id:
            lead["status"] = "responded"
            lead["responded_at"] = datetime.now().isoformat()
            data["stats"]["total_responses"] += 1
            save_conversions(data)
            print(f"💬 Marked responded: {lead['name']}")
            return
    print(f"❌ Lead {lead_id} not found")

def win_lead(lead_id, actual_value=None):
    """Mark lead as won."""
    data = load_conversions()
    for lead in data["leads"]:
        if lead["id"] == lead_id:
            lead["status"] = "won"
            lead["actual_value"] = actual_value or lead["value"]
            data["stats"]["total_won"] += 1
            save_conversions(data)
            print(f"🎉 Marked WON: {lead['name']} (${actual_value or lead['value']})")
            return
    print(f"❌ Lead {lead_id} not found")

def show_stats():
    """Display conversion statistics."""
    data = load_conversions()
    stats = data["stats"]
    leads = data["leads"]
    
    total_value = sum(l["value"] for l in leads)
    won_value = sum(l.get("actual_value", l["value"]) for l in leads if l["status"] == "won")
    
    response_rate = (stats["total_responses"] / stats["total_sent"] * 100) if stats["total_sent"] else 0
    win_rate = (stats["total_won"] / stats["total_sent"] * 100) if stats["total_sent"] else 0
    
    print("=" * 50)
    print("📊 CONVERSION STATS")
    print("=" * 50)
    print(f"Total Leads: {len(leads)}")
    print(f"Total Pipeline: ${total_value:,}")
    print(f"")
    print(f"Sent: {stats['total_sent']}")
    print(f"Responses: {stats['total_responses']} ({response_rate:.1f}%)")
    print(f"Won: {stats['total_won']} ({win_rate:.1f}%)")
    print(f"")
    print(f"Revenue Won: ${won_value:,}")
    print(f"Conversion Rate: {win_rate:.1f}%")
    print("=" * 50)

def show_followups():
    """Show leads needing follow-up."""
    data = load_conversions()
    now = datetime.now()
    
    needs_followup = []
    for lead in data["leads"]:
        if lead["status"] == "sent" and lead["sent_at"]:
            sent_time = datetime.fromisoformat(lead["sent_at"])
            days_since = (now - sent_time).days
            if days_since >= 3 and lead["follow_up_count"] < 2:
                needs_followup.append({**lead, "days_since": days_since})
    
    if not needs_followup:
        print("✅ No follow-ups needed")
        return
    
    print("📋 FOLLOW-UP NEEDED")
    print("─" * 40)
    for lead in needs_followup:
        print(f"#{lead['id']} {lead['name']} ({lead['days_since']} days)")

def list_leads():
    """List all leads with status."""
    data = load_conversions()
    print("📋 ALL LEADS")
    print("─" * 50)
    for lead in data["leads"]:
        status_emoji = {
            "ready": "⏳", "sent": "📤", "responded": "💬",
            "called": "📞", "won": "🎉", "lost": "❌"
        }.get(lead["status"], "❓")
        print(f"#{lead['id']} {status_emoji} {lead['name']} — {lead['status']} (${lead['value']:,})")

def init_ready_leads():
    """Batch load the 8 ready leads into tracking."""
    ready_leads = [
        ("Additional Leads (Various)", 152000, "mixed"),
        ("DAO Leads (Compound/Aave)", 127500, "dao"),
        ("Ethereum Foundation", 40000, "grant"),
        ("Fireblocks", 35000, "service"),
        ("Balancer Labs", 20000, "service"),
        ("Curve Finance", 20000, "service"),
        ("Yearn Finance", 25000, "service"),
        ("Lido Finance", 15000, "service"),
    ]
    
    data = load_conversions()
    existing_names = {l["name"] for l in data["leads"]}
    
    added = 0
    for name, value, channel in ready_leads:
        if name not in existing_names:
            lead = {
                "id": len(data["leads"]) + 1,
                "name": name,
                "value": value,
                "channel": channel,
                "status": "ready",
                "sent_at": None,
                "responded_at": None,
                "follow_up_count": 0,
                "notes": ""
            }
            data["leads"].append(lead)
            added += 1
    
    save_conversions(data)
    total_value = sum(v for _, v, _ in ready_leads)
    print(f"✅ Loaded {added} ready leads (${total_value:,} total)")
    print(f"   Run: python3 tools/conversion-tracker.py list")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        show_stats()
        print()
        list_leads()
        print()
        show_followups()
    elif sys.argv[1] == "add":
        add_lead(sys.argv[2], int(sys.argv[3]), sys.argv[4] if len(sys.argv) > 4 else "email")
    elif sys.argv[1] == "send":
        send_lead(int(sys.argv[2]))
    elif sys.argv[1] == "respond":
        respond_lead(int(sys.argv[2]))
    elif sys.argv[1] == "win":
        win_lead(int(sys.argv[2]), int(sys.argv[3]) if len(sys.argv) > 3 else None)
    elif sys.argv[1] == "followups":
        show_followups()
    elif sys.argv[1] == "list":
        list_leads()
    elif sys.argv[1] == "init-ready-leads":
        init_ready_leads()
