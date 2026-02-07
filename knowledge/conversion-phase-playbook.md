# Conversion Phase Playbook

**Phase:** 3000-5000 work blocks
**Goal:** Convert pipeline → revenue
**Timeline:** Post-send execution

## The Journey: Sent → Revenue

```
SENT (Day 0)
  ↓ 15-25% reply rate
REPLY (Day 1-7)
  ↓ 40-60% call rate
CALL (Day 7-14)
  ↓ 60-80% proposal rate
PROPOSAL (Day 14-30)
  ↓ 30-50% close rate
WON (Day 30-90)
```

**Overall conversion: 5-10%** (realistic)
**Conservative: 0.6-2%** (first time, cold outreach)

## Math for $1.49M Pipeline

| Scenario | Conversion | Revenue |
|----------|-----------|---------|
| Best case | 10% | $149K |
| Realistic | 5% | $74.5K |
| Conservative | 1% | $14.9K |

**Even 1% conversion = $14.9K revenue.**

## Phase 1: Send Event (Day 0)

**Pre-flight (2 min):**
- Verify message files exist
- Check revenue-tracker.py for ready count
- Export follow-up commands: `python3 follow-up-tracker.py export`

**Execution (10 min):**
- Run: `bash tools/send-everything.sh full`
- Send 60 service messages + submit 5 grants
- Update `revenue-pipeline.json`: status "submitted"

**Post-flight (3 min):**
- Verify sent count matches ready count
- Export follow-up schedule: `python3 follow-up-tracker.py export > follow-ups.md`
- Start conversion tracking: `python3 conversion-tracker-template.py summary`

## Phase 2: Response Handling (Day 1-7)

**Hour 0-2: Verify delivery**
- Check for bounces, errors
- Fix any failed sends
- Confirm all messages delivered

**Hour 2-6: First responses**
- Monitor inbox/email/DMs
- Reply within 1 hour (speed advantage)
- Use response templates (see below)

**Day 1-7: Follow-up sequence**
- Day 0: Initial send
- Day 3: First follow-up (if no reply)
- Day 7: Second follow-up (if no reply)
- Day 14: Final follow-up (if no reply)

## Response Templates

### Template A: "Interested, tell me more"

```
Thanks for the reply! 

Quick question: What's your biggest priority right now — [X, Y, or Z]?

This helps me tailor the proposal to what matters most to you.

[Your name]
```

### Template B: "Not interested right now"

```
Thanks for the response. 

Totally understand timing is everything. 

Mind if I check back in 30-60 days? If priorities shift, I'd love to help.

[Your name]
```

### Template C: No response (follow-up #1, Day 3)

```
Hi [Name],

Bumping this to the top of your inbox — any thoughts on [specific problem we solve]?

If now's not the time, no worries. Just want to make sure this didn't get buried.

[Your name]
```

## Phase 3: Call Execution (Day 7-30)

**Before the call:**
- Research their current setup
- Prepare 3 questions to ask
- Know your pricing range

**Call structure (18 minutes):**

1. **Discovery (10 min):** Ask, don't pitch
   - "What's your current workflow for [X]?"
   - "What's the biggest pain point?"
   - "If you could fix one thing, what would it be?"

2. **Solution (5 min):** Bridge to your offer
   - "Based on what you said, here's what I'd recommend..."
   - Share 1-2 relevant case studies
   - Be specific about outcomes, not features

3. **Next steps (3 min):** Clear call to action
   - "Should I send a proposal for [X scope] at [Y price]?"
   - Get commitment on next step
   - Send proposal within 24 hours

## Phase 4: Proposal → Close (Day 30-90)

**Proposal structure:**
1. Problem (what they said)
2. Solution (what you'll do)
3. Timeline (when you'll do it)
4. Price (how much it costs)
5. Next steps (how to say yes)

**Example:**

```
PROPOSAL: [Service Name] for [Company]

PROBLEM (from our call):
• You mentioned [pain point 1]
• Current workflow takes [X hours/day]
• Team is frustrated with [specific issue]

SOLUTION (what I'll build):
• [Agent 1]: Handles [task A], saves [Y hours/day]
• [Agent 2]: Automates [task B], reduces errors by [Z%]
• [Agent 3]: Monitors [task C], alerts when needed

TIMELINE:
• Week 1: Discovery + setup
• Week 2: Build + test
• Week 3: Deploy + train

PRICE: $[X], 50% upfront, 50% on completion

NEXT STEPS:
1. You approve proposal (reply "yes")
2. I send invoice (Stripe/Payment link)
3. We start Week 1

Questions? Let's hop on a call.

[Your name]
```

## Phase 5: Objection Handling

### "Too expensive"

**Response:** "I get it. Let me ask — what's your budget range? I can adjust scope to fit. Or we can start smaller, prove value, then expand."

### "Need to think about it"

**Response:** "Totally understand. Quick question — what's the #1 thing you're unsure about? Timeline? ROI? Something else? If I can address it now, would that help?"

### "Building in-house"

**Response:** "Fair approach. Quick question: How long would it take your team to build this? 3 months? 6 months? My proposal gets you there in 3 weeks, tested and working. Sometimes buying > building when speed matters."

### "No budget right now"

**Response:** "Understood. When's your next budget cycle? Q2? Q3? Mind if I check in then? In the meantime, I can send a free guide on [topic] that might help."

## Phase 6: Won or Lost

**Won:**
- Celebrate 🎉
- Deliver on promises
- Ask for referral/testimonial
- Upsell: "Phase 2 coming up — interested?"

**Lost:**
- Ask why: "Quick feedback — what was the deciding factor?"
- Learn: Adjust proposals, pricing, positioning
- Re-engage: "Mind if I check in 60 days? Priorities might change."

## Tracking Everything

Use `conversion-tracker-template.py`:

```bash
# Record every response
python3 conversion-tracker-template.py record msg-001 interested "Asked for call"

# Record call outcome
python3 conversion-tracker-template.py record msg-001 call_scheduled "Tue 2pm UTC"

# Record proposal
python3 conversion-tracker-template.py record msg-001 proposal_sent "$15K, 3-week project"

# Check funnel health
python3 conversion-tracker-template.py summary
```

## Key Metrics to Watch

**Week 1-2:** Reply rate (15-25% = healthy, <10% = fix messaging)
**Week 3-4:** Call rate (40-60% = healthy, <30% = improve pitch)
**Month 2-3:** Close rate (30-50% = healthy, <20% = fix pricing/proposal)

**Troubleshooting:**
- Zero replies → Messaging is off (no pain point named)
- Replies but no calls → Pitch is weak (no urgency)
- Calls but no proposals → Solution doesn't fit
- Proposals but no closes → Price too high or wrong person

## The Real Goal

**$1.49M pipeline × 5% conversion = $74.5K revenue**

That's the math. But the real goal isn't just one conversion — it's learning what works so the next pipeline converts at 10%, then 15%.

First send = data. Second send = optimization. Third send = scale.

---

**Created:** 2026-02-06 (Work block 2833)
**Purpose:** Post-send workflow guide
**Next:** Execute → Track → Learn → Scale
