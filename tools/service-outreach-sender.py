#!/usr/bin/env python3
"""
Service Outreach Sender — Quick-send tool for $152K service pipeline

Send value-first outreach messages to 10 Web3 teams (zero blockers).
Updates revenue-pipeline.json automatically after sending.

Usage:
    # List all ready messages
    python3 tools/service-outreach-sender.py --list

    # Mark message as sent
    python3 tools/service-outreach-sender.py --sent "Ethereum Foundation"

    # Show next message to send
    python3 tools/service-outreach-sender.py --next

Pipeline: $152K ready NOW (10 messages)
Created: 2026-02-04 (Work block 1745)
"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime

# Paths
WORKSPACE = Path("/home/node/.openclaw/workspace")
MESSAGES_DIR = WORKSPACE / "outreach/messages"
PIPELINE_FILE = WORKSPACE / "data/revenue-pipeline.json"
SENT_LOG = WORKSPACE / "data/outreach-sent.json"

# Message files (in priority order)
MESSAGES = [
    {"file": "ethereum-foundation-agent-automation.md", "name": "Ethereum Foundation", "value": 40000, "priority": "HIGH"},
    {"file": "fireblocks-security-automation.md", "name": "Fireblocks", "value": 35000, "priority": "HIGH"},
    {"file": "uniswap-devx-automation.md", "name": "Uniswap", "value": 40000, "priority": "HIGH"},
    {"file": "alchemy-devx-automation.md", "name": "Alchemy", "value": 30000, "priority": "MEDIUM"},
    {"file": "aave-marc-zeller-value-first.md", "name": "Aave", "value": 30000, "priority": "MEDIUM"},
    {"file": "arbitrum-dao-governance-value-first.md", "name": "Arbitrum DAO", "value": 25000, "priority": "MEDIUM"},
    {"file": "balancer-governance-automation.md", "name": "Balancer DAO", "value": 20000, "priority": "MEDIUM"},
    {"file": "autogpt-infrastructure-automation-outreach.md", "name": "AutoGPT", "value": 20000, "priority": "MEDIUM"},
    {"file": "nouns-dao-governance.md", "name": "Nouns DAO", "value": 15000, "priority": "MEDIUM"},
    {"file": "003-stripe-api-docs-proposal.md", "name": "Stripe", "value": 30000, "priority": "MEDIUM"},
]

def load_sent_log():
    """Load sent message log."""
    if SENT_LOG.exists():
        with open(SENT_LOG, 'r') as f:
            return json.load(f)
    return {"sent": [], "last_updated": None}

def save_sent_log(log):
    """Save sent message log."""
    with open(SENT_LOG, 'w') as f:
        json.dump(log, f, indent=2)

def list_messages():
    """List all messages with status."""
    log = load_sent_log()
    sent_set = set(log["sent"])

    print("\n📬 Service Outreach Pipeline")
    print(f"   Ready: {len(MESSAGES) - len(sent_set)} messages")
    print(f"   Sent: {len(sent_set)} messages")
    print(f"   Value: ${sum(m['value'] for m in MESSAGES if m['name'] not in sent_set):,} ready\n")

    for i, msg in enumerate(MESSAGES, 1):
        status = "✅ SENT" if msg['name'] in sent_set else "📤 READY"
        priority = msg['priority']
        value = msg['value']
        print(f"{i}. [{status}] {msg['name']} (${value:,}, {priority})")

    print(f"\n📂 Message files: {MESSAGES_DIR}")
    print(f"📊 Pipeline: {PIPELINE_FILE}")

def show_next():
    """Show next message to send."""
    log = load_sent_log()
    sent_set = set(log["sent"])

    for msg in MESSAGES:
        if msg['name'] not in sent_set:
            print(f"\n📤 NEXT: {msg['name']} (${msg['value']:,}, {msg['priority']} priority)")
            print(f"   File: {MESSAGES_DIR / msg['file']}")
            print(f"\n   Action: Open file → Copy message → Send via Discord/Twitter/Email")
            print(f"   Then: python3 tools/service-outreach-sender.py --sent '{msg['name']}'")
            return

    print("\n✅ All messages sent!")

def mark_sent(name):
    """Mark message as sent and update pipeline."""
    log = load_sent_log()
    sent_set = set(log["sent"])

    if name in sent_set:
        print(f"⚠️  '{name}' already marked as sent.")
        return

    # Find message
    msg = next((m for m in MESSAGES if m['name'] == name), None)
    if not msg:
        print(f"❌ Message '{name}' not found.")
        return

    # Mark as sent
    log["sent"].append(name)
    log["last_updated"] = datetime.now().isoformat()
    save_sent_log(log)

    # Update pipeline if file exists
    if PIPELINE_FILE.exists():
        with open(PIPELINE_FILE, 'r') as f:
            pipeline = json.load(f)

        # Find and update service entry
        for item in pipeline.get('services', []):
            if name.lower() in item.get('name', '').lower():
                item['status'] = 'submitted'
                item['updated'] = datetime.now().isoformat()
                if 'notes' not in item:
                    item['notes'] = []
                item['notes'].append(f"Outreach sent via {datetime.now().strftime('%Y-%m-%d')}")
                break

        with open(PIPELINE_FILE, 'w') as f:
            json.dump(pipeline, f, indent=2)

    print(f"✅ Marked '{name}' as sent (${msg['value']:,})")
    print(f"   Pipeline updated")
    print(f"   Sent log: {len(log['sent'])}/{len(MESSAGES)} messages")

def main():
    if len(sys.argv) < 2:
        print("Service Outreach Sender — Quick-send tool for $152K pipeline\n")
        print("Usage:")
        print("  python3 tools/service-outreach-sender.py --list")
        print("  python3 tools/service-outreach-sender.py --next")
        print("  python3 tools/service-outreach-sender.py --sent 'Name'")
        print("\nExample:")
        print("  python3 tools/service-outreach-sender.py --list      # Show all messages")
        print("  python3 tools/service-outreach-sender.py --next      # Show next to send")
        print("  python3 tools/service-outreach-sender.py --sent 'Ethereum Foundation'  # Mark sent")
        sys.exit(1)

    arg = sys.argv[1]

    if arg == "--list":
        list_messages()
    elif arg == "--next":
        show_next()
    elif arg == "--sent" and len(sys.argv) > 2:
        mark_sent(sys.argv[2])
    else:
        print("❌ Invalid argument. Use --list, --next, or --sent 'Name'")
        sys.exit(1)

if __name__ == "__main__":
    main()
