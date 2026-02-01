#!/usr/bin/env python3
"""
Moltbook Notification System
Checks for mentions, new followers, and activity requiring response.
Uses urllib (no external deps).
"""

import urllib.request
import urllib.error
import json
import os
from datetime import datetime, timezone

API_BASE = "https://www.moltbook.com/api/v1"
TOKEN = "moltbook_sk_xSwszjAM8vLLaa7VsSZVgNWp5a-R5XqD"

def api_get(endpoint):
    """Make authenticated GET request"""
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/json"
    }
    req = urllib.request.Request(f"{API_BASE}{endpoint}", headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        return {"error": f"HTTP {e.code}: {e.reason}"}
    except Exception as e:
        return {"error": str(e)}

def check_feed():
    """Check feed for mentions and activity"""
    data = api_get("/feed")
    
    if "error" in data:
        return data
    
    posts = data.get("posts", [])
    mentions = []
    
    for post in posts:
        content = post.get("content", "").lower()
        if "nova" in content:
            mentions.append({
                "id": post.get("id"),
                "author": post.get("author", {}).get("username"),
                "snippet": post.get("content", "")[:80]
            })
    
    return {
        "total_posts": len(posts),
        "mentions": mentions,
        "mention_count": len(mentions)
    }

def main():
    now = datetime.now(timezone.utc).strftime("%H:%M")
    print(f"🔄 Moltbook Check — {now} UTC")
    
    result = check_feed()
    
    # Save results
    out_path = "/home/node/.openclaw/workspace/notifications/moltbook-check.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    
    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        **result
    }
    
    with open(out_path, "w") as f:
        json.dump(record, f, indent=2)
    
    # Output summary
    if "error" in result:
        print(f"❌ Error: {result['error']}")
        return
    
    m_count = result.get("mention_count", 0)
    total = result.get("total_posts", 0)
    
    if m_count > 0:
        print(f"⚠️  {m_count} mention(s) detected!")
        for m in result["mentions"]:
            print(f"   → @{m['author']}: {m['snippet'][:50]}...")
    else:
        print(f"✅ No mentions (scanned {total} posts)")

if __name__ == "__main__":
    main()
