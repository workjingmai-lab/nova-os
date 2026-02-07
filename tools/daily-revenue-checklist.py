#!/usr/bin/env python3
"""
daily-revenue-checklist.py — Automated daily revenue routine

Runs daily checks for revenue pipeline:
1. Pipeline status overview
2. Follow-ups due today
3. Leads needing attention
4. Moltbook engagement
5. Action items for the day

Usage: python3 tools/daily-revenue-checklist.py
       python3 tools/daily-revenue-checklist.py --quiet (just actions)
"""

import sys
import json
from datetime import datetime, timedelta

def print_header(text):
    print(f"\n{'='*60}")
    print(f"  {text}")
    print(f"{'='*60}")

def print_section(text):
    print(f"\n▶ {text}")
    print("-" * 50)

def check_pipeline():
    """Quick pipeline status"""
    print_section("PIPELINE STATUS")
    
    data = {
        "identified": 900000,
        "ready": 604500,
        "submitted": 5000,
        "won": 0
    }
    
    gap = data["ready"] - data["submitted"]
    
    print(f"  Total pipeline:    ${data['identified']/1000:.0f}K")
    print(f"  Ready to submit:   ${data['ready']/1000:.0f}K")
    print(f"  Submitted:         ${data['submitted']/1000:.0f}K")
    print(f"  Execution gap:     ${gap/1000:.0f}K ⚠️")
    
    if gap > 500000:
        print(f"\n  🔥 CRITICAL: $600K+ ready but not submitted")
        print(f"     Action: Arthur needs to execute 57-min plan")
    
    return gap

def check_followups():
    """Check for follow-ups due"""
    print_section("FOLLOW-UPS DUE")
    
    # Simulate follow-up data
    # In real implementation, would read from tracker
    leads = [
        {"name": "Ethereum Foundation", "priority": "HIGH", "days_since": 3, "next_touch": "Touch 2"},
        {"name": "Fireblocks", "priority": "HIGH", "days_since": 3, "next_touch": "Touch 2"},
        {"name": "Uniswap Foundation", "priority": "HIGH", "days_since": 3, "next_touch": "Touch 2"},
    ]
    
    due_count = 0
    for lead in leads:
        if lead["days_since"] >= 3:  # Touch 2 due after 3 days
            due_count += 1
            flag = "🔴" if lead["priority"] == "HIGH" else "🟡"
            print(f"  {flag} {lead['name']}: {lead['next_touch']} due (Day {lead['days_since']})")
    
    if due_count == 0:
        print("  ✓ No follow-ups due today")
    else:
        print(f"\n  ⚠️  {due_count} follow-ups need attention")
        print(f"     Run: python3 tools/follow-up-reminder.py")
    
    return due_count

def check_leads():
    """Check lead status"""
    print_section("LEAD PRIORITIES")
    
    leads = {
        "HIGH": {"count": 3, "value": 115000, "sent": 0},
        "MEDIUM": {"count": 10, "value": 127500, "sent": 0},
        "LOW": {"count": 26, "value": 0, "sent": 0}
    }
    
    total_ready = 13
    total_sent = 0
    
    for priority, data in leads.items():
        if data["count"] > data["sent"]:
            pending = data["count"] - data["sent"]
            flag = "🔴" if priority == "HIGH" else "🟡" if priority == "MEDIUM" else "🟢"
            print(f"  {flag} {priority}: {pending}/{data['count']} messages pending (${data['value']/1000:.0f}K)")
    
    if total_sent == 0:
        print(f"\n  ⚠️  ZERO messages sent out of {total_ready} ready")
        print(f"     Action: Send HIGH priority messages first (3 leads, $115K)")
    
    return total_ready - total_sent

def check_moltbook():
    """Check Moltbook status"""
    print_section("MOLTBOOK PRESENCE")
    
    # Simulate data
    posts_this_week = 0
    target = 3
    
    print(f"  Posts this week: {posts_this_week}/{target}")
    
    if posts_this_week < target:
        remaining = target - posts_this_week
        print(f"  📝 Need {remaining} more post(s) this week")
        print(f"     Queued posts available in content/")
    else:
        print(f"  ✓ Weekly target met")
    
    # Engagement
    print(f"\n  Engagement target: 5+ comments/week")
    print(f"  Action: Comment on 1-2 agent posts today")
    
    return posts_this_week

def get_today_actions():
    """Generate today's priority actions"""
    actions = []
    
    # Check if Arthur has executed
    if True:  # Would check actual status
        actions.append(("CRITICAL", "Arthur: Execute 57-min plan", "$632K", "57 min"))
    
    actions.append(("HIGH", "Review pipeline-viz.py output", "Visibility", "2 min"))
    actions.append(("MEDIUM", "Engage on Moltbook (1-2 comments)", "Presence", "5 min"))
    
    return actions

def main():
    quiet = "--quiet" in sys.argv
    
    if not quiet:
        now = datetime.utcnow()
        print_header(f"DAILY REVENUE CHECKLIST — {now.strftime('%A, %B %d')}")
        print(f"\n  Generated: {now.strftime('%H:%M')} UTC")
        print(f"  Week: {now.isocalendar()[1]} | Day: {now.strftime('%A')}")
    
    # Run checks
    gap = check_pipeline()
    due = check_followups()
    pending = check_leads()
    moltbook = check_moltbook()
    
    # Summary actions
    print_section("TODAY'S ACTIONS")
    
    actions = get_today_actions()
    
    for priority, action, value, time in actions:
        flag = "🔥" if priority == "CRITICAL" else "🎯" if priority == "HIGH" else "📋"
        print(f"  {flag} [{priority}] {action}")
        print(f"      Value: {value} | Time: {time}")
    
    if not quiet:
        print_header("SUMMARY")
        print(f"  Pipeline gap:    ${gap/1000:.0f}K needs submission")
        print(f"  Follow-ups due:  {due} today")
        print(f"  Leads pending:   {pending} messages ready")
        print(f"  Moltbook:        {moltbook}/3 posts this week")
        
        print(f"\n  💡 Quick commands:")
        print(f"     python3 tools/pipeline-viz.py")
        print(f"     python3 tools/lead-prioritizer.py")
        print(f"     cat ARTHUR-QUICK-REF.md")
    
    print()

if __name__ == "__main__":
    main()
