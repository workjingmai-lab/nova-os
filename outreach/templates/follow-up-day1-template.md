# Day 1 Follow-Up Template

**Timing:** Send 24-36 hours after initial message
**Purpose:** Gentle nudge for warm leads who haven't responded yet
**Tone:** Casual, low-pressure, "just bumping this up"
**Use Case:** High-confidence prospects (8+/10) who might have missed the first message

## Template 1: Casual Bump (Best for warm leads)

**Subject:** Re: [previous subject line]

Hey [Name],

Just wanted to bump this to the top of your inbox — I know how easily messages get buried.

Quick recap: I reached out about [specific pain point] → [solution] for [company name].

No pressure at all. If this isn't a priority right now, no worries.

Best,
[Your name]

---

## Template 2: Value Reminder (Best for busy prospects)

**Subject:** Re: [previous subject line] → quick update

Hi [Name],

Following up on my note from yesterday about [specific pain point].

I noticed [new observation or validation of their pain point] — thought you might find this relevant.

Worth a quick chat this week? If not, totally understand.

Best,
[Your name]

---

## Template 3: Question-Based (Best for engagement)

**Subject:** Re: [previous subject line] → one question

Hi [Name],

Quick follow-up — curious:

Is [specific pain point] still on your radar, or has this shifted for [company name]?

Trying to understand timing. If it's not relevant anymore, no worries at all.

Best,
[Your name]

---

## When to Use Day 1 Follow-Up

✅ **Send Day 1 if:**
- Prospect is 8+/10 confidence score
- You have strong signal they're a good fit
- Initial message was personalized and value-first
- You want to stay top-of-mind before they forget

❌ **Skip Day 1 if:**
- Prospect is cold (<6/10 confidence)
- Initial message was generic
- No strong pain point identified
- They've clearly seen and ignored (viewed multiple times)

## Success Metrics

- **Response rate target:** 15-25% (higher than Day 3 because it's fresh)
- **Unsubscribe rate:** Should be <2% (if higher, you're being too pushy)
- **Positive reply:** "Thanks for the reminder, let's talk" = good signal
- **Negative reply:** "Not interested, stop emailing" = remove from list immediately

## Day 1 vs Day 3 Follow-Up

| Aspect | Day 1 | Day 3 |
|--------|-------|-------|
| Purpose | Gentle nudge before forgotten | Reminder after they've had time to consider |
| Tone | Casual, low-pressure | More professional, value-focused |
| Best for | Warm leads (8+/10) | All leads who haven't responded |
| Response rate | 15-25% | 10-15% |
| Risk | Can seem pushy if overused | Safer, more expected |

## Integration with Batch Sender

```bash
# Send Day 1 follow-ups to prospects who got initial message yesterday
python3 tools/service-batch-send.py --followup day1 --since 24h
```

**Created:** 2026-02-04 (Work block 1551)
**Rationale:** Day 3 follow-ups are too slow for warm leads. A gentle Day 1 nudge captures attention while your message is still fresh in their mental context.
