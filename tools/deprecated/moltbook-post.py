#!/usr/bin/env python3
"""
Moltbook Poster — Quick content publishing
Uses urllib (no external deps)
"""

import urllib.request
import urllib.error
import json
import sys
import os

API_BASE = "https://www.moltbook.com/api/v1"
TOKEN = os.getenv("MOLTBOOK_TOKEN", "YOUR_MOLTBOOK_TOKEN_HERE")

def post_content(content):
    """Post to Moltbook feed"""
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    data = json.dumps({"content": content}).encode("utf-8")

    req = urllib.request.Request(
        f"{API_BASE}/posts",
        data=data,
        headers=headers,
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            result = json.loads(resp.read().decode())
            print(f"✅ Posted successfully!")
            print(f"   Post ID: {result.get('id')}")
            return True
    except urllib.error.HTTPError as e:
        print(f"❌ HTTP Error {e.code}: {e.reason}")
        try:
            err_body = e.read().decode()
            print(f"   Details: {err_body[:200]}")
        except:
            pass
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: moltbook-post.py 'your content here'")
        print("   or: moltbook-post.py --file path/to/post.md")
        sys.exit(1)

    if sys.argv[1] == "--file":
        if len(sys.argv) < 3:
            print("Error: --file requires a path")
            sys.exit(1)
        with open(sys.argv[2], "r") as f:
            content = f.read()
    else:
        content = sys.argv[1]

    print(f"📝 Posting to Moltbook...")
    print(f"   Content length: {len(content)} chars")

    success = post_content(content)

    if success:
        # Log it
        log_path = "/home/node/.openclaw/workspace/notifications/moltbook-posts.json"
        os.makedirs(os.path.dirname(log_path), exist_ok=True)

        log_entry = {
            "timestamp": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(),
            "content_preview": content[:100] + "..." if len(content) > 100 else content,
            "length": len(content)
        }

        logs = []
        if os.path.exists(log_path):
            with open(log_path, "r") as f:
                logs = json.load(f)
        logs.append(log_entry)

        with open(log_path, "w") as f:
            json.dump(logs, f, indent=2)

    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
