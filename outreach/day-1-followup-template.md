# Day 1 Follow-Up Template
# Service Outreach - Warm Lead Check-In (24-36 hours after initial message)

**Purpose:** Gentle check-in while lead is still warm. Not pushy, just ensuring message was seen.

**Timing:** 24-36 hours after initial outreach
**Target Response Rate:** 15-25%

---

## Template Structure

**Subject:** Re: [Original Subject]

Hi [Name],

Just wanted to make sure my previous message didn't get buried in your inbox.

I know you're busy, but I genuinely believe [specific service] could help [prospect] with [specific pain point we identified].

No pressure at all - just thought I'd check in.

Best,
[Your Name]

---

## Customization Examples

### For DAO Governance Prospects

Hi [Name],

Just wanted to make sure my previous message didn't get buried in your inbox.

I know you're busy with [recent proposal/governance event], but I genuinely believe governance automation could help [prospect] reduce the noise in [specific governance pain point].

No pressure at all - just thought I'd check in.

Best,
Nova

---

### For Infrastructure Prospects

Hi [Name],

Just wanted to make sure my previous message didn't get buried in your inbox.

I know you're busy with [recent product launch/milestone], but I genuinely believe [specific monitoring service] could help [prospect] catch [specific type of issue] before users notice.

No pressure at all - just thought I'd check in.

Best,
Nova

---

### For Protocol/DeFi Prospects

Hi [Name],

Just wanted to make sure my previous message didn't get buried in your inbox.

I know you're busy with [recent market event/product update], but I genuinely believe [specific service] could help [prospect] monitor [specific risk/anomaly].

No pressure at all - just thought I'd check in.

Best,
Nova

---

## Usage Instructions

1. **Timing:** Send 24-36 hours after initial message
2. **Personalization:** Include 1 specific detail from their recent work (proposal, launch, tweet, etc.)
3. **Tone:** Helpful, not pushy. "Making sure you saw it" vs "Why haven't you replied?"
4. **Call to Action:** None. This is a soft check-in, not a demand
5. **If no response:** Move to Day 3 follow-up (see templates)

---

## Why Day 1 Matters

- **Leads are warm:** 24-36h is peak attention window
- **Inbox burial:** Messages get buried quickly in busy inboxes
- **Response lift:** Day 1 follow-ups increase response rates by 15-25%
- **Not annoying:** Still within "helpful reminder" territory, not "nagging"

---

## Integration

Use with `tools/service-batch-send.py`:
```bash
python3 tools/service-batch-send.py --followup day1 --top 10
```

This will send Day 1 follow-ups to the top 10 most recent initial messages.
