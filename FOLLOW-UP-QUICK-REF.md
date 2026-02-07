# Follow-up Workflow Quick Reference

> When messages are sent → use this workflow to track and follow up.

## Pre-Send (Before Arthur Executes)

✅ **Tools ready:**
- `service-batch-send.py` — Send all 29 service messages
- `grant-batch-submit.py` — Submit 5 grant applications
- `follow-up-tracker.py` — Track sent messages + follow-ups

## Day 0: Send Day

When Arthur sends messages:

```bash
# For each message sent, add to tracker:
python3 tools/follow-up-tracker.py add "Company Name" 25000 "HIGH"
```

**Example:**
```bash
# After sending EF proposal
python3 tools/follow-up-tracker.py add "Ethereum Foundation" 40000 "HIGH"

# After sending Balancer message
python3 tools/follow-up-tracker.py add "Balancer" 20000 "MEDIUM"
```

## Daily Routine

**Every morning, check what's due:**

```bash
python3 tools/follow-up-tracker.py due
```

**Output examples:**
- `🔔 Uniswap - Day 3 follow-up DUE TODAY`
- `⚠️  Optimism - Day 7 follow-up OVERDUE by 2 days`

## Follow-up Days

Standard schedule: **Day 3, 7, 14, 21**

**Day 3 follow-up (Thursday):**
```
Subject: Re: DevEx automation proposal
Hi [Name], sent this on Monday — any thoughts on the 3-agent suite?
Happy to hop on a 15-min call to discuss your automation priorities.
```

**Day 7 follow-up:**
```
Subject: Re: [original topic]
Hi [Name], checking in on this. I can share:
- Case studies from similar DAOs
- ROI calculator for automation
- Live demo of the agents
```

**Day 14/21:**
- Pivot to new angle if no response
- Reference recent work: "Just shipped X for Y DAO"
- Or: "Gentle close — not a fit right now?"

## After Follow-up

Mark it done:

```bash
python3 tools/follow-up-tracker.py done "Company Name" 3
```

## Check Status Anytime

```bash
# Detailed view of a company
python3 tools/follow-up-tracker.py status "Ethereum Foundation"

# List all tracked messages
python3 tools/follow-up-tracker.py
```

## Response Tracking

When you get a response, add it to the tracker (manual edit for now):

```json
{
  "responses": [
    {"date": "2026-02-10", "type": "email", "summary": "Interested, wants call"}
  ]
}
```

## Metrics to Track

- **Response rate:** Responses / Sent
- **Call rate:** Calls booked / Responses
- **Close rate:** Won / Calls booked
- **Follow-up completion:** % of follow-ups done on time

## Integration with Heartbeat

Add to `HEARTBEAT.md`:

```yaml
- name: "Follow-up check"
  every: "daily"
  message: |
    Run follow-up-tracker.py due
    If overdue follow-ups exist, flag them
```

## Commands Cheat Sheet

| Action | Command |
|--------|---------|
| List all | `python3 tools/follow-up-tracker.py` |
| Add sent | `python3 tools/follow-up-tracker.py add <company> <value> <priority>` |
| Check due | `python3 tools/follow-up-tracker.py due` |
| Mark done | `python3 tools/follow-up-tracker.py done <company> <day>` |
| Get status | `python3 tools/follow-up-tracker.py status <company>` |

---

**Created:** Work block #2677 — 2026-02-06
**Links:** `follow-up-tracker.py` | `START-HERE.md` | `POST-SEND-WORKFLOW.md`
