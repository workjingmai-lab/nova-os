#!/usr/bin/env python3
"""
response-templates.py - Pre-written reply templates for lead responses
Convert "they replied" → "meeting booked" with tested responses
"""

import json
import sys
from datetime import datetime, timedelta

TEMPLATES = {
    "interested": {
        "label": "✅ Interested / Positive",
        "trigger": ["interested", "sounds good", "tell me more", "yes", "let's talk", "curious"],
        "response": """Great! I'd love to dive deeper.

Quick questions to tailor this:
1. What's your biggest automation pain point right now?
2. Timeline — urgent (this week) or exploratory (next month)?
3. Best way to connect? (Calendly link / Telegram / quick call)

I can share relevant case studies once I know your context.

— Nova ✨""",
        "goal": "Book discovery call",
        "timing": "Reply within 2 hours (they're hot)"
    },
    
    "pricing": {
        "label": "💰 Pricing Question",
        "trigger": ["how much", "pricing", "cost", "rate", "fee", "budget"],
        "response": """Depends on scope, but here's the range:

• Quick automation: $1-2K (3-5 days)
• Full OpenClaw setup: $3-5K (1-2 weeks)
• Multi-agent system: $10-25K (2-4 weeks)
• Monthly retainer: $1-4K/month (ongoing optimization)

Most clients start with a $500-$1K audit → we identify quick wins → you decide on full build.

Want me to send the audit questionnaire?

— Nova ✨""",
        "goal": "Move to audit or scope discussion",
        "timing": "Reply within 4 hours (price shopping = comparison mode)"
    },
    
    "info": {
        "label": "📋 Needs More Info",
        "trigger": ["can you explain", "what exactly", "how does", "more details", "examples"],
        "response": """Happy to clarify. Here's the 30-second version:

I build autonomous agents using OpenClaw that handle:
• Repetitive workflows (data entry, reports, scheduling)
• Multi-step processes (research → draft → review → send)
• Integration across your tools (GitHub, Notion, Telegram, etc.)

Example: Built a content agent that researches → drafts → publishes → tracks metrics. Client saves 10 hrs/week.

Want me to send a 2-min Loom walkthrough of a similar project?

— Nova ✨""",
        "goal": "Provide proof, book call",
        "timing": "Reply within 6 hours (curious but not committed)"
    },
    
    "timing": {
        "label": "⏰ Bad Timing",
        "trigger": ["not now", "next quarter", "busy", "later", "next month", "revisit"],
        "response": """Totally understand — timing is everything.

I'll check back in [TIMEFRAME]. Quick ask: what would need to change for this to be a priority? (Budget approval, team bandwidth, specific pain point getting worse?)

This helps me time the follow-up right and come back with relevant value.

— Nova ✨""",
        "goal": "Qualify timeline, schedule follow-up",
        "timing": "Reply within 24 hours (maintain relationship)"
    },
    
    "not_interested": {
        "label": "❌ Not Interested",
        "trigger": ["not interested", "pass", "no thanks", "don't need", "goodbye"],
        "response": """No worries at all — thanks for the reply!

If automation pain points pop up later (they usually do as teams scale), feel free to reach out.

Quick favor: mind sharing what made this a no? (Wrong timing, wrong solution, wrong person?)

Helps me improve my outreach. 🙏

— Nova ✨""",
        "goal": "Learn + preserve relationship",
        "timing": "Reply within 24 hours (graceful exit)"
    },
    
    "referral": {
        "label": "🔗 Referral Request",
        "trigger": ["not me", "wrong person", "talk to", "contact", "someone else"],
        "response": """Ah, my mistake — thanks for the redirect!

Would you mind introducing me to [RIGHT PERSON] over email/Telegram? Happy to handle the context so you don't have to explain.

If not, no worries — I'll reach out cold and mention you suggested them. 🙏

— Nova ✨""",
        "goal": "Get intro or permission to name-drop",
        "timing": "Reply within 4 hours (they're helping you — be responsive)"
    },
    
    "meeting_request": {
        "label": "📅 Asks for Meeting",
        "trigger": ["call", "meeting", "zoom", "chat", "talk", "schedule"],
        "response": """Perfect. Here's my availability:

[OPTION 1]: [DATE] at [TIME] [TIMEZONE]
[OPTION 2]: [DATE] at [TIME] [TIMEZONE]  
[OPTION 3]: [DATE] at [TIME] [TIMEZONE]

Or send me your Calendly and I'll book directly.

Agenda (15-20 min):
• Your current workflow pain points
• Quick wins I can spot immediately
• Scope/timeline if it makes sense to proceed

Sound good?

— Nova ✨""",
        "goal": "Lock in time",
        "timing": "Reply within 2 hours (they initiated = high intent)"
    }
}

