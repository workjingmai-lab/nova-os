#!/usr/bin/env python3
"""
Grant Opportunity Monitor
Tracks grant programs, deadlines, and auto-alerts on new opportunities.
Nova — 2026-02-01
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

GRANTS_FILE = Path(__file__).parent.parent / "data" / "grants" / "opportunities.json"
ALERT_DAYS = [7, 3, 1]  # Alert at 7, 3, and 1 days before deadline

def load_opportunities() -> list[dict]:
    """Load grant opportunities from JSON."""
    if not GRANTS_FILE.exists():
        return []
    with open(GRANTS_FILE) as f:
        return json.load(f)

def save_opportunities(opps: list[dict]):
    """Save grant opportunities to JSON."""
    GRANTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(GRANTS_FILE, "w") as f:
        json.dump(opps, f, indent=2)

def parse_date(date_str: str) -> Optional[datetime]:
    """Parse ISO date string."""
    try:
        return datetime.fromisoformat(date_str.replace("Z", "+00:00"))
    except:
        return None

def days_until(deadline: datetime) -> int:
    """Calculate days until deadline."""
    now = datetime.utcnow().replace(tzinfo=deadline.tzinfo)
    delta = deadline - now
    return delta.days

def check_alerts():
    """Check for upcoming deadlines and generate alerts."""
    opps = load_opportunities()
    alerts = []
    now = datetime.utcnow()
    
    for opp in opps:
        if opp.get("status") == "submitted":
            continue
            
        deadline_str = opp.get("deadline")
        if not deadline_str or deadline_str == "Rolling":
            continue
            
        deadline = parse_date(deadline_str)
        if not deadline:
            continue
            
        days = days_until(deadline)
        
        # Alert thresholds
        for alert_day in ALERT_DAYS:
            if days == alert_day:
                alerts.append({
                    "grant": opp["name"],
                    "days_left": days,
                    "deadline": deadline_str,
                    "urgency": "high" if days <= 1 else "medium" if days <= 3 else "low"
                })
        
        # Overdue check
        if days < 0:
            opp["status"] = "missed"
    
    save_opportunities(opps)
    return alerts

def add_opportunity(name: str, url: str, amount: str, deadline: str, 
                   category: str = "", notes: str = ""):
    """Add a new grant opportunity."""
    opps = load_opportunities()
    
    opp = {
        "id": len(opps) + 1,
        "name": name,
        "url": url,
        "amount": amount,
        "deadline": deadline,
        "category": category,
        "notes": notes,
        "status": "researching",
        "added": datetime.utcnow().isoformat(),
        "last_check": None
    }
    
    opps.append(opp)
    save_opportunities(opps)
    return opp

def list_opportunities(status: Optional[str] = None) -> list[dict]:
    """List all opportunities, optionally filtered by status."""
    opps = load_opportunities()
    if status:
        opps = [o for o in opps if o.get("status") == status]
    return sorted(opps, key=lambda x: x.get("deadline", "9999"))

def format_opportunity(opp: dict) -> str:
    """Format opportunity for display."""
    deadline = opp.get("deadline", "N/A")
    status = opp.get("status", "unknown")
    
    if deadline != "Rolling" and deadline != "N/A":
        dt = parse_date(deadline)
        if dt:
            days = days_until(dt)
            deadline = f"{deadline} ({days}d)"
    
    return f"""
📋 {opp['name']}
   Amount: {opp['amount']}
   Deadline: {deadline}
   Status: {status}
   URL: {opp['url']}
   Notes: {opp.get('notes', 'None')}
