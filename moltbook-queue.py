#!/usr/bin/env python3
"""
moltbook-queue.py — Moltbook post queue manager
Check queue status, see what's ready to publish, track posting schedule.
Usage: python3 moltbook-queue.py [status|next|history]
"""

import json
import os
from datetime import datetime, timedelta

QUEUE_FILE = "moltbook-queue.json"
HISTORY_FILE = "moltbook-history.json"

def load_queue():
    """Load post queue or return defaults."""
    if os.path.exists(QUEUE_FILE):
        with open(QUEUE_FILE) as f:
            return json.load(f)
    return {"posts": [], "lastPosted": None}

def load_history():
    """Load post history or return defaults."""
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE) as f:
            return json.load(f)
    return {"posts": []}

def save_queue(queue):
    """Save queue to file."""
    with open(QUEUE_FILE, "w") as f:
        json.dump(queue, f, indent=2)

def get_post_status(post):
    """Determine if post is ready to publish."""
    if post.get("published"):
        return "published"
    if post.get("scheduled"):
        sched = datetime.fromisoformat(post["scheduled"].replace("Z", "+00:00"))
        if datetime.now().timestamp() >= sched.timestamp():
            return "ready"
        return f"scheduled ({sched.strftime('%b %d')})"
    return "draft"

def cmd_status():
    """Show queue status."""
    queue = load_queue()
    history = load_history()
    
    print("=" * 50)
    print("📱 MOLTBOOK QUEUE STATUS")
    print("=" * 50)
    
    # Queue stats
    posts = queue.get("posts", [])
    published = [p for p in posts if p.get("published")]
    drafts = [p for p in posts if not p.get("published") and not p.get("scheduled")]
    scheduled = [p for p in posts if p.get("scheduled") and not p.get("published")]
    ready = [p for p in scheduled if get_post_status(p) == "ready"]
    
    print(f"\n📊 QUEUE SUMMARY")
    print(f"   Published:   {len(published)}")
    print(f"   Scheduled:   {len(scheduled)}")
    print(f"   Drafts:      {len(drafts)}")
    print(f"   ✅ Ready now: {len(ready)}")
    
    # This week's posts
    week_ago = datetime.now() - timedelta(days=7)
    recent = [p for p in history.get("posts", []) 
              if datetime.fromisoformat(p.get("date", "2000-01-01")) > week_ago]
    print(f"   This week:   {len(recent)}")
    
    # Ready to publish
    if ready:
        print(f"\n🚀 READY TO PUBLISH")
        for p in ready[:3]:
            print(f"   • {p.get('title', 'Untitled')[:35]}")
    
    # Upcoming scheduled
    upcoming = [p for p in scheduled if get_post_status(p).startswith("scheduled")]
    if upcoming:
        print(f"\n📅 UPCOMING")
        for p in sorted(upcoming, key=lambda x: x.get("scheduled", ""))[:3]:
            status = get_post_status(p)
            print(f"   • {p.get('title', 'Untitled')[:30]:30} {status}")
    
    # Drafts waiting
    if drafts:
        print(f"\n📝 DRAFTS")
        for p in drafts[:3]:
            print(f"   • {p.get('title', 'Untitled')[:35]}")
    
    print(f"\n" + "=" * 50)

def cmd_next():
    """Show next post to publish."""
    queue = load_queue()
    posts = queue.get("posts", [])
    
    # Find ready posts
    ready = [p for p in posts if get_post_status(p) == "ready"]
    
    if ready:
        p = ready[0]
        print("🚀 NEXT POST READY:\n")
        print(f"Title: {p.get('title', 'Untitled')}")
        print(f"Type:  {p.get('type', 'post')}")
        print(f"\nContent preview:")
        content = p.get('content', '')
        print(content[:200] + "..." if len(content) > 200 else content)
        print(f"\n✅ Ready to publish via moltbook-suite.py")
    else:
        # Find next scheduled
        scheduled = [p for p in posts if p.get("scheduled") and not p.get("published")]
        if scheduled:
            p = min(scheduled, key=lambda x: x.get("scheduled", ""))
            print(f"📅 NEXT SCHEDULED: {p.get('title', 'Untitled')}")
            print(f"   Goes live: {get_post_status(p)}")
        else:
            print("⚠️  No posts ready or scheduled.")
            print("   Add posts to moltbook-queue.json or run moltbook-suite.py")

def cmd_history():
    """Show publishing history."""
    history = load_history()
    posts = history.get("posts", [])
    
    print("📜 PUBLISH HISTORY (last 10)")
    print("-" * 50)
    
    for p in sorted(posts, key=lambda x: x.get("date", ""), reverse=True)[:10]:
        date = p.get("date", "Unknown")[:10]
        title = p.get("title", "Untitled")[:35]
        likes = p.get("likes", 0)
        print(f"{date}  {title:35} ♥{likes}")

def main():
    import sys
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    
    if cmd == "status":
        cmd_status()
    elif cmd == "next":
        cmd_next()
    elif cmd == "history":
        cmd_history()
    else:
        print(f"Unknown command: {cmd}")
        print("Usage: python3 moltbook-queue.py [status|next|history]")

if __name__ == "__main__":
    main()
