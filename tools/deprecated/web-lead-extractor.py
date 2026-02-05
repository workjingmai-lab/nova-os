#!/usr/bin/env python3
"""
Web Lead Extractor - Extract potential leads from web pages

When browser access is available, use this to scan pages for:
- Pain points ("manual", "slow", "automation needed")
- Contact info (emails, Twitter handles)
- Company names and descriptions

Usage (when browser is unblocked):
    python3 tools/web-lead-extractor.py scan --url "https://example.com/about"
    python3 tools/web-lead-extractor.py batch --urls urls.txt
"""

import sys
import re
from pathlib import Path

# Pain point keywords that signal automation needs
PAIN_KEYWORDS = [
    "manual process",
    "manual workflow",
    "slow process",
    "time consuming",
    "need automation",
    "looking for automation",
    "automation needed",
    "manual tracking",
    "spreadsheet hell",
    "data entry",
    "repetitive task",
    "monitoring issues",
    "incident response slow"
]

SERVICE_KEYWORDS = {
    "monitoring": ["monitoring", "alerts", "incidents", "uptime", "tracking"],
    "automation": ["automation", "workflow", "pipeline", "integration"],
    "support": ["support", "customer service", "helpdesk", "tickets"],
    "governance": ["governance", "voting", "proposal", "dao", "treasury"],
    "analytics": ["analytics", "data", "dashboard", "reporting", "insights"],
    "security": ["security", "monitoring", "alerts", "incidents", "breach"]
}

def extract_contacts(text: str) -> list:
    """Extract emails and social handles from text"""
    contacts = []

    # Emails
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    contacts.extend([f"email:{e}" for e in emails])

    # Twitter handles
    twitter = re.findall(r'@([A-Za-z0-9_]{1,15})', text)
    contacts.extend([f"twitter:@{t}" for t in twitter])

    # Discord mentions
    discord = re.findall(r'discord\.gg/([A-Za-z0-9-]+)', text)
    contacts.extend([f"discord:{d}" for d in discord])

    return list(set(contacts))

def detect_pain_points(text: str) -> list:
    """Find pain point signals in text"""
    text_lower = text.lower()
    found = []

    for keyword in PAIN_KEYWORDS:
        if keyword in text_lower:
            found.append(keyword)

    return found

def match_service_type(text: str) -> str:
    """Match text to best service type"""
    text_lower = text.lower()
    scores = {}

    for service, keywords in SERVICE_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw in text_lower)
        if score > 0:
            scores[service] = score

    if not scores:
        return "unknown"

    # Return highest scoring service
    return max(scores, key=scores.get)

def scan_page(url: str, content: str) -> dict:
    """Scan page content for leads"""
    pain_points = detect_pain_points(content)
    contacts = extract_contacts(content)
    service_type = match_service_type(content)

    return {
        "url": url,
        "pain_points": pain_points,
        "contacts": contacts,
        "suggested_service": service_type,
        "pain_score": len(pain_points),
        "has_contacts": len(contacts) > 0
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: web-lead-extractor.py scan|--help")
        print("\nNote: Requires browser access or web_fetch to get page content")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "scan":
        if len(sys.argv) < 4:
            print("Usage: web-lead-extractor.py scan --url <URL> --content <TEXT>")
            sys.exit(1)

        url = sys.argv[3] if len(sys.argv) > 3 and sys.argv[2] == "--url" else "unknown"
        content = " ".join(sys.argv[4:])

        result = scan_page(url, content)

        print(f"\n🔍 Lead Scan: {url}")
        print(f"   Pain Points: {', '.join(result['pain_points']) if result['pain_points'] else 'None detected'}")
        print(f"   Suggested Service: {result['suggested_service']}")
        print(f"   Contacts: {', '.join(result['contacts'][:5]) if result['contacts'] else 'None found'}")
        print(f"   Pain Score: {result['pain_score']}/10")

        if result['pain_score'] >= 2:
            print("   ✅ GOOD LEAD - Multiple pain signals")
        elif result['pain_score'] == 1:
            print("   ⚠️ POSSIBLE LEAD - Single pain signal")
        else:
            print("   ❌ WEAK LEAD - No clear pain signals")

    elif cmd == "--help":
        print(__doc__)

    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)

if __name__ == "__main__":
    main()
