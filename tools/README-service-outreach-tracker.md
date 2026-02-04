# service-outreach-tracker.py

Track outbound service proposals and monitor responses.

## What It Does

Manages the complete pipeline for service outreach: logging sent messages, tracking responses, calculating conversion rates, and identifying follow-ups needed.

## Installation

No dependencies required beyond Python 3. Uses `service-outreach-tracker.json` for data persistence.

## Usage

### Get summary
```bash
python3 tools/service-outreach-tracker.py summary
```

Output:
```
📊 Outreach Summary:
   Sent: 10
   Pending: 10
   Replied: 0
   Conversion: 0.0%
```

### Check pending follow-ups
```bash
python3 tools/service-outreach-tracker.py pending
```

Shows messages needing follow-up (default: 48+ hours old).

### Log a sent message
```bash
python3 tools/service-outreach-tracker.py log "Prospect Name" "Service Type" "$1-2K" "Message preview..."
```

### Log a response
```python
from service_outreach_tracker import log_reply

log_reply("Prospect Name", "interested", "Wants discovery call")
```

## Data Structure

Tracked data stored in `service-outreach-tracker.json`:
- `totalSent`: Total messages sent
- `totalReplied`: Total responses received
- `conversionRate`: Reply rate percentage
- `messages[]`: Array of sent messages with timestamps, status, responses

## Message Status Flow

1. `sent` — Message sent, awaiting response
2. `replied` — Prospect responded
3. `negotiating` — In discussion
4. `won` — Converted to client
5. `declined` — Not interested

## Use Cases

- **Pipeline tracking**: Monitor $122K service pipeline
- **Follow-up management**: Identify messages needing attention
- **Conversion analytics**: Track response rates by service type
- **Revenue forecasting**: Calculate pipeline health

## Examples

Log outreach to Charlinho:
```bash
python3 tools/service-outreach-tracker.py \
  log "Charlinho" "Quick Automation" "$1-2K" \
  "Engagement automation for your agent"
```

Check follow-ups needed:
```bash
python3 tools/service-outreach-tracker.py pending
```

## Integration

Works with:
- `revenue-tracker.py` — Pipeline overview
- `outreach-messages/` — Draft message templates
- `revenue-pipeline.json` — Total pipeline tracking

## Return Codes

- `0` — Success
- `1` — Error (file not found, invalid arguments)

## Notes

- All timestamps in UTC
- Message previews truncated to 100 chars
- Follow-up threshold: 48 hours (configurable in code)
- Tracker file auto-created on first run

---

*Tracks $122K service pipeline across 10 prospects*
