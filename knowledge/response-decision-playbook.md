# Lead Response Decision Playbook
# Quick-reference for handling any lead response
# Created: Work block 3062, 2026-02-07

┌─────────────────────────────────────────────────────────────────────────┐
│                    INBOUND RESPONSE RECEIVED                            │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  STEP 1: CATEGORIZE (2 seconds)                                         │
│                                                                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌─────────────┐ │
│  │   POSITIVE   │  │    NEUTRAL   │  │   NEGATIVE   │  │   UNCLEAR   │ │
│  │  (interested)│  │   (question) │  │  (rejection) │  │  (vague)    │ │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  └──────┬──────┘ │
└─────────┼────────────────┼────────────────┼────────────────┼──────────┘
          │                │                │                │
          ▼                ▼                ▼                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  STEP 2: TEMPLATE (5 seconds)                                           │
│                                                                         │
│  POSITIVE → Template 5 (schedule call)                                  │
│  NEUTRAL  → Identify specific question → Template 4 or custom           │
│  NEGATIVE → Template 3 (intelligence gathering) or Template 8 (price)   │
│  UNCLEAR  → Ask clarifying question before proceeding                   │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  STEP 3: RECORD (3 seconds)                                             │
│                                                                         │
│  python3 tools/template-tracker.py record "Lead Name" <template_id>     │
│                                                                         │
│  Examples:                                                              │
│    record "Uniswap Labs" 5        # Positive response                   │
│    record "Balancer" 4            # Asked for info                      │
│    record "Curve" 3               # Not interested                      │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  STEP 4: SEND RESPONSE (varies)                                         │
│                                                                         │
│  Positive: Same-day response (within 2 hours optimal)                   │
│  Neutral: Same-day response                                             │
│  Negative: 24-hour window (don't seem desperate)                        │
│  Unclear: Clarify immediately                                           │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  STEP 5: UPDATE STATUS                                                  │
│                                                                         │
│  1. Update lead status in revenue-tracker.py:                           │
│     python3 tools/revenue-tracker.py update "Lead Name" contacted       │
│                                                                         │
│  2. If call scheduled, update pipeline stage:                           │
│     python3 tools/revenue-tracker.py update "Lead Name" negotiating     │
│                                                                         │
│  3. If deal closed, mark won and record value:                          │
│     python3 tools/revenue-tracker.py win "Lead Name" <amount>           │
└─────────────────────────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════════
                           RESPONSE PATTERNS
═══════════════════════════════════════════════════════════════════════════

POSITIVE SIGNALS                    → TEMPLATE 5
───────────────────────────────────────────────────────────────────────────
"This looks interesting"
"Can you tell me more?"
"I'd like to learn more"
"Let's schedule a call"
"When are you available?"

Action: Send scheduling options immediately

NEUTRAL/QUESTIONS                   → TEMPLATE 4 or CUSTOM
───────────────────────────────────────────────────────────────────────────
"What does this cost?"
"How long does it take?"
"Do you work with [specific tech]?"
"Can you handle [specific requirement]?"

Action: Answer specifically, then Template 4 (Send More Info)

NEGATIVE/REJECTIONS                 → TEMPLATE 3 or 8
───────────────────────────────────────────────────────────────────────────
"Not interested"                    → Template 3 (intelligence)
"No budget right now"               → Template 8 (alternatives)
"We're good with current setup"     → Template 3 (intelligence)
"Wrong time"                        → Template 2 (check back later)

Action: Don't argue. Gather intel or offer alternatives.

REFERRALS                           → TEMPLATE 7
───────────────────────────────────────────────────────────────────────────
"Forwarding to [name]"
"I'll pass this to [team]"
"Talk to [person]"

Action: Template 7 + follow up with new contact

DELAYS/SILENCE                      → TEMPLATES 1, 2, or 10
───────────────────────────────────────────────────────────────────────────
No response 3 days                  → Template 1
No response 7 days                  → Template 2
Response after weeks                → Template 10

Action: Maintain presence without being annoying

═══════════════════════════════════════════════════════════════════════════
                          TIMING GUIDELINES
═══════════════════════════════════════════════════════════════════════════

Inbound Response → Your Reply
───────────────────────────────────────────────────────────────────────────
Positive (interested): Within 2 hours (same business day max)
Neutral (question):    Within 4 hours
Negative (rejection):  Within 24 hours (measured response)
Unclear (vague):       Ask clarification within 2 hours

Follow-Up Cadence
───────────────────────────────────────────────────────────────────────────
Day 0:  Initial outreach
Day 3:  First follow-up (Template 1)
Day 7:  Second follow-up (Template 2)
Day 14: Final follow-up or archive

═══════════════════════════════════════════════════════════════════════════
                          RED FLAGS (Ignore These)
═══════════════════════════════════════════════════════════════════════════

❌ "Unsubscribe" — Honor immediately, no follow-up
❌ Hostile/abusive — Archive, no response
❌ Clear mismatch — "We don't use automation" (archive politely)
❌ Auto-reply vacation — Wait for return, don't count as response

═══════════════════════════════════════════════════════════════════════════
                          GREEN FLAGS (Prioritize)
═══════════════════════════════════════════════════════════════════════════

✅ Asks about pricing → High intent
✅ Suggests specific time → Very high intent
✅ Mentions specific problem → Qualify and close
✅ Forwards to decision-maker → Jackpot, follow up immediately

═══════════════════════════════════════════════════════════════════════════

## Usage

1. Print and keep visible during work sessions
2. When response arrives: Categorize → Template → Record → Send → Update
3. Total decision time: <10 seconds per response

## Integration

- Templates: `knowledge/follow-up-templates.md`
- Tracker: `tools/template-tracker.py`
- Pipeline: `tools/revenue-tracker.py`
- Leads: `data/outreach-leads.json`

---
*Created: Work block 3062*
*Purpose: Eliminate thinking time on every response*
