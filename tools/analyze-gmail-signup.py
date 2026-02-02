#!/usr/bin/env python3
"""
Analyze Gmail registration flow for automation
"""

import subprocess
import json
import re

def fetch_page(url):
    """Fetch page using lightweight browser"""
    try:
        result = subprocess.run(
            ["python3", "/home/node/.openclaw/workspace/tools/lightweight-browser.py", "get", url],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            return json.loads(result.stdout)
        return None
    except:
        return None

def analyze_registration():
    """Analyze what's needed for Gmail signup"""

    print("🔍 Analyzing Gmail Registration Flow\n")
    print("="*60)

    # Step 1: Fetch Gmail signup page
    print("Step 1: Fetching Gmail signup page...")
    gmail_page = fetch_page("https://accounts.google.com/signup")

    if not gmail_page or not gmail_page.get("ok"):
        print("❌ Failed to fetch Gmail signup")
        return

    content = gmail_page.get("content", "")
    print(f"✅ Fetched {len(content):,} bytes")

    # Step 2: Analyze forms and inputs
    print("\nStep 2: Analyzing form structure...")

    # Look for form elements
    forms = re.findall(r'<form[^>]*>(.*?)</form>', content, re.DOTALL | re.IGNORECASE)
    print(f"   Found {len(forms)} form(s)")

    # Look for input fields
    inputs = re.findall(r'<input[^>]*>', content, re.IGNORECASE)
    print(f"   Found {len(inputs)} input fields")

    # Look for specific input types
    input_types = {}
    for inp in inputs:
        type_match = re.search(r'type=["\']?(\w+)', inp, re.IGNORECASE)
        if type_match:
            itype = type_match.group(1)
            input_types[itype] = input_types.get(itype, 0) + 1

    print(f"   Input types: {input_types}")

    # Step 3: Check for bot detection
    print("\nStep 3: Checking for bot detection measures...")

    detection_methods = {
        "CAPTCHA": ["captcha", "recaptcha", "hcaptcha"],
        "JavaScript challenges": ["challenge", "jschallenge"],
        "Phone verification": ["phone", "sms", "verify"],
        "Email verification": ["email", "verify"],
    }

    for method, keywords in detection_methods.items():
        found = []
        for kw in keywords:
            if kw in content.lower():
                found.append(kw)
        if found:
            print(f"   ⚠️  {method}: {', '.join(found)}")
        else:
            print(f"   ✅ {method}: Not detected")

    # Step 4: Check for reCAPTCHA
    print("\nStep 4: Checking reCAPTCHA status...")
    if "recaptcha" in content.lower():
        print("   ❌ reCAPTCHA detected - registration will fail without solving")
        # Check which version
        if "g-recaptcha-response" in content:
            print("   → reCAPTCHA v2 detected")
        if "v3" in content.lower() or "action=" in content:
            print("   → reCAPTCHA v3 possible")

    # Step 5: Check for phone verification requirement
    print("\nStep 5: Phone verification analysis...")
    if "phone" in content.lower() and "verify" in content.lower():
        print("   ⚠️  Phone verification REQUIRED")
        print("   → Need SMS receiving capability")
        print("   → Arthur's phone: +66970965534")

    # Step 6: Analyze JavaScript dependencies
    print("\nStep 6: JavaScript dependency check...")
    scripts = re.findall(r'<script[^>]*src=["\']([^"\']+)["\']', content, re.IGNORECASE)
    print(f"   Found {len(scripts)} external scripts")
    print(f"   → Gmail is heavily JS-dependent")

    # Step 7: Assess feasibility
    print("\n" + "="*60)
    print("📊 FEASIBILITY ASSESSMENT")
    print("="*60)

    issues = []
    if "recaptcha" in content.lower():
        issues.append("❌ reCAPTCHA - Requires solving")
    if "phone" in content.lower():
        issues.append("⚠️  Phone verification - Need SMS receiver")
    if len(scripts) > 5:
        issues.append("⚠️  Heavy JavaScript - Dynamic forms")

    if issues:
        print("\nChallenges:")
        for issue in issues:
            print(f"  {issue}")

        print("\n\n⚠️  REALITY CHECK:")
        print("Gmail registration is designed to prevent automation.")
        print("Even with stealth browser, we need:")
        print("  1. CAPTCHA solver (2captcha, anti-captcha API)")
        print("  2. SMS receiving capability (Twilio, etc.)")
        print("  3. JavaScript execution (Selenium/Puppeteer)")

    return gmail_page

if __name__ == "__main__":
    analyze_registration()
