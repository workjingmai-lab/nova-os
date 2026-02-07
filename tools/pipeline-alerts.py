#!/usr/bin/env python3
"""
pipeline-alerts.py - Monitor pipeline health and alert on actionable conditions

Usage:
    python3 tools/pipeline-alerts.py check          # Run all checks
    python3 tools/pipeline-alerts.py stale          # Check for stale leads
    python3 tools/pipeline-alerts.py followups      # Check for due follow-ups
    python3 tools/pipeline-alerts.py rate-limit     # Check Moltbook cooldown
"""

import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

def load_conversion_log():
    """Load conversion tracking data."""
    log_path = Path("data/conversion-log.json")
    if not log_path.exists():
        return {"leads": [], "follow_ups": []}
    
    with open(log_path) as f:
        return json.load(f)

def load_revenue_data():
    """Load revenue pipeline data."""
    pipeline_path = Path("data/revenue-pipeline.json")
    if not pipeline_path.exists():
        return {}
    
    with open(pipeline_path) as f:
        return json.load(f)

def check_stale_leads(days_threshold=3):
    """Check for leads that have been in 'ready' status too long."""
    data = load_conversion_log()
    stale = []
    
    for lead in data.get("leads", []):
        if lead.get("status") != "ready":
            continue
        
        updated = lead.get("updated_at", "")
        if not updated:
            continue
        
        try:
            updated_dt = datetime.fromisoformat(updated.replace("Z", "+00:00"))
            days_old = (datetime.now().replace(tzinfo=updated_dt.tzinfo) - updated_dt).days
            
            if days_old >= days_threshold:
                stale.append({
                    "name": lead.get("name", "Unknown"),
                    "days_old": days_old,
                    "value": lead.get("value", 0)
                })
        except:
            continue
    
    return stale

def check_due_followups():
    """Check for follow-ups that are due today."""
    data = load_conversion_log()
    due = []
    now = datetime.now()
    
    for fu in data.get("follow_ups", []):
        due_date = fu.get("due_date", "")
        if not due_date:
            continue
        
        try:
            due_dt = datetime.fromisoformat(due_date.replace("Z", "+00:00"))
            if due_dt.date() <= now.date():
                due.append({
                    "lead": fu.get("lead_name", "Unknown"),
                    "due": due_date,
                    "message": fu.get("message", "")[:50]
                })
        except:
            continue
    
    return due

def check_rate_limit():
    """Check Moltbook rate limit status."""
    queue_path = Path("data/moltbook-queue.json")
    if not queue_path.exists():
        return {"queued": 0, "cooldown": False, "ready": True}
    
    with open(queue_path) as f:
        data = json.load(f)
    
    posts = data.get("posts", [])
    queued = len([p for p in posts if p.get("status") == "queued"])
    
    # Check for recent rate limit
    last_rate_limit = None
    for p in posts:
        if p.get("last_error", "").startswith("429"):
            ts = p.get("last_attempt", "")
            if ts:
                try:
                    dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                    if not last_rate_limit or dt > last_rate_limit:
                        last_rate_limit = dt
                except:
                    pass
    
    cooldown = False
    if last_rate_limit:
        minutes_since = (datetime.now().replace(tzinfo=last_rate_limit.tzinfo) - last_rate_limit).total_seconds() / 60
        cooldown = minutes_since < 15  # Assume 15 min cooldown
    
    return {
        "queued": queued,
        "cooldown": cooldown,
        "ready": not cooldown and queued > 0,
        "minutes_since_rate_limit": minutes_since if last_rate_limit else None
    }

def format_currency(value):
    """Format value as currency."""
    if value >= 1000000:
        return f"${value/1000000:.1f}M"
    elif value >= 1000:
        return f"${value/1000:.0f}K"
    return f"${value}"

def run_all_checks():
    """Run all pipeline health checks."""
    print("=" * 60)
    print("🚨 PIPELINE ALERTS")
    print("=" * 60)
    
    alerts_found = 0
    
    # Check 1: Stale leads
    stale = check_stale_leads(days_threshold=2)
    print(f"\n📋 STALE LEADS (ready >2 days)")
    print("-" * 40)
    if stale:
        total_value = sum(s["value"] for s in stale)
        print(f"⚠️  {len(stale)} stale leads worth {format_currency(total_value)}")
        for s in stale[:3]:
            print(f"   • {s['name']}: {s['days_old']} days, {format_currency(s['value'])}")
        if len(stale) > 3:
            print(f"   ... and {len(stale) - 3} more")
        alerts_found += len(stale)
    else:
        print("✅ No stale leads")
    
    # Check 2: Due follow-ups
    due = check_due_followups()
    print(f"\n📅 DUE FOLLOW-UPS")
    print("-" * 40)
    if due:
        print(f"⚠️  {len(due)} follow-ups due today")
        for d in due[:3]:
            print(f"   • {d['lead']}: {d['message']}...")
        if len(due) > 3:
            print(f"   ... and {len(due) - 3} more")
        alerts_found += len(due)
    else:
        print("✅ No follow-ups due")
    
    # Check 3: Rate limit
    rl = check_rate_limit()
    print(f"\n🐦 MOLTBOOK STATUS")
    print("-" * 40)
    if rl["ready"]:
        print(f"✅ Ready to post ({rl['queued']} in queue)")
    elif rl["cooldown"]:
        mins = int(15 - (rl.get("minutes_since_rate_limit") or 0))
        print(f"⏳ Rate limited (~{mins} min remaining)")
        print(f"   {rl['queued']} posts queued")
    else:
        print(f"ℹ️  {rl['queued']} posts queued")
    
    # Check 4: Pipeline summary
    revenue = load_revenue_data()
    print(f"\n💰 PIPELINE SUMMARY")
    print("-" * 40)
    
    # Handle different data structures
    services = revenue.get("services", {})
    grants = revenue.get("grants", {})
    
    if isinstance(services, list):
        ready = sum(s.get("potential", 0) for s in services if s.get("status") == "ready")
    else:
        ready = services.get("ready", 0)
    
    if isinstance(grants, list):
        submitted = sum(g.get("potential", 0) for g in grants if g.get("status") == "submitted")
    else:
        submitted = grants.get("submitted", 0)
    
    print(f"   Services ready: {format_currency(ready)}")
    print(f"   Grants submitted: {format_currency(submitted)}")
    
    # Summary
    print(f"\n{'=' * 60}")
    if alerts_found > 0:
        print(f"⚠️  {alerts_found} ALERTS REQUIRE ATTENTION")
    else:
        print("✅ All pipeline checks passed")
    print("=" * 60)
    
    return alerts_found

def main():
    if len(sys.argv) < 2:
        run_all_checks()
        return
    
    cmd = sys.argv[1]
    
    if cmd == "check":
        run_all_checks()
    elif cmd == "stale":
        stale = check_stale_leads()
        for s in stale:
            print(f"{s['name']}: {s['days_old']} days")
    elif cmd == "followups":
        due = check_due_followups()
        for d in due:
            print(f"{d['lead']}: due {d['due']}")
    elif cmd == "rate-limit":
        rl = check_rate_limit()
        print(f"Queued: {rl['queued']}")
        print(f"Ready: {rl['ready']}")
        print(f"Cooldown: {rl['cooldown']}")
    else:
        print(__doc__)

if __name__ == "__main__":
    main()
