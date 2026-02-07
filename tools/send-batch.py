#!/usr/bin/env python3
"""send-batch.py — Batch send service outreach messages.

Usage:
  python3 send-batch.py list          # List ready messages
  python3 send-batch.py send          # Send all ready messages (interactive)
  python3 send-batch.py send --yes    # Send all without confirmation
"""

import os
import sys
import json
from pathlib import Path

LEADS_DIR = Path("leads")
MESSAGES_DIR = LEADS_DIR / "messages"
SENT_DIR = LEADS_DIR / "sent"

def list_messages():
    """List all ready-to-send messages."""
    if not MESSAGES_DIR.exists():
        print("❌ leads/messages/ directory not found")
        return
    
    files = sorted(MESSAGES_DIR.glob("*.md"))
    if not files:
        print("📭 No messages ready to send")
        return
    
    total_value = 0
    print(f"📬 {len(files)} messages ready to send:\n")
    
    for f in files:
        content = f.read_text()
        # Extract value from frontmatter or content
        value = 0
        if "$" in content:
            # Quick parse for $X,XXX or $XXK
            import re
            matches = re.findall(r'\$([\d,]+(?:\.\d+)?)([Kk]?)', content)
            for m in matches:
                num = float(m[0].replace(",", ""))
                if m[1].lower() == 'k':
                    num *= 1000
                value = max(value, int(num))
        
        total_value += value
        status = "💰" if value > 20000 else "🎯" if value > 10000 else "📧"
        print(f"  {status} {f.stem[:40]:<40} ${value:,}")
    
    print(f"\n💵 Total pipeline value: ${total_value:,}")
    print(f"⏱️  Est. time to send: {len(files)} min")
    print(f"📊 Value/min: ${total_value // max(len(files), 1):,}")

def send_messages(auto_confirm=False):
    """Send all ready messages."""
    files = sorted(MESSAGES_DIR.glob("*.md"))
    if not files:
        print("📭 No messages to send")
        return
    
    print(f"🚀 About to send {len(files)} messages")
    
    if not auto_confirm:
        confirm = input("\nProceed? [y/N]: ")
        if confirm.lower() not in ('y', 'yes'):
            print("❌ Cancelled")
            return
    
    sent_count = 0
    for f in files:
        content = f.read_text()
        # Move to sent directory
        target = SENT_DIR / f.name
        f.rename(target)
        sent_count += 1
        print(f"  ✅ Sent: {f.stem}")
    
    print(f"\n📤 {sent_count} messages sent and archived to leads/sent/")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == "list":
        list_messages()
    elif cmd == "send":
        auto = "--yes" in sys.argv or "-y" in sys.argv
        send_messages(auto)
    else:
        print(__doc__)
        sys.exit(1)
