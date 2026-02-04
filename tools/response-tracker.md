# response-tracker.py — Outreach Response Tracking

**Purpose:** Track responses to outreach messages through the full pipeline (sent → replied → interested → won/lost). Completes the outreach ecosystem: generate → send → track.

**When to use:** When prospects respond to outreach messages. Track status, notes, and conversion.

---

## What It Does

1. **Add responses** — Log prospect responses to sent messages
2. **List responses** — View all responses or filter by status
3. **Show stats** — Response rate, pipeline conversion funnel
4. **Update status** — Change status as pipeline progresses

---

## Usage

### Add a Response

```bash
# Prospect replied "interested"
python3 tools/response-tracker.py add \
  --msg 001 \
  --response interested \
  --note "Asked for proposal, send next week"

# Prospect replied "not interested"
python3 tools/response-tracker.py add \
  --msg 002 \
  --response lost \
  --note "Budget frozen, try again next quarter"
```

### List Responses

```bash
# Show all responses
python3 tools/response-tracker.py list

# Filter by status
python3 tools/response-tracker.py list --status interested
python3 tools/response-tracker.py list --status won
```

**Example output:**
```
📊 Responses (12):
------------------------------------------------------------
001 | interested           | Asked for proposal, send next week
002 | lost                 | Budget frozen, try again next quarter
003 | call_scheduled       | Call on Thursday 2pm EST
004 | replied              | Wants more info on pricing
005 | proposal_sent        | Sent $25K proposal for multi-agent system
```

### Show Statistics

```bash
python3 tools/response-tracker.py stats
```

**Example output:**
```
📈 Response Statistics:
----------------------------------------
Total responses: 12
Replied: 10 (83%)

By status:
  interested: 5
  replied: 2
  call_scheduled: 2
  proposal_sent: 1
  won: 1
  lost: 1
```

---

## Status Types

**Pipeline flow:**

```
sent → no_response
     → replied → interested → call_scheduled → proposal_sent → negotiation → won/lost
```

**Status meanings:**

| Status | Description | Next Step |
|--------|-------------|-----------|
| **no_response** | No reply yet | Follow up in 3-5 days |
| **replied** | Replied, not yet qualified | Ask qualifying questions |
| **interested** | Expressed interest | Schedule call |
| **call_scheduled** | Call booked | Prepare proposal |
| **proposal_sent** | Proposal sent | Follow up in 1 week |
| **negotiation** | In negotiation | Close the deal |
| **won** | Converted! | Start project |
| **lost** | Not interested | Note reason for future |

---

## Data File

**Location:** `data/responses.json`

**Format:**
```json
[
  {
    "msg_id": "001",
    "status": "interested",
    "note": "Asked for proposal, send next week",
    "created_at": "2026-02-04T05:30:00Z",
    "updated_at": "2026-02-04T05:30:00Z"
  },
  {
    "msg_id": "002",
    "status": "lost",
    "note": "Budget frozen, try again next quarter",
    "created_at": "2026-02-04T05:31:00Z",
    "updated_at": "2026-02-04T05:31:00Z"
  }
]
```

**msg_id format:** Matches the message ID in `service-outreach-tracker.json`

---

## Integration

**Part of outreach pipeline:**

1. **Generate** — `outreach-message-template-generator.py` creates messages
2. **Send** — `send-service-messages.py` sends to prospects
3. **Track** — `response-tracker.py` logs responses (this tool)
4. **Convert** — Won/lost status feeds back into `revenue-tracker.py`

**Full funnel:**
```
Leads → Messages → Sent → Responses → Interested → Won → $
```

---

## Metrics

**Key metrics:**

| Metric | Formula | What It Means |
|--------|---------|---------------|
| **Response rate** | replied / total sent × 100% | Message quality |
| **Interest rate** | interested / replied × 100% | Lead quality |
| **Conversion rate** | won / interested × 100% | Closing ability |
| **Pipeline velocity** | avg days from sent → won | Sales speed |

**Example:**
- 83% response rate → Excellent targeting
- 50% interest rate → Good message quality
- 20% conversion rate → Room for improvement

---

## Dependencies

- Python 3.6+
- Standard library only (`json`, `sys`, `datetime`, `pathlib`, `typing`)
- **Related:** `service-outreach-tracker.json` (matches msg_id)

---

## Use Cases

**After sending messages:**
```bash
# Track responses as they come in
python3 tools/response-tracker.py add --msg 001 --response interested --note "Asked for pricing"
```

**Weekly review:**
```bash
# Check all responses
python3 tools/response-tracker.py list

# View stats
python3 tools/response-tracker.py stats

# Filter for follow-ups
python3 tools/response-tracker.py list --status interested
```

**Pipeline management:**
```bash
# Update status as pipeline progresses
python3 tools/response-tracker.py add --msg 001 --response call_scheduled --note "Thursday 2pm EST"

# After call
python3 tools/response-tracker.py add --msg 001 --response proposal_sent --note "Sent $25K proposal"

# After decision
python3 tools/response-tracker.py add --msg 001 --response won --note "Signed contract, starting Feb 15"
```

---

## Created

2026-02-04 — Work block 1422
