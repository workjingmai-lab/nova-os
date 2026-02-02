#!/usr/bin/env python3
"""
Test lightweight browser against popular websites
Checks for bot detection, captchas, and access issues
"""

import subprocess
import json
import re

SITES = [
    ("Google", "https://www.google.com"),
    ("YouTube", "https://www.youtube.com"),
    ("Facebook", "https://www.facebook.com"),
    ("Twitter/X", "https://twitter.com"),
    ("Instagram", "https://www.instagram.com"),
    ("Amazon", "https://www.amazon.com"),
    ("Reddit", "https://www.reddit.com"),
    ("Wikipedia", "https://en.wikipedia.org"),
    ("GitHub", "https://github.com"),
    ("LinkedIn", "https://www.linkedin.com"),
]

# Detection keywords
DETECTION_PATTERNS = [
    "captcha",
    "robot",
    "bot detection",
    "access denied",
    "unable to process",
    "please verify",
    "security check",
    "human verification",
    "we've detected",
    "suspicious activity",
    "enter the characters",
    "i'm not a robot",
]

def fetch_url(url):
    """Fetch URL using lightweight browser"""
    try:
        result = subprocess.run(
            ["python3", "/home/node/.openclaw/workspace/tools/lightweight-browser.py", "get", url],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            return json.loads(result.stdout)
        else:
            return {"ok": False, "error": result.stderr}
    except Exception as e:
        return {"ok": False, "error": str(e)}

def detect_bot_page(content):
    """Check if content contains bot detection markers"""
    content_lower = content.lower()
    for pattern in DETECTION_PATTERNS:
        if pattern in content_lower:
            return pattern
    return None

def test_site(name, url):
    """Test a single site"""
    print(f"\n{'='*60}")
    print(f"Testing: {name}")
    print(f"URL: {url}")
    print('='*60)

    result = fetch_url(url)

    if not result.get("ok"):
        print(f"❌ FAILED: {result.get('error', 'Unknown error')}")
        return False

    status = result.get("status")
    content = result.get("content", "")
    content_length = len(content)

    print(f"✅ Status: {status}")
    print(f"📊 Content length: {content_length:,} chars")

    # Check for bot detection
    detected = detect_bot_page(content[:10000])  # Check first 10KB
    if detected:
        print(f"⚠️  DETECTION TRIGGERED: '{detected}'")
        print(f"   First 300 chars: {content[:300]}")
        return False

    # Check if it looks like HTML
    if content_length > 0:
        if "<!DOCTYPE html" in content or "<html" in content[:200].lower():
            print(f"✅ Valid HTML response")
            # Show title if available
            title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
            if title_match:
                title = title_match.group(1).strip()
                if len(title) > 80:
                    title = title[:80] + "..."
                print(f"   Title: {title}")
        else:
            print(f"⚠️  Non-HTML response")
            print(f"   First 100 chars: {content[:100]}")

    return True

def main():
    print("🧪 Testing Lightweight Browser Against Popular Sites")
    print("="*60)

    passed = 0
    failed = 0
    results = {}

    for name, url in SITES:
        success = test_site(name, url)
        results[name] = {
            "url": url,
            "success": success,
            "status": "✅ PASS" if success else "❌ FAIL"
        }

        if success:
            passed += 1
        else:
            failed += 1

    # Summary
    print(f"\n{'='*60}")
    print("📊 SUMMARY")
    print('='*60)
    print(f"Passed: {passed}/10")
    print(f"Failed: {failed}/10")
    print(f"Success Rate: {passed*10}%")

    print("\nDetailed Results:")
    for name, result in results.items():
        print(f"  {result['status']}: {name}")

    if failed == 0:
        print("\n🎉 ALL TESTS PASSED! Browser is undetectable!")
        return 0
    else:
        print(f"\n⚠️  {failed} site(s) had issues. Check logs above.")
        return 1

if __name__ == "__main__":
    import sys
    sys.exit(main())
