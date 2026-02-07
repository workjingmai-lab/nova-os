#!/usr/bin/env python3
"""
Service Message Batch Sender
Helps Arthur send multiple outreach messages in one session
"""

import json
from pathlib import Path

OUTREACH_DIR = Path("/home/node/.openclaw/workspace/outreach/messages")
TRACKER_FILE = Path("/home/node/.openclaw/workspace/follow-up-tracker.json")

def list_ready_messages(limit=None):
    """List all ready outreach messages"""
    messages = []

    for file in sorted(OUTREACH_DIR.glob("*.md")):
        with open(file) as f:
            content = f.read()

        # Extract metadata from content
        name = file.stem.replace("-", " ").title()
        potential = extract_potential(content)

        messages.append({
            "file": file,
            "name": name,
            "potential": potential,
            "content": content
        })

    # Sort by potential value (descending)
    messages.sort(key=lambda x: x["potential"], reverse=True)

    if limit:
        messages = messages[:limit]

    return messages

def extract_potential(content):
    """Extract potential value from message content"""
    for line in content.split("\n"):
        if "Potential Value:" in line or "Value:" in line:
            # Extract dollar amount
            parts = line.split("$")
            if len(parts) > 1:
                try:
                    amount_str = parts[1].split()[0].replace(",", "")
                    return float(amount_str)
                except:
                    pass
    return 0

def generate_send_plan(top_n=None):
    """Generate send plan for top N prospects"""
    messages = list_ready_messages(top_n)

    print(f"📋 SEND PLAN: Top {len(messages)} prospects")
    print("=" * 60)

    total_value = sum(m["potential"] for m in messages)

    for i, msg in enumerate(messages, 1):
        print(f"\n{i}. {msg['name']} — ${msg['potential']:,.0f}")
        print(f"   File: {msg['file']}")
        print(f"   Preview: {msg['content'][:100]}...")

    print(f"\n💰 Total value: ${total_value:,.0f}")
    print(f"⏱️  Estimated time: {len(messages) * 2} minutes")

    return messages

def generate_commands(messages):
    """Generate shell commands for sending"""
    commands = []

    for msg in messages:
        commands.append(f"# {msg['name']} (${msg['potential']:,.0f})")
        commands.append(f"cat {msg['file']} | pbcopy  # Copy to clipboard")
        commands.append(f"# Paste into email/Discord and send")
        commands.append(f"python3 tools/follow-up-tracker.py add \"{msg['name']}\" {msg['potential']} \"MEDIUM\"")
        commands.append("")

    return "\n".join(commands)

def main():
    """Main function"""
    import sys

    if len(sys.argv) < 2:
        print("Usage:")
        print("  service-batch-send.py --top N     # Show top N prospects")
        print("  service-batch-send.py --all       # Show all prospects")
        print("  service-batch-send.py --commands  # Generate copy-paste commands")
        return

    if sys.argv[1] == "--top":
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 10
        messages = generate_send_plan(n)

    elif sys.argv[1] == "--all":
        messages = generate_send_plan()

    elif sys.argv[1] == "--commands":
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 10
        messages = list_ready_messages(n)
        commands = generate_commands(messages)
        print(commands)

        # Save to file for easy reference
        with open("/home/node/.openclaw/workspace/tmp/send-commands.txt", "w") as f:
            f.write(commands)
        print(f"\n✅ Commands saved to tmp/send-commands.txt")

if __name__ == "__main__":
    main()
