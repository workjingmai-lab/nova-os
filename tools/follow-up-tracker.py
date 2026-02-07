#!/usr/bin/env python3
"""
Follow-up Tracker for Sent Messages

Tracks sent outreach messages and their follow-up schedules.
When a message is sent, record it here to ensure proper follow-up.

Usage:
    python3 tools/follow-up-tracker.py                    # List all sent messages
    python3 tools/follow-up-tracker.py add <company> <value> [priority]  # Add sent message
    python3 tools/follow-up-tracker.py due                # Show follow-ups due now
    python3 tools/follow-up-tracker.py status <company>   # Check specific lead
    python3 tools/follow-up-tracker.py export             # Export markdown checklist
    python3 tools/follow-up-tracker.py done <company> <day>  # Mark follow-up complete

Data: stored in follow-up-tracker.json
"""

import json
from datetime import datetime, timedelta
from pathlib import Path

DATA_FILE = Path("follow-up-tracker.json")
FOLLOWUP_DAYS = [0, 3, 7, 14, 21]  # Standard follow-up schedule

def load_data():
    """Load tracking data or create new structure."""
    if DATA_FILE.exists():
        with open(DATA_FILE) as f:
            return json.load(f)
    return {"sent": [], "last_updated": None}

def save_data(data):
    """Save tracking data."""
    data["last_updated"] = datetime.now().isoformat()
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_sent(company, value, date=None, priority="MEDIUM"):
    """Add a sent message to tracking."""
    data = load_data()
    if date is None:
        date = datetime.now().isoformat()
    
    data["sent"].append({
        "company": company,
        "value": value,
        "sent_date": date,
        "priority": priority,
        "followups": [
            {"day": d, "done": False, "date": None} for d in FOLLOWUP_DAYS
        ],
        "responses": [],
        "status": "SENT"
    })
    save_data(data)
    return f"✓ Tracked: {company} (${value:,.0f}) - Follow-ups on days {FOLLOWUP_DAYS[1:]}"

def list_all():
    """List all sent messages."""
    data = load_data()
    if not data["sent"]:
        return "📭 No sent messages tracked yet."
    
    total = len(data["sent"])
    total_value = sum(s["value"] for s in data["sent"])
    return f"📬 Sent: {total} messages, ${total_value:,.0f} total value\n" + "\n".join(
        f"  • {s['company']} (${s['value']:,.0f}) — {s['status']}" 
        for s in data["sent"]
    )

def due_now():
    """Show follow-ups due now."""
    data = load_data()
    if not data["sent"]:
        return "📭 No sent messages tracked."
    
    now = datetime.now()
    due = []
    
    for msg in data["sent"]:
        sent_date = datetime.fromisoformat(msg["sent_date"])
        for fp in msg["followups"]:
            if fp["day"] == 0:
                continue  # Skip day 0 (sent date)
            if fp["done"]:
                continue  # Already done
            
            due_date = sent_date + timedelta(days=fp["day"])
            if due_date <= now:
                days_overdue = (now - due_date).days
                if days_overdue == 0:
                    due.append(f"🔔 {msg['company']} - Day {fp['day']} follow-up DUE TODAY")
                else:
                    due.append(f"⚠️  {msg['company']} - Day {fp['day']} follow-up OVERDUE by {days_overdue} days")
    
    if not due:
        return "✅ No follow-ups due right now."
    return "\n".join(due)

def mark_done(company, day):
    """Mark a follow-up as complete."""
    data = load_data()
    for msg in data["sent"]:
        if msg["company"].lower() == company.lower():
            for fp in msg["followups"]:
                if fp["day"] == day:
                    fp["done"] = True
                    fp["date"] = datetime.now().isoformat()
                    save_data(data)
                    return f"✓ Marked day {day} follow-up complete for {company}"
    return f"❌ Company not found: {company}"

def get_status(company):
    """Get detailed status for a company."""
    data = load_data()
    for msg in data["sent"]:
        if msg["company"].lower() == company.lower():
            sent_date = datetime.fromisoformat(msg["sent_date"])
            age = (datetime.now() - sent_date).days
            
            status = f"""
📧 {msg['company']} (${msg['value']:,.0f})
  Status: {msg['status']}
  Sent: {sent_date.strftime('%Y-%m-%d')} ({age} days ago)
  Priority: {msg['priority']}
  
  Follow-ups:
"""
            for fp in msg["followups"]:
                if fp["day"] == 0:
                    status += f"    ✓ Day 0 (sent): {fp['done']}\n"
                else:
                    check = "✓" if fp["done"] else " "
                    due_date = sent_date + timedelta(days=fp["day"])
                    status += f"    [{check}] Day {fp['day']}: {due_date.strftime('%Y-%m-%d')}\n"
            
            if msg["responses"]:
                status += f"\n  Responses: {len(msg['responses'])}\n"
            
            return status
    return f"❌ Company not found: {company}"

def export_checklist():
    """Export follow-ups as markdown checklist for easy review."""
    data = load_data()
    if not data["sent"]:
        return "# Follow-up Checklist\n\n📭 No sent messages tracked yet."
    
    now = datetime.now()
    output = ["# Follow-up Checklist", "", f"Generated: {now.strftime('%Y-%m-%d %H:%MZ')}", ""]
    
    # Sort by priority: HIGH > MEDIUM > LOW
    priority_order = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
    sorted_msgs = sorted(data["sent"], key=lambda m: priority_order.get(m["priority"], 99))
    
    for msg in sorted_msgs:
        sent_date = datetime.fromisoformat(msg["sent_date"])
        age = (now - sent_date).days
        
        output.append(f"## {msg['company']} (${msg['value']:,.0f})")
        output.append(f"**Status:** {msg['status']} | **Priority:** {msg['priority']} | **Sent:** {sent_date.strftime('%Y-%m-%d')} ({age}d ago)")
        output.append("")
        
        # Follow-ups checklist
        output.append("### Follow-ups")
        for fp in msg["followups"]:
            if fp["day"] == 0:
                continue
            due_date = sent_date + timedelta(days=fp["day"])
            is_overdue = due_date <= now and not fp["done"]
            
            if is_overdue:
                output.append(f"- [ ] Day {fp['day']} ({due_date.strftime('%Y-%m-%d')}) ⚠️ **OVERDUE**")
            elif fp["done"]:
                output.append(f"- [x] Day {fp['day']} ({due_date.strftime('%Y-%m-%d')}) ✓ Done")
            else:
                output.append(f"- [ ] Day {fp['day']} ({due_date.strftime('%Y-%m-%d')})")
        
        # Responses
        if msg["responses"]:
            output.append("\n### Responses")
            for resp in msg["responses"]:
                output.append(f"- {resp['date']}: {resp.get('summary', 'No summary')}")
        
        output.append("")
    
    return "\n".join(output)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print(list_all())
    elif sys.argv[1] == "add" and len(sys.argv) >= 4:
        company = sys.argv[2]
        value = float(sys.argv[3])
        priority = sys.argv[4] if len(sys.argv) > 4 else "MEDIUM"
        print(add_sent(company, value, priority=priority))
    elif sys.argv[1] == "due":
        print(due_now())
    elif sys.argv[1] == "done" and len(sys.argv) >= 4:
        company = sys.argv[2]
        day = int(sys.argv[3])
        print(mark_done(company, day))
    elif sys.argv[1] == "status" and len(sys.argv) >= 3:
        print(get_status(sys.argv[2]))
    elif sys.argv[1] == "export":
        print(export_checklist())
    else:
        print(list_all())
