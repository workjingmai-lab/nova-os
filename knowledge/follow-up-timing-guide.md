# Follow-Up Timing: When to Reach Out

*Created: 2026-02-06 23:16Z — Work block 2909*

## The Golden Rule

**Follow up too soon = Annoying**
**Follow up too late = Forgotten**

**Sweet spot:** 3-7 days between touches

---

## Timeline: From First Message to Deal

### Day 0: Initial Outreach
```
Send first message
↓
Wait for response
```

**What to do:**
- Send researched, value-first message
- Note: sent in revenue-tracker.py
- Set reminder: follow-up in 7 days if no response

---

### Day 1-3: Response Window (Most Replies Happen Here)

**If they reply:**
- Respond within 1 hour (80% win rate)
- Ask qualifying questions
- Propose call
- Set next steps

**If they don't reply:**
- Do nothing yet
- Wait for Day 7 follow-up

---

### Day 7: First Follow-Up (No Response)

**Template:**
```
Subject: Re: [Original subject]

Hi [Name],

Following up on my previous email—any thoughts?

If this isn't a priority right now, no worries. Just wanted to
bump this to the top of your inbox in case it got buried.

Let me know,
[Your name]
```

**Response rate on first follow-up:** 10-20% of original list

**Automation:**
```bash
python3 tools/follow-up-reminder.py due
```

---

### Day 14: Second Follow-Up (Still No Response)

**Template:**
```
Subject: Re: [Original subject]

Hi [Name],

Checking in one more time.

I know you're busy, so I'll keep this brief:
[One sentence value prop]

If you're still not interested, no hard feelings—I'll stop
bugging you. Just wanted to make sure this didn't get lost.

Best,
[Your name]
```

**Response rate on second follow-up:** 5-10% of original list

**Decision point:** After this, archive or add to long-term nurture

---

### Day 30: Long-Term Nurture (3 Months Later)

**Template:**
```
Subject: Quick update: [New value/offering]

Hi [Name],

Hope you're doing well!

I wanted to share a quick update:
[New case study, new service, new insight]

Thought of you since we last spoke about [topic].

If timing's better now, I'd love to revisit our conversation.
If not, no worries—just wanted to stay in touch.

Best,
[Your name]
```

**Use for:** High-value leads that said "not now" or "timing is bad"

---

## Post-Call Follow-Up Timeline

### During Call: Agree on Next Steps

**Always set clear expectations:**
- "I'll send a proposal by Friday"
- "You'll discuss with your team next week"
- "We'll reconvene in 2 weeks"

### Within 1 Hour: Send Call Summary

**Template:**
```
Subject: Re: Call summary — [Date]

Hi [Name],

Great chatting with you!

**Summary:**
- [Key point 1]
- [Key point 2]
- [Key point 3]

**Next steps:**
- I'll send [proposal/quote] by [date]
- You'll [discuss with team / review] by [date]
- We'll [reconnect / move forward] by [date]

I'll follow up on [date] if I don't hear from you earlier.

Best,
[Your name]
```

**Why speed matters:** Shows you're organized, reliable, and care

---

### Day 3-4: Check in (If No Response to Proposal)

**Template:**
```
Subject: Re: Proposal sent [Date]

Hi [Name],

Just checking in—did you have a chance to review the proposal?

Any questions or concerns? Happy to hop on a quick call
to discuss.

Let me know,
[Your name]
```

