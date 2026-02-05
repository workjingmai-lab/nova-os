# Outreach Toolkit — Templates & Frameworks

**Purpose:** Value-first outreach that converts better than pitch-first messages.

**Key Insight:** Generic "hi" messages get ignored. Specific research + named pain + clear solution = "yes, that's me" moment.

---

## Quick Start

```bash
# Check which leads to prioritize
python3 tools/lead-prioritizer.py

# Check if follow-ups are due today
python3 tools/follow-up-reminder.py check

# Check pipeline status
python3 tools/revenue-tracker.py summary
```

---

## Files

### Core Framework
- **`outreach-value-template.md`** — PROOF Framework guide (Problem → Research → Offer → Outcome → Follow-up)
  - Template structure
  - Follow-up sequence (Day 0/3/7/14/21)
  - Conversion math
  - Common mistakes

### Message Templates
- **`messages/ethereum-foundation-agent-automation.md`** — Ethereum Foundation outreach ($40K)
- **`messages/fireblocks-security-automation.md`** — Fireblocks outreach ($35K)
- **`messages/uniswap-devx-automation.md`** — Uniswap outreach ($40K)
- **`messages/infura-devex-automation.md`** — Infura DevEx outreach ($30K) ✨ NEW
- **`messages/yearn-governance-automation.md`** — Yearn governance outreach ($25K) ✨ NEW
- **`messages/optimism-governance-value-first.md`** — Optimism governance outreach ($30K) ✨ NEW
- **`messages/balancer-grant-workflow.md`** — Balancer DAO outreach ($20K)
- **`messages/curve-governance-automation.md`** — Curve DAO outreach ($20K)
- **10+ DAO outreach messages** — Aave, Compound, Lido, MakerDAO, etc. ($212.5K)

**Total: 42 messages worth $417.5K (as of 2026-02-04)**

### Reference Documents
- **`BLOCKER-SUMMARY-FOR-ARTHUR.md`** — Execution plan (57 min → $552K)
- **`SERVICE-OUTREACH-QUICK-START.md`** — Zero-fluff execution guide ($332K ready NOW)
- **`TOP-3-FOLLOW-UP-SCHEDULE.md`** — Follow-up sequence for HIGH priority leads

---

## PROOF Framework

### P — Problem (Named Pain)
Identify specific pain point the target is experiencing.

### R — Research (Evidence)
Show you did homework (mention specific projects, metrics, news).

### O — Offer (Specific Solution)
Clear value proposition with deliverable, timeline, and pricing.

### O — Outcome (Measurable Results)
What success looks like (hours saved, $ saved, users served).

### F — Follow-Up (Next Steps)
Single, clear CTA with specific time commitment.

---

## Conversion Math

- **39 messages ready** → $332K services pipeline
- **Expected response rate:** 28% (11 responses)
- **Expected conversion:** 10-20% of responses = 1-2 contracts
- **Revenue potential:** $40K-$115K

**Key:** 1-3 wins from 39 messages justifies the effort.

---

## Follow-Up Sequence

### Day 0 — Initial Message
Send value-first message using PROOF framework.

### Day 3 — First Follow-Up
Reply to original thread with new value (insight, article, tip).

### Day 7 — Second Follow-Up
Check if they're still the right person.

### Day 14 — Third Follow-Up (Value-Add)
Share something useful (tool, article, insight) — no explicit ask.

### Day 21 — Final Follow-Up
Direct question: "Is this worth exploring, or should I close this thread?"

---

## Tools

### Lead Prioritizer
```bash
python3 tools/lead-prioritizer.py
```
Sort leads by priority/value. Focus on HIGH priority first.

### Follow-Up Reminder
```bash
python3 tools/follow-up-reminder.py check
```
Check which follow-ups are due today. Prevents forgotten opportunities.

### Revenue Tracker
```bash
python3 tools/revenue-tracker.py summary
```
Pipeline status: ready → submitted → won/lost. Single source of truth.

---

## Execution Checklist

- [ ] Research target (projects, pain points, recent news)
- [ ] Build message using PROOF framework
- [ ] Set follow-up reminders (Day 3/7/14/21)
- [ ] Send message (via DM, email, or contact form)
- [ ] Update revenue-tracker.py status (ready → submitted)
- [ ] Follow up on scheduled dates
- [ ] Track responses → calls → won/lost

---

## Common Mistakes

1. **No research** — Mass outreach = low response
2. **Generic pitch** — "I can help" = deleted
3. **No clear CTA** — "Let me know" = no action
4. **No follow-up** — One-and-done = lost deals
5. **Wrong target** — Reaching out to non-decision-makers = wasted effort

---

## Quick Reference

### Message Template
```
Subject: [Specific pain] + [Specific solution]

Hi [Name],

I noticed [PROBLEM — Named Pain].

[RESEARCH — 2-3 sentences showing homework]

I can help by [OFFER — Specific solution + timeline + pricing].

Based on similar work, this should [OUTCOME — Measurable result].

Open to a 15-min call to discuss?

[Your name]
P.S. I'll follow up in 3 days if I don't hear back.
```

### CTA Examples
- "Open to a 15-min call this week?"
- "Want me to send over a proposal?"
- "Should I build a quick prototype?"

---

**Created:** 2026-02-04 (Work block 1744)
**Purpose:** Comprehensive outreach toolkit for $332K service pipeline
**Files:** 13 message templates + framework + quick-start guides
