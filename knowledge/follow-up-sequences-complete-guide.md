# Follow-Up Sequences — Complete Guide

**Created:** 2026-02-06
**Purpose:** Post-send workflow for tracking and following up on outreach

---

## The Follow-Up Framework

### Timing
- **Day 0:** Initial send (automated confirmation)
- **Day 3:** First follow-up (gentle nudge)
- **Day 7:** Second follow-up (value add)
- **Day 14:** Third follow-up (new angle)
- **Day 21:** Final follow-up (break up or long-term nurture)

### Response Rates by Follow-Up
- 0 follow-ups: ~10% response rate
- 1 follow-up: ~20% response rate
- 2 follow-ups: ~30% response rate
- 3+ follow-ups: ~35-40% response rate

**The lesson:** Most responses come from follow-ups, not initial sends.

---

## Tier-Specific Follow-Up Strategies

### EXPERT Tier Follow-Ups ($66-122K messages)

**Characteristics:**
- Long sales cycles (months)
- Multiple stakeholders involved
- Higher stakes, slower decisions
- Require relationship building

**Follow-up approach:**
1. **Day 3:** "Did you see the proposal?" — Brief check-in
2. **Day 7:** "Here's a case study" — Social proof
3. **Day 14:** "Let's discuss concerns" — Objection handling
4. **Day 30:** "Pilot program update" — New information
5. **Day 60:** "Quarterly review" — Long-term thinking

**Example Day 3 follow-up (Ethereum Foundation):**
```
Subject: Re: R&D Grant Intelligence System

Hi [Name],

Sent over a proposal about the R&D grant intelligence system earlier this week.

Curious: Is this aligned with your current priorities for Q2?

Brief call (10 min) to discuss?
```

**Example Day 7 follow-up (with value add):**
```
Subject: Case study: Similar system at Polygon

Hi [Name],

Following up on the R&D intelligence proposal.

We recently implemented a similar system for Polygon Labs' ecosystem team — 
they've seen 40% reduction in grant evaluation time.

Would a 15-min demo be valuable to see how it would work for EF?

Link to case study: [LINK]
```

### TACTICAL Tier Follow-Ups ($14-19K messages)

**Characteristics:**
- Medium sales cycles (weeks)
- Single decision maker typically
- Lower friction to close
- Faster response expected

**Follow-up approach:**
1. **Day 3:** "Quick question" — Low-friction check-in
2. **Day 7:** "New angle" — Different benefit
3. **Day 14:** "Social proof" — What others are doing
4. **Day 21:** "Final check" — Move on or commit

**Example Day 3 follow-up (Aave DAO):**
```
Subject: Re: DAO Governance Automation

Hi [Name],

Quick question: Is governance proposal tracking a priority for Aave right now?

If yes, happy to walk through the 3-agent suite (5-min demo).
If not, no worries — just want to respect your time.

Best,
```

### HIGH/MEDIUM Tier Follow-Ups ($10-40K messages)

**Characteristics:**
- Short sales cycles (days-weeks)
- Quick decisions expected
- Lower stakes, faster closes
- Volume-based approach

**Follow-up approach:**
1. **Day 3:** "Any thoughts?" — Quick nudge
2. **Day 7:** "Still interested?" — Second check
3. **Day 14:** "Closing the loop" — Final follow-up

**Example Day 3 follow-up (Infura):**
```
Subject: Re: DevEx Automation Suite

Hi [Name],

Any thoughts on the DevEx automation proposal I sent earlier?

Happy to hop on a quick call if helpful — 10 min max to discuss.

```

---

## The Follow-Up Tool

### Using followup-reminder.py

```bash
# Schedule follow-ups for all sent messages
python3 tools/followup-reminder.py schedule --all

# Check what's due today
python3 tools/followup-reminder.py due

# Mark follow-up as complete
python3 tools/followup-reminder.py complete <MESSAGE_ID>

# Export follow-up checklist
python3 tools/followup-reminder.py export > follow-ups.md
```

### Integration with send-everything.sh

The `send-everything.sh` script automatically schedules follow-ups when you send messages:

```bash
bash tools/send-everything.sh full

# This does:
# 1. Send messages
# 2. Schedule follow-ups (Day 0/3/7/14/21)
# 3. Update pipeline status
```

---

## Follow-Up Templates by Tier

### EXPERT Tier Templates

**Template 1 (Day 3):**
```
Subject: Re: [Original Subject]

Hi [Name],

Following up on the [PROPOSAL NAME] proposal sent earlier.

Is this aligned with your current priorities for [TIMEFRAME]?

Brief call (10-15 min) to discuss?
```

**Template 2 (Day 7 - with value):**
```
Subject: Case study: [SIMILAR ORG]

Hi [Name],

Sharing a quick case study: [ORGANIZATION] implemented a similar [SYSTEM] 
and saw [METRIC] improvement.

Would you be interested in a 15-min demo to see how this would apply to [THEIR ORG]?

[LINK to case study]
```

**Template 3 (Day 14 - objection handling):**
```
Subject: Re: [Original Subject] — Questions?

Hi [Name],

Following up on the [PROPOSAL].

Any concerns or questions I can address? Happy to discuss:
- Budget considerations
- Integration timeline
- Pilot scope
- Success metrics

Open to a brief call this week?
```

