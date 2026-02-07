#!/usr/bin/env python3
"""
import os
read-replies.py — Extract full reply content from Infura + Balancer
"""

import imaplib
import email

EMAIL_ADDRESS = os.getenv("GMAIL_USER", "YOUR_GMAIL_HERE")
APP_PASSWORD = "qvhwovbtlpcuosxw"

def main():
    print("="*70)
    print("EXTRACTING REPLIES FROM INFURA + BALANCER")
    print("="*70)
    print()

    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(EMAIL_ADDRESS, APP_PASSWORD)
    mail.select('INBOX')

    # Search for replies
    status, messages = mail.search(None, '(SUBJECT "Re: Service Proposal" SINCE 05-Feb-2026)')

    if status == 'OK':
        for num in messages[0].split():
            _, msg_data = mail.fetch(num, '(RFC822)')
            raw_email = msg_data[0][1]
            msg = email.message_from_bytes(raw_email)

            from_addr = msg['From']
            subject = msg['Subject']

            print(f"From: {from_addr}")
            print(f"Subject: {subject}")
            print()
            print("BODY:")
            print("-" * 70)

            # Extract body
            for part in msg.walk():
                if part.get_content_type() == 'text/plain':
                    body = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                    print(body)
                    break

            print("-" * 70)
            print()

    mail.close()
    mail.logout()

if __name__ == "__main__":
    main()