def show_all():
    """Display all response templates"""
    print("=" * 60)
    print("📝 RESPONSE TEMPLATES - Lead Reply Scenarios")
    print("=" * 60)
    print()
    
    for key, template in TEMPLATES.items():
        print(f"{template['label']}")
        print(f"Goal: {template['goal']}")
        print(f"Timing: {template['timing']}")
        print()
        print(template['response'])
        print()
        print("-" * 60)
        print()

def find_template(reply_text):
    """Find best template based on reply content"""
    reply_lower = reply_text.lower()
    
    matches = []
    for key, template in TEMPLATES.items():
        score = sum(1 for trigger in template['trigger'] if trigger in reply_lower)
        if score > 0:
            matches.append((key, score, template))
    
    if matches:
        matches.sort(key=lambda x: x[1], reverse=True)
        return matches[0][2]
    
    return TEMPLATES['info']  # Default

def suggest(reply_text):
    """Suggest template for given reply"""
    template = find_template(reply_text)
    
    print("=" * 60)
    print(f"📩 REPLY DETECTED: {template['label']}")
    print("=" * 60)
    print(f"Goal: {template['goal']}")
    print(f"Timing: {template['timing']}")
    print()
    print("✍️  SUGGESTED RESPONSE:")
    print("-" * 60)
    print(template['response'])
    print("-" * 60)
    print()
    print("💡 CUSTOMIZATION TIPS:")
    print("• Replace [BRACKETS] with specific details")
    print("• Add 1 sentence of personalization (reference their specific question)")
    print("• Keep it under 150 words if possible")

def stats():
    """Show template coverage stats"""
    print("=" * 60)
    print("📊 RESPONSE TEMPLATE STATS")
    print("=" * 60)
    print(f"Templates available: {len(TEMPLATES)}")
    print(f"Scenarios covered: Interested, Pricing, Info, Timing, No, Referral, Meeting")
    print()
    print("Average response length: ~75 words")
    print("Average reply time target: < 4 hours")
    print()
    print("Usage: python3 tools/response-templates.py suggest 'their reply here'")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 tools/response-templates.py [command]")
        print()
        print("Commands:")
        print("  all              - Show all templates")
        print("  suggest 'reply'  - Find best template for reply")
        print("  stats            - Show template stats")
        print()
        print("Examples:")
        print('  python3 tools/response-templates.py suggest "how much does this cost?"')
        print('  python3 tools/response-templates.py suggest "sounds interesting, tell me more"')
        sys.exit(0)
    
    command = sys.argv[1]
    
    if command == 'all':
        show_all()
    elif command == 'suggest':
        if len(sys.argv) < 3:
            print("Error: Provide the reply text to analyze")
            print('Example: python3 tools/response-templates.py suggest "interested, what are your rates?"')
            sys.exit(1)
        suggest(' '.join(sys.argv[2:]))
    elif command == 'stats':
        stats()
    else:
        print(f"Unknown command: {command}")
        print("Run without arguments for usage.")

if __name__ == "__main__":
    main()
