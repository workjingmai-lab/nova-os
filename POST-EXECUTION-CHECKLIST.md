# Post-Execution Checklist — What Happens After You Send

**Created:** 2026-02-06
**Work block:** 2856
**For:** Arthur (after running send-everything.sh)

---

## Immediate (Day 0 — After Sending)

### ✅ Verify Shipments
```bash
# Check what was sent
python3 tools/revenue-tracker.py summary

# Should show:
# - Services: 60 sent ($609.5K)
# - Grants: 4-5 sent ($125-130K)
# - Total sent: $734.5-739.5K
```

### ✅ Update Execution Gap
```bash
# Gap should drop from 99.3% to ~0%
python3 tools/execution-gap.py

# Should show:
# - Execution gap: < 1%
# - ROI achieved: $734.5K shipped in 15-20 min
```

### ✅ Log to Follow-up Tracker
```bash
# Export sent messages for follow-up tracking
python3 tools/service-batch-send.py --dry-run | grep "sent" | while read line; do
  # Parse and log to follow-up-tracker.py
  # (Automated by service-batch-send.py output)
done
```

### ✅ Document Milestone
```bash
# Update diary.md with execution timestamp
echo "## [EXECUTION COMPLETE — 2026-02-06 HH:MMZ]" >> diary.md
echo "Action: Arthur executed send-everything.sh full" >> diary.md
echo "Result: $734.5K shipped, 99.3% → 0% execution gap" >> diary.md
```

---

## Day 1-3: Response Monitoring

### ✅ Check Inboxes Daily
**Channels to monitor:**
- Email (primary outreach channel)
- Telegram (if configured)
- Discord servers (DAOs often discuss in Discord)
- Twitter/X DMs (if reached out there)

**Look for:**
- Replies with questions
- Meeting requests
- "Send more info" requests
- Referrals to other teams
- Polite "not interested" (log for analysis)

### ✅ Log All Responses
```bash
# For each response, log to follow-up-tracker.py
python3 tools/follow-up-tracker.py add \
  --target "Organization Name" \
  --channel "email" \
  --potential 25000 \
  --status "replied" \
  --notes "Asked for case study, send by Friday"
```

### ✅ Categorize Responses
**Hot leads (reply within 24h, interested):**
- Schedule call immediately
- Send requested info within 2h
- Add to high-priority follow-up queue

**Warm leads (reply, interested but timing):**
- Ask: "When would be good to reconnect?"
- Schedule follow-up for suggested date
- Add value between now and then (share relevant article, etc.)

**Cold leads (no response after 3 days):**
- Proceed to Day 3 follow-up template

---

## Day 3/7/14/21: Follow-Up Sequence

### Day 3 Follow-Up (if no response)
**Template:**
```
Subject: Re: [Original Subject]

Hi [Name],

Following up on my previous email about [value prop].

Any thoughts on [specific pain point we addressed]?

If now's not the right time, no worries — just let me know
when would be better to reconnect.

Best,
[Your name]
```

### Day 7 Follow-Up (value-add)
**Template:**
```
Subject: [New insight] Re: [Original Subject]

Hi [Name],

Saw this [article/news] about [their industry/competitor]
and thought of our conversation about [pain point].

[1-2 sentence insight]

Worth discussing?

Best,
[Your name]
```

### Day 14 Follow-Up (permission to close)
**Template:**
```
Subject: Re: [Original Subject]

Hi [Name],

I've reached out a few times about [topic] but haven't
heard back — I assume this isn't a priority right now.

Should I close your file, or is there someone else on your
team who'd be better to talk to?

No pressure either way.

Best,
[Your name]
```

### Day 21 Follow-Up (final check-in)
**Template:**
```
Subject: Last check-in: [Original Subject]

Hi [Name],

Final ping from me on this — if timing changes and
[value prop] becomes relevant, my door is always open.

Best of luck with [current project/initiative].

Best,
[Your name]
```

---

## Week 1: Weekly Review

### ✅ Conversion Metrics
```bash
# Check conversion rate
python3 tools/revenue-tracker.py summary

# Track:
# - Sent: 60-65 messages
# - Replies: X (response rate %)
# - Calls booked: Y
# - Deals closed: Z
# - Revenue: $ZZZ
```

### ✅ Response Rate Analysis
**Good response rate:** >15% (9+ replies from 60 messages)
**Acceptable:** 10-15% (6-9 replies)
**Needs adjustment:** <10% (<6 replies)

**If response rate <10%:**
1. Review message templates (value-first?)
2. Check targeting (right prospects?)
3. Test A/B variants (use A/B test generator)
4. Adjust subject lines, opening hooks

### ✅ Hot Lead Prioritization
```bash
# Get top leads by response level
python3 tools/lead-prioritizer.py top 10

# Focus 80% of energy on top 20% of responsive leads
```

---

## Week 2-4: Closing Phase

### ✅ Proposal Templates
**Have ready:**
- Quick Automation proposal ($1-2K)
- OpenClaw Setup proposal ($3-5K)
- Multi-Agent System proposal ($10-25K)
- Retainer proposal ($1-4K/month)

**Customize for each prospect:**
- Use their specific language
- Reference their exact pain points
- Include relevant case studies
- Add timeline + payment terms

### ✅ Meeting Flow
**Pre-meeting:**
- Research their current setup
- Prepare demo (if applicable)
- Have questions ready

**During meeting:**
- Listen 80%, talk 20%
- Focus on their pain, not your features
- Take notes (log to follow-up-tracker.py)

**Post-meeting:**
- Send summary email within 2h
- Include: discussed points, next steps, timeline
- Copy to follow-up-tracker.py

---

## Ongoing: Pipeline Management

### ✅ Daily (5 minutes)
```bash
# Check for new responses
python3 tools/follow-up-tracker.py due

# Check conversion status
python3 tools/revenue-tracker.py summary
```

### ✅ Weekly (30 minutes)
```bash
# Full pipeline review
python3 tools/revenue-tracker.py list

# Update statuses: ready → submitted → won/lost
python3 tools/revenue-tracker.py update <id> --status "won"

# Export follow-up checklist
python3 tools/follow-up-tracker.py export > follow-ups.md
```

### ✅ Monthly (1 hour)
- Review conversion rate by tier (EXPERT, TACTICAL, HIGH, MEDIUM)
- Analyze which message templates perform best
- Update templates based on learnings
- Adjust targeting strategy

---

## Key Metrics to Track

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Response rate | >15% | replies / sent × 100 |
| Call booking rate | >30% of replies | calls / replies × 100 |
| Close rate | >10% of calls | won / calls × 100 |
| Average deal size | $15-30K | total won / deals |
| Pipeline velocity | 4-8 weeks | first contact → close |

---

## Troubleshooting

**Low response rate (<10%):**
- Check subject lines (are they compelling?)
- Verify prospect relevance (right person?)
- Test A/B variants (different hooks)

**Good response rate, low bookings:**
- Review call-to-action (is it clear?)
- Check friction (asking too much too soon?)
- Test softer CTAs ("15-min chat" vs "demo")

**Good bookings, low closes:**
- Review proposal quality (customized enough?)
- Check pricing (aligned with value?)
- Improve discovery phase (understand true pain)

---

**Post-execution philosophy:** Sending is step 1. Following up is step 2-20. Most revenue comes from persistence, not the initial message.

---

*Work block 2856 — 2026-02-06 22:03Z*
