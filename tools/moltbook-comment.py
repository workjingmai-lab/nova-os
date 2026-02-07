#!/usr/bin/env python3
"""
moltbook-comment.py — Reliable Moltbook commenting with proper JSON handling
Fixes the JSON escaping issues with curl-based posting
"""
import argparse
import json
import urllib.request
import urllib.error
import os

API_BASE = "https://www.moltbook.com/api/v1"
TOKEN = os.getenv("MOLTBOOK_TOKEN", "YOUR_MOLTBOOK_TOKEN_HERE")

def comment_on_post(post_id: str, content: str) -> dict:
    """Post a comment to a Moltbook post with proper JSON encoding."""
    url = f"{API_BASE}/posts/{post_id}/comments"
    
    data = json.dumps({"content": content}).encode('utf-8')
    
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json"
        },
        method="POST"
    )
    
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        return {"error": f"HTTP {e.code}: {e.reason}", "body": e.read().decode('utf-8')}
    except Exception as e:
        return {"error": str(e)}

def main():
    parser = argparse.ArgumentParser(description="Post comments to Moltbook")
    parser.add_argument("post_id", help="UUID of the post to comment on")
    parser.add_argument("content", help="Comment content (can include quotes)")
    args = parser.parse_args()
    
    result = comment_on_post(args.post_id, args.content)
    print(json.dumps(result, indent=2))
    
    if "error" in result:
        exit(1)
    print("✅ Comment posted successfully")

if __name__ == "__main__":
    main()
