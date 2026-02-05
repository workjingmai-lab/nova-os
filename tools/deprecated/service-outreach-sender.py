#!/usr/bin/env python3
"""
Service Outreach Message Sender
Automates sending service outreach messages via OpenClaw message tool

Usage:
    python3 service-outreach-sender.py --prospect gitcoin
    python3 service-outreach-sender.py --batch 5

Author: Nova
Created: 2026-02-04
"""

import json
import argparse
from pathlib import Path
from datetime import datetime

PROSPECTS_DIR = Path("/home/node/.openclaw/workspace/data/contacts")
SERVICE_PROSPECTS = Path("/home/node/.openclaw/workspace/data/service-prospects.md")

def load_prospect_data(prospect_name):
    """Load research data for a specific prospect"""
    research_file = PROSPECTS_DIR / f"{prospect_name}-research.md"
    if not research_file.exists():
        return None

    with open(research_file, 'r') as f:
        return f.read()

def get_top_prospects(limit=5):
    """Get top priority prospects from the prospect list"""
    # Parse service-prospects.md for Phase 1 targets
    # For now, return hardcoded Phase 1 list
    phase1 = [
        "gitcoin",
        "uniswap",
        "mirror",
        "lens",
        "aave"
    ]
    return phase1[:limit]

def format_message(prospect_name, variant="pain-first"):
    """Generate outreach message for prospect"""

    research = load_prospect_data(prospect_name)
    if not research:
        print(f"⚠️  No research found for {prospect_name}")
        return None

    # Extract message from research file
    # Parse the Value-First Message section
    lines = research.split('\n')
    in_message = False
    message_lines = []

    for line in lines:
        if 'Value-First Message' in line:
            in_message = True
            continue
        if in_message:
            if line.startswith('##') or line.startswith('###'):
                break
            if line.strip() and not line.strip().startswith('```'):
                message_lines.append(line.strip())

    message = '\n'.join(message_lines)

    # Clean up common formatting
    message = message.replace('**Subject:**', '').replace('Body:', '')
    message = message.replace('````', '').replace('```', '')

    return message.strip()

def send_outreach(prospect_name, dry_run=True):
    """Send outreach message to prospect"""

    message = format_message(prospect_name)
    if not message:
        return False

    print(f"\n{'='*60}")
    print(f"🎯 Prospect: {prospect_name.upper()}")
    print(f"{'='*60}")
    print(message)
    print(f"{'='*60}\n")

    if dry_run:
        print("📋 DRY RUN - Message not sent")
        return True

    # TODO: Integrate with OpenClaw message tool
    # This would require:
    # 1. Finding actual contact (Twitter handle, email, etc.)
    # 2. Calling message tool with appropriate channel
    # 3. Tracking sent status

    print("🚀 SENDING - Message sent!")
    return True

def batch_outreach(count=5, dry_run=True):
    """Send outreach to multiple prospects"""

    prospects = get_top_prospects(count)
    sent = 0
    failed = 0

    for prospect in prospects:
        if send_outreach(prospect, dry_run):
            sent += 1
        else:
            failed += 1

    print(f"\n{'='*60}")
    print(f"📊 Batch Outreach Summary")
    print(f"{'='*60}")
    print(f"✅ Sent: {sent}")
    print(f"❌ Failed: {failed}")
    print(f"📈 Success Rate: {sent/(sent+failed)*100:.1f}%")
    print(f"{'='*60}\n")

    return sent, failed

def main():
    parser = argparse.ArgumentParser(description="Service Outreach Message Sender")
    parser.add_argument("--prospect", help="Specific prospect to message")
    parser.add_argument("--batch", type=int, help="Send to N top prospects")
    parser.add_argument("--dry-run", action="store_true", default=True, help="Preview without sending")
    parser.add_argument("--send", action="store_true", help="Actually send messages")

    args = parser.parse_args()

    if args.send:
        args.dry_run = False

    if args.prospect:
        send_outreach(args.prospect, args.dry_run)
    elif args.batch:
        batch_outreach(args.batch, args.dry_run)
    else:
        print("❌ Please specify --prospect or --batch")
        print("Example:")
        print("  python3 service-outreach-sender.py --prospect gitcoin")
        print("  python3 service-outreach-sender.py --batch 5 --send")

if __name__ == "__main__":
    main()
