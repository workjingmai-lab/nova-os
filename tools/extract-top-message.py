#!/usr/bin/env python3
"""
extract-top-message.py — Extract top message for Moltbook posting

Arthur's Rule: Execute. Use what works.
Post high-value outreach to Moltbook → DAOs see it → deals happen
"""

import json
from pathlib import Path

def main():
    # Load fixed tracker
    tracker_path = Path("/home/node/.openclaw/workspace/service-outreach-tracker-fixed.json")
    with open(tracker_path) as f:
        data = json.load(f)

    # Get top message
    top_message = data['messages'][0]  # Already sorted by value

    # Load content
    msg_path = Path("/home/node/.openclaw/workspace") / top_message['file']
    with open(msg_path) as f:
        content = f.read()

    print("="*70)
    print(f"TOP PROSPECT: {top_message['prospect']}")
    print(f"VALUE: ${top_message['pipeline_value']}K")
    print(f"FILE: {top_message['file']}")
    print("="*70)
    print()
    print(content)
    print()
    print("="*70)
    print("USE THIS CONTENT FOR MOLTBOOK POST")
    print("Title: Service Proposal: [Prospect Name]")
    print("Tags: services, outreach, web3, dao")
    print("="*70)

if __name__ == "__main__":
    main()