"""

def seed_default_opportunities():
    """Seed with known grant opportunities."""
    defaults = [
        {
            "id": 1,
            "name": "Ethereum Foundation ESP",
            "url": "https://esp.ethereum.foundation/",
            "amount": "$10K-$500K",
            "deadline": "Rolling",
            "category": "Public Goods",
            "notes": "Perfect fit for security tools work",
            "status": "draft_complete",
            "added": "2026-02-01T00:00:00Z",
            "last_check": None
        },
        {
            "id": 2,
            "name": "Gitcoin Grants",
            "url": "https://grants.gitcoin.co/",
            "amount": "Matching pool",
            "deadline": "2026-02-15",
            "category": "OSS",
            "notes": "Application drafted, needs credentials",
            "status": "ready_to_submit",
            "added": "2026-02-01T00:00:00Z",
            "last_check": None
        },
        {
            "id": 3,
            "name": "Optimism RetroPGF Round 4",
            "url": "https://community.optimism.io/docs/governance/retropgf/",
            "amount": "Variable",
            "deadline": "TBD",
            "category": "Retroactive",
            "notes": "Need proven impact first",
            "status": "researching",
            "added": "2026-02-01T00:00:00Z",
            "last_check": None
        },
        {
            "id": 4,
            "name": "Arbitrum DAO Grant",
            "url": "https://arbitrum.foundation/grants",
            "amount": "$5K-$500K",
            "deadline": "2026-03-01",
            "category": "Ecosystem",
            "notes": "Draft in progress",
            "status": "drafting",
            "added": "2026-02-01T00:00:00Z",
            "last_check": None
        },
        {
            "id": 5,
            "name": "Build DAO Microgrant",
            "url": "https://www.build.top/",
            "amount": "$1K-$10K",
            "deadline": "Rolling",
            "category": "Builder",
            "notes": "Fast turnaround, good for quick wins",
            "status": "researching",
            "added": "2026-02-01T00:00:00Z",
            "last_check": None
        }
    ]
    
    if not GRANTS_FILE.exists():
        save_opportunities(defaults)
        return defaults
    return load_opportunities()

def run_check():
    """Main check function — run via cron/heartbeat."""
    # Ensure data exists
    seed_default_opportunities()
    
    # Check for alerts
    alerts = check_alerts()
    
    # Generate report
    all_opps = list_opportunities()
    
    report = []
    report.append("=" * 50)
    report.append("📊 GRANT OPPORTUNITY REPORT")
    report.append(f"Generated: {datetime.utcnow().isoformat()}")
    report.append("=" * 50)
    
    # Summary
    by_status = {}
    for opp in all_opps:
        status = opp.get("status", "unknown")
        by_status[status] = by_status.get(status, 0) + 1
    
    report.append("\n📈 Status Summary:")
    for status, count in sorted(by_status.items()):
        report.append(f"   {status}: {count}")
    
    # Alerts
    if alerts:
        report.append(f"\n🚨 UPCOMING DEADLINES ({len(alerts)}):")
        for alert in sorted(alerts, key=lambda x: x['days_left']):
            emoji = "🔴" if alert['urgency'] == 'high' else "🟡" if alert['urgency'] == 'medium' else "🟢"
            report.append(f"   {emoji} {alert['grant']}: {alert['days_left']} days left")
            report.append(f"      Deadline: {alert['deadline']}")
    else:
        report.append("\n✅ No urgent deadlines")
    
    # All opportunities
    report.append("\n📋 ALL OPPORTUNITIES:")
    for opp in all_opps:
        report.append(format_opportunity(opp))
    
    return "\n".join(report)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        
        if cmd == "check":
            print(run_check())
        elif cmd == "add":
            if len(sys.argv) < 5:
                print("Usage: grant-monitor.py add <name> <url> <amount> [deadline] [category]")
                sys.exit(1)
            opp = add_opportunity(sys.argv[2], sys.argv[3], sys.argv[4], 
                                 sys.argv[5] if len(sys.argv) > 5 else "Rolling",
                                 sys.argv[6] if len(sys.argv) > 6 else "")
            print(f"Added: {opp['name']}")
        elif cmd == "list":
            opps = list_opportunities()
            for opp in opps:
                print(format_opportunity(opp))
        else:
            print(f"Unknown command: {cmd}")
            print("Commands: check, add, list")
    else:
        print(run_check())
