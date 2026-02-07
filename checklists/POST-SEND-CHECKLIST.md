# Post-Send Checklist

Actions to take immediately after sending outreach messages and daily follow-up routine.

## Immediate Actions (Within 1 Hour After Sending)

### ✅ Step 1: Update Pipeline Status

```bash
# Mark all sent leads as submitted
python3 tools/revenue-tracker.py submit all
```

This moves leads from "ready" to "submitted" status in your pipeline.

---

### ✅ Step 2: Schedule Follow-Up Reminders

```bash
# Schedule automatic follow-ups for all sent leads
python3 tools/follow-up-reminder.py schedule
```

This sets reminders for:
- Day 3: First follow-up
- Day 7: Second follow-up
- Day 14: Final follow-up (high-value only)
- Day 21+: Nurture queue

---

### ✅ Step 3: Document the Send

```bash
# Add to diary.md
echo "- [$	now.strftime('%Y-%m-%d %H:%MZ')] OUTREACH BATCH: Sent \$735K (42 messages: 10 EXPERT + 19 TACTICAL + 10 HIGH/MEDIUM + 5 grants)" >> diary.md
```

Or manually add to `diary.md`:
```markdown
### [WORK BLOCK XXXX — YYYY-MM-DD HH:MMZ]
**Task:** Outreach batch send
**Result:** Sent $735K in 42 messages
- EXPERT: 10 messages ($660-1,220K)
- TACTICAL: 19 messages ($268-357K)
- HIGH/MEDIUM: 10 messages ($305K)
- Grants: 5 applications ($125K)
- Total execution time: 40 minutes
**Next:** Monitor responses, follow up on Day 3/7/14
```

---

### ✅ Step 4: Verify Send Success

```bash
# Check pipeline status
python3 tools/daily-revenue-dashboard.py
```

Verify:
- Execution gap decreased from ~99% to ~0%
- Submitted amount increased to ~$735K
- No errors in send log

---

### ✅ Step 5: Prepare for Responses

Create response templates folder:
```bash
mkdir -p outreach/responses
```

Prepare these templates (use `response-handling-playbook.md` as guide):
- `yes-response.md` — For "Yes, I'm interested" responses
- `more-info-response.md` — For "Tell me more" responses
- `call-confirmation.md` — For confirming scheduled calls
- `proposal-send.md` — For sending proposals post-call
- `objection-handler.md` — For handling common objections

---

## Daily Routine (Days 1-21)

### Morning Checklist (5 minutes)

Run every morning:

```bash
# 1. Check for due follow-ups
python3 tools/follow-up-reminder.py check

# 2. Quick pipeline status
python3 tools/daily-revenue-dashboard.py --mini

# 3. Check conversion tracking
python3 tools/revenue-tracker.py status
```

---

### Response Handling (Same Day)

**🔥 Critical Rule: Respond within 1 hour**

When you receive a response:

1. **Categorize the response:**
   - Yes / Interested
   - Tell me more
   - No budget
   - Not interested
   - Already handled
   - Objection

2. **Use the appropriate template:**
   - See `response-handling-playbook.md` for templates
   - Customize with lead-specific details

3. **Track the interaction:**
   - Update `conversion-tracking-template.md` for that lead
   - Mark as responded in follow-up tracker

4. **Set next step:**
   - If interested → Propose call
   - If call scheduled → Send calendar link
   - If objection → Handle objection
   - If not interested → Move to nurture or archive

---

### Weekly Review (Every Friday)

```bash
# 1. Full pipeline review
python3 tools/daily-revenue-dashboard.py

# 2. Conversion metrics
python3 tools/revenue-tracker.py conversion

# 3. Weekly revenue review
cp templates/weekly-revenue-review-template.md memory/reviews/weekly-review-$(date +%Y-%m-%d).md
# Fill in the review template

# 4. Update diary with wins/losses/learnings
```

Track:
- Messages sent
- Response rate
- Calls booked
- Proposals sent
- Deals closed
- Blockers removed
- Key learnings

---

## Follow-Up Timeline

### Day 1-2: Monitor Responses
- Check for incoming responses
- Respond within 1 hour
- Update tracking

### Day 3: First Follow-Up
For all non-responders:
```bash
python3 tools/follow-up-reminder.py follow-up day3
```

Template approach:
- "Hi [Name], bumping this to the top of your inbox"
- Keep it brief, no new value needed yet
- 10-20% additional response rate

### Day 7: Second Follow-Up
For still non-responders:
```bash
python3 tools/follow-up-reminder.py follow-up day7
```

Template approach:
- "Hi [Name], any thoughts on my previous message?"
- Add new value: recent work, case study, relevant insight
- 5-10% additional response rate

