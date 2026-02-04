#!/usr/bin/env python3
"""
response-tracker.py — Track outreach message responses

Usage:
    python3 tools/response-tracker.py add --msg 001 --response "interested" --date 2026-02-04
    python3 tools/response-tracker.py list --status "interested"
    python3 tools/response-tracker.py stats

Commands:
    add       Add a response to a sent message
    list      List responses by status/company
    stats     Show response rate and pipeline conversion
    update    Change response status (e.g., interested → call_scheduled)

Status types:
    - no_response
    - replied
    - interested
    - call_scheduled
    - proposal_sent
    - negotiation
    - won
    - lost
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List

RESPONSES_FILE = Path("/home/node/.openclaw/workspace/data/responses.json")

def load_responses() -> List[Dict]:
    """Load responses from JSON file."""
    if not RESPONSES_FILE.exists():
        return []
    with open(RESPONSES_FILE) as f:
        return json.load(f)

def save_responses(responses: List[Dict]):
    """Save responses to JSON file."""
    RESPONSES_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(RESPONSES_FILE, "w") as f:
        json.dump(responses, f, indent=2)

def add_response(msg_id: str, status: str, note: str = "", date: str = None):
    """Add a response to a message."""
    responses = load_responses()

    # Check if response already exists
    for r in responses:
        if r["msg_id"] == msg_id:
            r["status"] = status
            r["note"] = note
            r["updated_at"] = datetime.utcnow().isoformat()
            print(f"✅ Updated response for {msg_id}: {status}")
            save_responses(responses)
            return

    # Add new response
    response = {
        "msg_id": msg_id,
        "status": status,
        "note": note,
        "created_at": date or datetime.utcnow().isoformat(),
        "updated_at": datetime.utcnow().isoformat()
    }
    responses.append(response)
    save_responses(responses)
    print(f"✅ Added response for {msg_id}: {status}")

def list_responses(status_filter: str = None):
    """List responses, optionally filtered by status."""
    responses = load_responses()

    if status_filter:
        responses = [r for r in responses if r["status"] == status_filter]

    if not responses:
        print("📭 No responses found")
        return

    print(f"\n📊 Responses ({len(responses)}):")
    print("-" * 60)
    for r in responses:
        print(f"{r['msg_id']} | {r['status']:20} | {r.get('note', '')[:40]}")
    print()

def show_stats():
    """Show response statistics."""
    responses = load_responses()

    if not responses:
        print("📭 No responses tracked yet")
        return

    # Count by status
    status_counts = {}
    for r in responses:
        status_counts[r["status"]] = status_counts.get(r["status"], 0) + 1

    total = len(responses)
    replied = sum(c for s, c in status_counts.items() if s != "no_response")

    print("\n📈 Response Statistics:")
    print("-" * 40)
    print(f"Total responses: {total}")
    print(f"Replied: {replied} ({replied*100//total if total > 0 else 0}%)")
    print()
    print("By status:")
    for status, count in sorted(status_counts.items(), key=lambda x: -x[1]):
        print(f"  {status}: {count}")
    print()

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    command = sys.argv[1]

    if command == "add":
        if "--msg" not in sys.argv or "--response" not in sys.argv:
            print("❌ Usage: add --msg ID --response STATUS [--note NOTE] [--date DATE]")
            return

        msg_id = sys.argv[sys.argv.index("--msg") + 1]
        status = sys.argv[sys.argv.index("--response") + 1]
        note = sys.argv[sys.argv.index("--note") + 1] if "--note" in sys.argv else ""
        date = sys.argv[sys.argv.index("--date") + 1] if "--date" in sys.argv else None

        add_response(msg_id, status, note, date)

    elif command == "list":
        status = sys.argv[sys.argv.index("--status") + 1] if "--status" in sys.argv else None
        list_responses(status)

    elif command == "stats":
        show_stats()

    else:
        print(f"❌ Unknown command: {command}")
        print(__doc__)

if __name__ == "__main__":
    main()
