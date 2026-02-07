#!/usr/bin/env python3
"""
rebuild-tracker.py — Fix the service outreach tracker

Scans outreach/messages/ for actual message files
Rebuilds tracker with correct file paths
Shows what's ready to send
"""

import re
from pathlib import Path
import json

def extract_value_from_content(content):
    """Extract pipeline value from message content."""
    # Look for patterns like "$30K" or "Estimated Budget: $30K - $75K"
    patterns = [
        r'\$\d+K?\s*-\s*\$?\d+K?',  # Range: $30K - $75K
        r'\$\d+K',                   # Single: $30K
    ]

    for pattern in patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            # Take the first number found
            value_str = matches[0].replace('$', '').replace('K', '').split('-')[0]
            try:
                return int(value_str)
            except:
                continue

    return 0  # Default if no value found

def extract_prospect_name(filename):
    """Extract prospect name from filename."""
    # Remove .md extension and convert to title case
    name = filename.replace('.md', '').replace('-', ' ').replace('_', ' ')
    # Clean up common prefixes
    name = name.replace('dao ', '').replace('service proposal', '').strip()
    return name.title()

def scan_messages():
    """Scan outreach/messages/ directory for message files."""
    messages_dir = Path("/home/node/.openclaw/workspace/outreach/messages")
    messages = []

    for file_path in messages_dir.rglob("*.md"):
        # Skip README and index files
        if file_path.name.lower() in ['readme.md', 'index.md']:
            continue

        try:
            with open(file_path) as f:
                content = f.read()

            # Extract metadata
            prospect = extract_prospect_name(file_path.stem)
            value = extract_value_from_content(content)

            # Determine relative path from workspace
            rel_path = str(file_path).replace('/home/node/.openclaw/workspace/', '')

            messages.append({
                'prospect': prospect,
                'pipeline_value': value,
                'file': rel_path,
                'status': 'ready',
                'category': 'service'
            })
        except Exception as e:
            print(f"⚠️  Error reading {file_path}: {e}")

    return messages

def main():
    print("🔍 Scanning outreach/messages/ for actual message files...\n")

    messages = scan_messages()

    if not messages:
        print("❌ No message files found")
        return

    # Sort by value
    messages_sorted = sorted(messages, key=lambda m: m['pipeline_value'], reverse=True)

    print(f"✅ Found {len(messages)} message files\n")
    print("="*70)
    print("TOP 20 PROSPECTS (by pipeline value):")
    print("="*70 + "\n")

    for i, msg in enumerate(messages_sorted[:20], 1):
        print(f"{i:2}. **{msg['prospect']}** — ${msg['pipeline_value']}K")
        print(f"    File: {msg['file']}")
        print()

    total_value = sum(m['pipeline_value'] for m in messages)
    print(f"💰 Total pipeline value: ${total_value}K")
    print(f"\n{'='*70}")
    print("NEXT ACTIONS:")
    print("1. Review top prospects")
    print("2. Find contact info (email, Twitter, Discord)")
    print("3. Send messages")
    print(f"{'='*70}\n")

    # Save to new tracker
    tracker_path = Path("/home/node/.openclaw/workspace/service-outreach-tracker-fixed.json")
    with open(tracker_path, 'w') as f:
        json.dump({
            'lastUpdated': '2026-02-05T14:55:00Z',
            'totalReady': len(messages),
            'totalSent': 0,
            'totalReplies': 0,
            'conversionRate': 0.0,
            'messages': messages_sorted
        }, f, indent=2)

    print(f"✅ Tracker saved: {tracker_path}")

if __name__ == "__main__":
    main()
