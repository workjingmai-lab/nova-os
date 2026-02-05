#!/usr/bin/env python3
"""Quick Moltbook engagement check - find recent posts to interact with."""

import requests
import json
from datetime import datetime

def main():
    # Moltbook API endpoint for feed
    url = "https://www.moltbook.com/api/v1/feed"
    headers = {"Authorization": "Bearer moltbook_sk_xSwszjAM8vLLaa7VsSZVgNWp5a-R5XqD"}

    try:
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code == 200:
            posts = resp.json().get('posts', [])[:5]  # Last 5 posts
            print(f"📱 Recent Moltbook activity ({len(posts)} posts):\n")
            for p in posts:
                author = p.get('author', 'Unknown')
                content = p.get('content', '')[:80]
                likes = p.get('likes', 0)
                print(f"  • {author}: {content}... ({likes}❤️)")
            print("\n💡 Engagement: Like posts, comment thoughtfully, follow interesting agents")
        else:
            print(f"⚠️ API error: {resp.status_code}")
    except Exception as e:
        print(f"⚠️ Connection error: {e}")

if __name__ == "__main__":
    main()
