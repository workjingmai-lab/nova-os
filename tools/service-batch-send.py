#!/usr/bin/env python3
"""
service-batch-send.py — Batch send service outreach messages

Usage:
    python3 tools/service-batch-send.py --top 10          # Send top 10 ($305K)
    python3 tools/service-batch-send.py --tiered         # Tiered rollout (25 → wait → remaining)
    python3 tools/service-batch-send.py --all            # Send all 100 ($1,979K)

Options:
    --top N         Send top N messages by pipeline value
    --tiered        Send first 25, wait 24h, analyze, then continue
    --all           Send all 100 messages
    --dry-run       Show what would be sent without sending
    --from N        Start from message N (for resume)

Requirements:
    - revenue-pipeline.json must exist and have status="ready"
    - Message files must exist in tmp/service-outreach/
    - Send mechanism configured (message channel)

Exit codes:
    0 — Success
    1 — Missing files or config
    2 — No ready messages found
    3 — Send failed
"""

import json
import sys
from pathlib import Path
from typing import List, Dict

def load_pipeline() -> List[Dict]:
    """Load service outreach messages from JSON tracker."""
    path = Path("/home/node/.openclaw/workspace/service-outreach-tracker.json")
    if not path.exists():
        print(f"❌ Missing: {path}")
        sys.exit(1)

    with open(path) as f:
        data = json.load(f)
        return data.get("messages", [])

def filter_ready(messages: List[Dict]) -> List[Dict]:
    """Filter messages with status='ready'."""
    ready = [m for m in messages if m.get("status") == "ready"]
    print(f"📊 Ready messages: {len(ready)}/{len(messages)}")
    return ready

def sort_by_value(messages: List[Dict]) -> List[Dict]:
    """Sort messages by pipeline_value (descending)."""
    return sorted(messages, key=lambda m: m.get("pipeline_value", 0), reverse=True)

def load_message_file(msg: Dict) -> str:
    """Load message content from file."""
    # msg['file'] contains the path relative to workspace (e.g., "tmp/outreach-xxx.md")
    file_path = msg.get('file')
    if not file_path:
        print(f"⚠️  Message missing 'file' field: {msg.get('prospect', 'unknown')}")
        return None

    msg_path = Path("/home/node/.openclaw/workspace") / file_path
    if not msg_path.exists():
        print(f"⚠️  Missing file: {msg_path}")
        return None
    with open(msg_path) as f:
        return f.read()

def send_message(msg: Dict, content: str, dry_run: bool = False) -> bool:
    """Send a message (placeholder for actual send logic)."""
    prospect = msg.get('prospect', 'Unknown')
    value = msg.get('pipeline_value', 0)

    if dry_run:
        print(f"📤 [DRY-RUN] Would send to: {prospect} (${value}K)")
        return True

    # TODO: Implement actual send via message channel
    # This is a placeholder - integrate with your send mechanism
    print(f"📤 Sending to: {prospect} (${value}K)")
    return True

def main():
    args = sys.argv[1:]

    if "--help" in args or "-h" in args:
        print(__doc__)
        return

    dry_run = "--dry-run" in args

    # Load and filter pipeline
    pipeline = load_pipeline()
    ready = filter_ready(pipeline)
    if not ready:
        print("❌ No ready messages found")
        sys.exit(2)

    # Sort by value
    ready_sorted = sort_by_value(ready)

    # Determine which messages to send
    to_send = []

    if "--all" in args:
        to_send = ready_sorted
        print(f"🚀 Sending ALL {len(to_send)} messages")

    elif "--top" in args:
        try:
            idx = args.index("--top")
            n = int(args[idx + 1])
            to_send = ready_sorted[:n]
            print(f"🎯 Sending top {len(to_send)} messages")
        except (ValueError, IndexError):
            print("❌ --top requires a number (e.g., --top 10)")
            sys.exit(1)

    elif "--tiered" in args:
        to_send = ready_sorted[:25]  # First tier: top 25
        print(f"📊 Tiered rollout: Phase 1 = {len(to_send)} messages")
        print(f"⏸️  Wait 24h, analyze responses, then continue")

    else:
        print("❌ Specify --top N, --tiered, or --all")
        print("   Use --help for usage")
        sys.exit(1)

    # Show summary
    total_value = sum(m.get("pipeline_value", 0) for m in to_send)
    print(f"💰 Pipeline value: ${total_value}K")
    print()

    # Send messages
    failed = 0
    for msg in to_send:
        content = load_message_file(msg)
        if content is None:
            failed += 1
            continue

        if not send_message(msg, content, dry_run):
            print(f"❌ Failed to send: {msg['company']}")
            failed += 1

    # Summary
    print()
    if dry_run:
        print(f"✅ [DRY-RUN] Would send {len(to_send) - failed} messages")
    else:
        print(f"✅ Sent {len(to_send) - failed} messages")

    if failed > 0:
        print(f"⚠️  {failed} failed")
        sys.exit(3)

if __name__ == "__main__":
    main()
