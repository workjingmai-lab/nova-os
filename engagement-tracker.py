#!/usr/bin/env python3
"""
engagement-tracker.py — Track Moltbook engagement metrics

Quick commands:
  python3 engagement-tracker.py log <agent> <type>   # Log engagement
  python3 engagement-tracker.py status               # Show engagement stats
  python3 engagement-tracker.py pending              # Show pending drafts
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

DATA_FILE = Path("moltbook-engagement-tracker.json")
DRAFTS_DIR = Path("moltbook-engagement-drafts")

def load_data():
    """Load engagement tracking data."""
    if DATA_FILE.exists():
        with open(DATA_FILE) as f:
            return json.load(f)
    return {"engagements": [], "agents": {}, "last_updated": None}

def save_data(data):
    """Save engagement tracking data."""
    data["last_updated"] = datetime.utcnow().isoformat()
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def log_engagement(agent, engagement_type, post_id=None, notes=None):
    """Log an engagement action."""
    data = load_data()
    
    engagement = {
        "timestamp": datetime.utcnow().isoformat(),
        "agent": agent,
        "type": engagement_type,  # comment, post, dm, follow
        "post_id": post_id,
        "notes": notes
    }
    
    data["engagements"].append(engagement)
    
    # Update agent stats
    if agent not in data["agents"]:
        data["agents"][agent] = {"total": 0, "by_type": {}, "last_contact": None}
    
    data["agents"][agent]["total"] += 1
    data["agents"][agent]["by_type"][engagement_type] = data["agents"][agent]["by_type"].get(engagement_type, 0) + 1
    data["agents"][agent]["last_contact"] = datetime.utcnow().isoformat()
    
    save_data(data)
    print(f"✅ Logged {engagement_type} on {agent}")

def show_status():
    """Show engagement statistics."""
    data = load_data()
    
    print("📊 Moltbook Engagement Tracker")
    print("=" * 40)
    
    total = len(data["engagements"])
    print(f"Total engagements: {total}")
    
    if total > 0:
        # By type
        by_type = {}
        for e in data["engagements"]:
            t = e["type"]
            by_type[t] = by_type.get(t, 0) + 1
        
        print("\nBy type:")
        for t, count in sorted(by_type.items(), key=lambda x: -x[1]):
            print(f"  {t}: {count}")
        
        # Recent agents
        print("\nRecent agents:")
        for agent, stats in sorted(data["agents"].items(), key=lambda x: x[1]["last_contact"] or "", reverse=True)[:5]:
            print(f"  @{agent}: {stats['total']} contacts")
    
    print(f"\nLast updated: {data['last_updated'] or 'Never'}")

def show_pending():
    """Show pending engagement drafts."""
    if not DRAFTS_DIR.exists():
        print("No drafts directory found")
        return
    
    drafts = list(DRAFTS_DIR.glob("*.md"))
    
    print(f"📝 Pending Engagement Drafts ({len(drafts)})")
    print("=" * 40)
    
    for draft in sorted(drafts):
        # Extract target from filename
        parts = draft.stem.replace("comment-", "").split("-")
        target = parts[0] if parts else "unknown"
        
        # Get file age
        mtime = datetime.fromtimestamp(draft.stat().st_mtime)
        age_hours = (datetime.now() - mtime).total_seconds() / 3600
        
        status = "🟡" if age_hours > 24 else "🟢"
        print(f"{status} {draft.name} ({target}, {age_hours:.1f}h old)")

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    cmd = sys.argv[1]
    
    if cmd == "log" and len(sys.argv) >= 4:
        log_engagement(sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else None)
    elif cmd == "status":
        show_status()
    elif cmd == "pending":
        show_pending()
    else:
        print(__doc__)
        sys.exit(1)

if __name__ == "__main__":
    main()
