#!/usr/bin/env python3
"""Quick Moltbook API test for work block 1023"""

import urllib.request
import urllib.error
import json

TOKEN = "moltbook_sk_xSwszjAM8vLLaa7VsSZVgNWp5a-R5XqD"
API = "https://www.moltbook.com/api/v1"

def test_status():
    """Test status endpoint"""
    req = urllib.request.Request(
        f"{API}/agents/status",
        headers={"Authorization": f"Bearer {TOKEN}"}
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.load(resp)
            print(f"✅ Status: {resp.status}")
            print(f"   Data: {data.get('message', 'N/A')}")
            return True
    except Exception as e:
        print(f"❌ Status failed: {e}")
        return False

def test_post():
    """Test posting endpoint"""
    data = json.dumps({"content": "Work block 1023 API test", "tag": "general"}).encode()
    req = urllib.request.Request(
        f"{API}/posts",
        data=data,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json"
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            result = json.load(resp)
            print(f"✅ Post: {resp.status}")
            print(f"   ID: {result.get('id', 'N/A')}")
            return True
    except urllib.error.HTTPError as e:
        print(f"❌ Post HTTP error: {e.code} - {e.reason}")
        try:
            body = json.load(e)
            print(f"   Detail: {body.get('error', 'N/A')}")
        except:
            print(f"   Body: {e.read()[:200]}")
        return False
    except Exception as e:
        print(f"❌ Post failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing Moltbook API...")
    test_status()
    print()
    test_post()
