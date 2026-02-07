#!/usr/bin/env python3
"""
send-ready-leads.py - Prepare outreach sends for ready leads
Generates message previews and send commands for highest-ROI leads.
"""

import json
from datetime import datetime

# Ready leads from execution-gap analysis
READY_LEADS = [
    {"name": "Additional Leads (Various)", "value": 152000, "priority": 1, "type": "MIXED"},
    {"name": "DAO Leads (Compound/Aave)", "value": 127500, "priority": 2, "type": "DAO"},
    {"name": "Ethereum Foundation", "value": 40000, "priority": 3, "type": "GRANT"},
    {"name": "Fireblocks", "value": 35000, "priority": 4, "type": "SERVICE"},
    {"name": "Balancer Labs", "value": 20000, "priority": 5, "type": "SERVICE"},
    {"name": "Curve Finance", "value": 20000, "priority": 6, "type": "SERVICE"},
    {"name": "Yearn Finance", "value": 25000, "priority": 7, "type": "SERVICE"},
    {"name": "Lido Finance", "value": 15000, "priority": 8, "type": "SERVICE"},
    {"name": "Gitcoin", "value": 5000, "priority": 9, "type": "GRANT", "status": "submitted"},
]

def format_currency(value):
    if value >= 1000000:
        return f"${value/1000000:.1f}M"
    elif value >= 1000:
        return f"${value/1000:.0f}K"
    return f"${value}"

def show_ready_leads():
    """Display ready leads with send preparation."""
    print("=" * 60)
    print("🚀 READY LEADS — Send Preparation")
    print("=" * 60)
    
    ready = [l for l in READY_LEADS if l.get("status") != "submitted"]
    total = sum(l["value"] for l in ready)
    
    print(f"\n📊 Summary: {len(ready)} leads ready, {format_currency(total)} total value\n")
    
    for lead in ready:
        roi_per_min = lead["value"] / 3  # Assume 3 min per send
        print(f"\n{'─' * 50}")
        print(f"#{lead['priority']} {lead['name']}")
        print(f"   Value: {format_currency(lead['value'])} | Type: {lead['type']}")
        print(f"   ROI: {format_currency(roi_per_min)}/min")
        
        # Message preview based on type
        if lead['type'] == 'DAO':
            preview = "GM [Name] — Noticed [DAO] has [specific pain]. Built automation for [similar org] that saved [outcome]. Quick 5-min chat?"
        elif lead['type'] == 'GRANT':
            preview = "Hi [Name], submitting [specific grant] for [specific project]. Aligns with [their mission]. Happy to discuss?"
        elif lead['type'] == 'SERVICE':
            preview = "Hi [Name], saw [recent news/pain point]. Helped [similar co] automate [specific process] → [specific outcome]. Worth a brief chat?"
        else:
            preview = "Hi [Name], researched [company] — [specific insight]. Built solution for [similar situation]. Quick convo?"
        
        print(f"\n   💬 Preview: {preview}")
        print(f"   📁 Message file: outreach/{lead['name'].lower().replace(' ', '-')}.md")
    
    print(f"\n{'=' * 60}")
    print(f"⚡ Total: {len(ready)} sends, ~{len(ready) * 3} minutes")
    print(f"💰 Value: {format_currency(total)} | ROI: {format_currency(total/(len(ready)*3))}/min")
    print(f"🎯 Conversion scenarios:")
    print(f"   5% response rate → {format_currency(total * 0.05)} potential")
    print(f"   10% response rate → {format_currency(total * 0.10)} potential")
    print(f"   20% response rate → {format_currency(total * 0.20)} potential")
    print("=" * 60)

def generate_send_checklist():
    """Generate actionable checklist."""
    print("\n📋 SEND CHECKLIST")
    print("─" * 40)
    ready = [l for l in READY_LEADS if l.get("status") != "submitted"]
    
    for lead in ready:
        status = "[ ]"  # Unchecked
        print(f"{status} {lead['name']} ({format_currency(lead['value'])})")
    
    print(f"\nProgress: 0/{len(ready)} complete")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "checklist":
        generate_send_checklist()
    else:
        show_ready_leads()
