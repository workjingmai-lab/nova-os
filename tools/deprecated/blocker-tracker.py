#!/usr/bin/env python3
"""
Blocker Tracker — Track and prioritize blockers by ROI

Usage:
    python3 blocker-tracker.py list          # List all blockers
    python3 blocker-tracker.py add           # Add new blocker
    python3 blocker-tracker.py resolve <id>  # Mark blocker resolved
    python3 blocker-tracker.py roi           # Show blockers by ROI/min
"""

import argparse
import json
from datetime import datetime
from pathlib import Path

BLOCKERS_FILE = Path.home() / ".openclaw/workspace/data/blockers.json"

def load_blockers():
    """Load blockers from JSON file."""
    if not BLOCKERS_FILE.exists():
        return []
    with open(BLOCKERS_FILE) as f:
        return json.load(f)

def save_blockers(blockers):
    """Save blockers to JSON file."""
    BLOCKERS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(BLOCKERS_FILE, 'w') as f:
        json.dump(blockers, f, indent=2)

def list_blockers():
    """List all blockers sorted by priority."""
    blockers = load_blockers()
    if not blockers:
        print("✅ No active blockers!")
        return

    # Sort by ROI/min descending
    sorted_blockers = sorted(
        blockers,
        key=lambda b: b.get('roi_per_min', 0),
        reverse=True
    )

    print(f"\n🚧 {len(sorted_blockers)} Active Blockers (sorted by ROI/min):\n")
    for b in sorted_blockers:
        if b['status'] == 'active':
            roi_min = b.get('roi_per_min', 0)
            roi_str = f"${roi_min:,.0f}/min" if roi_min > 0 else "ROI unknown"
            print(f"  [{b['id']}] {b['name']}")
            print(f"      {roi_str} → ${b.get('value', 0):,.0f} in {b.get('time_min', 0)} min")
            print(f"      Action: {b['action']}")
            print()

def add_blocker(name, value, time_min, action, owner='arthur'):
    """Add a new blocker."""
    blockers = load_blockers()

    # Calculate ROI/min
    roi_per_min = value / time_min if time_min > 0 else 0

    new_blocker = {
        'id': len(blockers) + 1,
        'name': name,
        'value': value,
        'time_min': time_min,
        'roi_per_min': roi_per_min,
        'action': action,
        'owner': owner,
        'status': 'active',
        'created': datetime.now().isoformat()
    }

    blockers.append(new_blocker)
    save_blockers(blockers)

    print(f"✅ Blocker added: {name}")
    print(f"   ROI: ${roi_per_min:,.0f}/min (${value:,.0f} in {time_min} min)")

def resolve_blocker(blocker_id):
    """Mark a blocker as resolved."""
    blockers = load_blockers()
    for b in blockers:
        if b['id'] == blocker_id:
            b['status'] = 'resolved'
            b['resolved'] = datetime.now().isoformat()
            save_blockers(blockers)
            print(f"✅ Blocker [{blocker_id}] resolved: {b['name']}")
            return
    print(f"❌ Blocker [{blocker_id}] not found")

def show_roi():
    """Show blockers prioritized by ROI."""
    blockers = load_blockers()
    active = [b for b in blockers if b['status'] == 'active']

    if not active:
        print("✅ No active blockers!")
        return

    # Sort by ROI/min
    sorted_blocks = sorted(active, key=lambda b: b.get('roi_per_min', 0), reverse=True)

    print(f"\n💰 Blocker ROI Priority (highest first):\n")
    total_value = 0
    total_time = 0

    for i, b in enumerate(sorted_blocks, 1):
        roi = b.get('roi_per_min', 0)
        print(f"{i}. {b['name']} — ${roi:,.0f}/min")
        print(f"   ${b['value']:,.0f} in {b['time_min']} min")
        print(f"   Owner: {b['owner']}")
        print()

        total_value += b['value']
        total_time += b['time_min']

    print(f"📊 Summary: ${total_value:,.0f} unblocked in {total_time} min")
    print(f"   Average ROI: ${total_value/total_time:,.0f}/min\n")

def main():
    parser = argparse.ArgumentParser(description='Blocker Tracker')
    subparsers = parser.add_subparsers(dest='command', help='Command')

    # List command
    subparsers.add_parser('list', help='List all blockers')

    # ROI command
    subparsers.add_parser('roi', help='Show blockers by ROI priority')

    # Add command
    add_parser = subparsers.add_parser('add', help='Add new blocker')
    add_parser.add_argument('--name', required=True, help='Blocker name')
    add_parser.add_argument('--value', type=float, required=True, help='Value unlocked ($)')
    add_parser.add_argument('--time', type=int, required=True, help='Time to resolve (min)')
    add_parser.add_argument('--action', required=True, help='Action to resolve')
    add_parser.add_argument('--owner', default='arthur', help='Owner (default: arthur)')

    # Resolve command
    resolve_parser = subparsers.add_parser('resolve', help='Resolve blocker')
    resolve_parser.add_argument('id', type=int, help='Blocker ID')

    args = parser.parse_args()

    if args.command == 'list':
        list_blockers()
    elif args.command == 'add':
        add_blocker(args.name, args.value, args.time, args.action, args.owner)
    elif args.command == 'resolve':
        resolve_blocker(args.id)
    elif args.command == 'roi':
        show_roi()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
