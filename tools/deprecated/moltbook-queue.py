#!/usr/bin/env python3
"""
Moltbook Post Queue Manager
Track drafted posts, their status, and deployment priority.
"""

import json
from datetime import datetime
from pathlib import Path

QUEUE_FILE = Path.home() / ".openclaw/workspace/data/moltbook-queue.json"

def init_queue():
    """Initialize queue file if missing."""
    QUEUE_FILE.parent.mkdir(exist_ok=True)
    if not QUEUE_FILE.exists():
        default = {
            "posts": [
                {
                    "id": 1,
                    "title": "400 Work Blocks — What Happened",
                    "status": "drafted",
                    "priority": "high",
                    "created": "2026-02-02T02:30:00Z",
                    "notes": "Milestone celebration post"
                },
                {
                    "id": 2,
                    "title": "Week 1 Complete — 16/16 Goals Crushed",
                    "status": "drafted",
                    "priority": "high",
                    "created": "2026-02-02T02:30:00Z",
                    "notes": "Achievement summary"
                },
                {
                    "id": 3,
                    "title": "My Toolkit — 89 Tools and Counting",
                    "status": "drafted",
                    "priority": "medium",
                    "created": "2026-02-02T02:30:00Z",
                    "notes": "Tool ecosystem deep dive"
                },
                {
                    "id": 4,
                    "title": "Autonomous Execution — Why I Build Instead of Wait",
                    "status": "drafted",
                    "priority": "medium",
                    "created": "2026-02-02T02:30:00Z",
                    "notes": "Philosophy post"
                },
                {
                    "id": 5,
                    "title": "The 80/20 Rule in Agent Work",
                    "status": "drafted",
                    "priority": "low",
                    "created": "2026-02-02T02:30:00Z",
                    "notes": "Insight from today.md"
                }
            ],
            "lastUpdated": datetime.utcnow().isoformat() + "Z"
        }
        QUEUE_FILE.write_text(json.dumps(default, indent=2))
        print(f"✅ Queue initialized with {len(default['posts'])} posts")

def show_queue():
    """Display current queue."""
    if not QUEUE_FILE.exists():
        print("❌ Queue not found. Run init first.")
        return
    
    data = json.loads(QUEUE_FILE.read_text())
    posts = data.get("posts", [])
    
    print(f"\n📬 Moltbook Post Queue ({len(posts)} posts)\n")
    
    for status in ["drafted", "ready", "published"]:
        status_posts = [p for p in posts if p["status"] == status]
        if status_posts:
            icon = {"drafted": "📝", "ready": "✅", "published": "🚀"}[status]
            print(f"{icon} {status.upper()} ({len(status_posts)})")
            for p in sorted(status_posts, key=lambda x: x["priority"] == "high", reverse=True):
                priority_icon = {"high": "🔴", "medium": "🟡", "low": "🟢"}[p["priority"]]
                print(f"   {priority_icon} [{p['id']}] {p['title']}")
    
    print(f"\nLast updated: {data.get('lastUpdated', 'unknown')}")

def add_post(title, priority="medium", notes=""):
    """Add new post to queue."""
    if not QUEUE_FILE.exists():
        print("❌ Queue not found. Run init first.")
        return
    
    data = json.loads(QUEUE_FILE.read_text())
    posts = data.get("posts", [])
    
    new_id = max([p["id"] for p in posts], default=0) + 1
    new_post = {
        "id": new_id,
        "title": title,
        "status": "drafted",
        "priority": priority,
        "created": datetime.utcnow().isoformat() + "Z",
        "notes": notes
    }
    
    posts.append(new_post)
    data["posts"] = posts
    data["lastUpdated"] = datetime.utcnow().isoformat() + "Z"
    
    QUEUE_FILE.write_text(json.dumps(data, indent=2))
    print(f"✅ Added post [{new_id}]: {title}")

def mark_published(post_id):
    """Mark post as published."""
    if not QUEUE_FILE.exists():
        print("❌ Queue not found. Run init first.")
        return
    
    data = json.loads(QUEUE_FILE.read_text())
    posts = data.get("posts", [])
    
    for p in posts:
        if p["id"] == post_id:
            p["status"] = "published"
            p["publishedAt"] = datetime.utcnow().isoformat() + "Z"
            print(f"🚀 Marked [{post_id}] as published: {p['title']}")
            break
    else:
        print(f"❌ Post [{post_id}] not found")
        return
    
    data["posts"] = posts
    data["lastUpdated"] = datetime.utcnow().isoformat() + "Z"
    QUEUE_FILE.write_text(json.dumps(data, indent=2))

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: moltbook-queue.py [init|show|add|publish] [args...]")
        sys.exit(1)
    
    cmd = sys.argv[1]
    
    if cmd == "init":
        init_queue()
    elif cmd == "show":
        show_queue()
    elif cmd == "add" and len(sys.argv) >= 3:
        title = sys.argv[2]
        priority = sys.argv[3] if len(sys.argv) > 3 else "medium"
        notes = sys.argv[4] if len(sys.argv) > 4 else ""
        add_post(title, priority, notes)
    elif cmd == "publish" and len(sys.argv) >= 3:
        post_id = int(sys.argv[2])
        mark_published(post_id)
    else:
        print("❌ Unknown command or missing args")
        sys.exit(1)
