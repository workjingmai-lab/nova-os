#!/usr/bin/env python3
"""
import os
email-sender-batch2.py — Send remaining emails
"""

import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path

EMAIL_ADDRESS = os.getenv("GMAIL_USER", "YOUR_GMAIL_HERE")
APP_PASSWORD = "qvhwovbtlpcuosxw"

def send_email(to_address, subject, body):
    """Send email via Gmail SMTP."""
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_address
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, APP_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, to_address, msg.as_string())
        server.quit()
        return True, None
    except Exception as e:
        return False, str(e)

def load_message(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    tracker_path = Path("/home/node/.openclaw/workspace/tmp/prospects-with-emails.json")
    with open(tracker_path) as f:
        prospects = json.load(f)

    # Send batch 2 (prospects 6-18)
    print("="*70)
    print("BATCH 2: Remaining 13 prospects")
    print("="*70)
    print()

    success_count = 0
    fail_count = 0

    for i, prospect in enumerate(prospects[5:18], 6):
        prospect_name = prospect['prospect']
        emails = prospect['emails']
        value = prospect['pipeline_value']
        file_path = Path("/home/node/.openclaw/workspace") / prospect['file']

        print(f"{i}. {prospect_name} (${value}K)")
        print(f"   Emails: {', '.join(emails)}")

        if not file_path.exists():
            print(f"   ⚠️  File not found")
            fail_count += 1
            continue

        message_content = load_message(file_path)

        for email in emails:
            subject = f"Service Proposal: {prospect_name}"
            print(f"   📤 {email}...")

            success, error = send_email(email, subject, message_content)

            if success:
                print(f"   ✅ Sent")
                success_count += 1
            else:
                print(f"   ❌ {error}")
                fail_count += 1

        print()

    print("="*70)
    print(f"BATCH 2 COMPLETE: {success_count} sent, {fail_count} failed")
    print("="*70)

if __name__ == "__main__":
    main()
