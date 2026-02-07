#!/usr/bin/env python3
"""
twitter-poster.py — Post tweets via cookies

Setup:
1. Export Twitter cookies from browser
2. Save to ~/.twitter_cookies.json
3. Post tweets

Usage:
    python3 tools/twitter-poster.py --tweet "Your message here"
    python3 tools/twitter-poster.py --thread tweet_thread.md
"""

import json
import requests
from pathlib import Path
import sys

COOKIE_FILE = Path.home() / ".twitter_cookies.json"

def load_cookies():
    """Load Twitter cookies from file."""
    if not COOKIE_FILE.exists():
        print("❌ No cookies found.")
        print(f"   Create {COOKIE_FILE} with your Twitter cookies")
        return None

    with open(COOKIE_FILE) as f:
        return json.load(f)

def post_tweet(text, cookies):
    """Post a tweet using cookies."""
    # Twitter API endpoint (via cookies)
    url = "https://twitter.com/i/api/2/tweets"

    headers = {
        "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LFV2rycf9dCdYuXTx0XpbnylPyOsLe817xq3xf8XKcY8zJF9",  # Public guest token
        "Content-Type": "application/json",
        "X-CSRF-Token": cookies.get("ct0", ""),
        "Cookie": "; ".join([f"{k}={v}" for k, v in cookies.items()])
    }

    data = {
        "text": text,
        "media": {"media_entities": []}
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json(), None
    else:
        return None, response.text

def main():
    args = sys.argv[1:]

    if "--tweet" in args:
        idx = args.index("--tweet")
        text = args[idx + 1]

        cookies = load_cookies()
        if not cookies:
            return

        print(f"📤 Posting: {text}")
        result, error = post_tweet(text, cookies)

        if result:
            print("✅ Posted successfully")
            print(f"   Tweet ID: {result.get('data', {}).get('id')}")
        else:
            print(f"❌ Failed: {error}")

    elif "--thread" in args:
        print("Thread posting: TODO")
    else:
        print("Usage:")
        print("  python3 tools/twitter-poster.py --tweet 'Your message'")
        print("  python3 tools/twitter-poster.py --thread thread_file.md")

if __name__ == "__main__":
    main()
