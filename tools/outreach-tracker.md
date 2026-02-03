# outreach-tracker.md — Track Outreach Messages & Responses

**Version:** 1.0  
**Category:** Outreach / CRM  
**Created:** 2026-02-01

---

## What It Does

Tracks outbound messages (proposals, DMs, emails) and monitors responses for lead management.

### Features

- Log outbound messages with metadata
- Track response status
- Calculate response rates
- Categorize by channel (email, Moltbook, Discord)
- Generate pipeline reports
- Follow-up reminders

---

## Usage

```bash
# Log a sent message
python3 tools/outreach-tracker.py log "Guillermo Rauch" --channel email --type proposal

# Update status (received response)
python3 tools/outreach-tracker.py update 1 --status responded

# Show pipeline
python3 tools/outreach-tracker.py pipeline

# Generate report
python3 tools/outreach-tracker.py report

# Show follow-ups due
python3 tools/outreach-tracker.py followups
```

---

## Message Types

| Type | Description | Example |
|------|-------------|---------|
| `proposal` | Service proposal | OpenClaw Setup ($3-5K) |
| `intro` | Introduction | "Hi, I'm Nova..." |
| `followup` | Follow-up message | "Any updates?" |
| `dm` | Direct message | Moltbook DM |
| `comment` | Comment on post | Moltbook comment |

---

## Status Values

- `sent` — Message sent, awaiting response
- `responded` — Received reply
- `interested` — Expressed interest
- `converted` — Became client/customer
- `declined` — Not interested
- `ghosted` — No response after follow-up

---

## Data Storage

Stored in `.outreach-pipeline.json`:

```json
{
  "messages": [
    {
      "id": 1,
      "recipient": "Guillermo Rauch",
      "channel": "email",
      "type": "proposal",
      "status": "sent",
      "sent_at": "2026-02-02T20:50:00Z",
      "followup_due": "2026-02-05T20:50:00Z"
    }
  ]
}
```

---

## Pipeline Report

```bash
$ python3 tools/outreach-tracker.py pipeline

📊 OUTREACH PIPELINE
────────────────────────────────────────────────────────────

Sent: 5 messages
  • Proposals: 3
  • Intros: 1
  • Follow-ups: 1

Status:
  • Sent: 4 (awaiting response)
  • Responded: 1 (20% response rate)
  • Interested: 0
  • Converted: 0

Channels:
  • Email: 3
  • Moltbook DM: 2

Follow-ups due: 2 (next 24h)
```

---

## Dependencies

- Python 3.7+
- Standard library only

---

## Integration

- Pair with `proposal-generator.py` for proposal creation
- Use `moltbook-engagement.py` for relationship tracking
- Feed into `self-improvement-loop.py` for analytics

---

## Tips

1. Log every outbound message immediately
2. Set follow-up reminders (3-7 days)
3. Categorize accurately for pipeline reporting
4. Track response rates to optimize outreach
5. Archive declined leads to avoid re-contacting
