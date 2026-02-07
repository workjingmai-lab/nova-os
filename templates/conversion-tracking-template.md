# Conversion Tracking Template

Track every lead through the full funnel: Sent → Response → Call → Proposal → Won/Lost.

## How to Use

For each lead you send outreach to, create a tracking entry using this template. Update as the lead progresses through stages.

---

## Lead Tracking Entry

### Lead: [Company Name]
**ID:** [lead-id]
**Tier:** [EXPERT/TACTICAL/HIGH/MEDIUM]
**Value:** $[Amount]
**Contact:** [Name] - [email/telegram]

---

### Funnel Stages

#### ✅ Stage 1: SENT
- **Date:** [YYYY-MM-DD]
- **Message type:** [value-first outreach/follow-up]
- **Channel:** [email/telegram]
- **Notes:** [Any initial observations]

#### ⏳ Stage 2: RESPONSE (Waiting/Received)
**Status:** ⏳ Waiting / ✅ Received / ❌ No Response

*If Received:*
- **Date:** [YYYY-MM-DD]
- **Response type:** [Yes/Tell me more/No budget/Not interested/Ghost]
- **Response time:** [X hours/days after sending]
- **Notes:** [What did they say? Any objections?]

*If No Response:*
- **Follow-up 1 sent:** [YYYY-MM-DD]
- **Follow-up 2 sent:** [YYYY-MM-DD]
- **Final status:** [Nurtured/Archived]

#### ⏳ Stage 3: CALL BOOKED (Waiting/Completed)
**Status:** ⏳ Waiting / ✅ Completed / ❌ Declined

*If Waiting:*
- **Scheduled:** [YYYY-MM-DD at HH:MM]
- **Prep notes:** [Research topics, questions to ask]

*If Completed:*
- **Date:** [YYYY-MM-DD]
- **Duration:** [X minutes]
- **Attendees:** [Names]
- **Outcome:** [Positive/Neutral/Negative]
- **Next step:** [Proposal/Another call/Not interested]
- **Notes:** [Key takeaways from call]

#### ⏳ Stage 4: PROPOSAL SENT (Waiting/Sent)
**Status:** ⏳ Drafting / ✅ Sent / ❌ Not needed

*If Sent:*
- **Date:** [YYYY-MM-DD]
- **Proposal type:** [Quick automation/Setup/Multi-agent/Retainer/Audit]
- **Amount:** $[Amount]
- **Timeline:** [X days/weeks]
- **Scope:** [Brief description of what you'll deliver]
- **Response deadline:** [YYYY-MM-DD]

#### ⏳ Stage 5: NEGOTIATION (If applicable)
**Status:** ⏳ In negotiation / ✅ Agreed / ❌ Declined

- **Their concern:** [Price/timeline/scope/other]
- **Your response:** [How did you address it?]
- **Counter-offer:** [If any]
- **Final terms:** [Agreed price, timeline, scope]

#### ✅ Stage 6: WON/LOST
**Status:** ✅ WON / ❌ LOST

*If WON:*
- **Date:** [YYYY-MM-DD]
- **Final value:** $[Amount]
- **Payment terms:** [Upfront/Milestone/Monthly]
- **Start date:** [YYYY-MM-DD]
- **Time to close:** [X days from first send]
- **Lessons learned:** [What worked?]

*If LOST:*
- **Date:** [YYYY-MM-DD]
- **Reason:** [Budget/Not ready/Went with competitor/Timing/Other]
- **Lessons learned:** [What could you have done differently?]

---

## Conversion Metrics (Per Lead)

Track key metrics to identify patterns:

| Metric | Value |
|--------|-------|
| Time to first response | [X days] |
| Time to call booked | [X days from response] |
| Time to proposal sent | [X days from call] |
| Time to close | [X days from proposal] |
| Total sales cycle | [X days from first send] |
| Touchpoints before close | [X messages/calls] |

---

## Quick Status Reference

**Active Pipeline:**
- [ ] [Lead A] - Stage: [Response/Call/Proposal/Negotiation] - Days in stage: [X]
- [ ] [Lead B] - Stage: [Response/Call/Proposal/Negotiation] - Days in stage: [X]
- [ ] [Lead C] - Stage: [Response/Call/Proposal/Negotiation] - Days in stage: [X]

**Needs Follow-up:**
- [ ] [Lead A] - [X] days since last contact - Follow up: [Day 3/7/14]
- [ ] [Lead B] - [X] days since last contact - Follow up: [Day 3/7/14]

**Recent Wins:**
- [x] [Lead A] - Won on [YYYY-MM-DD] - $[Amount] - [X] days to close
- [x] [Lead B] - Won on [YYYY-MM-DD] - $[Amount] - [X] days to close

**Recent Losses:**
- [x] [Lead A] - Lost on [YYYY-MM-DD] - Reason: [Budget/Timing/Competitor]
- [x] [Lead B] - Lost on [YYYY-MM-DD] - Reason: [Budget/Timing/Competitor]

---

## Automation

Use `follow-up-reminder.py` to automate follow-up tracking:

```bash
# Schedule follow-ups for all active leads
python3 tools/follow-up-reminder.py schedule

# Check which leads need follow-up today
python3 tools/follow-up-reminder.py check

# Mark a lead as responded
python3 tools/follow-up-reminder.py respond [lead-id]
```

---

## Tips

1. **Update immediately:** Don't rely on memory. Update the tracking entry right after every interaction.
2. **Be specific:** Instead of "Good call," write "They mentioned needing automation for Discord moderation. Budget: $5-10K."
3. **Track time:** Days-in-stage metrics show where your funnel leaks.
4. **Review weekly:** Look for patterns in losses. Are most losses due to budget? Timing? Adjust outreach accordingly.
5. **Celebrate wins:** Document what worked. Did value-first outreach convert better? Use that for future leads.

---

## Why This Matters

**What gets measured gets managed.**

Without tracking:
- You don't know your true conversion rate
- You can't identify where leads drop off
- You can't optimize your process

With tracking:
- You know exactly which stages need improvement
- You can predict revenue based on pipeline stages
- You can scale what works and fix what doesn't

---

**Created:** Work block 2917 — 2026-02-06 23:24Z
**Related:** weekly-revenue-review-template.md, follow-up-timing-guide.md, conversion-math.md
