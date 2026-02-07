#!/usr/bin/env python3
"""
Top Leads — Shows highest-value targets ready to send

Focus your execution on the biggest opportunities first.

Usage:
    python3 tools/top-leads.py
"""

import json
from pathlib import Path

PIPELINE_FILE = Path.home() / ".openclaw/workspace/data/revenue-pipeline.json"

def load_pipeline():
    with open(PIPELINE_FILE) as f:
        return json.load(f)

def get_ready_leads(pipeline):
    """Extract all leads with ready status."""
    ready_statuses = ["ready", "ready_to_submit", "messages_ready", "outreach-ready"]

    leads = []

    for category in ["grants", "services", "bounties"]:
        for item in pipeline.get(category, []):
            status = item.get("status", "lead")
            if status in ready_statuses:
                leads.append({
                    "name": item.get("name", "Unknown"),
                    "potential": item.get("potential", 0),
                    "status": status,
                    "category": category,
                    "file": item.get("notes", "").split("File: ")[-1].split(".")[0] if "File: " in item.get("notes", "") else None
                })

    # Sort by potential (descending)
    leads.sort(key=lambda x: x["potential"], reverse=True)

    return leads

def format_currency(amount):
    if amount >= 1_000_000:
        return f"${amount/1_000_000:.1f}M"
    elif amount >= 1_000:
        return f"${amount/1_000:.0f}K"
    return f"${amount:.0f}"

def main():
    pipeline = load_pipeline()
    leads = get_ready_leads(pipeline)

    print("\n" + "="*60)
    print("🎯 TOP LEADS — Ready to Send")
    print("="*60)

    if not leads:
        print("\n✅ No ready leads — all submitted or won!")
    else:
        total = sum(lead["potential"] for lead in leads)

        print(f"\n📊 {len(leads)} leads ready → {format_currency(total)} potential")
        print(f"💡 Focus on top 5 = {format_currency(sum(l['potential'] for l in leads[:5]))}\n")

        # Top 10 leads
        for i, lead in enumerate(leads[:10], 1):
            priority = "🔴 HIGH" if lead["potential"] >= 30_000 else "🟡 MEDIUM" if lead["potential"] >= 15_000 else "🟢 LOW"
            print(f"{i:2d}. {lead['name']:<30} {format_currency(lead['potential']):>8} {priority}")

        if len(leads) > 10:
            print(f"\n... and {len(leads) - 10} more leads")

    print("\n" + "="*60)
    print("📋 Quick Actions:")
    print("   1. Check messages: ls outreach/messages/")
    print("   2. Execute plan: cat ARTHUR-57-MIN-QUICK-REF.md")
    print("   3. Track status: python3 tools/execution-gap-visualizer.py")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