### Day 14: Final Follow-Up (High-Value Only)
For HIGH priority leads only:
```bash
python3 tools/follow-up-reminder.py follow-up day14 --tier HIGH
```

Template approach:
- "Hi [Name], final check-in before I close this loop"
- Offer alternative: "Would a different contact be better?"
- 2-5% additional response rate

### Day 21+: Nurture Queue
For non-responsive leads that might be relevant later:
```bash
python3 tools/follow-up-reminder.py nurture [lead-id]
```

Re-contact in 1-3 months with:
- New work/case study
- Relevant industry update
- "Saw this and thought of you"

---

## Tracking Progress

### Daily Metrics
Track in `diary.md`:
- Responses received
- Responses sent
- Calls scheduled
- Proposals sent

### Weekly Metrics
Track in weekly review:
- Response rate (responses / sent)
- Call booking rate (calls / responses)
- Proposal rate (proposals / calls)
- Close rate (deals / proposals)
- Average deal size
- Sales cycle length

### Milestone Celebrations
Celebrate in `diary.md`:
- First response! 🎉
- First call booked! 📞
- First proposal sent! 📄
- First deal closed! 💰
- $10K milestone! 💵
- $50K milestone! 🚀
- $100K milestone! 🏆

---

## Conversion Stages Tracking

Use `conversion-tracking-template.md` to track each lead:

```
Sent → Response → Call → Proposal → Won/Lost
  ↓        ↓        ↓         ↓         ↓
Stage 1  Stage 2  Stage 3  Stage 4  Stage 6
```

Update the template for each lead as they progress through stages.

---

## Quick Reference Commands

```bash
# Check for follow-ups due today
python3 tools/follow-up-reminder.py check

# Send day 3 follow-ups
python3 tools/follow-up-reminder.py follow-up day3

# Mark a lead as responded
python3 tools/follow-up-reminder.py respond [lead-id]

# View full dashboard
python3 tools/daily-revenue-dashboard.py

# Check conversion metrics
python3 tools/revenue-tracker.py conversion

# Schedule a call reminder
python3 tools/follow-up-reminder.py remind [lead-id] [YYYY-MM-DD]
```

---

## Common Scenarios

### Scenario: "Yes, I'm interested"
1. Respond within 1 hour
2. Ask for discovery call: "Can we chat for 20 min to discuss your needs?"
3. Send calendar link
4. Add to tracking: Stage 3 (Call Booked)
5. Prep for call: Research, questions, pricing

### Scenario: "Tell me more"
1. Respond within 1 hour
2. Send focused value prop: "Here's what I can do for [specific pain]"
3. Include 1-2 relevant case studies
4. Ask: "Does this address your [pain]?"
5. Add to tracking: Stage 2 (Nurturing)

### Scenario: "No budget"
1. Respond within 1 hour
2. Validate: "I understand. Budget is real."
3. Pivot: "What if we started small? I can do [smaller scope] for $[lower amount]."
4. Or nurture: "Let's reconnect in [timeline] when budget opens up."
5. Add to tracking: Stage 2 (Nurturing) or Archive

### Scenario: "Not interested"
1. Respond within 1 hour (gracefully)
2. Accept: "Understood. Thanks for considering."
3. Nurture: "Mind if I reach out in [3 months] with updates?"
4. Add to tracking: Archive
5. Remove from follow-up queue

### Scenario: Ghost (no response after 3 follow-ups)
1. Stop active outreach
2. Move to nurture queue
3. Re-contact in 1-3 months with new value
4. Add to tracking: Nurture

---

## Response Speed Benchmarks

| Response Time | Win Rate |
|---------------|----------|
| < 1 hour | 80% |
| 1-4 hours | 60% |
| 4-24 hours | 40% |
| 24-48 hours | 20% |
| > 48 hours | <10% |

**Rule:** Respond within 1 hour. Speed = Revenue.

---

## Templates Folder Structure

```
outreach/
├── responses/
│   ├── yes-response.md
│   ├── more-info-response.md
│   ├── no-budget-response.md
│   ├── not-interested-response.md
│   ├── call-confirmation.md
│   ├── proposal-send.md
│   └── objection-handler.md
├── follow-ups/
│   ├── day3-follow-up.md
│   ├── day7-follow-up.md
│   └── day14-follow-up.md
└── tracking/
    └── conversion-tracking-[lead-id].md
```

---

## Why This Matters

**The fortune is in the follow-up.**

- 48% of salespeople never follow up with a prospect
- 80% of sales are made on the 5th-12th contact
- Most agents quit after 1 message

Your edge: Persistence + Speed + Tracking

---

**Created:** Work block 2920 — 2026-02-06 23:28Z
**Purpose:** Ensure consistent follow-up and conversion tracking
**Next:** Arthur uses this checklist daily after sending messages
