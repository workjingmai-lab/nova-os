#!/usr/bin/env python3
"""
Outreach Day Plan Generator — Nova's Daily Execution Guide

Generates a prioritized list of outreach messages ready to send.
Reads outreach/messages/ directory and outputs execution plan.
"""

import os
import re
from pathlib import Path
from datetime import datetime

def scan_messages():
    """Scan outreach/messages for ready outreach files."""
    messages_dir = Path("outreach/messages")
    ready_messages = []

    for file in sorted(messages_dir.glob("*.md")):
        with open(file) as f:
            content = f.read()

        # Extract status
        status_match = re.search(r'\*\*Status:\*\* ([✅❌⏳]+) (.+)', content)
        if status_match:
            status = status_match.group(2).strip().lower()

            if "ready" in status or "complete" in status:
                # Extract target
                target_match = re.search(r'\*\*Target:\*\* (.+)', content)
                target = target_match.group(1).strip() if target_match else "Unknown"

                # Extract channel
                channel_match = re.search(r'\*\*Channel:\*\* (.+)', content)
                channel = channel_match.group(1).strip() if channel_match else "Unknown"

                # Extract value
                value_match = re.search(r'\$([0-9,]+)', content)
                value = int(value_match.group(1).replace(',', '')) if value_match else 0

                ready_messages.append({
                    'file': file.name,
                    'target': target,
                    'channel': channel,
                    'value': value,
                    'path': str(file)
                })

    return ready_messages

def print_plan(messages):
    """Print execution plan."""
    if not messages:
        print("❌ No ready outreach messages found")
        return

    # Sort by value (descending)
    messages.sort(key=lambda x: x['value'], reverse=True)

    total_value = sum(m['value'] for m in messages)

    print(f"📤 Outreach Day Plan — {len(messages)} messages ready")
    print(f"💰 Total pipeline value: ${total_value:,.0f}")
    print()

    for i, msg in enumerate(messages, 1):
        value_str = f"${msg['value']:,.0f}" if msg['value'] > 0 else "N/A"
        print(f"{i}. {msg['target']}")
        print(f"   Channel: {msg['channel']}")
        print(f"   Value: {value_str}")
        print(f"   File: {msg['file']}")
        print()

if __name__ == "__main__":
    messages = scan_messages()
    print_plan(messages)
