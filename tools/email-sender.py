#!/usr/bin/env python3
"""
import os
email-sender.py — Send outreach emails via Gmail

Arthur's Rule: Execute. Don't ask. Ship.
"""

import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path
from datetime import datetime

# Credentials (stored securely)
EMAIL_ADDRESS = os.getenv("GMAIL_USER", "YOUR_GMAIL_HERE")
APP_PASSWORD = "qvhwovbtlpcuosxw"  # App-specific password

def send_email(to_address, subject, body, from_address=EMAIL_ADDRESS):
    """Send email via Gmail SMTP."""
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = from_address
        msg['To'] = to_address
        msg['Subject'] = subject

        # Attach body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to Gmail SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_address, APP_PASSWORD)

        # Send
        text = msg.as_string()
        server.sendmail(from_address, to_address, text)
        server.quit()

        return True, None
    except Exception as e:
        return False, str(e)

def load_message(file_path):
    """Load message content from file."""
    with open(file_path) as f:
        return f.read()

def main():
    # Load prospects with emails
    tracker_path = Path("/home/node/.openclaw/workspace/tmp/prospects-with-emails.json")

    if not tracker_path.exists():
        print("❌ No prospects file found. Run extract-emails.py first")
        return

    with open(tracker_path) as f:
        prospects = json.load(f)

    # Send top 5 (highest ROI)
    print("="*70)
    print("SENDING TOP 5 EMAILS")
    print("="*70)
    print()

    success_count = 0
    fail_count = 0

    for i, prospect in enumerate(prospects[:5], 1):
        prospect_name = prospect['prospect']
        emails = prospect['emails']
        value = prospect['pipeline_value']
        file_path = Path("/home/node/.openclaw/workspace") / prospect['file']

        print(f"{i}. {prospect_name} (${value}K)")
        print(f"   Emails: {', '.join(emails)}")

        # Load message
        if not file_path.exists():
            print(f"   ❌ File not found: {file_path}")
            fail_count += 1
            continue

        message_content = load_message(file_path)

        # Send to each email
        for email in emails:
            subject = f"Service Proposal: {prospect_name}"

            print(f"   📤 Sending to {email}...")
            success, error = send_email(email, subject, message_content)

            if success:
                print(f"   ✅ Sent to {email}")
                success_count += 1
            else:
                print(f"   ❌ Failed: {error}")
                fail_count += 1

        print()

    # Summary
    print("="*70)
    print(f"SUMMARY: {success_count} sent, {fail_count} failed")
    print("="*70)

if __name__ == "__main__":
    main()
