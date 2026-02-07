#!/usr/bin/env python3
"""
update-tracker-sent.py — Mark sent emails in tracker
"""

import json
from pathlib import Path
from datetime import datetime

def main():
    # Load tracker
    tracker_path = Path("/home/node/.openclaw/workspace/tmp/prospects-with-emails.json")
    with open(tracker_path) as f:
        prospects = json.load(f)

    # Mark top 5 as sent
    sent_prospects = ['1Inch Dex Automation', 'Gitcoin Carlos Value First',
                     'Yearn Governance Automation', 'Optimism Governance Value First',
                     'Gitcoin Grant Automation Outreach']

    timestamp = datetime.utcnow().isoformat() + 'Z'

    for prospect in prospects[:5]:
        prospect['status'] = 'sent'
        prospect['sentAt'] = timestamp

    # Save updated tracker
    with open(tracker_path, 'w') as f:
        json.dump(prospects, f, indent=2)

    print(f"✅ Tracker updated: 5 prospects marked as sent")
    print(f"   Timestamp: {timestamp}")

if __name__ == "__main__":
    main()
