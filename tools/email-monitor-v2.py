#!/usr/bin/env python3
"""
import os
email-monitor-v2.py — Fixed version, extract bounce details
"""

import imaplib
import email
import json
from pathlib import Path
from datetime import datetime, timedelta

EMAIL_ADDRESS = os.getenv("GMAIL_USER", "YOUR_GMAIL_HERE")
APP_PASSWORD = "qvhwovbtlpcuosxw"

def connect_gmail():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(EMAIL_ADDRESS, APP_PASSWORD)
    mail.select('INBOX')
    return mail

def extract_bounce_details(mail):
    """Extract which specific emails bounced."""
    status, messages = mail.search(None, '(SUBJECT "Service Proposal" UNSEEN)')
    bounced = []

    if status == 'OK':
        for num in messages[0].split()[:20]:  # Last 20
            _, msg_data = mail.fetch(num, '(RFC822)')
            raw_email = msg_data[0][1]
            msg = email.message_from_bytes(raw_email)

            subject = msg['Subject']

            # Check if it's a bounce
            if 'delivery failed' in str(msg).lower() or 'address not found' in str(msg).lower():
                # Extract which email bounced
                for part in msg.walk():
                    if part.get_content_type() == 'text/plain':
                        body = part.get_payload(decode=True).decode('utf-8', errors='ignore')

                        # Find the email address that bounced
                        import re
                        emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', body)

                        bounced.append({
                            'subject': subject,
                            'bounced_to': emails[:3],  # First 3 emails found
                            'from': msg['From']
                        })
                        break

    return bounced

def extract_replies(mail):
    """Extract actual reply content."""
    status, messages = mail.search(None, '(SINCE 05-Feb-2026 UNSEEN)')
    replies = []

    if status == 'OK':
        for num in messages[0].split():
            _, msg_data = mail.fetch(num, '(RFC822)')
            raw_email = msg_data[0][1]
            msg = email.message_from_bytes(raw_email)

            if msg.get('In-Reply-To'):
                for part in msg.walk():
                    if part.get_content_type() == 'text/plain':
                        body = part.get_payload(decode=True).decode('utf-8', errors='ignore')

                        replies.append({
                            'from': msg['From'],
                            'subject': msg['Subject'],
                            'body': body[:500],  # First 500 chars
                            'date': msg['Date']
                        })
                        break

    return replies

def main():
    print("="*70)
    print("EMAIL STATUS CHECK - V2")
    print("="*70)
    print()

    mail = connect_gmail()

    # Check bounces
    print("📬 Bounced emails (last 20):")
    bounces = extract_bounce_details(mail)

    for bounce in bounces:
        print(f"   Subject: {bounce['subject']}")
        print(f"   Bounced to: {bounce['bounced_to']}")
        print(f"   From: {bounce['from']}")
        print()

    # Check replies
    print("💬 Real replies:")
    replies = extract_replies(mail)

    for reply in replies:
        print(f"   From: {reply['from']}")
        print(f"   Subject: {reply['subject']}")
        print(f"   Date: {reply['date']}")
        print(f"   Body: {reply['body'][:200]}...")
        print()

    mail.close()
    mail.logout()

    print("="*70)
    print(f"Total bounces: {len(bounces)}")
    print(f"Total replies: {len(replies)}")
    print("="*70)

if __name__ == "__main__":
    main()