**Response rate:** 30-40% (they're interested, just busy)

---

### Day 7: Final Nudge Before "Not Interested"

**Template:**
```
Subject: Re: Proposal sent [Date]

Hi [Name],

Following up one more time on the proposal.

Is this still a priority for you? If timing has changed or
priorities shifted, just let me know—I'd rather know now
than keep following up.

If you're still interested, great—let's move forward.
If not, no hard feelings.

Best,
[Your name]
```

**Purpose:** Get a clear yes or no

---

### Day 14: Archive or Long-Term Nurture

**If they said "let me think" and disappeared:**
- Send to nurture list
- Re-engage in 3-6 months with new value/offering

**If they said "not interested":**
- Archive (don't follow up further)
- Ask for referral: "Anyone else you'd recommend?"

---

## Special Cases

### Case 1: "I Need to Ask My Team/Boss"

**Day 3:**
```
Hi [Name],

Any update from your team/boss?

Let me know if you need any additional info to help make the case.
```

**Day 7:**
```
Hi [Name],

Checking in—any decision yet?

If timing is challenging on your end, just let me know.
No pressure, just want to know where things stand.
```

**Day 14:**
```
Hi [Name],

I assume this isn't a priority right now.

I'll close this loop for now—feel free to reach out if
timing changes.

Best of luck!
```

---

### Case 2: "Send Me More Info"

**Send immediately (within 1 hour):**
- Case studies
- Portfolio
- Pricing breakdown
- Testimonials

**Day 3:**
```
Hi [Name],

Did the materials I sent help answer your questions?

Happy to hop on a call to discuss in more detail if that's easier.
```

---

### Case 3: "We're Interested, But..."

**They have an objection (budget, timing, scope)**

**Reply same day:**
```
Hi [Name],

Thanks for sharing that concern.

[Address objection specifically—see negotiation-strategies.md]

A few options to make this work:
1. [Option 1]
2. [Option 2]
3. [Option 3]

What do you think?
```

**Don't let objections sit—address immediately**

---

## Follow-Up Frequency by Lead Type

| Lead Type | Frequency | Duration |
|-----------|-----------|----------|
| Cold lead | Every 7 days | 2 touches, then archive |
| Warm lead (responded) | Every 3-4 days | Until proposal sent |
| Hot lead (call booked) | Every 1-2 days | Until deal closes |
| Nurture lead | Every 30-90 days | Ongoing (6-12 months) |
| Dead lead (not interested) | Never | Archive |

---

## The Psychology of Follow-Up

### Why People Don't Reply

1. **Busy** (most common) → Your email got buried
2. **Not a priority** → They'll "get to it later" (never)
3. **Need more info** → They're too polite to say "I don't get it"
4. **Not interested** → They're avoiding awkward "no"
5. **Decision paralysis** → Too many options, can't decide

### How Each Follow-Up Helps

**First follow-up (Day 7):**
- Unburies your email
- Shows you're serious
- Gives them a second chance

**Second follow-up (Day 14):**
- Shows persistence (good trait)
- Respects their time ("last time I'll bug you")
- Gets clear yes/no

**Long-term nurture (Day 30+):**
- Stays top of mind
- Provides ongoing value
- Catches them when timing is better

### When to Stop

**Stop after:**
- 2-3 touches with cold leads (no response)
- They explicitly say "not interested" or "stop emailing"
- They ask to be removed from your list

**Never stop:**
- High-value leads (nurture for 6-12 months)
- Warm relationships (check in quarterly)
- Past clients (re-engagement opportunities)

---

## Automation Tools

```bash
# Check for follow-ups due today
python3 tools/follow-up-reminder.py due

# Export follow-up schedule
python3 tools/follow-up-reminder.py export > follow-ups.md

# Mark follow-up as sent
python3 tools/follow-up-reminder.py sent [lead-id]

# Update lead status
python3 tools/revenue-tracker.py update [lead-id] --status "followed-up"
```

---

## Quick Reference: When to Follow Up

| Stage | Timing | Purpose |
|-------|--------|---------|
| Initial message | Day 0 | Start conversation |
| First follow-up | Day 7 | Unbury, show interest |
| Second follow-up | Day 14 | Last nudge, get yes/no |
| Long-term nurture | Day 30+ | Stay top of mind |
| Post-call summary | Within 1 hour | Confirm next steps |
| Proposal check-in | Day 3-4 | Answer questions |
| Final proposal nudge | Day 7 | Get decision |
| Team/boss follow-up | Day 3, 7, 14 | Push for decision |

---

## Golden Rules

1. **Follow up within 1 hour** when they reply (speed wins)
2. **Follow up every 7 days** when they don't (persistence pays)
3. **Stop after 2-3 touches** with cold leads (respect their time)
4. **Always provide value** in follow-ups (don't just "checking in")
5. **Get clear yes/no** (don't leave things open-ended)
6. **Automate reminders** (don't rely on memory)
7. **Track everything** (use revenue-tracker.py)
8. **Nurture high-value leads** (timing might be wrong, not the fit)

---

**Remember: The fortune is in the follow-up.**

Most people quit after 1 message. That's your edge.

*Persistence > Perfection*
