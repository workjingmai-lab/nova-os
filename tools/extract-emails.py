#!/usr/bin/env python3
"""
extract-emails.py — Extract email addresses from outreach messages

Arthur's Rule: Execute. Send what we can.
"""

import re
import json
from pathlib import Path
from collections import defaultdict

def extract_emails(text):
    """Extract email addresses from text."""
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)

def main():
    # Load fixed tracker
    tracker_path = Path("/home/node/.openclaw/workspace/service-outreach-tracker-fixed.json")
    with open(tracker_path) as f:
        data = json.load(f)

    # Scan all messages for emails
    prospects_with_emails = []

    for msg in data['messages']:
        # Load message content
        msg_path = Path("/home/node/.openclaw/workspace") / msg['file']

        if not msg_path.exists():
            continue

        with open(msg_path) as f:
            content = f.read()

        # Extract emails
        emails = extract_emails(content)

        if emails:
            prospects_with_emails.append({
                'prospect': msg['prospect'],
                'pipeline_value': msg['pipeline_value'],
                'file': msg['file'],
                'emails': list(set(emails))  # Deduplicate
            })

    # Sort by value
    prospects_with_emails.sort(key=lambda x: x['pipeline_value'], reverse=True)

    # Output results
    print("="*70)
    print(f"PROSPECTS WITH EMAIL ADDRESSES: {len(prospects_with_emails)}")
    print("="*70)
    print()

    total_value = 0

    for i, prospect in enumerate(prospects_with_emails, 1):
        print(f"{i}. **{prospect['prospect']}** — ${prospect['pipeline_value']}K")
        print(f"   Emails: {', '.join(prospect['emails'])}")
        print(f"   File: {prospect['file']}")
        print()
        total_value += prospect['pipeline_value']

    print("="*70)
    print(f"TOTAL PIPELINE VALUE WITH EMAILS: ${total_value}K")
    print("="*70)
    print()
    print("NEXT ACTIONS:")
    print("1. Copy email addresses")
    print("2. Draft email campaign")
    print("3. Send via Arthur's email or integration")
    print()

    # Save to file for easy reference
    output_path = Path("/home/node/.openclaw/workspace/tmp/prospects-with-emails.json")
    with open(output_path, 'w') as f:
        json.dump(prospects_with_emails, f, indent=2)

    print(f"✅ Saved: {output_path}")

if __name__ == "__main__":
    main()
