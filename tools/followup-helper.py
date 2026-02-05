#!/usr/bin/env python3
"""
followup-helper.py — Follow-Up Management Tool

Purpose: Track and manage follow-ups for revenue pipeline.
Checks pipeline for items needing follow-up, suggests templates, logs attempts.

Usage:
    python3 tools/followup-helper.py check          # Check who needs follow-up
    python3 tools/followup-helper.py send --name "Lido DAO" --type value-add
    python3 tools/followup-helper.py respond --name "Lido DAO" --response interested
    python3 tools/followup-helper.py log --name "Lido DAO" --note "Replied, want call"
"""

import json
import argparse
from datetime import datetime, timedelta
from pathlib import Path

# Configuration
PIPELINE_FILE = Path("/home/node/.openclaw/workspace/data/revenue-pipeline.json")
FOLLOWUP_LOG = Path("/home/node/.openclaw/workspace/data/followups.json")

# Follow-up templates
TEMPLATES = {
    "clarification": """Hi {name},

Sent over the {proposal} on {date}. Any questions I can clarify?

A few folks asked about {common_question} — happy to walk through it if helpful.

Best,
Nova""",
    "value-add": """Hi {name},

Saw your post about {topic} — great insight on {specific_point}.

Reminded me of our conversation about {problem}. The {solution} I sent last week addresses exactly this. Let me know if you'd like to revisit.

Best,
Nova""",
    "close": """Hi {name},

Circling back on the {proposal} from {date}.

Should I close the loop on this, or is there still interest? No pressure either way.

Best,
Nova""",
    "news": """Hi {name},

Saw the news about {event} — seems relevant to what we discussed.

{insight}

The {proposal} I sent covers this. Worth revisiting?

Best,
Nova"""
}


def load_pipeline():
    """Load pipeline data from JSON file."""
    if not PIPELINE_FILE.exists():
        print(f"❌ Pipeline file not found: {PIPELINE_FILE}")
        return None

    with open(PIPELINE_FILE, 'r') as f:
        return json.load(f)


def save_pipeline(data):
    """Save pipeline data to JSON file."""
    PIPELINE_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(PIPELINE_FILE, 'w') as f:
        json.dump(data, f, indent=2)


def load_followup_log():
    """Load follow-up log from JSON file."""
    if not FOLLOWUP_LOG.exists():
        FOLLOWUP_LOG.parent.mkdir(parents=True, exist_ok=True)
        return {"followups": []}

    with open(FOLLOWUP_LOG, 'r') as f:
        return json.load(f)


def save_followup_log(data):
    """Save follow-up log to JSON file."""
    FOLLOWUP_LOG.parent.mkdir(parents=True, exist_ok=True)

    with open(FOLLOWUP_LOG, 'w') as f:
        json.dump(data, f, indent=2)


def check_followups():
    """Check pipeline for items needing follow-up."""
    pipeline = load_pipeline()
    if not pipeline:
        return

    today = datetime.now()
    needs_followup = []

    for category in ["grants", "services", "bounties"]:
        if category not in pipeline:
            continue

        for item in pipeline[category]:
            # Only check submitted items
            if item.get("status") != "submitted":
                continue

            # Parse submitted date (try multiple fields)
            submitted_str = item.get("submittedDate") or item.get("updated") or item.get("created")
            if not submitted_str:
                continue

            try:
                # Handle various datetime formats
                submitted_str = submitted_str.replace("Z", "+00:00").split(".")[0].replace("+00:00", "")
                submitted_date = datetime.fromisoformat(submitted_str)
            except Exception as e:
                continue

            # Calculate days since submission
            days_since = (today - submitted_date.replace(tzinfo=None)).days

            # Check existing follow-ups
            followups = item.get("followUps", [])
            last_followup_date = None
            if followups:
                try:
                    last_followup_date = datetime.fromisoformat(followups[-1].get("date", "").replace("Z", "+00:00"))
                except:
                    pass

            # Determine if follow-up needed
            followup_type = None
            urgency = "normal"

            if days_since >= 3 and days_since < 7 and not any(f.get("type") == "clarification" for f in followups):
                followup_type = "clarification"
                urgency = "high"
            elif days_since >= 7 and days_since < 14 and not any(f.get("type") == "value-add" for f in followups):
                followup_type = "value-add"
                urgency = "normal"
            elif days_since >= 14 and not any(f.get("type") == "close" for f in followups):
                followup_type = "close"
                urgency = "low"
            elif days_since >= 30:
                followup_type = "archive"
                urgency = "archive"

            if followup_type:
                needs_followup.append({
                    "name": item.get("name"),
                    "category": category,
                    "potential": item.get("potential"),
                    "days_since": days_since,
                    "followup_type": followup_type,
                    "urgency": urgency,
                    "submitted_date": submitted_str
                })

    # Sort by urgency (high > normal > low > archive)
    urgency_order = {"high": 0, "normal": 1, "low": 2, "archive": 3}
    needs_followup.sort(key=lambda x: urgency_order.get(x["urgency"], 99))

    # Display results
    if not needs_followup:
        print("✅ No follow-ups needed today!")
    else:
        print(f"📧 {len(needs_followup)} items need follow-up:\n")

        for item in needs_followup:
            emoji = "🔴" if item["urgency"] == "high" else "🟡" if item["urgency"] == "normal" else "🟢"
            print(f"{emoji} **{item['name']}** ({item['category']})")
            print(f"   Potential: ${item['potential']:,}")
            print(f"   Days since submission: {item['days_since']}")
            print(f"   Suggested action: {item['followup_type']}")
            print(f"   Template: `followup-helper.py send --name '{item['name']}' --type {item['followup_type']}`")
            print()


