#!/usr/bin/env python3
"""
send-service-messages.py — Execute service outreach sends

Usage:
    # Send top 10 by value
    python3 tools/send-service-messages.py --top 10

    # Send all ready messages
    python3 tools/send-service-messages.py --all

    # Send specific batch
    python3 tools/send-service-messages.py --batch 16

    # Dry run (show what would be sent)
    python3 tools/send-service-messages.py --top 10 --dry-run

This script:
1. Loads messages from service-outreach-tracker.json
2. Filters by status ("ready")
3. Sorts by value (high to low)
4. Sends messages via configured channel (Telegram/Signal/etc.)
5. Updates tracker with "sent" status and timestamp

⚠️  REQUIRES: Arthur approval and channel configuration
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from typing import List, Dict

TRACKER_FILE = Path("/home/node/.openclaw/workspace/service-outreach-tracker.json")

def load_messages() -> List[Dict]:
    """Load all messages from tracker."""
    if not TRACKER_FILE.exists():
        print(f"❌ Tracker not found: {TRACKER_FILE}")
        sys.exit(1)

    with open(TRACKER_FILE) as f:
        data = json.load(f)
        return data.get("messages", [])

def filter_ready(messages: List[Dict]) -> List[Dict]:
    """Filter messages with status='ready'."""
    return [m for m in messages if m.get("status") == "ready"]

def sort_by_value(messages: List[Dict]) -> List[Dict]:
    """Sort messages by amountRange (high to low)."""
    def extract_value(msg):
        amount = msg.get("amountRange", "$0K")
        import re
        match = re.search(r'(\d+)', amount)
        return int(match.group(1)) if match else 0

    return sorted(messages, key=extract_value, reverse=True)

def get_top_n(messages: List[Dict], n: int) -> List[Dict]:
    """Get top N messages by value."""
    return messages[:n]

def send_message(msg: Dict, dry_run: bool = False) -> bool:
    """Send a single message.

    NOTE: This is a placeholder. Actual implementation depends on:
    - Channel configuration (Telegram, Signal, email, etc.)
    - Message routing (how to reach each prospect)
    - Rate limiting (don't spam)

    For now, this simulates sending and returns True.
    """
    if dry_run:
        print(f"  📧 [DRY RUN] Would send to: {msg['prospect']}")
        return True

    # TODO: Implement actual sending logic
    # This would use OpenClaw's message tool or direct API calls
    print(f"  📧 Sending to: {msg['prospect']}")
    # Simulate send
    return True

def update_tracker(messages: List[Dict]):
    """Update tracker with sent status."""
    with open(TRACKER_FILE) as f:
        data = json.load(f)

    # Update message statuses
    msg_map = {m.get("file"): m for m in data["messages"]}
    for msg in messages:
        file = msg.get("file")
        if file and file in msg_map:
            msg_map[file]["status"] = "sent"
            msg_map[file]["sentAt"] = datetime.utcnow().isoformat() + "Z"

    # Recalculate totals
    data["totalReady"] = len([m for m in data["messages"] if m.get("status") == "ready"])
    data["totalSent"] = len([m for m in data["messages"] if m.get("status") == "sent"])

    # Save
    with open(TRACKER_FILE, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"  ✅ Tracker updated")

def main():
    """Execute send workflow."""
    import argparse
    parser = argparse.ArgumentParser(description="Send service outreach messages")
    parser.add_argument("--top", type=int, help="Send top N messages by value")
    parser.add_argument("--all", action="store_true", help="Send all ready messages")
    parser.add_argument("--batch", type=int, help="Send specific batch number")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be sent")
    args = parser.parse_args()

    # Validate args
    if not any([args.top, args.all, args.batch]):
        print("❌ Error: Must specify --top N, --all, or --batch N")
        parser.print_help()
        sys.exit(1)

    # Load messages
    print("📊 Loading messages...")
    all_messages = load_messages()
    ready_messages = filter_ready(all_messages)
    print(f"   Total messages: {len(all_messages)}")
    print(f"   Ready to send: {len(ready_messages)}")

    # Select messages to send
    if args.all:
        to_send = ready_messages
        print(f"   Sending all: {len(to_send)} messages")
    elif args.top:
        sorted_messages = sort_by_value(ready_messages)
        to_send = get_top_n(sorted_messages, args.top)
        print(f"   Sending top {args.top}: {len(to_send)} messages")
    elif args.batch:
        # Filter by batch number (file contains "batch-{n}")
        to_send = [m for m in ready_messages if f"batch-{args.batch}-" in m.get("file", "")]
        print(f"   Sending batch {args.batch}: {len(to_send)} messages")

    if not to_send:
        print("❌ No messages to send!")
        sys.exit(1)

    # Show preview
    total_value = 0
    for msg in to_send[:5]:
        amount = msg.get("amountRange", "$0K")
        import re
        match = re.search(r'(\d+)', amount)
        if match:
            total_value += int(match.group(1))
        print(f"   - {msg['prospect']}: {amount}")

    if len(to_send) > 5:
        print(f"   ... and {len(to_send) - 5} more")

    print(f"\n   Total value: ${total_value}K")

    # Confirm
    if args.dry_run:
        print("\n[DRY RUN] No messages will be sent.")
    else:
        print("\n⚠️  Ready to send!")
        confirm = input("   Type 'yes' to confirm: ")
        if confirm.lower() != 'yes':
            print("❌ Cancelled")
            sys.exit(0)

    # Send messages
    print(f"\n🚀 Sending {len(to_send)} messages...")
    sent = []
    failed = []

    for i, msg in enumerate(to_send, 1):
        print(f"[{i}/{len(to_send)}]", end=" ")
        success = send_message(msg, dry_run=args.dry_run)
        if success:
            sent.append(msg)
        else:
            failed.append(msg)

    # Update tracker
    if sent and not args.dry_run:
        update_tracker(sent)

    # Summary
    print(f"\n✅ Done!")
    print(f"   Sent: {len(sent)}")
    print(f"   Failed: {len(failed)}")
    if failed:
        print(f"   Failed prospects:")
        for msg in failed:
            print(f"     - {msg['prospect']}")

if __name__ == "__main__":
    main()
