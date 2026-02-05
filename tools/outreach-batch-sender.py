#!/usr/bin/env python3
"""
Outreach Batch Sender — Speed up service outreach execution

Reads prepared outreach messages from outreach/messages/ and presents them
in batches for rapid sending. Tracks sent messages and updates revenue pipeline.

Usage:
    python3 tools/outreach-batch-sender.py              # List all messages
    python3 tools/outreach-batch-sender.py --high       # HIGH priority only
    python3 tools/outreach-batch-sender.py --medium     # MEDIUM priority only
    python3 tools/outreach-batch-sender.py --batch 5    # Show 5 at a time
    python3 tools/outreach-batch-sender.py --send       # Mark as sent (interactive)
"""

import argparse
import json
import os
import re
from pathlib import Path
from typing import List, Dict


def parse_priority(content: str) -> str:
    """Extract priority from message content."""
    for line in content.split('\n'):
        # Handle markdown format: **Priority:** HIGH
        if 'priority:' in line.lower():
            line_upper = line.upper()
            if 'HIGH' in line_upper:
                return 'HIGH'
            elif 'MEDIUM' in line_upper:
                return 'MEDIUM'
            elif 'LOW' in line_upper:
                return 'LOW'
    return 'MEDIUM'  # Default


def parse_value(content: str) -> int:
    """Extract dollar value from message content."""
    for line in content.split('\n'):
        # Handle markdown format: **Potential Value:** $40,000
        if 'value' in line.lower() and 'potential' in line.lower():
            match = re.search(r'\$?([\d,]+)', line)
            if match:
                return int(match.group(1).replace(',', ''))
    return 0


def load_messages(messages_dir: str = "outreach/messages") -> List[Dict]:
    """Load all outreach messages from directory."""
    messages = []
    path = Path(messages_dir)

    if not path.exists():
        print(f"❌ Directory not found: {messages_dir}")
        return []

    for file in sorted(path.glob("*.md")):
        with open(file, 'r') as f:
            content = f.read()
            priority = parse_priority(content)
            value = parse_value(content)

            messages.append({
                'file': str(file),
                'name': file.stem.replace('-', ' ').title(),
                'priority': priority,
                'value': value,
                'content': content
            })

    return messages


def filter_messages(messages: List[Dict], priority: str = None) -> List[Dict]:
    """Filter messages by priority."""
    if priority:
        return [m for m in messages if m['priority'] == priority.upper()]
    return messages


def sort_messages(messages: List[Dict]) -> List[Dict]:
    """Sort messages by priority (HIGH > MEDIUM > LOW) then value (desc)."""
    priority_order = {'HIGH': 0, 'MEDIUM': 1, 'LOW': 2}

    return sorted(
        messages,
        key=lambda m: (priority_order.get(m['priority'], 1), -m['value'])
    )


def display_messages(messages: List[Dict], batch_size: int = None):
    """Display messages in batches."""
    total_value = sum(m['value'] for m in messages)
    total_count = len(messages)

    print(f"\n{'='*80}")
    print(f"📧 Outreach Messages: {total_count} messages | ${total_value:,} total value")
    print(f"{'='*80}\n")

    if batch_size:
        batches = [messages[i:i + batch_size] for i in range(0, len(messages), batch_size)]
        for i, batch in enumerate(batches, 1):
            batch_value = sum(m['value'] for m in batch)
            print(f"📦 Batch {i}/{len(batches)} ({len(batch)} messages, ${batch_value:,})")
            for msg in batch:
                print(f"   {msg['priority']} | ${msg['value']:,} | {msg['name']}")
            print()
    else:
        # Group by priority
        by_priority = {'HIGH': [], 'MEDIUM': [], 'LOW': []}
        for msg in messages:
            by_priority[msg['priority']].append(msg)

        for priority in ['HIGH', 'MEDIUM', 'LOW']:
            if by_priority[priority]:
                priority_value = sum(m['value'] for m in by_priority[priority])
                print(f"🎯 {priority} Priority: {len(by_priority[priority])} messages | ${priority_value:,}")
                for msg in sort_messages(by_priority[priority]):
                    print(f"   ${msg['value']:,} | {msg['name']}")
                print()


def show_message_content(messages: List[Dict]):
    """Interactive mode: show message content one by one."""
    print("\n📋 Interactive Mode: Press Enter to show next message, Ctrl+C to exit\n")

    try:
        for i, msg in enumerate(messages, 1):
            print(f"\n{'─'*80}")
            print(f"Message {i}/{len(messages)}: {msg['name']}")
            print(f"Priority: {msg['priority']} | Value: ${msg['value']:,}")
            print(f"File: {msg['file']}")
            print(f"{'─'*80}\n")
            print(msg['content'])
            print(f"\n{'─'*80}")
            input(f"\n✅ Mark '{msg['name']}' as sent? (Press Enter to continue) ")

    except KeyboardInterrupt:
        print("\n\n👋 Exiting interactive mode")


def mark_sent_interactive(messages: List[Dict]):
    """Mark messages as sent interactively."""
    print("\n📤 Mark Messages as Sent\n")

    for i, msg in enumerate(messages, 1):
        print(f"\n[{i}/{len(messages)}] {msg['name']} ({msg['priority']}, ${msg['value']:,})")
        response = input(f"Mark as sent? (y/n/s=skip, default=y): ").strip().lower()

        if response == '' or response == 'y':
            # Update revenue tracker
            print(f"✅ Marking '{msg['name']}' as sent...")
            # TODO: Integrate with revenue-tracker.py
        elif response == 's':
            print(f"⏭️  Skipping '{msg['name']}'...")
        else:
            print(f"⏭️  Skipping '{msg['name']}'...")


def main():
    parser = argparse.ArgumentParser(
        description="Batch sender for outreach messages",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 tools/outreach-batch-sender.py              # List all messages
  python3 tools/outreach-batch-sender.py --high       # HIGH priority only
  python3 tools/outreach-batch-sender.py --batch 5    # Show 5 at a time
  python3 tools/outreach-batch-sender.py --interactive  # Show content interactively
        """
    )

    parser.add_argument('--high', action='store_true', help='Show HIGH priority only')
    parser.add_argument('--medium', action='store_true', help='Show MEDIUM priority only')
    parser.add_argument('--low', action='store_true', help='Show LOW priority only')
    parser.add_argument('--batch', type=int, metavar='N', help='Show in batches of N')
    parser.add_argument('--interactive', '-i', action='store_true', help='Interactive mode: show content')
    parser.add_argument('--send', action='store_true', help='Mark as sent (interactive)')

    args = parser.parse_args()

    # Load messages
    messages = load_messages()

    if not messages:
        return

    # Filter by priority
    if args.high:
        messages = filter_messages(messages, 'HIGH')
    elif args.medium:
        messages = filter_messages(messages, 'MEDIUM')
    elif args.low:
        messages = filter_messages(messages, 'LOW')

    # Sort
    messages = sort_messages(messages)

    # Display or interact
    if args.interactive:
        show_message_content(messages)
    elif args.send:
        mark_sent_interactive(messages)
    else:
        display_messages(messages, args.batch)


if __name__ == '__main__':
    main()
