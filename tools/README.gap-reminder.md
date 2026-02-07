# gap-reminder.py

**Daily reminder of what you're leaving on the table.**

## What It Does

Shows your execution gap in motivational terms:
- How much you have ready to send
- How much you've actually sent
- What you're leaving on the table
- Time estimate to close the gap
- Quick wins to execute

## Usage

```bash
python3 tools/gap-reminder.py
```

## Output Example

```
============================================================
⏰ 2026-02-07 08:10:40 UTC
============================================================

💰 You have $892,000 ready to send.
📤 You've only sent $5,000.

🚨 ** You're leaving $887,000 on the table. **

⚠️  At $10K/min, that's 89 minutes of work.
⚠️  Why haven't you hit send yet?

💡 Reminder: Execution beats planning every time.
💡 Hit send. Then optimize.

📋 Quick wins:
   1. Run: python3 tools/execution-gap-visualizer.py
   2. Check: outreach/messages/ for ready messages
   3. Execute: ARTHUR-57-MIN-QUICK-REF.md

============================================================
```

## Why It Works

**Psychological trigger:** "Leaving $887K on the table" is more motivating than "99.4% gap."

**Time framing:** "89 minutes of work" makes the gap feel actionable, not overwhelming.

**Action catalyst:** Provides 3 concrete next steps — no ambiguity about what to do.

**Shame-driven motivation:** "Why haven't you hit send yet?" — rhetorical question that drives action.

## When to Use

- **Daily:** Run once per day to stay focused on execution
- **Pre-execution:** Run before starting outreach to create urgency
- **Post-blocker:** Run after unblocking (GitHub auth, gateway restart) to see what's now possible

## Integration

Add to cron or run manually during daily check-in.

**Status:** Active ✅
**Created:** 2026-02-07 (Work block 3249)
**Version:** 1.0
