# Response Handling Playbook — Post-Execution Workflow

**Purpose:** Handle incoming responses from $1.9M pipeline outreach systematically.

**Current Status:**
- Pipeline: $1.9M+ ready to send
- Execution gap: 99.3% (not yet sent)
- When sent: Expect 10-30% response rate = $190-570K in conversations

---

## Phase 1: Immediate Response (Within 1 hour)

### Category A: "Yes, I'm Interested" 🎯
**Action:** Schedule discovery call immediately
**Template:**
```
Subject: Re: [Their Name] — [Context]

Hi [Name],

Great to hear you're interested! 

To make the most of our conversation, I'd like to schedule a 30-min discovery call. We'll cover:
- Your current pain points with [specific problem]
- What a solution looks like for [their org]
- Timeline and next steps

When works best for you? I'm available [2-3 time slots].

Best,
Nova (for Arthur)
```

**Next Steps:**
1. Add to revenue-tracker.py: status="call_scheduled"
2. Calendar invite sent
3. Call prep sheet created (research their stack, recent news, specific problems)

### Category B: "Tell Me More" / "Send Details" 📄
**Action:** Send targeted case study + proposal outline
**Template:**
```
Subject: Re: [Their Name] — [Context]

Hi [Name],

Here's what I'm proposing for [their org]:

**The Problem:**
[Specific pain I identified in my research]

**The Solution:**
[3-agent suite I proposed] → [Specific outcome]

**Proof:**
- [Case study or similar work]
- [Quantitative result if available]

**Investment:**
[Range from original message]

**Timeline:**
[30-60-90 day delivery]

Shall we schedule a call to dive deeper?

Best,
Nova (for Arthur)
```

**Next Steps:**
1. revenue-tracker.py: status="details_sent"
2. Follow-up in 3 days if no response

### Category C: "Not Right Now" / "Wrong Person" 🔄
**Action:** Add to long-term nurture sequence
**Response:**
```
Thanks for the response, [Name].

I understand timing isn't right. Would you mind if I:
1. Follow up in [3-6 months] when circumstances might change?
2. Connect with the right person on your team if this is better suited for [role]?

No pressure either way. Just want to make sure I'm helpful, not annoying.

Best,
Nova (for Arthur)
```

**Next Steps:**
1. revenue-tracker.py: status="nurture", followup_date=[3-6 months out]
2. Add to follow-up-tracker.py queue

---

## Phase 2: Discovery Call (Before Call)

### Pre-Call Checklist
- [ ] Research their current stack/tools
- [ ] Review original outreach message
- [ ] Identify 2-3 specific problems to solve
- [ ] Prepare case studies for similar work
- [ ] Set clear call objectives

### Call Structure (30 minutes)
**0-5 min:** Build rapport, confirm pain points
**5-15 min:** Deep dive on problems, current solutions, what's missing
**15-25 min:** Proposed solution, timeline, investment
**25-30 min:** Next steps, timeline, agreement

### Post-Call (Within 24 hours)
Send recap email:
```
Subject: Recap: Our conversation — [Date]

Hi [Name],

Great chatting earlier! Here's what I heard:

**Your Challenges:**
- [Problem 1]
- [Problem 2]

**My Proposed Solution:**
- [Solution summary]
- [Timeline: X weeks]

**Investment:** [Range from discussion]

**Next Steps:**
1. [Their action item]
2. [My action item]
3. [Timeline for next step]

Sound right?

Best,
Nova (for Arthur)
```

---

## Phase 3: Proposal & Negotiation

### When to Send Proposal
- After discovery call
- When they've confirmed budget + timeline
- Never before (wastes time on unqualified leads)

### Proposal Structure
1. **Executive Summary** — One-page overview
2. **Problem Statement** — What they told me (their words)
3. **Proposed Solution** — Agent suite + deliverables
4. **Timeline** — Week-by-week breakdown
5. **Investment** — Fixed fee or retainer structure
6. **Terms** — Payment schedule, scope, revisions

### Red Flags 🚩
- "Can you do this for free?" → Politely decline
- "We'll pay you on success/rev share" → Not worth the risk
- "Send us a full proposal first" → Already done discovery, no need for more unpaid work
- "We need to think about it" → Set follow-up in 7 days, then move on

---

## Phase 4: Closing & Onboarding

### The Close
When they say "yes":
```
Hi [Name],

Excited to work with [org name]!

To get started:
1. I'll send over a simple agreement + invoice for [deposit%]
2. Once signed, we'll schedule a kickoff call
3. Week 1: [First deliverable]

Target start date: [Date]

Best,
Nova (for Arthur)
```

### Onboarding Checklist
- [ ] Agreement signed
- [ ] Deposit received (50% upfront standard)
- [ ] Kickoff call scheduled
- [ ] Shared workspace created (Notion/GitHub/Slack)
- [ ] Access granted (API keys, repos, documentation)
- [ ] Success metrics defined

---

## Phase 5: Delivery & Retention

### Weekly Updates (Every Friday)
```
Subject: Weekly Update — [Project Name] — Week [N]

**Completed This Week:**
- [Deliverable 1]
- [Deliverable 2]

**In Progress:**
- [Deliverable 3]

**Blockers:**
- [Any issues + how I'm solving them]

**Next Week:**
- [Planned deliverables]

Questions? Just ask.

Best,
Nova (for Arthur)
```

### Upsell Opportunities
Look for natural expansion points:
- "This agent suite is working great for X. Have you thought about Y?"
- End of project: "What's next? Here's what I see as opportunities."

---

## Follow-Up Sequences

### Lead Sequence (Sent → No Response)
**Day 0:** Send message
**Day 3:** "Any thoughts on my previous email?"
**Day 7:** "Bumping this — is this still a priority?"
**Day 14:** Final check-in, then archive

### Proposal Sent Sequence
**Day 0:** Send proposal
**Day 3:** "Any questions on the proposal?"
**Day 7:** "Shall we discuss?"
**Day 14:** "Last call — moving on to other projects if no interest"

### Call Scheduled Sequence
**Day -1:** Confirmation + agenda
**Day 0:** Call + recap email (within 24h)
**Day 3:** If no decision, "Any updates?"
**Day 7:** "Still interested or should I close this file?"

---

## Tool Integration

**revenue-tracker.py usage:**
```bash
# Add new response
python3 tools/revenue-tracker.py add \
  --org "Ethereum Foundation" \
  --status "call_scheduled" \
  --value 75000 \
  --stage "discovery" \
  --notes "Interested in governance suite, call Feb 10"

# Update status
python3 tools/revenue-tracker.py update \
  --org "Ethereum Foundation" \
  --status "proposal_sent"

# Follow-up check
python3 tools/follow-up-tracker.py due
```

---

## Response Rate Math

**Assumptions:**
- 50 messages sent ($1.9M pipeline)
- 15% response rate = 7-8 conversations
- 30% conversion of responses = 2-3 deals
- Avg deal size: $40-75K

**Expected Outcome:**
- 2-3 closed deals = $80-225K revenue
- From 50 messages = $1.6-4.5K revenue per message sent

**Key Insight:** Response rate × conversion rate = revenue. Even modest rates (15% × 30% = 4.5%) generate meaningful revenue from large pipeline.

---

*Created: 2026-02-06 15:07Z — Work block 2745*
*Part of: Post-Execution Response Systems*
