#!/usr/bin/env python3
"""
notification-monitor.py — Nova's Alert System
Monitors external signals: Moltbook mentions, grant opportunities, competition alerts
"""

import json
import urllib.request
import urllib.error
import os
from datetime import datetime, timedelta
from pathlib import Path

STATE_FILE = Path(__file__).parent / ".notification_state.json"
MOLTBOOK_API = "https://www.moltbook.com/api/v1"
MOLTBOOK_TOKEN = os.getenv("MOLTBOOK_TOKEN", "moltbook_sk_xSwszjAM8vLLaa7VsSZVgNWp5a-R5XqD")

# Grant sources to monitor (URLs/feeds)
GRANT_SOURCES = {
    "ethereum_foundation": "https://esp.ethereum.foundation/api/rounds",
    "gitcoin": "https://grants.gitcoin.co/api/rounds",
    "optimism": "https://vote.optimism.io/api/grants",
}

# Code4rena competition feed
CODE4RENA_API = "https://code4rena.com/api/competitions"

def load_state():
    """Load persistent notification state."""
    if STATE_FILE.exists():
        with open(STATE_FILE) as f:
            return json.load(f)
    return {
        "lastMoltbookCheck": None,
        "lastGrantCheck": None,
        "lastCompetitionCheck": None,
        "seenMentions": [],
        "seenGrants": [],
        "seenCompetitions": [],
        "alerts": [],
        "pending": []
    }

def save_state(state):
    """Save persistent notification state."""
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2, default=str)

def fetch_moltbook_mentions(agent_id="nova"):
    """Check for mentions/notifications on Moltbook."""
    try:
        req = urllib.request.Request(
            f"{MOLTBOOK_API}/agents/{agent_id}/notifications",
            headers={"Authorization": f"Bearer {MOLTBOOK_TOKEN}"}
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        return {"error": str(e)}

def check_new_mentions(state):
    """Check for new mentions and update state."""
    data = fetch_moltbook_mentions()
    
    if "error" in data:
        return [{"type": "error", "source": "moltbook", "message": data["error"]}]
    
    alerts = []
    mentions = data.get("mentions", [])
    
    for mention in mentions:
        mention_id = mention.get("id")
        if mention_id and mention_id not in state["seenMentions"]:
            state["seenMentions"].append(mention_id)
            alerts.append({
                "type": "mention",
                "source": "moltbook", 
                "priority": "high",
                "message": f"Mentioned by {mention.get('author', 'unknown')}: {mention.get('text', '')[:100]}...",
                "timestamp": datetime.utcnow().isoformat()
            })
    
    # Keep list bounded
    state["seenMentions"] = state["seenMentions"][-100:]
    state["lastMoltbookCheck"] = datetime.utcnow().isoformat()
    
    return alerts

def generate_daily_digest(state):
    """Generate summary of pending opportunities."""
    now = datetime.utcnow()
    
    digest = {
        "generated_at": now.isoformat(),
        "summary": {
            "unread_mentions": len([a for a in state["alerts"] if a["type"] == "mention"]),
            "new_grants": len([a for a in state["alerts"] if a["type"] == "grant"]),
            "active_competitions": len([a for a in state["alerts"] if a["type"] == "competition"]),
        },
        "action_items": []
    }
    
    # Priority sorting
    if digest["summary"]["unread_mentions"] > 0:
        digest["action_items"].append("🚨 Respond to Moltbook mentions")
    if digest["summary"]["new_grants"] > 0:
        digest["action_items"].append("💰 Review new grant opportunities")
    if digest["summary"]["active_competitions"] > 0:
        digest["action_items"].append("⚔️ Check Code4rena competitions")
    
    if not digest["action_items"]:
        digest["action_items"].append("✅ No urgent notifications")
    
    return digest

def main():
    """Main monitor loop — called by cron/heartbeat."""
    state = load_state()
    
    # Check all sources
    new_alerts = check_new_mentions(state)
    
    # Add to pending alerts queue
    state["alerts"].extend(new_alerts)
    state["alerts"] = state["alerts"][-50:]  # Keep last 50
    
    # Generate digest
    digest = generate_daily_digest(state)
    
    # Output for logging/cron capture
    output = {
        "timestamp": datetime.utcnow().isoformat(),
        "new_alerts": len(new_alerts),
        "digest": digest,
        "alerts": new_alerts[:3]  # Last 3 for preview
    }
    
    print(json.dumps(output, indent=2))
    
    # Persist state
    save_state(state)
    
    # Return exit code based on urgency
    return 1 if any(a.get("priority") == "high" for a in new_alerts) else 0

if __name__ == "__main__":
    exit(main())
