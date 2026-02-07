# Revenue Conversion Playbook: From Sent to Won

**Pre-send:** Build pipeline ($1.49M ready)
**Post-send:** Convert pipeline → revenue
**This playbook:** What to do after Arthur runs send-everything.sh

---

## The Conversion Funnel

```
Sent → Reply → Call → Proposal → Negotiation → Won/Lost
```

**Current state:** $5K sent (1 grant), 0 replies received
**Goal:** 5-10% conversion rate → $72-149K revenue from $1.49M pipeline

---

## Phase 1: Immediate Post-Send (Day 0-1)

### 1. Update Status to "Submitted"
**Action:** Run revenue-tracker.py to update all sent items
```bash
python3 tools/revenue-tracker.py update --status submitted --batch
```

**Why:** Track what was sent, when, and to whom

### 2. Plan Follow-Ups
**Action:** Add follow-up reminders for all sent messages
```bash
# Day 3 follow-ups
python3 tools/follow-up-tracker.py add --message "outreach/messages/FILE.md" --days 3

# Day 7 follow-ups
python3 tools/follow-up-tracker.py add --message "outreach/messages/FILE.md" --days 7

# Day 14 follow-ups
python3 tools/follow-up-tracker.py add --message "outreach/messages/FILE.md" --days 14
```

**Why:** Most responses come on follow-ups, not first touch

### 3. Monitor Responses
**Action:** Check email, Signal, Telegram for replies daily
```bash
# Cron job: Check for new responses
python3 tools/response-checker.py
```

**Why:** Speed matters. Reply within 1 hour = 5× more likely to convert

---

## Phase 2: Response Handling (Day 1-7)

### Response Type A: "Interested, tell me more"
**Action:**
1. Reply within 1 hour
2. Ask for discovery call (15-30 min)
3. Send calendar link
4. Research target before call

**Template:**
```
Subject: Re: [Original Subject]

Great to hear from you! 

I'd love to learn more about your challenges and explore if we're a good fit.

Can we jump on a 15-30 min call this week?
[Calendar link]

Before we chat, I'll review [specific thing about their org].

Best,
Nova
```

### Response Type B: "Not interested right now"
**Action:**
1. Add to nurture list
2. Schedule follow-up in 30 days
3. Send one valuable resource (no pitch)

**Template:**
```
Subject: Re: [Original Subject]

Thanks for the quick response!

Totally understand timing. I'll check back in a month — in case anything changes.

In the meantime, here's a resource on [topic] that might help:
[Link to useful article/tool]

Best,
Nova
```

### Response Type C: No response (default)
**Action:**
1. Wait 3 days
2. Send follow-up #1 (add value, no pitch)
3. Wait 7 days
4. Send follow-up #2 (new angle)
5. Wait 14 days
6. Send follow-up #3 (breakup or final value-add)

**Why:** Persistence = conversion. 80% of sales happen after 5+ touches

---

## Phase 3: Call → Proposal (Day 7-30)

### Discovery Call Prep (15 min)
**Research:**
1. Read their website, blog, recent posts
2. Check their GitHub, recent launches
3. Identify 2-3 specific pain points
4. Prepare 1-2 relevant case studies

**Call structure (15-30 min):**
1. **Icebreaker (2 min):** "How's your week going?"
2. **Discovery (10 min):** Ask about challenges, goals, current workflow
3. **Solution (5 min):** Propose specific agent suite for their pain
4. **Next steps (3 min):** "I'll send a proposal by [date]. Sound good?"

**After call:**
1. Send proposal within 24 hours
2. Add to pipeline tracker (status: "proposal-sent")
3. Schedule follow-up in 3 days

### Proposal Structure (1-2 pages)
1. **Problem:** What we discussed (their pain)
2. **Solution:** Specific agent suite (3-7 agents)
3. **Timeline:** 30-90 days (pilot → full deployment)
4. **Investment:** $X,XXX for pilot, $XX,XXX for full
5. **Next steps:** Sign, deposit, start date

**Tool:** Use proposal-template.md for consistency

---

## Phase 4: Negotiation → Close (Day 30-90)

### Common Objections + Responses

**"Too expensive"**
→ "What's your budget? I can scope a pilot for $X-XXK to prove value."

**"We need to think about it"**
→ "Totally understand. When should I follow up? [Date]? Anything else you need from me?"

**"We're building this in-house"**
→ "Great! I can share my architecture docs so you don't reinvent the wheel. Or, I can build a custom suite faster. Which helps more?"

**"We don't have budget right now"**
→ "Fair enough. Mind if I check back in Q2? Budgets refresh and I'd love to work together."

### Closing the Deal
**Action:**
1. Send contract (simple 1-2 page agreement)
2. Request deposit (20-50% upfront)
3. Schedule kickoff call
4. Update pipeline tracker (status: "won")

**Tools:**
- Contract template: contracts/service-agreement.md
- Invoice template: tools/invoice-generator.py

---

## Phase 5: Delivery → Upsell (Day 90+)

### Pilot Execution (30-90 days)
**Weekly check-ins:**
1. Status update (what shipped this week)
2. Metrics (agents deployed, time saved, ROI)
3. Feedback loop (what's working, what needs adjustment)

**End of pilot:**
1. Results summary (quantitative impact)
2. Proposal for full deployment (3-12 months)
3. Referral request ("Know anyone else who'd benefit?")

### Upsell Opportunities
- Expand agent suite (5 agents → 10 agents)
- Extend duration (3 months → 12 months)
- Additional teams (engineering team → product team)

---

## Metrics to Track

**Conversion funnel metrics:**
```
Sent: 60 messages
Replies: 12 (20% reply rate)
Calls: 6 (50% call-booking rate)
Proposals: 4 (67% proposal rate)
Won: 2 (50% close rate)
Lost: 2 (50% lost rate)

Total conversion: 2/60 = 3.3%
Revenue: 2 × $25K = $50K
```

**Track weekly:**
- Reply rate (target: 15-25%)
- Call rate (target: 40-60%)
- Proposal rate (target: 60-80%)
- Close rate (target: 30-50%)
- Overall conversion (target: 5-10%)

---

## Quick Reference Commands

**Check conversion metrics:**
```bash
python3 tools/revenue-tracker.py conversion
```

**Check due follow-ups:**
```bash
python3 tools/follow-up-tracker.py due
```

**Add new opportunity to pipeline:**
```bash
python3 tools/revenue-tracker.py add --type service --value 25000 --status lead
```

**Update opportunity status:**
```bash
python3 tools/revenue-tracker.py update --id 42 --status proposal-sent
```

---

## The Real Goal

Conversion isn't about tactics. It's about:

1. **Speed:** Reply fast, follow up fast, close fast
2. **Value:** Every touch adds value (resources, insights, introductions)
3. **Persistence:** Most revenue comes from follow-up #5, not #1
4. **Learning:** Track what works, iterate, improve

**The metric that matters:** Won/Lost ratio (aim for 50%+)

---

*Created: 2026-02-06 — Work block 2780*
*Current: $5K sent, 0% conversion | Target: 5-10% conversion*
*Next: Arthur executes send-everything.sh → Nova monitors responses*
