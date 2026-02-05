# Outreach Message Template — PROOF Framework

**Purpose:** Value-first outreach that converts better than pitch-first messages.

**Core Insight:** Generic "hi" or "buy my service" messages get ignored. Specific research + named pain + clear solution = "yes, that's me" moment.

---

## PROOF Framework

### P — Problem (Named Pain)
- Identify specific pain point the target is experiencing
- Use their language, not generic descriptions
- Show you understand their context

### R — Research (Evidence You Did Homework)
- Mention specific projects, metrics, or recent news
- Reference their tech stack, team, or public statements
- Show you're not mass-copy-pasting

### O — Offer (Specific Solution)
- Clear value proposition
- Specific deliverable (not "I can help" but "I will build X")
- Concrete timeline and pricing

### O — Outcome (Measurable Results)
- What success looks like
- Quantifiable impact (hours saved, $ saved, users served)
- Reference past results (your own or industry standards)

### F — Follow-Up (Next Steps)
- Single, clear CTA (not "let me know what you think")
- Specific time commitment (15-min call, DM reply)
- Mention you'll follow up in 3 days if no response

---

## Template Structure

```
Subject: Specific pain + specific solution

Hi [Name],

I noticed [PROBLEM — Named Pain].

[YOUR RESEARCH — 2-3 sentences showing you did homework]

I can help by [OFFER — Specific solution with timeline].

Based on similar work, this should [OUTCOME — Measurable result].

Open to a 15-min call to discuss?

[Your name]
P.S. I'll follow up in a few days if I don't hear back.
```

---

## Key Principles

### 1. Be Specific, Not Generic
❌ "I can help with automation"
✅ "I can build autonomous agents to handle your grant workflow, reducing 8 hours/week to 30 minutes"

### 2. Research Before Reaching Out
❌ "Hi, I saw your company and thought..."
✅ "I saw your V4 hooks documentation is still in progress — I can write complete docs in 2 weeks"

### 3. Offer Value, Not Just Services
❌ "I'm available for freelance work"
✅ "I'll deliver a working DevX agent package with 100% documentation, tested workflows, and 30-day support"

### 4. Make Response Easy
❌ "Let me know if you're interested"
✅ "Open to a 15-min call this week? I'll follow up on Thursday if I don't hear back."

---

## Timing & Follow-Up Sequence

### Day 0 — Initial Message
- Send value-first message using PROOF framework
- Include specific follow-up date (Day 3)

### Day 3 — First Follow-Up
- Reply to original thread (new message)
- Add value: new insight, relevant article, or quick tip
- Reiterate CTA briefly

### Day 7 — Second Follow-Up
- Check if they're still the right person
- Offer alternative: "If this isn't a priority right now, no worries — should I check back next quarter?"

### Day 14 — Third Follow-Up (Value-Add)
- Share something useful: tool, article, or insight relevant to them
- No explicit ask — just "thought you'd find this useful"

### Day 21 — Final Follow-Up
- Direct question: "Is this worth exploring, or should I close this thread?"
- Respects their time, creates urgency

---

## Conversion Math

Based on Week 2-3 data:
- **Outreach sent:** 39 messages (Services $332K)
- **Expected response rate:** 28% (11 responses)
- **Expected conversion:** 10-20% of responses = 1-2 contracts
- **Revenue potential:** $40K-$115K (based on HIGH priority leads)

**Key insight:** 1-3 wins from 39 messages = $40K-$115K revenue. Worth the effort.

---

## Common Mistakes to Avoid

1. **No research** — Mass outreach without context = low response
2. **Generic pitch** — "I can help" = instantly deleted
3. **No clear CTA** — "Let me know" = no action
4. **No follow-up** — One-and-done = lost deals
5. **Wrong target** — Reaching out to people who don't buy = wasted effort

---

## Tools Reference

- **Outreach messages:** `outreach/messages/*.md` — Ready-to-send templates
- **Lead prioritizer:** `tools/lead-prioritizer.py` — Sort by priority/value
- **Follow-up tracker:** `tools/follow-up-reminder.py` — Daily check
- **Revenue tracker:** `tools/revenue-tracker.py` — Pipeline status

---

## Quick Command Reference

```bash
# Check lead priority
python3 tools/lead-prioritizer.py

# Check follow-ups due today
python3 tools/follow-up-reminder.py check

# Check pipeline status
python3 tools/revenue-tracker.py summary

# Create new outreach message
cp outreach/messages/template.md outreach/messages/[target-name].md
```

---

**File:** `outreach/outreach-value-template.md`
**Created:** 2026-02-04 (Work block 1743)
**Purpose:** Reduce execution friction for 39 outreach messages ready to send
