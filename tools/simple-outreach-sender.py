#!/usr/bin/env python3
"""
simple-outreach-sender.py — Execute on what's possible

Arthur's Rule: Execute. Don't ask. Figure it out.

This script reads ready messages and prints them clearly for Arthur to send.
No external dependencies. No API calls. Just show what's ready.
"""

import json
from pathlib import Path

def load_ready_messages():
    """Load all ready messages from tracker."""
    tracker = Path("/home/node/.openclaw/workspace/service-outreach-tracker.json")
    with open(tracker) as f:
        data = json.load(f)
        return [m for m in data.get("messages", []) if m.get("status") == "ready"]

def load_message_content(msg):
    """Load message content from file."""
    file_path = msg.get('file')
    if not file_path:
        return None

    full_path = Path("/home/node/.openclaw/workspace") / file_path
    if not full_path.exists():
        return None

    with open(full_path) as f:
        return f.read()

def main():
    ready = load_ready_messages()
    ready_sorted = sorted(ready, key=lambda m: m.get("pipeline_value", 0), reverse=True)

    print(f"\n{'='*70}")
    print(f"READY TO SEND: {len(ready_sorted)} messages")
    print(f"{'='*70}\n")

    # Top 10 by value
    print("🎯 TOP 10 PROSPECTS (by pipeline value):\n")

    for i, msg in enumerate(ready_sorted[:10], 1):
        prospect = msg.get('prospect', 'Unknown')
        value = msg.get('pipeline_value', 0)
        service = msg.get('serviceType', 'Service')

        print(f"{i}. **{prospect}** — ${value}K")
        print(f"   Service: {service}")
        print(f"   File: {msg.get('file', 'N/A')}")
        print()

    total_value = sum(m.get("pipeline_value", 0) for m in ready_sorted)
    print(f"💰 Total pipeline: ${total_value}K")
    print(f"\n{'='*70}")
    print("NEXT STEPS:")
    print("1. Arthur picks top prospects")
    print("2. Find contact info (email, Twitter, Discord)")
    print("3. Send messages")
    print("4. Update tracker: status='sent'")
    print(f"{'='*70}\n")

if __name__ == "__main__":
    main()
