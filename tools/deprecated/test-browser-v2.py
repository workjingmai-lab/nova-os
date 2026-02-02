#!/usr/bin/env python3
"""
Improved detection logic - filter out false positives
"""

import subprocess
import json
import re

# More specific detection patterns (not just "robot")
REAL_DETECTION = [
    "are you a robot",
    "please complete the security check",
    "human verification",
    "we need to make sure you're not a robot",
    "unusual traffic",
    "captcha",
    "enter the characters you see",
    "your access has been rate limited",
    "you have been blocked",
    "access denied",
    "security verification",
]

# False positive patterns (appear in normal pages)
IGNORE_PATTERNS = [
    "robots.txt",
    "robot.txt",
    "bingbot",
    "googlebot",
    "user-agent",
    "robotics",
]

def is_real_detection(content):
    """Check if it's actual bot detection, not just mentioning robots"""
    content_lower = content.lower()

    # Filter out false positives
    for ignore in IGNORE_PATTERNS:
        if ignore in content_lower:
            # Check if it's just in a meta tag or tech context
            if "meta name=" in content_lower or "content-type" in content_lower:
                continue

    # Check for real detection
    for pattern in REAL_DETECTION:
        if pattern in content_lower:
            return pattern

    return None

def test_site_detailed(name, url):
    """Detailed test of a single site"""
    print(f"\n{'='*60}")
    print(f"Testing: {name}")
    print(f"URL: {url}")
    print('='*60)

    try:
        result = subprocess.run(
            ["python3", "/home/node/.openclaw/workspace/tools/lightweight-browser.py", "get", url],
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode != 0:
            print(f"❌ EXECUTION FAILED")
            print(f"   Error: {result.stderr[:200]}")
            return False

        data = json.loads(result.stdout)

        if not data.get("ok"):
            print(f"❌ FETCH FAILED")
            print(f"   Error: {data.get('error', 'Unknown')}")
            return False

        status = data.get("status")
        content = data.get("content", "")
        content_length = len(content)

        print(f"✅ Status: {status}")
        print(f"📊 Content length: {content_length:,} chars")

        # Improved detection check
        detected = is_real_detection(content[:15000])
        if detected:
            print(f"⚠️  REAL DETECTION: '{detected}'")
            # Show snippet
            snippet = content[:500]
            print(f"   Content: {snippet[:200]}...")
            return False

        # Extract title
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        if title_match:
            title = title_match.group(1).strip()[:80]
            print(f"✅ Valid HTML")
            print(f"   Title: {title}")

        print(f"✅ PASS - Site accessible")
        return True

    except subprocess.TimeoutExpired:
        print(f"❌ TIMEOUT (30s)")
        return False
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

def main():
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

    print("🧪 Improved Bot Detection Test")
    print("="*60)

    results = {}
    passed = 0
    failed = 0

    for name, url in SITES:
        success = test_site_detailed(name, url)
        results[name] = success

        if success:
            passed += 1
        else:
            failed += 1

    # Summary
    print(f"\n{'='*60}")
    print("📊 FINAL RESULTS")
    print('='*60)
    print(f"✅ Passed: {passed}/10")
    print(f"❌ Failed: {failed}/10")
    print(f"📈 Success Rate: {passed*10}%")

    print("\nDetailed breakdown:")
    for name, success in results.items():
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"  {status}: {name}")

    if failed == 0:
        print("\n🎉 ALL TESTS PASSED!")
        return 0
    else:
        print(f"\n⚠️  {failed} sites still blocking. Need more stealth improvements.")
        return 1

if __name__ == "__main__":
    import sys
    sys.exit(main())
