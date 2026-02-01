#!/usr/bin/env python3
"""
grant-status-tracker.py — Track grant application lifecycle
Monitors status, deadlines, follow-ups, and outcomes

TODO: Support reading grants/SUBMISSION-QUEUE.md for batch status checks
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path

GRANTS_FILE = Path("data/grants.json")
STATUS_LOG = Path("diary.md")

def load_grants():
    """Load grant applications from JSON."""
    if GRANTS_FILE.exists():
        with open(GRANTS_FILE) as f:
            raw = json.load(f)
            # Handle both old array format and new object format
            if isinstance(raw, list):
                return {"applications": raw, "last_updated": datetime.utcnow().isoformat()}
            return raw
    return {"applications": [], "last_updated": datetime.utcnow().isoformat()}

def save_grants(data):
    """Save grant applications to JSON."""
    GRANTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    data["last_updated"] = datetime.utcnow().isoformat()
    with open(GRANTS_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_grant(name, amount, url, status="draft", deadline=None, notes=""):
    """Add a new grant application."""
    data = load_grants()
    grant = {
        "id": f"grant_{len(data['applications']) + 1:03d}",
        "name": name,
        "amount_usd": amount,
        "url": url,
        "status": status,  # draft, submitted, pending, approved, rejected
        "deadline": deadline,
        "submitted_at": datetime.utcnow().isoformat() if status == "submitted" else None,
        "notes": notes,
        "follow_ups": [],
        "outcome": None
    }
    data["applications"].append(grant)
    save_grants(data)
    return grant["id"]

def update_status(grant_id, new_status, note=""):
    """Update grant status and log to diary."""
    data = load_grants()
    for grant in data["applications"]:
        if grant["id"] == grant_id:
            old_status = grant.get("status", "unknown")
            grant["status"] = new_status
            grant["updated_at"] = datetime.utcnow().isoformat()
            
            if new_status == "submitted" and old_status != "submitted":
                grant["submitted_at"] = datetime.utcnow().isoformat()
            
            if "follow_ups" not in grant:
                grant["follow_ups"] = []
            
            if note:
                grant["follow_ups"].append({
                    "date": datetime.utcnow().isoformat(),
                    "note": note
                })
            
            save_grants(data)
            
            # Log to diary
            name = grant.get("name") or grant.get("program") or "Unknown"
            amount = grant.get("amount_usd", 0)
            log_entry = f"""
[2026-02-01T{datetime.utcnow().strftime('%H:%M:%S')}Z] GRANT UPDATE: {name}
Status: {old_status} → {new_status}
Amount: ${amount:,}
{note if note else "No additional notes"}
"""
            with open(STATUS_LOG, "a") as f:
                f.write(log_entry)
            
            return True
    return False

def get_summary():
    """Generate status summary."""
    data = load_grants()
    apps = data["applications"]
    
    total = len(apps)
    by_status = {}
    total_ask = 0
    total_secured = 0
    urgent = []
    
    for grant in apps:
        status = grant.get("status", "unknown")
        by_status[status] = by_status.get(status, 0) + 1
        
        # Handle both old and new field names
        amount = grant.get("amount_usd", 0)
        if not amount and "amount" in grant:
            # Parse amount like "$10,000-50,000" or "$5,000"
            amt_str = grant["amount"].replace("$", "").replace(",", "")
            if "-" in amt_str:
                amt_str = amt_str.split("-")[0]
            try:
                amount = int(amt_str)
            except:
                amount = 0
        total_ask += amount
        
        if status == "approved":
            total_secured += amount
        
        # Check for deadlines within 7 days
        if grant.get("deadline") and grant["deadline"] not in ["rolling", "ongoing"]:
            try:
                deadline = datetime.fromisoformat(grant["deadline"].replace("Z", "+00:00"))
                days_until = (deadline - datetime.utcnow().replace(tzinfo=deadline.tzinfo)).days
                if days_until <= 7 and status in ["draft", "submitted", "drafted", "ready"]:
                    name = grant.get("name") or grant.get("program") or "Unknown"
                    urgent.append({
                        "name": name,
                        "deadline": grant["deadline"],
                        "days_until": days_until,
                        "status": status
                    })
            except:
                pass
    
    return {
        "total_applications": total,
        "by_status": by_status,
        "total_asked": total_ask,
        "total_secured": total_secured,
        "conversion_rate": (by_status.get("approved", 0) / total * 100) if total > 0 else 0,
        "urgent_deadlines": sorted(urgent, key=lambda x: x["days_until"])
    }

def generate_report():
    """Generate markdown report."""
    summary = get_summary()
    
    report = f"""# Grant Status Report
Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}

## Summary
| Metric | Value |
|--------|-------|
| Total Applications | {summary['total_applications']} |
| Total Asked | ${summary['total_asked']:,} |
| Total Secured | ${summary['total_secured']:,} |
| Conversion Rate | {summary['conversion_rate']:.1f}% |

## By Status
"""
    for status, count in sorted(summary['by_status'].items()):
        report += f"- {status.capitalize()}: {count}\n"
    
    if summary['urgent_deadlines']:
        report += "\n## ⚠️ Urgent Deadlines (≤7 days)\n"
        for item in summary['urgent_deadlines']:
            report += f"- **{item['name']}**: {item['days_until']} days ({item['deadline'][:10]}) — {item['status']}\n"
    else:
        report += "\n## Deadlines\nNo urgent deadlines.\n"
    
    report_path = Path("reports/grant-status.md")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, "w") as f:
        f.write(report)
    
    return report_path

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python grant-status-tracker.py [add|update|summary|report]")
        sys.exit(1)
    
    cmd = sys.argv[1]
    
    if cmd == "add":
        if len(sys.argv) < 5:
            print("Usage: add <name> <amount> <url> [deadline]")
            sys.exit(1)
        grant_id = add_grant(sys.argv[2], int(sys.argv[3]), sys.argv[4], 
                           deadline=sys.argv[5] if len(sys.argv) > 5 else None)
        print(f"Added grant: {grant_id}")
    
    elif cmd == "update":
        if len(sys.argv) < 4:
            print("Usage: update <grant_id> <new_status> [note]")
            sys.exit(1)
        note = sys.argv[4] if len(sys.argv) > 4 else ""
        if update_status(sys.argv[2], sys.argv[3], note):
            print(f"Updated {sys.argv[2]} → {sys.argv[3]}")
        else:
            print(f"Grant {sys.argv[2]} not found")
    
    elif cmd == "summary":
        s = get_summary()
        print(f"Applications: {s['total_applications']}")
        print(f"Asked: ${s['total_asked']:,}")
        print(f"Secured: ${s['total_secured']:,}")
        for status, count in s['by_status'].items():
            print(f"  {status}: {count}")
    
    elif cmd == "report":
        path = generate_report()
        print(f"Report saved: {path}")
    
    else:
        print(f"Unknown command: {cmd}")
