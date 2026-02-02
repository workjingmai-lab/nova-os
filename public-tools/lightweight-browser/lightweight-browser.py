#!/usr/bin/env python3
"""
Nova's Lightweight Browser — HTTP-based, no Chromium overhead

Capabilities:
- GET/POST requests with auth headers
- JSON API calls (Moltbook, etc.)
- HTML fetching and parsing
- Cookie handling
- Form submission

Usage:
    python lightweight-browser.py get https://example.com
    python lightweight-browser.py post https://api.example.com/data --json '{"key": "value"}'
    python lightweight-browser.py api https://www.moltbook.com/api/v1/feed --token TOKEN
"""

import sys
import json
import argparse
from urllib.parse import urlparse
import subprocess
import random
import os

# Try requests first (most common), fall back to curl
try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

# Decompression support
try:
    import gzip
    import zlib
    HAS_DECOMPRESSION = True
except ImportError:
    HAS_DECOMPRESSION = False

# Stealth: Realistic User-Agents that rotate
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0",
]

# Session storage for cookie persistence
SESSION_FILE = "/home/node/.openclaw/workspace/data/.browser_session.json"

def load_session():
    """Load session cookies from file"""
    try:
        if os.path.exists(SESSION_FILE):
            with open(SESSION_FILE, 'r') as f:
                return json.load(f)
    except:
        pass
    return {}

def save_session(session_data):
    """Save session cookies to file"""
    try:
        os.makedirs(os.path.dirname(SESSION_FILE), exist_ok=True)
        with open(SESSION_FILE, 'w') as f:
            json.dump(session_data, f, indent=2)
    except:
        pass

def get_stealth_headers(url=None):
    """Generate realistic browser headers"""
    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9,en-GB;q=0.8,en;q=0.7",
        # Remove Accept-Encoding - let requests handle compression
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
    }

    # Add Referer if URL provided (simulate navigation)
    if url:
        parsed = urlparse(url)
        headers["Referer"] = f"{parsed.scheme}://{parsed.netloc}/"

    return headers

def requests_get(url, headers=None, cookies=None):
    """Fetch URL using requests library with stealth"""
    session_data = load_session()

    # Merge stealth headers with custom headers
    stealth = get_stealth_headers(url)
    if headers:
        stealth.update(headers)

    # Use session cookies if available
    session_cookies = session_data.get("cookies", {})
    if cookies:
        session_cookies.update(cookies)

    try:
        # Create session for cookie handling
        session = requests.Session()
        resp = session.get(url, headers=stealth, cookies=session_cookies, timeout=30)

        # Save new cookies
        session_data["cookies"] = dict(session.cookies)
        save_session(session_data)

        # Handle encoding properly
        content = resp.text
        if not content and resp.content:
            # Fallback: decode manually if resp.text is empty
            content = resp.content.decode('utf-8', errors='ignore')

        return {
            "status": resp.status_code,
            "headers": dict(resp.headers),
            "content": content,
            "json": None,
            "ok": resp.ok,
            "cookies": dict(resp.cookies),
            "url": resp.url  # Final URL after redirects
        }
    except Exception as e:
        return {"error": str(e), "ok": False}

def requests_post(url, data=None, json_data=None, headers=None, cookies=None):
    """POST using requests library with stealth"""
    session_data = load_session()

    # Merge stealth headers with custom headers
    stealth = get_stealth_headers(url)
    if headers:
        stealth.update(headers)

    # Use session cookies if available
    session_cookies = session_data.get("cookies", {})
    if cookies:
        session_cookies.update(cookies)

    try:
        # Create session for cookie handling
        session = requests.Session()
        resp = session.post(url, data=data, json=json_data, headers=stealth, cookies=session_cookies, timeout=30)

        # Save new cookies
        session_data["cookies"] = dict(session.cookies)
        save_session(session_data)

        result = {
            "status": resp.status_code,
            "headers": dict(resp.headers),
            "content": resp.text,
            "ok": resp.ok,
            "cookies": dict(resp.cookies),
            "url": resp.url
        }
        try:
            result["json"] = resp.json()
        except:
            result["json"] = None
        return result
    except Exception as e:
        return {"error": str(e), "ok": False}

def curl_get(url, headers=None):
    """Fetch URL using curl (fallback)"""
    header_args = []
    if headers:
        for k, v in headers.items():
            header_args.extend(["-H", f"{k}: {v}"])

    try:
        result = subprocess.run(
            ["curl", "-s", "-i", *header_args, url],
            capture_output=True,
            text=True,
            timeout=30
        )
        return {
            "status": None,
            "content": result.stdout,
            "ok": True
        }
    except Exception as e:
        return {"error": str(e), "ok": False}

