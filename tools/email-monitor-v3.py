#!/usr/bin/env python3
"""
import os
email-monitor-v3.py — Search ALL messages (not just unseen)
"""

import imaplib
import email
from pathlib import Path

EMAIL_ADDRESS = os.getenv("GMAIL_USER", "YOUR_GMAIL_HERE")
APP_PASSWORD = "qvhwovbtlpcuosxw"

def main():
    print("="*70)
    print("EMAIL STATUS CHECK - ALL MESSAGES")
    print("="*70)
    print()

    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(EMAIL_ADDRESS, APP_PASSWORD)
    mail.select('INBOX')

    # Search for ALL messages from today
    status, messages = mail.search(None, '(SINCE 05-Feb-2026)')

    if status == 'OK':
        total = len(messages[0].split())
        print(f"📊 Total messages since Feb 5: {total}")
        print()

        # Get last 50 messages
        recent = messages[0].split()[-50:]

        print("📬 Last 50 messages (most recent first):")
        print()

        for num in reversed(recent):
            _, msg_data = mail.fetch(num, '(RFC822)')
            raw_email = msg_data[0][1]
            msg = email.message_from_bytes(raw_email)

            from_addr = msg['From']
            subject = msg['Subject']

            # Categorize
            if 'delivery status' in subject.lower() or 'delivery failure' in subject.lower():
                category = "🔴 BOUNCE"
            elif 're: service proposal' in subject.lower():
                category = "🎉 REPLY"
            elif 'service proposal' in subject.lower():
                category = "📤 SENT"
            else:
                category = "📧 OTHER"

            print(f"{category} | {from_addr}")
            print(f"        {subject}")
            print()

    mail.close()
    mail.logout()

if __name__ == "__main__":
    main()
