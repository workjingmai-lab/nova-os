# Follow-up Workflow — Arthur Quick-Ref

**Created:** 2026-02-06
**Purpose:** How to track outreach and never miss a follow-up

---

## Overview

All 10 HIGH + MEDIUM priority outreach messages are now tracked in the follow-up system:

- **HIGH priority (3):** EF $40K, Fireblocks $35K, Uniswap $40K = $115K
- **MEDIUM priority (7):** Alchemy $30K, Circle $20K, Infura $30K, Polygon $30K, Chainlink $30K, Arbitrum $30K, Optimism $30K = $150K
- **Total:** 10 messages, $265K tracked

---

## Step 1: Send Messages (Day 0)

When you send outreach messages, they're already in the tracker. No action needed.

**To check what's tracked:**
```bash
python3 tools/follow-up-tracker.py --list
```

---

## Step 2: Check Follow-ups Daily (Day 3, Day 7)

Run this once per day:
```bash
python3 tools/follow-up-tracker.py --check
```

**If follow-ups are due, you'll see:**
```
🔔 2 follow-up(s) due:

  • Alchemy ($30,000)
    Email: devex@alchemy.com
    Follow-up: Day 3 (3 days since sent)
    Message: Quick check — did my message about DevEx automation reach the right person?

  • Circle ($20,000)
    Email: devrel@circle.com
    Follow-up: Day 7 (7 days since sent)
    Message: Last message. If DevEx automation ever becomes a priority for Circle...
```

---

## Step 3: Send Follow-ups

**Day 3 message template:**
```
Subject: Re: [Original Subject]

Quick check — did my message about DevEx automation reach the right person on your team?

No response needed if you've already seen it. Just wanted to make sure it didn't get lost in the inbox.

Best,
Nova
```

**Day 7 message template:**
```
Subject: Re: [Original Subject]

Last message from me.

If DevEx automation becomes a priority for [Company], my work is at docs.openclaw.ai

I'll leave you be. Best of luck with [specific challenge they face]!

Best,
Nova
```

---

## Step 4: Mark Follow-up as Sent

After sending a follow-up:
```bash
python3 tools/follow-up-tracker.py --sent "Alchemy"
# → ✓ Marked follow-up sent for Alchemy (Day 3)
```

---

## Step 5: Update Status When They Respond

**If they respond (stop follow-ups):**
```bash
python3 tools/follow-up-tracker.py --responded "Alchemy"
# → ✓ Marked Alchemy as responded
```

**If they buy (deal closed):**
```bash
python3 tools/follow-up-tracker.py --closed "Uniswap" 40000
# → ✓ Marked Uniswap as closed ($40,000 won)
```

**If they say no (deal lost):**
```bash
python3 tools/follow-up-tracker.py --lost "Circle"
# → ✓ Marked Circle as lost
```

---

## Quick Commands Reference

```bash
# Check for due follow-ups
python3 tools/follow-up-tracker.py --check

# List all tracked messages
python3 tools/follow-up-tracker.py --list

# Mark follow-up sent
python3 tools/follow-up-tracker.py --sent "Target Name"

# Mark as responded
python3 tools/follow-up-tracker.py --responded "Target Name"

# Mark as closed (won)
python3 tools/follow-up-tracker.py --closed "Target Name" 30000

# Mark as lost
python3 tools/follow-up-tracker.py --lost "Target Name"
```

---

## Why This Matters

**80% of sales happen after 5+ touchpoints.**

- Day 0: Send message
- Day 3: Nudge ("Did this reach you?")
- Day 7: Final value-add ("Last message")

Without a tracker, you'll forget follow-ups. Without follow-ups, you'll lose deals.

This tool = never miss a follow-up.

---

## Current Status (2026-02-06)

**All 10 messages tracked and ready.**

Once you send the messages, the follow-up schedule is automatic:
- Day 3 (Feb 9): "Quick check" reminders
- Day 7 (Feb 13): "Last message" reminders

Run `--check` daily to see what's due.

---

*Created: 2026-02-06 (Work block 2639)*
*Purpose: Arthur quick-ref for follow-up workflow*
