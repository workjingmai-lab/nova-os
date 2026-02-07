# Service Outreach Follow-Up Sequences

**Purpose:** Convert non-responsive leads through structured touch points  
**Created:** Work block 3274  
**Applies to:** 39 service leads ($332K pipeline)

---

## The 4-Touch Sequence

### Touch 1: Initial Outreach (Day 0)
**Channel:** Email/Telegram/Discord (lead-specific)  
**Goal:** Value-first introduction, establish relevance

**Template:**
```
Subject: [Specific pain point] — quick win for [Company]

Hi [Name],

[Personalized research sentence showing I understand their specific situation]

[Named pain point]: [brief observation of their current challenge]

[Solution]: I help [target] automate [specific outcome] — typically saves [X hours/$Y] per [timeframe].

[Proof]: Recent example: [similar company] reduced [metric] by [result] in [timeframe].

[CTA]: Worth a 10-minute chat to see if there's a fit?

Best,
Nova
```

**Expected response rate:** 15-25%  
**Expected timeline:** 24-72 hours

---

### Touch 2: Value Add (Day 4)
**Channel:** Same as initial  
**Goal:** Re-engage with additional value, demonstrate expertise

**Template:**
```
Subject: Re: [original subject] — [resource] for [Company]

Hi [Name],

Quick follow-up on my note about [pain point].

Even if automation isn't a priority right now, I thought this might help:

[Resource]: [link to relevant article, tool, or insight specific to their industry/challenge]

[Key insight from resource in 1-2 sentences]

No pitch — just something I thought was relevant given [specific context about their situation].

If automation does become a priority down the road, happy to chat.

Best,
Nova
```

**Expected response rate:** 10-15% (cumulative 25-35%)  
**Expected timeline:** 24-48 hours

---

### Touch 3: Social Proof (Day 8)
**Channel:** Same as initial  
**Goal:** Leverage peer behavior, create FOMO

**Template:**
```
Subject: [Peer company] just [achieved result] — thought of you

Hi [Name],

Wanted to share a quick win: [similar company in their space] just [specific outcome] using [type of automation].

[Specific metric]: [number] [improvement] in [timeframe]

Context: They had [similar situation to prospect's current state].

I know [Company] is focused on [their known priority] — this might be relevant given [connection].

If you'd like to see how they did it (or explore something similar), happy to share.

Either way, keep building.

Best,
Nova
```

**Expected response rate:** 8-12% (cumulative 33-45%)  
**Expected timeline:** 24-48 hours

---

### Touch 4: The Breakup (Day 14)
**Channel:** Same as initial  
**Goal:** Final attempt, leave positive impression, request referral

**Template:**
```
Subject: Permission to close your file?

Hi [Name],

I've reached out a few times about helping [Company] with [pain point], but haven't heard back.

No worries — timing is everything, and maybe now isn't it.

Quick ask: Should I close your file, or is there a better time to reconnect?

Also: If you know anyone else in [industry] struggling with [pain point], I'd appreciate the intro. Happy to return the favor.

Either way, best of luck with [Company's current initiative].

Nova
```

**Expected response rate:** 5-10% (cumulative 38-50%)  
**Expected timeline:** 24-72 hours

---

## Sequence Timeline Overview

| Touch | Day | Purpose | Response Rate | Cumulative |
|-------|-----|---------|---------------|------------|
| 1 | 0 | Initial value | 15-25% | 15-25% |
| 2 | 4 | Value add | 10-15% | 25-35% |
| 3 | 8 | Social proof | 8-12% | 33-45% |
| 4 | 14 | Breakup | 5-10% | 38-50% |

---

## Response Type Handling

### "Not now, but later"
**Action:** Add to nurture list, check in quarterly  
**Template:**
```
Thanks for the response! I'll check back in [timeframe]. 

In the meantime, I'll send occasional resources I think might help.
```

### "Not interested"
**Action:** Remove from active sequence, request referral  
**Template:**
```
No problem at all — appreciate the reply.

Quick ask: Know anyone else in [industry] who might benefit from this? Happy to return the intro favor.
```

### "Tell me more"
**Action:** Move to sales conversation, schedule call  
**Template:**
```
Great! Here are 3 ways we could work together:

1. [Quick win option — $1-2K, 3-5 days]
2. [Standard engagement — $3-5K, 1-2 weeks]  
3. [Comprehensive solution — $10-25K, 2-4 weeks]

Which feels like the right starting point? Happy to jump on a quick call to discuss.
```

### No response after 4 touches
**Action:** Archive lead, add to quarterly nurture  
**Note:** 50-62% of leads won't respond — this is normal

---

## Automation Tools

### Using follow-up-reminder.py
```bash
# Schedule follow-up for specific lead
python3 tools/follow-up-reminder.py add --lead "Uniswap" --date "2026-02-11" --touch 2

# Check due follow-ups
python3 tools/follow-up-reminder.py due

# Export follow-up schedule
python3 tools/follow-up-reminder.py export > follow-ups-schedule.md
```

### Using revenue-tracker.py
```bash
# Update lead status after each touch
python3 tools/revenue-tracker.py update --name "Uniswap" --field status --value "touch-2-sent"

# Check response rates by touch
python3 tools/revenue-tracker.py analyze --metric response-rate --by touch
```

---

## Metrics to Track

| Metric | Target | Current |
|--------|--------|---------|
| Response rate (Touch 1) | 20% | TBD |
| Response rate (all touches) | 45% | TBD |
| Meeting conversion | 30% of responders | TBD |
| Close rate | 25% of meetings | TBD |
| Time to response | <48 hours | TBD |

---

## Resources

- **Lead list:** outreach/leads-pipeline.json
- **Initial messages:** outreach/service-messages/
- **Follow-up tracker:** tools/follow-up-reminder.py
- **Revenue tracker:** tools/revenue-tracker.py
- **Top 3 follow-up schedule:** TOP-3-FOLLOW-UP-SCHEDULE.md

---

*Created by Nova — work block 3274*
