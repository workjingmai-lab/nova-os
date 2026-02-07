#!/usr/bin/env python3
"""
Moltbook Rate Limit Checker

Quick check if Moltbook API is rate limited before attempting to post.
Saves time by avoiding failed publish attempts.

Usage:
    python3 tools/moltbook-ratelimit-check.py

Output:
    ✓ OK: Can post
    ✗ RATE LIMITED: Wait before posting
"""

import requests
import json
import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

MOLTBOOK_API_BASE = "https://www.moltbook.com/api/v1"

def check_ratelimit():
    """Check if Moltbook API is rate limited by attempting a lightweight call."""

    # Try to get agent status (lightweight call)
    try:
        response = requests.get(
            f"{MOLTBOOK_API_BASE}/agents/status",
            headers={
                "Authorization": f"Bearer {os.getenv('MOLTBOOK_TOKEN', 'YOUR_MOLTBOOK_TOKEN_HERE')}",
                "Content-Type": "application/json"
            },
            timeout=5
        )

        if response.status_code == 429:
            return "RATE_LIMITED"
        elif response.status_code == 200:
            return "OK"
        elif response.status_code == 401:
            return "AUTH_ERROR"
        else:
            return f"UNKNOWN_{response.status_code}"

    except requests.exceptions.Timeout:
        return "TIMEOUT"
    except requests.exceptions.RequestException as e:
        return f"ERROR: {str(e)[:50]}"

def main():
    status = check_ratelimit()

    if status == "OK":
        print("✓ OK: Can post")
        return 0
    elif status == "RATE_LIMITED":
        print("✗ RATE LIMITED: Wait before posting")
        return 1
    elif status == "AUTH_ERROR":
        print("✗ AUTH ERROR: Check token")
        return 2
    elif status == "TIMEOUT":
        print("✗ TIMEOUT: API not responding")
        return 3
    else:
        print(f"✗ {status}")
        return 4

if __name__ == "__main__":
    exit(main())
