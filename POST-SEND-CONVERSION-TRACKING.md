# Post-Send Conversion Tracking Guide

**Purpose:** Track responses → calls → won deals from sent messages
**Time:** 5 min/day to maintain
**Created:** 2026-02-06
**Work Block:** 2742

---

## The System

Once messages are sent, track conversion through these stages:

```
Sent → Responded → Call Scheduled → Call Completed → Proposal Sent → Won/Lost
```

---

## Daily Checklist (5 min)

### 1. Check for Responses
```bash
# Check email responses (manual)
# Check Moltbook DMs
# Check Telegram/WhatsApp for replies
```

**Log responses:**
```bash
python3 tools/follow-up-tracker.py respond <message_id> <response_type>
```

Response types:
- `interested` — "Tell me more" or "Let's talk"
- `questions` — Has questions before call
- `not_interested` — "Not for us" or decline
- `maybe_later` — "Check back in Q2"
- `no_response` — After 7 days

---

### 2. Schedule Calls
```bash
python3 tools/follow-up-tracker.py call <message_id> <date>
```

**Example:**
```bash
python3 tools/follow-up-tracker.py call ef_optimism-fractal 2026-02-10
```

---

### 3. Log Call Outcomes
```bash
python3 tools/follow-up-tracker.py outcome <message_id> <outcome>
```

Outcomes:
- `proposal_sent` — Send proposal, track value
- `follow_up_scheduled` — Needs more time
- `not_interested` — Not moving forward
- `ghosted` — No show, no response

---

### 4. Track Won/Lost
```bash
python3 tools/follow-up-tracker.py won <message_id> <value>
python3 tools/follow-up-tracker.py lost <message_id> <reason>
```

**Example:**
```bash
python3 tools/follow-up-tracker.py won ef_optimism-fractal 75000
```

---

## Conversion Metrics

Track these weekly:

| Metric | Formula | Target |
|--------|---------|--------|
| Response Rate | Responses ÷ Sent | 20%+ |
| Call Rate | Calls ÷ Responses | 50%+ |
| Proposal Rate | Proposals ÷ Calls | 60%+ |
| Win Rate | Won ÷ Proposals | 25%+ |
| Conversion Rate | Won ÷ Sent | 1.5%+ |

**Overall conversion:** 1.5% (industry standard for cold outreach)

---

## Pipeline Velocity

Time between stages (track averages):

- Sent → Response: 3-7 days
- Response → Call: 2-5 days
- Call → Proposal: 1-3 days
- Proposal → Won: 7-30 days

**Total cycle:** 14-45 days from send to revenue

---

## Weekly Report (Every Monday)

```bash
python3 tools/follow-up-tracker.py report
```

**Outputs:**
- Total sent
- Response rate
- Call rate
- Win rate
- Pipeline value
- Revenue won

**Update diary.md with key metrics.**

---

## Follow-Up Sequences

### Day 0 (Send)
- Initial message sent
- Status: `sent`

### Day 3 (First follow-up)
```bash
python3 tools/follow-up-tracker.py followup <message_id> 3
```
Message: "Any thoughts on [specific pain]?"

### Day 7 (Second follow-up)
```bash
python3 tools/follow-up-tracker.py followup <message_id> 7
```
Message: "Worth a quick call?"

### Day 14 (Final follow-up)
```bash
python3 tools/follow-up-tracker.py followup <message_id> 14
```
Message: "Last check-in — closing the loop"

### Day 21 (Archive)
```bash
python3 tools/follow-up-tracker.py archive <message_id>
```
Status: `no_response` (move on)

---

## Tools Reference

| Tool | Purpose |
|------|---------|
| `follow-up-tracker.py` | Track sent messages + follow-ups |
| `revenue-tracker.py` | Track pipeline value + conversion |
| `status` | Quick pipeline overview |

---

## Example Workflow

**1. Send message (Arthur):**
```bash
bash tools/send-everything.sh full
```

**2. Log sends (auto):**
```bash
python3 tools/follow-up-tracker.py log sent ef_optimism-fractal expert "50-100K"
```

**3. Check responses (daily):**
```bash
python3 tools/follow-up-tracker.py status
```

**4. Log response (when received):**
```bash
python3 tools/follow-up-tracker.py respond ef_optimism-fractal interested
```

**5. Schedule call:**
```bash
python3 tools/follow-up-tracker.py call ef_optimism-fractal 2026-02-10
```

**6. Log outcome (after call):**
```bash
python3 tools/follow-up-tracker.py won ef_optimism-fractal 75000
```

**7. Update revenue tracker:**
```bash
python3 tools/revenue-tracker.py won services 75000
```

---

## The Insight

**What gets tracked gets managed.**

Without tracking:
- "How did that outreach go?" → "I think some people responded?"
- "What's our response rate?" → "I have no idea."
- "What's our conversion rate?" → "We haven't sent anything yet."

With tracking:
- "How did that outreach go?" → "39 sent, 8 responses, 4 calls, 1 proposal"
- "What's our response rate?" → "20.5% (above target)"
- "What's our conversion rate?" → "2.56% (above industry 1.5%)"

**Tracking = data. Data = optimization. Optimization = revenue.**

---

*Work block 2742 — Post-send conversion tracking guide*
*Related: POST-SEND-WORKFLOW.md, tools/follow-up-tracker.py, tools/revenue-tracker.py*
