# Response Handling Quick Reference
## What To Do When They Reply

> **You sent. They replied. Now what?**
> Speed = deals. Fast response = trust = revenue.

---

## 🚨 The Golden Rule

**Respond within 1 hour** (GREEN responses)
**Respond within 4 hours** (YELLOW responses)
**Respond within 24 hours** (BLUE responses)

Why? Speed shows you're serious. Fast replies = more deals.

---

## 🎯 4-Color Triage System

### 🟢 GREEN — Interested & Ready (Reply within 1 hour)
**What they say:** "This is interesting," "Let's talk," "Can you share more?"
**Your action:** Reply immediately → Ask for 15-min call → Book within 24h

**Template:**
```
Thanks [Name]! Great to hear from [company name].

I'd love to learn more about [specific pain mentioned]. 

Are you free tomorrow for a 15-min call? I can make [time slots] work.

Best,
Arthur
```

### 🟡 YELLOW — Warm & Curious (Reply within 4 hours)
**What they say:** "Tell me more," "What's your experience with X?", "Pricing?"
**Your action:** Answer questions → Move toward call → Book within 48h

**Template:**
```
Great question, [Name]!

[Specific answer to their question + proof point]

I think a quick call would be more efficient than email. 

Would [day/time] work for a 15-min chat?
```

### 🔵 BLUE — Considering (Reply within 24 hours)
**What they say:** "Not right now," "We're exploring options," "Maybe next quarter"
**Your action:** Add to nurture list → Follow up in 2 weeks → Keep warm

**Template:**
```
Thanks for the update, [Name].

Totally understand timing is everything. 

Mind if I check back in 2 weeks? If things change sooner, feel free to reach out.

Best,
Arthur
```

### 🔴 RED — Not Interested / Never Reply
**What they say:** "Not interested," "We have someone," [no response after 2 weeks]
**Your action:** Mark as lost → Move on → Don't waste time

---

## 📞 The Call Framework (15 minutes)

### Before the Call (5 minutes)
1. Research their company (website, recent news)
2. Identify 3 potential pain points
3. Prepare 3 discovery questions
4. Set pricing expectations in your head

### During the Call (15 minutes)
**Agenda:**
```
1. Warm-up (2 min)  → Build rapport, context
2. Discovery (7 min) → 3 questions, listen 80%
3. Proposal (5 min) → Clear solution + pricing + next steps
4. Close (1 min)    → "Shall I send a proposal?"
```

**Your 3 Discovery Questions:**
1. "What's the biggest challenge with [specific area] right now?"
2. "If you could fix one thing this month, what would it be?"
3. "What would success look like for you in 90 days?"

**Pro Tip:** Let them talk. The more they say, the more you learn.

### After the Call (Immediate)
1. Send proposal within 2 hours (use FIRST-24-HOURS.md template)
2. Add to response tracker: `python3 tools/response-tracker.py --add "company_name,call_booked,expecting_proposal"`
3. Follow up in 3 days if no reply

---

## 📧 Email Response Templates

### "Tell me more" Response
```
Hi [Name],

Great to hear from you!

[Specific detail about their company + relevant pain point]

Here's what I can help with:

1. [Pain point 1] → [Solution 1]
2. [Pain point 2] → [Solution 2]
3. [Pain point 3] → [Solution 3]

I've worked with [similar companies] to deliver [specific results].

Would you be open to a 15-min call to discuss?

Best,
Arthur
```

### "Pricing?" Response
```
Hi [Name],

Thanks for asking!

I offer 3 engagement models:

**Quick Automation** — $1-2K (3-5 days)
→ One specific task automated

**Full Setup** — $3-5K (1-2 weeks)
→ OpenClaw deployment + 3 automations

**Multi-Agent System** — $10-25K (2-4 weeks)
→ Custom agent architecture + full integration

Most companies start with Quick Automation, then expand.

Which model feels right for where you are now?

Best,
Arthur
```

### "Let's talk" Confirmation
```
Hi [Name],

Perfect! Here's my calendar link: [calendar link]

Or if easier, I can make these times work:
- [Day] at [time] (your timezone)
- [Day] at [time] (your timezone)

Looking forward to it!

Best,
Arthur
```

---

## 🎯 The Follow-Up Sequence

### Day 1 (After call)
```
Hi [Name],

Great chatting today!

As promised, here's the proposal: [link]

Key points:
- [Deliverable 1]
- [Deliverable 2]
- [Deliverable 3]

Timeline: [X] weeks | Investment: $[X]K

Any questions?

Best,
Arthur
```

### Day 3 (No reply)
```
Hi [Name],

Checking in on the proposal — any questions?

Happy to jump on another call if that would help.

Best,
Arthur
```

### Day 7 (Final follow-up)
```
Hi [Name],

Last check-in before I close this loop.

If the timing isn't right, no worries. 

I'll be here if things change.

Best,
Arthur
```

---

## 📊 Track Everything

### Add Response
```bash
python3 tools/response-tracker.py --add "company_name,responded,expecting_call"
```

### View All Responses
```bash
python3 tools/response-tracker.py
```

### View Response Stats
```bash
python3 tools/response-tracker.py --stats
```

### Status Types
- `no_response` — Haven't replied yet
- `responded` — Initial reply received
- `interested` — Showing interest
- `call_booked` — Call scheduled
- `proposal_sent` — Proposal sent
- `negotiating` — In discussion
- `won` — Deal closed (revenue!)
- `lost` — Not interested

---

## ⚡ Speed Tips

1. **Set up email filters** → Auto-flag responses
2. **Use templates** → Don't rewrite from scratch
3. **Batch replies** → Respond to all GREEN/YELLOW in one sitting
4. **Mobile response** → Reply on phone if needed (1-hour SLA)
5. **Track everything** → Never lose a lead

---

## 🎉 Expected Results

| Responses | Calls Booked | Proposals | Deals Closed | Revenue |
|-----------|--------------|-----------|--------------|---------|
| 5         | 2-3          | 2-3       | 0-1          | $0-15K  |
| 10        | 4-6          | 4-6       | 1-2          | $5K-30K |
| 15        | 6-9          | 6-9       | 2-4          | $10K-60K|
| 20        | 8-12         | 8-12      | 2-5          | $10K-90K|

**Most likely:** 10-15 responses → 4-6 calls → 2-3 deals → $10K-$45K

---

## 🚨 Common Mistakes

1. ❌ Waiting 24+ hours to reply → **They forget you**
2. ❌ Sending generic proposals → **They delete it**
3. ❌ Not asking for the call → **Email loops forever**
4. ❌ Following up too aggressively → **You become annoying**
5. ❌ Not tracking responses → **You lose deals**

---

## 💡 Key Mindset

**Speed + Specificity = Deals**

- Fast replies = you're serious
- Specific questions = you did your homework
- Clear calls-to-action = you're professional
- Tracking = you're organized

---

## 🎯 You're Ready

1. You sent messages ✓
2. They're replying ✓
3. You know how to respond ✓
4. You know how to close ✓

**Now execute.**

<small>Generated 2026-02-04 | Work Block 1287</small>
