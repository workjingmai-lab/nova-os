#!/usr/bin/env python3
"""
Moltbook Monitor - Notification system for agent activity
Checks for mentions, new followers, and engagement opportunities
Uses urllib to avoid external dependencies
"""

import urllib.request
import urllib.error
import json
import os
from datetime import datetime, timezone

MOLTBOOK_API = "https://www.moltbook.com/api/v1"
TOKEN = "moltbook_sk_xSwszjAM8vLLaa7VsSZVgNWp5a-R5XqD"
STATE_FILE = ".moltbook_state.json"
LOG_FILE = "logs/moltbook-activity.log"

def api_get(endpoint):
    """Make authenticated GET request"""
    url = f"{MOLTBOOK_API}{endpoint}"
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Accept": "application/json"
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        return {"error": f"HTTP {e.code}: {e.reason}"}
    except Exception as e:
        return {"error": str(e)}

def load_state():
    """Load last checked timestamps"""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"lastCheck": None, "lastMentionId": None}

def save_state(state):
    """Save state for next run"""
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def log_activity(message):
    """Log activity to file"""
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    timestamp = datetime.now(timezone.utc).isoformat()
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def check_claim_status():
    """Check if agent profile is claimed"""
    data = api_get("/agents/status")
    if "error" in data:
        return None
    return data.get("claimed", False)

def check_feed():
    """Check feed for new posts from followed agents"""
    data = api_get("/feed")
    if "error" in data:
        return data["error"]
    
    posts = data.get("posts", [])
    state = load_state()
    last_check = state.get("lastCheck")
    
    new_posts = []
    for post in posts[:10]:  # Check latest 10
        created = post.get("createdAt")
        if last_check and created and created > last_check:
            new_posts.append({
                "type": "new_post",
                "id": post.get("id"),
                "author": post.get("author", {}).get("name", "Unknown"),
                "title": (post.get("title") or "Untitled")[:60]
            })
    
    return new_posts

def main():
    """Main monitoring loop"""
    state = load_state()
    alerts = []
    
    # Check claim status first
    claimed = check_claim_status()
    if claimed is None:
        print("Error: Could not verify claim status")
        return 1
    if not claimed:
        print("Profile not yet claimed on Moltbook")
        return 0
    
    # Check feed for new posts
    new_posts = check_feed()
    if isinstance(new_posts, list) and new_posts:
        alerts.append(f"📝 {len(new_posts)} new post(s) from followed agents")
        for p in new_posts:
            log_activity(f"NEW POST by {p['author']}: {p['title']}...")
    elif isinstance(new_posts, str):
        print(f"Feed check error: {new_posts}")
    
    # Update state
    state["lastCheck"] = datetime.now(timezone.utc).isoformat()
    save_state(state)
    
    # Output summary
    if alerts:
        print(" | ".join(alerts))
        return 1  # Signal that attention needed
    else:
        print("No new activity")
        return 0

if __name__ == "__main__":
    exit(main())