def curl_post(url, data=None, json_data=None, headers=None):
    """POST using curl (fallback)"""
    args = ["curl", "-s", "-i", "-X", "POST"]

    if headers:
        for k, v in headers.items():
            args.extend(["-H", f"{k}: {v}"])

    if json_data:
        args.extend(["-H", "Content-Type: application/json"])
        args.extend(["-d", json.dumps(json_data)])
    elif data:
        args.extend(["-d", data])

    args.append(url)

    try:
        result = subprocess.run(args, capture_output=True, text=True, timeout=30)
        return {
            "status": None,
            "content": result.stdout,
            "ok": True
        }
    except Exception as e:
        return {"error": str(e), "ok": False}

def moltbook_api(endpoint, token, method="GET", data=None):
    """Moltbook API helper"""
    url = f"https://www.moltbook.com/api/v1{endpoint}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    if HAS_REQUESTS:
        if method.upper() == "POST":
            return requests_post(url, json_data=data, headers=headers)
        else:
            return requests_get(url, headers=headers)
    else:
        if method.upper() == "POST":
            return curl_post(url, json_data=data, headers=headers)
        else:
            return curl_get(url, headers=headers)

def main():
    parser = argparse.ArgumentParser(description="Lightweight HTTP Browser")
    subparsers = parser.add_subparsers(dest="command", help="Command")

    # GET
    get_parser = subparsers.add_parser("get", help="Fetch URL")
    get_parser.add_argument("url", help="URL to fetch")
    get_parser.add_argument("-H", "--header", action="append", help="Headers (key: value)")
    get_parser.add_argument("--show-headers", action="store_true", help="Show response headers")

    # POST
    post_parser = subparsers.add_parser("post", help="POST to URL")
    post_parser.add_argument("url", help="URL to POST to")
    post_parser.add_argument("--json", help="JSON data to POST")
    post_parser.add_argument("--data", help="Form data to POST")
    post_parser.add_argument("-H", "--header", action="append", help="Headers")

    # API (Moltbook specific)
    api_parser = subparsers.add_parser("api", help="Moltbook API call")
    api_parser.add_argument("endpoint", help="API endpoint (e.g., /feed)")
    api_parser.add_argument("--token", required=True, help="Auth token")
    api_parser.add_argument("--method", default="GET", help="HTTP method")
    api_parser.add_argument("--data", help="JSON data for POST")

    # Search
    search_parser = subparsers.add_parser("search", help="Web search (stealth mode)")
    search_parser.add_argument("query", help="Search query")
    search_parser.add_argument("--engine", default="google", choices=["google", "bing", "duckduckgo"], help="Search engine")

    # Clear session
    session_parser = subparsers.add_parser("clear-session", help="Clear cookies and session data")
    session_parser.add_argument("--confirm", action="store_true", help="Confirm deletion")

    args = parser.parse_args()

    if args.command == "get":
        headers = {}
        if args.header:
            for h in args.header:
                if ":" in h:
                    k, v = h.split(":", 1)
                    headers[k.strip()] = v.strip()

        if HAS_REQUESTS:
            result = requests_get(args.url, headers if headers else None)
        else:
            result = curl_get(args.url, headers if headers else None)

        print(json.dumps(result, indent=2))

    elif args.command == "post":
        headers = {}
        if args.header:
            for h in args.header:
                if ":" in h:
                    k, v = h.split(":", 1)
                    headers[k.strip()] = v.strip()

        json_data = json.loads(args.json) if args.json else None

        if HAS_REQUESTS:
            result = requests_post(args.url, data=args.data, json_data=json_data, headers=headers if headers else None)
        else:
            result = curl_post(args.url, data=args.data, json_data=json_data, headers=headers if headers else None)

        print(json.dumps(result, indent=2))

    elif args.command == "api":
        data = json.loads(args.data) if args.data else None
        result = moltbook_api(args.endpoint, args.token, args.method, data)
        print(json.dumps(result, indent=2))

    elif args.command == "search":
        # Build search URL
        engines = {
            "google": "https://www.google.com/search?q={}",
            "bing": "https://www.bing.com/search?q={}",
            "duckduckgo": "https://html.duckduckgo.com/html/?q={}"
        }
        url = engines[args.engine].format(args.query.replace(" ", "+"))

        if HAS_REQUESTS:
            result = requests_get(url)
        else:
            result = curl_get(url)

        if result.get("ok"):
            print(f"✅ Search results for '{args.query}' ({args.engine}):")
            print(f"Status: {result['status']}")
            print(f"Content length: {len(result.get('content', ''))} chars")
            print(f"\nFirst 500 chars:")
            print(result.get('content', '')[:500])
        else:
            print(f"❌ Search failed: {result}")

    elif args.command == "clear-session":
        if not args.confirm:
            print("❌ Error: Use --confirm to clear session data")
            return 1

        try:
            if os.path.exists(SESSION_FILE):
                os.remove(SESSION_FILE)
                print("✅ Session cleared (cookies removed)")
                return 0
            else:
                print("✅ No session data to clear")
                return 0
        except Exception as e:
            print(f"❌ Error clearing session: {e}")
            return 1

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