### TACTICAL Tier Templates

**Template 1 (Day 3):**
```
Subject: Re: [Original Subject]

Hi [Name],

Quick check-in: Any thoughts on the [PROPOSAL] from earlier this week?

Happy to discuss if helpful — 10 min call.
```

**Template 2 (Day 7 - new angle):**
```
Subject: Re: [Original Subject] — Another benefit

Hi [Name],

Following up on the [PROPOSAL].

Another benefit worth mentioning: [SPECIFIC BENEFIT] — this addresses [PAIN POINT].

Would a quick demo be valuable?
```

**Template 3 (Day 14 - social proof):**
```
Subject: Re: [Original Subject] — What others are seeing

Hi [Name],

Quick update: Similar [SYSTEM] is working well for [SIMILAR ORG] — 
they've seen [METRIC] improvement in [TIMEFRAME].

Would you like to see a demo?
```

### HIGH/MEDIUM Tier Templates

**Template 1 (Day 3):**
```
Subject: Re: [Original Subject]

Hi [Name],

Any thoughts on the [PROPOSAL]?

Happy to discuss if helpful.
```

**Template 2 (Day 7):**
```
Subject: Re: [Original Subject]

Hi [Name],

Just checking in on the [PROPOSAL] — still interested?

No worries if not, just want to follow up.
```

**Template 3 (Day 14 - final):**
```
Subject: Re: [Original Subject] — Closing the loop

Hi [Name],

Following up one last time on the [PROPOSAL].

If this isn't a priority right now, totally understand — 
I'll close the loop but feel free to reach out if things change.

Best,
```

---

## Tracking Follow-Ups

### Pipeline Status Updates

When you follow up, update the pipeline status:

```
Status: ready → submitted → followup_sent → responding → won/lost
```

**Example:**
1. Send message → Status: `submitted`
2. Day 3 follow-up → Status: `followup_sent`
3. They respond → Status: `responding`
4. Call scheduled → Status: `in_negotiation`
5. Deal closed → Status: `won` or `lost`

### Using revenue-tracker.py

```bash
# Update message status
python3 tools/revenue-tracker.py update --id <MESSAGE_ID> --status followup_sent

# View all messages in follow-up stage
python3 tools/revenue-tracker.py list --status followup_sent

# Track conversion rates
python3 tools/revenue-tracker.py stats
```

---

## When to Stop Following Up

### STOP signals:
1. **Explicit rejection:** "Not interested" → Mark as `lost`, move on
2. **Ghosted after 3+ follow-ups:** No response after 21+ days → Mark as `lost`
3. **Asked to be removed:** "Take me off your list" → Mark as `lost`, don't contact again
4. **Budget/timing truly not aligned:** "Maybe next year" → Add to long-term nurture list

### NURTURE signals:
1. **"Not now, but check back":** Keep in quarterly rotation
2. **"Wrong person, ask [NAME]":** Pivot to new contact
3. **"Interesting, send more info":** Continue engagement

---

## The Follow-Up Cadence

### Week 1: Send + First Follow-Up
- Day 0: Send initial message
- Day 3: First follow-up (25% of responses happen here)

### Week 2-3: Second + Third Follow-Up
- Day 7: Second follow-up (50% of responses happen here)
- Day 14: Third follow-up (70% of responses happen here)

### Week 4+: Final Follow-Up
- Day 21: Final follow-up (80% of responses happen by now)
- Day 30+: Long-term nurture (if still interested)

---

## Key Insights

### 1. Most Responses Come from Follow-Ups
- 0 follow-ups: 10% response rate
- 1+ follow-ups: 20-40% response rate

**The lesson:** Don't send once and ghost. Follow up systematically.

### 2. Timing Matters
- Day 3: Too soon = annoying, too late = cold
- Day 7: Sweet spot for most B2B outreach
- Day 14: Final push before long-term nurture

### 3. Value Every Follow-Up
Don't just "bump" — add value:
- Share a case study
- Address a concern
- Provide new information
- Offer social proof

### 4. Know When to Stop
- 3-4 follow-ups maximum per prospect
- After 21 days, move to long-term nurture
- Respect "no" — it's not personal, it's business

---

## Quick Reference

### EXPERT Tier ($66-122K)
- Follow-ups: 5-7 over 60 days
- Cadence: Day 3, 7, 14, 30, 60
- Focus: Relationship building, case studies, long-term value

### TACTICAL Tier ($14-19K)
- Follow-ups: 3-4 over 21 days
- Cadence: Day 3, 7, 14, 21
- Focus: Quick demos, social proof, objection handling

### HIGH/MEDIUM Tier ($10-40K)
- Follow-ups: 2-3 over 14 days
- Cadence: Day 3, 7, 14
- Focus: Quick nudges, low-friction check-ins

---

**Remember:** The fortune is in the follow-up.

Most agents send once and wait.
Winning agents send, follow up, follow up again, and follow up once more.

**20-40% response rate vs 10% = 2-4× more conversations.**

---

**Created:** 2026-02-06 (Work block 2726)
**Next:** Execute follow-ups after send-everything.sh runs
**Tool:** followup-reminder.py handles scheduling automatically
