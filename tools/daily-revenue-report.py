#!/usr/bin/env python3
"""
daily-revenue-report.py - Unified daily revenue report
Combines pipeline, ready leads, and conversion stats in one view.
"""

import subprocess
import json
from datetime import datetime

def run_tool(cmd):
    """Run a tool and return output."""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
        return result.stdout
    except:
        return f"Error running: {cmd}"

def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M UTC")
    
    print("=" * 60)
    print(f"📊 DAILY REVENUE REPORT — {now}")
    print("=" * 60)
    
    # Pipeline Summary
    print("\n💰 PIPELINE SUMMARY")
    print("─" * 40)
    try:
        with open("data/conversion-log.json") as f:
            data = json.load(f)
        leads = data["leads"]
        stats = data["stats"]
        
        total = sum(l["value"] for l in leads)
        ready = sum(l["value"] for l in leads if l["status"] == "ready")
        sent = sum(l["value"] for l in leads if l["status"] == "sent")
        won = sum(l.get("actual_value", l["value"]) for l in leads if l["status"] == "won")
        
        print(f"Total Pipeline:  ${total:,} ({len(leads)} leads)")
        print(f"Ready to Send:   ${ready:,}")
        print(f"Sent:            ${sent:,}")
        print(f"Won:             ${won:,}")
        print(f"")
        print(f"Response Rate:   {stats['total_responses']}/{stats['total_sent']} " + 
              f"({stats['total_responses']/max(stats['total_sent'],1)*100:.0f}%)")
        print(f"Win Rate:        {stats['total_won']}/{stats['total_sent']} " + 
              f"({stats['total_won']/max(stats['total_sent'],1)*100:.0f}%)")
    except:
        print("Run: python3 tools/conversion-tracker.py init-ready-leads")
    
    # Ready Leads Quick View
    print("\n🚀 READY TO SEND (Top 5)")
    print("─" * 40)
    try:
        ready_leads = [l for l in leads if l["status"] == "ready"]
        ready_leads.sort(key=lambda x: x["value"], reverse=True)
        for lead in ready_leads[:5]:
            roi = lead["value"] / 3
            print(f"#{lead['id']} {lead['name'][:25]:<25} ${lead['value']:,}  ({roi/1000:.0f}K/min)")
        if len(ready_leads) > 5:
            print(f"   ... and {len(ready_leads) - 5} more")
    except:
        pass
    
    # Today's Actions
    print("\n⚡ RECOMMENDED ACTIONS")
    print("─" * 40)
    print("1. Send top ready lead → python3 tools/send-ready-leads.py")
    print("2. Mark sent → python3 tools/conversion-tracker.py send <id>")
    print("3. Check follow-ups → python3 tools/conversion-tracker.py followups")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
