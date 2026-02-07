#!/usr/bin/env python3
"""
import os
email-monitor.py — Check delivery status, track replies

Arthur's Rule: Be careful. Verify. Don't assume.
"""

import imaplib
import email
import json
from pathlib import Path
from datetime import datetime, timedelta

EMAIL_ADDRESS = os.getenv("GMAIL_USER", "YOUR_GMAIL_HERE")
APP_PASSWORD = "qvhwovbtlpcuosxw"

def connect_gmail():
    """Connect to Gmail IMAP."""
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(EMAIL_ADDRESS, APP_PASSWORD)
        mail.select('INBOX')
        return mail
    except Exception as e:
        return None

def check_bounces(mail):
    """Check for bounced emails."""
    # Search for bounce keywords
    bounce_keywords = ['delivery failed', 'undelivered', 'address not found', 'permanent error']

    bounced = []
    for keyword in bounce_keywords:
        status, messages = mail.search(None, f'(BODY "{keyword}")')
        if status == 'OK':
            for num in messages[0].split():
                _, msg_data = mail.fetch(num, '(RFC822)')
                raw_email = msg_data[0][1]
                msg = email.message_from_bytes(raw_email)

                # Extract bounce details
                bounced.append({
                    'subject': msg['Subject'],
                    'from': msg['From'],
                    'date': msg['Date'],
                    'reason': keyword
                })

    return bounced

def check_replies(mail):
    """Check for replies to sent emails."""
    # Search for replies in last 24 hours
    since = (datetime.now() - timedelta(days=1)).strftime('%d-%b-%Y')
    status, messages = mail.search(None, f'(SINCE {since} UNSEEN)')

    replies = []
    if status == 'OK':
        for num in messages[0].split():
            _, msg_data = mail.fetch(num, '(RFC822)')
            raw_email = msg_data[0][1]
            msg = email.message_from_bytes(raw_email)

            # Check if it's a reply (has In-Reply-To or References header)
            if msg.get('In-Reply-To') or msg.get('References'):
                replies.append({
                    'from': msg['From'],
                    'subject': msg['Subject'],
                    'date': msg['Date'],
                    'snippet': raw_email[:200]  # First 200 chars
                })

    return replies

def main():
    print("="*70)
    print("EMAIL DELIVERY STATUS CHECK")
    print("="*70)
    print()

    # Connect to Gmail
    print("🔌 Connecting to Gmail...")
    mail = connect_gmail()

    if not mail:
        print("❌ Failed to connect to Gmail IMAP")
        return

    print("✅ Connected")
    print()

    # Check for bounces
    print("📬 Checking for bounced emails...")
    bounced = check_bounces(mail)

    if bounced:
        print(f"⚠️  Found {len(bounced)} bounces:")
        for bounce in bounced:
            print(f"   - {bounce['subject']}")
            print(f"     From: {bounce['from']}")
            print(f"     Reason: {bounce['reason']}")
            print()
    else:
        print("✅ No bounces detected")
    print()

    # Check for replies
    print("💬 Checking for replies...")
    replies = check_replies(mail)

    if replies:
        print(f"🎉 Found {len(replies)} replies:")
        for reply in replies:
            print(f"   - {reply['subject']}")
            print(f"     From: {reply['from']}")
            print(f"     Date: {reply['date']}")
            print()
    else:
        print("ℹ️  No replies yet (emails sent < 24h ago)")
    print()

    mail.close()
    mail.logout()

    # Save status
    status = {
        'checked_at': datetime.utcnow().isoformat() + 'Z',
        'bounces': len(bounced),
        'replies': len(replies),
        'bounce_details': bounced,
        'reply_details': replies
    }

    status_path = Path("/home/node/.openclaw/workspace/tmp/email-status.json")
    with open(status_path, 'w') as f:
        json.dump(status, f, indent=2)

    print("="*70)
    print(f"✅ Status saved: {status_path}")
    print("="*70)
    print()
    print("RECOMMENDATION:")
    if bounced:
        print(f"⚠️  {len(bounced)} emails bounced. Fix addresses and resend.")
    else:
        print("✅ All emails delivered successfully")
    print()

if __name__ == "__main__":
    main()
