#!/usr/bin/env python3
"""
Final browser test - checks if pages actually loaded meaningful content
"""

import subprocess
import json
import re

# Each site: what content should appear if page loaded successfully
SUCCESS_MARKERS = {
    "Google": ["search", "google", "google search"],
    "YouTube": ["youtube", "video", "home"],
    "Facebook": ["facebook", "log in", "sign up"],
    "Twitter": ["twitter", "sign up", "log in"],
    "Instagram": ["instagram", "sign up", "log in"],
    "Amazon": ["amazon", "cart", "today's deals"],
    "Reddit": ["reddit", "popular", "home"],
    "Wikipedia": ["wikipedia", "free encyclopedia", "article"],
    "GitHub": ["github", "sign up", "pricing"],
    "LinkedIn": ["linkedin", "sign in", "join now"],
}

def page_loaded(name, content):
    """Check if page has expected content"""
    content_lower = content.lower()
    markers = SUCCESS_MARKERS.get(name, [])

    for marker in markers:
        if marker in content_lower:
            return True, marker

    return False, None

def test_site_final(name, url):
    """Final comprehensive test"""
    print(f"\n{'='*60}")
    print(f"Testing: {name}")
    print('='*60)

    try:
        result = subprocess.run(
            ["python3", "/home/node/.openclaw/workspace/tools/lightweight-browser.py", "get", url],
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode != 0:
            print(f"❌ EXECUTION ERROR")
            print(f"   {result.stderr[:200]}")
            return False

        data = json.loads(result.stdout)

        if not data.get("ok"):
            print(f"❌ REQUEST FAILED: {data.get('error')}")
            return False

        status = data.get("status")
        content = data.get("content", "")

        print(f"✅ HTTP {status}")
        print(f"📊 {len(content):,} bytes received")

        # Check for meaningful content
        loaded, marker = page_loaded(name, content)
        if loaded:
            print(f"✅ PAGE LOADED (found: '{marker}')")

            # Extract title
            title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
            if title_match:
                title = title_match.group(1).strip()[:60]
                print(f"   Title: {title}")

            return True
        else:
            print(f"❌ CONTENT MISSING (no expected markers found)")
            print(f"   First 200 chars: {content[:200]}")
            return False

    except subprocess.TimeoutExpired:
        print(f"❌ TIMEOUT")
        return False
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

def main():
    print("🎯 Final Browser Test - Content Validation")
    print("="*60)

    SITES = [
        ("Google", "https://www.google.com"),
        ("YouTube", "https://www.youtube.com"),
        ("Facebook", "https://www.facebook.com"),
        ("Twitter", "https://twitter.com"),
        ("Instagram", "https://www.instagram.com"),
        ("Amazon", "https://www.amazon.com"),
        ("Reddit", "https://www.reddit.com"),
        ("Wikipedia", "https://en.wikipedia.org"),
        ("GitHub", "https://github.com"),
        ("LinkedIn", "https://www.linkedin.com"),
    ]

    results = {}
    for name, url in SITES:
        success = test_site_final(name, url)
        results[name] = success

    # Summary
    print(f"\n{'='*60}")
    print("📊 FINAL RESULTS")
    print('='*60)

    passed = sum(1 for s in results.values() if s)
    failed = len(results) - passed

    print(f"✅ Passed: {passed}/10")
    print(f"❌ Failed: {failed}/10")
    print(f"📈 Success: {passed*10}%")

    print("\nSite breakdown:")
    for name, success in results.items():
        print(f"  {'✅' if success else '❌'} {name}")

    if passed >= 8:
        print(f"\n🎉 EXCELLENT! {passed}/10 sites accessible!")
        print("   Browser is production-ready.")
        return 0
    elif passed >= 6:
        print(f"\n✅ GOOD! {passed}/10 sites accessible.")
        print("   Browser works for most use cases.")
        return 0
    else:
        print(f"\n⚠️  Need improvements: {passed}/10 only.")
        return 1

if __name__ == "__main__":
    import sys
    sys.exit(main())
