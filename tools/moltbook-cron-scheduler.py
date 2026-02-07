#!/usr/bin/env python3
"""
moltbook-cron-scheduler.py - Schedule Moltbook posts via cron
Auto-posts when rate limit expires, handles queue management
"""

import subprocess
import json
import os
from datetime import datetime, timedelta

QUEUE_FILE = "data/moltbook-queue.json"
LOG_FILE = "data/moltbook-post-log.json"

def load_queue():
    """Load post queue from file"""
    if not os.path.exists(QUEUE_FILE):
        return []
    with open(QUEUE_FILE, 'r') as f:
        data = json.load(f)
        return data.get('posts', [])

def load_log():
    """Load post history log"""
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, 'r') as f:
        return json.load(f)

def get_last_post_time():
    """Get timestamp of last successful post"""
    log = load_log()
    if not log:
        return None
    return datetime.fromisoformat(log[-1]['timestamp'])

def can_post(cooldown_minutes=10):
    """Check if enough time has passed since last post"""
    last = get_last_post_time()
    if not last:
        return True
    elapsed = datetime.now() - last
    return elapsed >= timedelta(minutes=cooldown_minutes)

def schedule_next_post():
    """Schedule cron job for next post attempt"""
    if not can_post():
        # Schedule for 10 min from now
        next_time = datetime.now() + timedelta(minutes=10)
        print(f"⏰ Rate limit active. Next attempt: {next_time.strftime('%H:%M')}")
        return
    
    queue = load_queue()
    if not queue:
        print("📭 Queue empty. Nothing to schedule.")
        return
    
    print(f"📤 Attempting post: {queue[0]['title'][:50]}...")
    # This would call moltbook-suite.py
    subprocess.run(["python3", "tools/moltbook-suite.py", "post", "--next"])

def status():
    """Show current queue status"""
    queue = load_queue()
    log = load_log()
    last = get_last_post_time()
    
    print("📊 Moltbook Queue Status\n")
    print(f"  Queue size:    {len(queue)} posts")
    print(f"  Posted today:  {len([p for p in log if p['timestamp'].startswith(datetime.now().strftime('%Y-%m-%d'))])}")
    
    if last:
        elapsed = datetime.now() - last
        cooldown = timedelta(minutes=10)
        remaining = cooldown - elapsed
        
        if remaining.total_seconds() > 0:
            print(f"  Rate limit:    {int(remaining.total_seconds() / 60)} min remaining")
        else:
            print(f"  Rate limit:    ✅ Ready to post")
    else:
        print(f"  Rate limit:    ✅ Ready to post (no history)")
    
    if queue:
        print(f"\n  Next in queue: {queue[0]['title'][:50]}...")

def main():
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "status":
            status()
        elif sys.argv[1] == "schedule":
            schedule_next_post()
        elif sys.argv[1] == "can-post":
            print("yes" if can_post() else "no")
        else:
            print("Usage: moltbook-cron-scheduler.py [status|schedule|can-post]")
    else:
        status()

if __name__ == "__main__":
    main()
