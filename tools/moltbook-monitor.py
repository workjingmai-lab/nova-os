#!/usr/bin/env python3
"""
Moltbook Activity Monitor
Checks for new posts and mentions since last check.
"""

import json
import sys
from pathlib import Path
from datetime import datetime

# Moltbook API endpoint and token
API_BASE = "https://www.moltbook.com/api/v1"
API_TOKEN = "moltbook_sk_xSwszjAM8vLLaa7VsSZVgNWp5a-R5XqD"

# State file
STATE_FILE = Path.home() / ".openclaw/workspace/.heartbeat_state.json"


def load_state():
    """Load heartbeat state."""
    if STATE_FILE.exists():
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"version": 1}


def save_state(state):
    """Save heartbeat state."""
    state["lastUpdated"] = int(datetime.now().timestamp())
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def check_claim_status():
    """Check if agent is claimed."""
    import subprocess

    result = subprocess.run(
        [
            "curl",
            "-s",
            f"{API_BASE}/agents/status",
            "-H",
            f"Authorization: Bearer {API_TOKEN}",
        ],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        return None, f"curl failed: {result.stderr}"

    try:
        data = json.loads(result.stdout)
        return data, None
    except json.JSONDecodeError as e:
        return None, f"JSON decode error: {e}"


def check_feed():
    """Check feed for new posts."""
    import subprocess

    result = subprocess.run(
        [
            "curl",
            "-s",
            f"{API_BASE}/feed",
            "-H",
            f"Authorization: Bearer {API_TOKEN}",
        ],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        return None, f"curl failed: {result.stderr}"

    try:
        data = json.loads(result.stdout)
        return data, None
    except json.JSONDecodeError as e:
        return None, f"JSON decode error: {e}"


def main():
    state = load_state()
    last_check = state.get("lastMoltbookCheck", 0)
    # Ensure last_check is an int
    if isinstance(last_check, str):
        try:
            last_check = int(last_check)
        except ValueError:
            last_check = 0

    # Check claim status
    status_data, err = check_claim_status()
    if err:
        print(f"ERROR checking claim status: {err}", file=sys.stderr)
        return 1

    # Check feed
    feed_data, err = check_feed()
    if err:
        print(f"ERROR checking feed: {err}", file=sys.stderr)
        return 1

    # Update last check time
    state["lastMoltbookCheck"] = int(datetime.now().timestamp())
    save_state(state)

    # Analyze results
    claimed = status_data.get("claimed", False) if status_data else False
    posts = feed_data.get("posts", []) if feed_data else []

    # Look for new posts (simplified check)
    new_posts = []
    for post in posts:
        post_time = post.get("created_at", 0)
        # Convert to int if it's a string
        if isinstance(post_time, str):
            try:
                post_time = int(post_time)
            except ValueError:
                post_time = 0
        if post_time > last_check:
            new_posts.append(post)

    # Check for mentions
    mentions = []
    for post in posts:
        content = post.get("content") or ""
        if "@nova" in content.lower() or "@orbit" in content.lower():
            mentions.append(post)

    # Output results
    if new_posts:
        print(f"📬 NEW POSTS ({len(new_posts)}):")
        for post in new_posts[:5]:  # Limit to 5 most recent
            author = post.get("author", {}).get("username", "unknown")
            content = post.get("content", "")[:100]
            print(f"  • @{author}: {content}...")
        print()

    if mentions:
        print(f"🏷️  MENTIONS ({len(mentions)}):")
        for post in mentions[:5]:
            author = post.get("author", {}).get("username", "unknown")
            content = post.get("content", "")[:100]
            print(f"  • @{author}: {content}...")
        print()

    # Status summary
    status_icon = "✅" if claimed else "⚠️"
    print(f"{status_icon} Claimed: {claimed}")
    print(f"📊 Total posts in feed: {len(posts)}")
    print(f"🆕 New since last check: {len(new_posts)}")
    print(f"🏷️  Mentions found: {len(mentions)}")

    # Return code based on activity
    if new_posts or mentions:
        return 0  # Activity found
    else:
        return 99  # No activity (special code for HEARTBEAT_OK)


if __name__ == "__main__":
    sys.exit(main())
