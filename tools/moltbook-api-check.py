#!/usr/bin/env python3
"""
Moltbook API Status Checker

Quick health check for Moltbook API before posting.
Prevents failed posts due to API downtime.

Usage:
    python3 moltbook-api-check.py
"""

import urllib.request
import urllib.error
import sys

def check_api_status():
    """Check Moltbook API health"""
    api_url = "https://www.moltbook.com/api/v1/agents/status"
    token = "moltbook_sk_xSwszjAM8vLLaa7VsSZVgNWp5a-R5XqD"

    try:
        req = urllib.request.Request(
            api_url,
            headers={"Authorization": f"Bearer {token}"}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            status = response.status
            if status == 200:
                print("✅ Moltbook API is healthy")
                return True
            else:
                print(f"⚠️ API returned status {status}")
                return False
    except urllib.error.HTTPError as e:
        print(f"❌ HTTP Error: {e.code} - {e.reason}")
        return False
    except urllib.error.URLError as e:
        print(f"❌ Connection Error: {e.reason}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    healthy = check_api_status()
    sys.exit(0 if healthy else 1)
