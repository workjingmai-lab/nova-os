# response-tracker.py — Track Outreach Responses

## What It Does

Tracks responses to your service outreach messages:
- Log replies as they come in
- Categorize by status (interested, call_scheduled, won, lost, etc.)
- Calculate response rates
- Monitor pipeline conversion

## Usage Examples

**Add a response:**
```bash
python3 tools/response-tracker.py add --msg 001 --response interested --note "Wants to discuss automation needs"
```

**List all responses:**
```bash
python3 tools/response-tracker.py list
```

**Filter by status:**
```bash
python3 tools/response-tracker.py list --status call_scheduled
```

**Show response statistics:**
```bash
python3 tools/response-tracker.py stats
```

**Update a response:**
```bash
python3 tools/response-tracker.py add --msg 001 --response call_scheduled --note "Call set for Feb 5"
```

## Response Status Types

| Status | Description |
|--------|-------------|
| `no_response` | No reply yet |
| `replied` | Replied but not qualified |
| `interested` | Expressed interest |
| `call_scheduled` | Call booked |
| `proposal_sent` | Proposal delivered |
| `negotiation` | In contract talks |
| `won` | Deal closed (revenue!) |
| `lost` | Not interested anymore |

## Data Storage

Responses stored in: `data/responses.json`

Format:
```json
[
  {
    "msg_id": "001",
    "status": "interested",
    "note": "Wants to discuss automation needs",
    "created_at": "2026-02-04T10:30:00Z",
    "updated_at": "2026-02-04T10:30:00Z"
  }
]
```

## Example Workflow

**After sending messages:**
```bash
# Send 100 messages
python3 tools/service-batch-send.py --all

# A few days later...
python3 tools/response-tracker.py stats
# → Total responses: 12
# → Replied: 10 (83%)
# → interested: 7, call_scheduled: 2, proposal_sent: 1
```

**Log responses as they arrive:**
```bash
# Email from Ethereum Foundation
python3 tools/response-tracker.py add --msg 001 --response interested --note "Interested in node monitoring"

# Reply from Fireblocks
python3 tools/response-tracker.py add --msg 002 --response call_scheduled --note "Call Feb 5, 2pm EST"

# Send proposal after call
python3 tools/response-tracker.py add --msg 002 --response proposal_sent --note "$30K proposal sent"

# Deal won!
python3 tools/response-tracker.py add --msg 002 --response won --note "Contract signed $30K"
```

## Use Cases

**Daily check-in:**
```bash
python3 tools/response-tracker.py list --status interested
# Follow up with interested prospects
```

**Pipeline health:**
```bash
python3 tools/response-tracker.py stats
# Know your conversion rates
```

**Weekly review:**
```bash
python3 tools/response-tracker.py list
# Review all responses, update statuses
```

## Integration

**Works with:**
- `service-batch-send.py` — Send messages
- `pipeline-snapshot.py` — View pipeline health
- `outreach-tracker.py` — Manage leads

## Why This Matters

**Response tracking = revenue conversion.**
- Without tracking: "Did they reply? I forget..."
- With tracking: "12 responses, 7 interested, 2 calls booked"

Fast response logging = fast follow-up = deals closed.

---

**Created:** Work block 1178  
**Last updated:** 2026-02-03  
**Related tools:** service-batch-send.py, pipeline-snapshot.py, outreach-tracker.py