def send_followup(name, followup_type, dry_run=False):
    """Generate follow-up message for a pipeline item."""
    pipeline = load_pipeline()
    if not pipeline:
        return

    # Find the item
    target_item = None
    target_category = None

    for category in ["grants", "services", "bounties"]:
        if category not in pipeline:
            continue

        for item in pipeline[category]:
            if item.get("name") == name:
                target_item = item
                target_category = category
                break

        if target_item:
            break

    if not target_item:
        print(f"❌ Item not found: {name}")
        return

    # Get template
    template = TEMPLATES.get(followup_type)
    if not template:
        print(f"❌ Unknown follow-up type: {followup_type}")
        print(f"   Available types: {', '.join(TEMPLATES.keys())}")
        return

    # Generate message
    message = template.format(
        name=name,
        proposal=f"{target_category} proposal",
        date=target_item.get("submittedDate", "recently"),
        common_question="timeline and deliverables",
        topic="recent developments",
        specific_point="governance challenges",
        problem=target_item.get("notes", "the problem we discussed"),
        solution="automation solution",
        event="relevant updates",
        insights="See proposal for details"
    )

    print(f"📧 Follow-up message for {name} ({followup_type}):\n")
    print("=" * 60)
    print(message)
    print("=" * 60)
    print()

    if not dry_run:
        # Log the follow-up
        log = load_followup_log()
        log["followups"].append({
            "name": name,
            "category": target_category,
            "type": followup_type,
            "date": datetime.now().isoformat(),
            "message": message
        })
        save_followup_log(log)

        # Update pipeline item
        if "followUps" not in target_item:
            target_item["followUps"] = []

        target_item["followUps"].append({
            "date": datetime.now().isoformat(),
            "type": followup_type,
            "response": "pending"
        })

        # Calculate next follow-up date
        today = datetime.now()
        if followup_type == "clarification":
            next_date = today + timedelta(days=4)
        elif followup_type == "value-add":
            next_date = today + timedelta(days=7)
        elif followup_type == "close":
            next_date = today + timedelta(days=14)
        else:
            next_date = today + timedelta(days=7)

        target_item["nextFollowUp"] = next_date.isoformat()
        save_pipeline(pipeline)

        print(f"✅ Follow-up logged and pipeline updated.")
        print(f"   Next follow-up: {next_date.strftime('%Y-%m-%d')}")


def log_response(name, response, note=None):
    """Log a response to a follow-up."""
    pipeline = load_pipeline()
    if not pipeline:
        return

    # Find the item
    for category in ["grants", "services", "bounties"]:
        if category not in pipeline:
            continue

        for item in pipeline[category]:
            if item.get("name") == name:
                # Update last follow-up response
                if "followUps" in item and item["followUps"]:
                    item["followUps"][-1]["response"] = response
                    if note:
                        item["followUps"][-1]["note"] = note

                save_pipeline(pipeline)
                print(f"✅ Response logged for {name}: {response}")
                return

    print(f"❌ Item not found: {name}")


def show_stats():
    """Show follow-up statistics."""
    log = load_followup_log()

    total_followups = len(log.get("followups", []))
    responses = sum(1 for f in log.get("followups", []) if f.get("response") not in ["none", "pending"])

    print(f"📊 Follow-Up Statistics:\n")
    print(f"Total follow-ups sent: {total_followups}")
    print(f"Responses received: {responses}")
    print(f"Response rate: {responses / total_followups * 100:.1f}%" if total_followups > 0 else "Response rate: N/A")


def main():
    parser = argparse.ArgumentParser(description="Follow-Up Management Tool")
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Check command
    subparsers.add_parser("check", help="Check who needs follow-up")

    # Send command
    send_parser = subparsers.add_parser("send", help="Generate follow-up message")
    send_parser.add_argument("--name", required=True, help="Pipeline item name")
    send_parser.add_argument("--type", required=True, choices=list(TEMPLATES.keys()), help="Follow-up type")
    send_parser.add_argument("--dry-run", action="store_true", help="Preview without logging")

    # Respond command
    respond_parser = subparsers.add_parser("respond", help="Log response to follow-up")
    respond_parser.add_argument("--name", required=True, help="Pipeline item name")
    respond_parser.add_argument("--response", required=True, choices=["interested", "not_interested", "replied", "none"], help="Response type")
    respond_parser.add_argument("--note", help="Additional notes")

    # Stats command
    subparsers.add_parser("stats", help="Show follow-up statistics")

    args = parser.parse_args()

    if args.command == "check":
        check_followups()
    elif args.command == "send":
        send_followup(args.name, args.type, args.dry_run)
    elif args.command == "respond":
        log_response(args.name, args.response, args.note)
    elif args.command == "stats":
        show_stats()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
