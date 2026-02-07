#!/usr/bin/env python3
"""
Daily Revenue Checklist — Work block 2169+
Prevents revenue leakage with daily checklist
Run: python3 tools/daily-revenue-checklist.py
"""

import json
import os
from datetime import datetime, timedelta

def load_json(path):
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return {}

def main():
    pipeline = load_json('data/revenue-pipeline.json')

    # Count by status
    ready_count = 0
    ready_value = 0
    submitted_count = 0
    submitted_value = 0
    follow_up_count = 0

    # Check services
    for item in pipeline.get('services', []):
        status = item.get('status', 'lead')
        potential = item.get('potential', 0)

        if status in ['ready', 'outreach-ready', 'messages_ready']:
            ready_count += 1
            ready_value += potential
        elif 'submitted' in status.lower():
            submitted_count += 1
            submitted_value += potential

        # Check follow-ups (last_contacted field)
        if item.get('last_contacted'):
            last_contacted = datetime.fromisoformat(item['last_contacted'].replace('Z', '+00:00'))
            days_since = (datetime.utcnow() - last_contacted).days
            if days_since >= 3:  # Follow-up due
                follow_up_count += 1

    # Check grants
    for item in pipeline.get('grants', []):
        status = item.get('status', 'lead')
        potential = item.get('potential', 0)

        if status == 'ready_to_submit':
            ready_count += 1
            ready_value += potential
        elif 'submitted' in status.lower():
            submitted_count += 1
            submitted_value += potential

    now = datetime.utcnow().strftime('%Y-%m-%d %H:%MZ')

    print(f"📋 DAILY REVENUE CHECKLIST — {now}")
    print("=" * 60)

    # Item 1: Send ready messages
    print(f"\n✅ 1. SEND READY MESSAGES ({ready_count} items, ${ready_value:,.0f})")
    if ready_count > 0:
        print(f"   Action: Run 'python3 tools/lead-prioritizer.py --status ready'")
        print(f"   Then: Copy messages from outreach/messages/ and send")
    else:
        print(f"   ✨ No messages waiting")

    # Item 2: Check due follow-ups
    print(f"\n✅ 2. CHECK DUE FOLLOW-UPS ({follow_up_count} need follow-up)")
    if follow_up_count > 0:
        print(f"   Action: Run 'python3 tools/follow-up-reminder.py'")
        print(f"   Why: 80% of deals close after 5th contact")
    else:
        print(f"   ✨ All caught up")

    # Item 3: Update submitted statuses
    print(f"\n✅ 3. UPDATE SUBMITTED STATUSES ({submitted_count} submitted)")
    if submitted_count > 0:
        print(f"   Action: Track responses, update pipeline")
        print(f"   Command: python3 tools/revenue-tracker.py update --status won --name 'Name'")
    else:
        print(f"   ℹ️  Nothing submitted yet")

    # Item 4: Clear blockers
    print(f"\n✅ 4. CLEAR BLOCKERS (if any)")
    bounties = pipeline.get('bounties', [])
    if bounties and any('browser' in b.get('notes', '').lower() for b in bounties):
        print(f"   ⚠️  Gateway restart needed: openclaw gateway restart")

    grants_ready = sum(g.get('potential', 0) for g in pipeline.get('grants', []) if g.get('status') == 'ready_to_submit')
    if grants_ready > 0:
        print(f"   ⚠️  GitHub auth needed: gh auth login")

    if not bounties and grants_ready == 0:
        print(f"   ✨ No blockers")

    # Item 5: Quick status check
    print(f"\n✅ 5. QUICK STATUS CHECK")
    print(f"   Action: python3 tools/quick-status.py")

    # Summary
    print(f"\n" + "=" * 60)
    print(f"🎯 DAILY SUMMARY:")
    print(f"   Ready to send: {ready_count} items (${ready_value:,.0f})")
    print(f"   Submitted: {submitted_count} items (${submitted_value:,.0f})")
    print(f"   Follow-ups due: {follow_up_count} items")

    if ready_value > 500000:
        print(f"\n   ⚠️  ${ready_value:,.0f} waiting to send!")
    elif ready_value > 100000:
        print(f"\n   ⚠️  ${ready_value:,.0f} ready to send")
    elif ready_value > 0:
        print(f"\n   💡 ${ready_value:,.0f} ready")

    print("\n💡 Remember: Revenue leakage = forgetting to follow up")
    print("=" * 60)

if __name__ == '__main__':
    main()
