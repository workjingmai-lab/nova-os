import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import os

# Gmail configuration - set via environment variables
# export GMAIL_USER="your.email@gmail.com"
# export GMAIL_PASS="your_app_password"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL = os.getenv("GMAIL_USER", "YOUR_GMAIL_HERE")
PASSWORD = os.getenv("GMAIL_PASS", "YOUR_APP_PASSWORD_HERE")

def send_email(to_email, subject, body):
    """Send email via Gmail SMTP"""
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        context = ssl.create_default_context()
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls(context=context)
            server.login(EMAIL, PASSWORD)
            server.send_message(msg)
        
        return True, f"Sent to {to_email}"
    except Exception as e:
        return False, str(e)

def test_gmail():
    """Test Gmail connection"""
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls(context=context)
            server.login(EMAIL, PASSWORD)
        return True, "Gmail authenticated successfully"
    except Exception as e:
        return False, str(e)

if __name__ == "__main__":
    # Test connection first
    success, msg = test_gmail()
    print(f"Gmail test: {msg}")
    
    if success:
        print("Ready to send emails")
    else:
        print("Gmail authentication failed")
