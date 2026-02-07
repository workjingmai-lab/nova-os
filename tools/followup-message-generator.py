#!/usr/bin/env python3
"""
Follow-up Message Generator
Creates Day 3/7/14/21 follow-up messages for pipeline leads
"""

import json
from datetime import datetime
from pathlib import Path

FOLLOWUP_TEMPLATES = {
    3: {
        "subject": "Quick follow-up: {opportunity}",
        "opening": "Hi {{name}},\n\nFollowing up on my previous message about {opportunity}.",
        "body": """I wanted to bump this to the top of your inbox.

{pain_point}

{solution}

I've attached the original message below for reference.

Are you available for a quick 15-minute call this week? I'd love to learn more about your current challenges and explore how I can help.

Best,
{sender}""",
        "closing": "No pressure — just wanted to ensure this didn't get buried."
    },
    7: {
        "subject": "Re: {opportunity} — Any thoughts?",
        "opening": "Hi {{name}},\n\nChecking in on {opportunity}.",
        "body": """I understand you're busy, so I'll be brief.

{pain_point}

{solution}

I'm still excited about this opportunity and would love to explore if there's a fit.

Would a quick call work next week?

Best,
{sender}"""
    },
    14: {
        "subject": "Still interested in {opportunity}?",
        "opening": "Hi {{name}},\n\nHope you're doing well.",
        "body": """I'm following up one more time about {opportunity}.

{pain_point}

{solution}

If the timing isn't right, I completely understand. But if you're still interested, I'm ready to move forward.

Let me know if you'd like to chat.

Best,
{sender}"""
    },
    21: {
        "subject": "Last check-in: {opportunity}",
        "opening": "Hi {{name}},\n\nFinal follow-up from my end.",
        "body": """I'll respect your time and make this the last check-in about {opportunity}.

{pain_point}

{solution}}

If you ever want to revisit this, my door is always open.

All the best,
{sender}

---

P.S. I'll be sharing case studies from similar projects soon — happy to keep you in the loop if you're interested."""
    }
}

def load_pipeline():
    """Load revenue pipeline data"""
    pipeline_file = Path("/home/node/.openclaw/workspace/revenue-pipeline.json")
    if not pipeline_file.exists():
        return []

    with open(pipeline_file) as f:
        return json.load(f)

def get_followups_due(pipeline):
    """Get items needing follow-up"""
    followups = []
    for item in pipeline:
        if item.get("last_contact"):
            last_contact = datetime.fromisoformat(item["last_contact"])
            days_since = (datetime.now() - last_contact).days

            if days_since in [3, 7, 14, 21]:
                followups.append({
                    "item": item,
                    "day": days_since,
                    "potential": item.get("potential_value", 0)
                })

    # Sort by potential value (descending)
    followups.sort(key=lambda x: x["potential"], reverse=True)
    return followups

def generate_followup(item, day):
    """Generate follow-up message for item"""
    template = FOLLOWUP_TEMPLATES[day]

    message = f"""Subject: {template['subject'].format(opportunity=item['name'])}

{template['opening']}

{template['body'].format(
    pain_point=item.get('pain_point', 'Your current challenge'),
    solution=item.get('solution', 'My proposed solution'),
    sender='Nova'
)}

{template.get('closing', '')}
"""
    return message

def main():
    """Main function"""
    pipeline = load_pipeline()
    followups = get_followups_due(pipeline)

    print(f"📋 FOLLOW-UP MESSAGES NEEDED: {len(followups)}")
    print("=" * 60)

    total_value = sum(f["potential"] for f in followups)

    for i, followup in enumerate(followups[:10], 1):  # Top 10
        item = followup["item"]
        day = followup["day"]
        potential = followup["potential"]

        print(f"\n{i}. {item['name']} — ${potential:,.0f} [Day {day}]")
        print(f"   Status: {item['status']}")

        message = generate_followup(item, day)
        print(f"\n{message}")
        print("-" * 60)

    print(f"\n💰 Total value needing follow-up: ${total_value:,.0f}")
    print(f"📧 Messages to send: {len(followups)}")

if __name__ == "__main__":
    main()
