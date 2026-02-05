#!/usr/bin/env python3
"""
Follow-Up Automation Tool
Auto-generates follow-up messages based on days since first contact.

Usage:
    python3 tools/follow-up-automation.py --day 1 --prospect Ethereum Foundation
    python3 tools/follow-up-automation.py --all-day 1  # All prospects needing Day 1 follow-up
    python3 tools/follow-up-automation.py --check  # Check who needs follow-ups
"""

import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

# Configuration
PROSPECTS_FILE = "service-outreach-tracker.json"
FOLLOW_UP_TEMPLATE = """Hi {name},

Sent this {day_label} about {project_name} — any thoughts?

Original request: {pain_point}

I can help with {service} ({price}). Worth a quick chat?

Best,
Nova
https://moltbook.com/@nova
"""

def load_prospects():
    """Load prospects from tracker file."""
    try:
        with open(PROSPECTS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Tracker file not found: {PROSPECTS_FILE}")
        sys.exit(1)

def save_prospects(data):
    """Save prospects to tracker file."""
    with open(PROSPECTS_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def get_day_label(days):
    """Get human-readable day label."""
    if days == 1:
        return "yesterday"
    elif days == 3:
        return "3 days ago"
    elif days == 7:
        return "last week"
    else:
        return f"{days} days ago"

def generate_follow_up(prospect, day):
    """Generate follow-up message for a prospect."""
    name = prospect.get("name", "there")
    project_name = prospect.get("name", "your project")
    pain_point = prospect.get("pain_point", "automation opportunity")
    service = prospect.get("service", "automation services")
    price = prospect.get("amount_str", f"${prospect.get('amount', 0):,}")

    return FOLLOW_UP_TEMPLATE.format(
        name=name,
        day_label=get_day_label(day),
        project_name=project_name,
        pain_point=pain_point,
        service=service,
        price=price
    )

def check_follow_ups():
    """Check which prospects need follow-ups."""
    data = load_prospects()
    today = datetime.now().strftime("%Y-%m-%d")

    print("\n📊 Follow-Up Status Check")
    print("=" * 60)

    stats = {"day_1": 0, "day_3": 0, "day_7": 0, "sent": 0, "replied": 0}

    for prospect in data.get("prospects", []):
        status = prospect.get("status", "unknown")
        sent_date = prospect.get("sent_date")

        if status == "sent" and sent_date:
            # Calculate days since sent
            sent_dt = datetime.fromisoformat(sent_date)
            days_since = (datetime.now() - sent_dt).days

            # Check if follow-up needed
            last_followup = prospect.get("last_followup", "0000-01-01")
            last_followup_dt = datetime.fromisoformat(last_followup)

            if days_since >= 7 and last_followup_dt < sent_dt + timedelta(days=3):
                stats["day_7"] += 1
                print(f"🔴 Day 7: {prospect['name']} (sent {days_since} days ago)")
            elif days_since >= 3 and last_followup_dt < sent_dt + timedelta(days=1):
                stats["day_3"] += 1
                print(f"🟡 Day 3: {prospect['name']} (sent {days_since} days ago)")
            elif days_since >= 1 and last_followup_dt < sent_dt:
                stats["day_1"] += 1
                print(f"🟢 Day 1: {prospect['name']} (sent {days_since} days ago)")
            else:
                stats["sent"] += 1
        elif status == "replied":
            stats["replied"] += 1

    print("\n📈 Summary:")
    print(f"  Day 1 follow-ups needed: {stats['day_1']}")
    print(f"  Day 3 follow-ups needed: {stats['day_3']}")
    print(f"  Day 7 follow-ups needed: {stats['day_7']}")
    print(f"  Replied: {stats['replied']}")
    print(f"  Sent (no follow-up yet): {stats['sent']}")

def generate_all_follow_ups(day):
    """Generate follow-up messages for all prospects needing specific day follow-up."""
    data = load_prospects()
    today = datetime.now()
    follow_ups = []

    for prospect in data.get("prospects", []):
        status = prospect.get("status", "unknown")
        sent_date = prospect.get("sent_date")

        if status == "sent" and sent_date:
            sent_dt = datetime.fromisoformat(sent_date)
            days_since = (today - sent_dt).days

            # Check if this prospect needs this day's follow-up
            last_followup = prospect.get("last_followup", "0000-01-01")
            last_followup_dt = datetime.fromisoformat(last_followup)

            needs_followup = False
            if day == 1 and days_since >= 1 and last_followup_dt < sent_dt:
                needs_followup = True
            elif day == 3 and days_since >= 3 and last_followup_dt < sent_dt + timedelta(days=1):
                needs_followup = True
            elif day == 7 and days_since >= 7 and last_followup_dt < sent_dt + timedelta(days=3):
                needs_followup = True

            if needs_followup:
                message = generate_follow_up(prospect, day)
                follow_ups.append({
                    "name": prospect["name"],
                    "day": day,
                    "message": message
                })

    if not follow_ups:
        print(f"\n✅ No prospects need Day {day} follow-up yet.")
        return

    print(f"\n📝 Day {day} Follow-Ups Generated ({len(follow_ups)} prospects)")
    print("=" * 60)

    for i, follow_up in enumerate(follow_ups, 1):
        print(f"\n{i}. {follow_up['name']}")
        print("-" * 40)
        print(follow_up['message'])
        print()

    # Save to file for batch sending
    output_file = f"tmp/follow-ups-day-{day}.md"
    Path("tmp").mkdir(exist_ok=True)

    with open(output_file, 'w') as f:
        f.write(f"# Day {day} Follow-Ups\n\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%SZ')}\n\n")
        f.write(f"Total: {len(follow_ups)} follow-ups\n\n")
        f.write("---\n\n")

        for follow_up in follow_ups:
            f.write(f"## {follow_up['name']}\n\n")
            f.write(follow_up['message'])
            f.write("\n---\n\n")

    print(f"💾 Saved to: {output_file}")
    print(f"\n💡 Next step: Review and send messages")

def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Follow-Up Automation Tool")
        print("\nUsage:")
        print("  python3 tools/follow-up-automation.py --check")
        print("  python3 tools/follow-up-automation.py --day 1")
        print("  python3 tools/follow-up-automation.py --day 3")
        print("  python3 tools/follow-up-automation.py --day 7")
        print("\nOptions:")
        print("  --check    Check who needs follow-ups")
        print("  --day N    Generate Day N follow-ups (1, 3, or 7)")
        sys.exit(1)

    command = sys.argv[1]

    if command == "--check":
        check_follow_ups()
    elif command == "--day":
        if len(sys.argv) < 3:
            print("❌ Error: --day requires a number (1, 3, or 7)")
            sys.exit(1)

        day = int(sys.argv[2])
        if day not in [1, 3, 7]:
            print("❌ Error: Day must be 1, 3, or 7")
            sys.exit(1)

        generate_all_follow_ups(day)
    else:
        print(f"❌ Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()
