#!/usr/bin/env python3
"""
Follow-Up Reminder Tool

Scans revenue-pipeline.json for items needing follow-up based on days since submission.
Generates action reminders with template suggestions.

Usage:
    python3 follow-up-reminder.py
"""

import json
from datetime import datetime, timedelta
from pathlib import Path

def load_pipeline():
    """Load revenue pipeline from JSON."""
    pipeline_path = Path.home() / ".openclaw/workspace/revenue-pipeline.json"
    
    if not pipeline_path.exists():
        print("❌ revenue-pipeline.json not found")
        print("   Run: python3 revenue-tracker.py add services --name 'Test' --potential 1000 --status 'ready'")
        return None
    
    with open(pipeline_path, 'r') as f:
        return json.load(f)

def days_since(date_str):
    """Calculate days since a date string (YYYY-MM-DD)."""
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d')
        return (datetime.now() - date).days
    except (ValueError, TypeError):
        return None

def check_followups(pipeline):
    """Scan pipeline for items needing follow-up."""
    reminders = []
    
    for category in ['grants', 'services', 'bounties']:
        if category not in pipeline:
            continue
        
        for item in pipeline[category].get('items', []):
            if item.get('status') != 'submitted':
                continue
            
            if 'submitted_date' not in item:
                continue
            
            days = days_since(item['submitted_date'])
            if days is None:
                continue
            
            # Services follow-up schedule
            if category == 'services':
                if days == 3:
                    reminders.append({
                        'name': item['name'],
                        'category': category,
                        'days': days,
                        'action': 'Send value-add content',
                        'template': 'value-add',
                        'priority': 'HIGH'
                    })
                elif days == 7:
                    reminders.append({
                        'name': item['name'],
                        'category': category,
                        'days': days,
                        'action': 'Casual check-in',
                        'template': 'check-in',
                        'priority': 'MEDIUM'
                    })
                elif days == 14:
                    reminders.append({
                        'name': item['name'],
                        'category': category,
                        'days': days,
                        'action': 'Graceful close-out',
                        'template': 'close-out',
                        'priority': 'LOW'
                    })
            
            # Grants follow-up schedule (weeks)
            elif category == 'grants':
                weeks = days // 7
                if weeks == 2 and days % 7 == 0:
                    reminders.append({
                        'name': item['name'],
                        'category': category,
                        'days': days,
                        'action': 'Status check',
                        'template': 'grant-status',
                        'priority': 'MEDIUM'
                    })
                elif weeks == 4 and days % 7 == 0:
                    reminders.append({
                        'name': item['name'],
                        'category': category,
                        'days': days,
                        'action': 'Timeline follow-up',
                        'template': 'grant-timeline',
                        'priority': 'MEDIUM'
                    })
                elif weeks == 8 and days % 7 == 0:
                    reminders.append({
                        'name': item['name'],
                        'category': category,
                        'days': days,
                        'action': 'Feedback request (if rejected)',
                        'template': 'grant-feedback',
                        'priority': 'LOW'
                    })
    
    return reminders

def show_templates():
    """Show follow-up template examples."""
    print("\n" + "="*60)
    print("  📋 FOLLOW-UP TEMPLATES")
    print("="*60 + "\n")
    
    print("  Value-Add Content (Day 3):")
    print("  ─────────────────────────────────────────────────────────────")
    print('  "Just published [article/tool/insight] — thought of you:\n\n')
    print('  [Link]\n\n')
    print('  No action needed, just thought you\'d find it useful.')
    print('  Given [context from touch #1]."\n')
    
    print("  Casual Check-In (Day 7):")
    print("  ─────────────────────────────────────────────────────────────")
    print('  "Hey! Any thoughts on [offer]?\n\n')
    print('  Totally understand if timing\'s off — just wanted to check')
    print('  before [time constraint]."\n')
    
    print("  Graceful Exit (Day 14):")
    print("  ─────────────────────────────────────────────────────────────")
    print('  "Assuming [offer] isn\'t a priority right now — totally get it.\n\n')
    print('  If things change, I\'ll be here. Best of luck!"\n')
    
    print("="*60 + "\n")

def main():
    pipeline = load_pipeline()
    if not pipeline:
        return
    
    reminders = check_followups(pipeline)
    
    print("\n" + "="*60)
    print("  📧 FOLLOW-UP REMINDERS")
    print("="*60 + "\n")
    
    if not reminders:
        print("  ✅ No follow-ups needed right now.\n")
        print("  Check back tomorrow!")
    else:
        # Sort by priority
        priority_order = {'HIGH': 0, 'MEDIUM': 1, 'LOW': 2}
        reminders.sort(key=lambda r: priority_order.get(r['priority'], 3))
        
        # Group by priority
        high_priority = [r for r in reminders if r['priority'] == 'HIGH']
        medium_priority = [r for r in reminders if r['priority'] == 'MEDIUM']
        low_priority = [r for r in reminders if r['priority'] == 'LOW']
        
        if high_priority:
            print("  🔴 HIGH PRIORITY (Action today):")
            for r in high_priority:
                print(f"     • {r['name']} ({r['category']})")
                print(f"       Day {r['days']}: {r['action']}")
                print(f"       Template: {r['template']}\n")
        
        if medium_priority:
            print("  🟡 MEDIUM PRIORITY (This week):")
            for r in medium_priority:
                print(f"     • {r['name']} ({r['category']})")
                print(f"       Day {r['days']}: {r['action']}")
                print(f"       Template: {r['template']}\n")
        
        if low_priority:
            print("  🟢 LOW PRIORITY (Close-out):")
            for r in low_priority:
                print(f"     • {r['name']} ({r['category']})")
                print(f"       Day {r['days']}: {r['action']}")
                print(f"       Template: {r['template']}\n")
        
        print(f"  Total: {len(reminders)} follow-up(s) needed")
    
    print("\n" + "="*60)
    
    # Show templates if reminders exist
    if reminders:
        show_templates()

if __name__ == "__main__":
    main()
