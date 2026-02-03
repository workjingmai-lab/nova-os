#!/usr/bin/env python3
"""
Moltbook Poster — Post content using lightweight browser

Usage:
    python moltbook-poster.py post "Your post content here" --tag agents --tag productivity
    python moltbook-poster.py post --file ./my-post.md --tag agent-life
"""

import sys
import os
import json
import argparse
import re

# Add tools directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def moltbook_api(endpoint, token, method="GET", data=None):
    """Moltbook API helper (inline from lightweight-browser.py)"""
    import subprocess
    from urllib.parse import urljoin

    url = f"https://www.moltbook.com/api/v1{endpoint}"

    # Try requests first
    try:
        import requests
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        if method.upper() == "POST":
            resp = requests.post(url, json=data, headers=headers, timeout=30)
        else:
            resp = requests.get(url, headers=headers, timeout=30)
        return {
            "ok": resp.ok,
            "status": resp.status_code,
            "content": resp.text,
            "json": resp.json() if resp.headers.get("content-type", "").startswith("application/json") else None
        }
    except ImportError:
        # Fall back to curl
        args = ["curl", "-s", "-i", "-X", method,
                "-H", f"Authorization: Bearer {token}",
                "-H", "Content-Type: application/json"]
        if data:
            args.extend(["-d", json.dumps(data)])
        args.append(url)

        result = subprocess.run(args, capture_output=True, text=True, timeout=30)
        return {
            "ok": result.returncode == 0,
            "content": result.stdout
        }

MOLTBOOK_TOKEN = "moltbook_sk_xSwszjAM8vLLaa7VsSZVgNWp5a-R5XqD"
MOLTBOOK_API = "https://www.moltbook.com/api/v1"
HEARTBEAT_STATE = "/home/node/.openclaw/workspace/.heartbeat_state.json"

def read_file(filepath):
    """Read content from file"""
    try:
        with open(filepath, 'r') as f:
            return f.read().strip()
    except Exception as e:
        return None

def extract_tags(content):
    """Extract hashtags from content"""
    return re.findall(r'#(\w+)', content)

def clean_content(content):
    """Remove tags from content (API handles them separately)"""
    return re.sub(r'#\S+', '', content).strip()

def load_heartbeat_state():
    """Load heartbeat state to check last post time"""
    try:
        with open(HEARTBEAT_STATE, 'r') as f:
            return json.load(f)
    except Exception:
        return {}

def save_heartbeat_state(state):
    """Save heartbeat state"""
    try:
        with open(HEARTBEAT_STATE, 'w') as f:
            json.dump(state, f, indent=2)
    except Exception:
        pass

def check_rate_limit():
    """Check if we're within the 30-minute rate limit"""
    import time

    state = load_heartbeat_state()
    last_post = state.get("lastMoltbookPost")

    if not last_post:
        return None  # No previous post, clear to post

    # Calculate minutes since last post
    current_time = int(time.time())
    minutes_since = (current_time - last_post) / 60

    if minutes_since < 30:
        return 30 - int(minutes_since)  # Minutes remaining

    return None  # Clear to post

def post_to_moltbook(content, tags=None, image_url=None, title=None, submolt="general"):
    """Post content to Moltbook"""
    import time

    endpoint = "/posts"

    # Generate title from content if not provided
    if not title:
        lines = clean_content(content).split('\n')
        title = lines[0][:50] + "..." if len(lines[0]) > 50 else lines[0]

    data = {
        "title": title,
        "content": clean_content(content),
        "submolt": submolt,
        "tags": tags or []
    }

    if image_url:
        data["imageUrl"] = image_url

    result = moltbook_api(
        endpoint,
        MOLTBOOK_TOKEN,
        method="POST",
        data=data
    )

    # Save last post time on success
    if result.get("ok"):
        state = load_heartbeat_state()
        state["lastMoltbookPost"] = int(time.time())
        save_heartbeat_state(state)

    return result

def main():
    parser = argparse.ArgumentParser(description="Post to Moltbook")
    parser.add_argument("content", nargs="?", help="Post content (or use --file)")
    parser.add_argument("--file", help="Read post from file")
    parser.add_argument("--tag", action="append", help="Tags (can use multiple times)")
    parser.add_argument("--image", help="Image URL to attach")
    parser.add_argument("--title", help="Post title")
    parser.add_argument("--submolt", default="general", help="Submolt to post to (default: general)")
    parser.add_argument("--dry-run", action="store_true", help="Preview without posting")
    parser.add_argument("--force", action="store_true", help="Bypass rate limit check (attempt anyway)")

    args = parser.parse_args()

    # Get content
    if args.file:
        content = read_file(args.file)
        if not content:
            print(f"❌ Error: Could not read file: {args.file}")
            return 1
    elif args.content:
        content = args.content
    else:
        # Read from stdin
        content = sys.stdin.read().strip()
        if not content:
            parser.print_help()
            return 1

    # Extract tags from content if none provided
    tags = args.tag or []
    if not tags:
        tags = extract_tags(content)

    # Clean content (remove tags for API)
    clean = clean_content(content)

    # Check rate limit
    wait_minutes = check_rate_limit()
    if wait_minutes and not args.force:
        print(f"⏸️ Rate limit active: {wait_minutes} minutes remaining")
        print(f"Wait until cooldown expires or use --force to attempt anyway")
        return 1
    elif wait_minutes and args.force:
        print(f"⚠️ Bypassing rate limit ({wait_minutes} min remaining)")
        print(f"Post may fail — API enforcement takes priority")

    # Preview
    print("📝 Post Preview:")
    print(f"Content: {clean[:100]}{'...' if len(clean) > 100 else ''}")
    print(f"Tags: {', '.join(tags) if tags else 'none'}")
    if args.image:
        print(f"Image: {args.image}")
    print()

    if args.dry_run:
        print("✅ Dry run complete — not posting")
        return 0

    # Post
    print("📤 Posting to Moltbook...")
    result = post_to_moltbook(content, tags, args.image, args.title, args.submolt)

    if result.get("ok"):
        print("✅ Post successful!")
        if result.get("json"):
            print(json.dumps(result["json"], indent=2))
        return 0
    else:
        print("❌ Post failed!")
        print(json.dumps(result, indent=2))
        return 1

if __name__ == "__main__":
    sys.exit(main())
