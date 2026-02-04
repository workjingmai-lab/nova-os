# README: send-service-messages.py

## Overview
Execute service outreach sends from your pipeline. Filter, sort, and send messages to prospects.

## Purpose
Transform "ready" messages into "sent" messages. This is the execution engine that takes your built pipeline and activates it.

## Installation
No installation required. Uses Python 3 standard library.

## Usage

### Send Top 10 by Value
```bash
python3 tools/send-service-messages.py --top 10
```
Sends the 10 highest-value ready messages.

### Send All Ready Messages
```bash
python3 tools/send-service-messages.py --all
```
Sends all messages with status="ready".

### Send Specific Batch
```bash
python3 tools/send-service-messages.py --batch 16
```
Sends messages from batch-16 (filtered by filename).

### Dry Run (Preview)
```bash
python3 tools/send-service-messages.py --top 10 --dry-run
```
Shows what would be sent without actually sending.

## Workflow

1. **Load** messages from `service-outreach-tracker.json`
2. **Filter** by status="ready"
3. **Sort** by value (high to low)
4. **Preview** first 5 messages
5. **Confirm** (type "yes")
6. **Send** messages via configured channel
7. **Update** tracker with "sent" status

## Output

### Console Output
```
📊 Loading messages...
   Total messages: 103
   Ready to send: 100
   Sending top 10: 10 messages
   - EigenLayer: $150K
   - EigenDA: $20K
   ... and 7 more

   Total value: $580K

⚠️  Ready to send!
   Type 'yes' to confirm:

🚀 Sending 10 messages...
[1/10] 📧 Sending to: EigenLayer
[2/10] 📧 Sending to: EigenDA
...

✅ Done!
   Sent: 10
   Failed: 0
```

### Tracker Update
Each sent message gets:
- `status`: "sent"
- `sentAt`: ISO timestamp

Pipeline metrics recalculated:
- `totalReady`: decreased
- `totalSent`: increased

## Data Files

### Input: service-outreach-tracker.json
```json
{
  "messages": [
    {
      "file": "batch-16-eigenlayer.md",
      "prospect": "EigenLayer",
      "amountRange": "$150K",
      "status": "ready"
    }
  ],
  "totalReady": 100,
  "totalSent": 0
}
```

### Output: Updated Tracker
```json
{
  "messages": [
    {
      "file": "batch-16-eigenlayer.md",
      "prospect": "EigenLayer",
      "amountRange": "$150K",
      "status": "sent",
      "sentAt": "2026-02-03T20:00:00Z"
    }
  ],
  "totalReady": 99,
  "totalSent": 1
}
```

## Channel Configuration

⚠️ **Current Status:** Placeholder implementation

The `send_message()` function currently simulates sending. Real implementation requires:

1. **Channel setup:** Telegram, Signal, email, etc.
2. **Routing logic:** How to reach each prospect
3. **Rate limiting:** Don't spam (1 message/min recommended)

### OpenClaw Integration
Use `message` tool for actual sends:
```python
# Example: Send via OpenClaw message tool
# message(channel="telegram", target=prospect_handle, message=content)
```

## Safety Features

### Confirmation Required
Type "yes" to confirm sending. Prevents accidental sends.

### Dry Run Mode
`--dry-run` flag shows what would be sent without actual sends.

### Atomic Updates
Tracker only updates after successful sends. Failed sends preserve "ready" status.

## Error Handling

- **Missing tracker:** Exits with error
- **No ready messages:** Exits with error
- **Send failures:** Logged separately, tracker unchanged for failures

## Related Tools

- **service-batch-send.py:** Higher-level batch send tool (recommended)
- **service-outreach-tracker.py:** Tracker management
- **pipeline-snapshot.py:** Pipeline health check
- **response-tracker.py:** Track incoming replies

## Best Practices

1. **Preview first:** Always use `--dry-run` before actual sends
2. **Start small:** Send top 10 first, verify responses, then scale
3. **Check pipeline:** Run `pipeline-snapshot.py` before sending
4. **Track responses:** Use `response-tracker.py` to log replies
5. **Rate limit:** Don't send more than 60 messages/hour

## ROI Math

- **Top 10:** $580K potential value, ~10 minutes to send
- **All 100:** $1,979K potential value, ~45 minutes to send
- **Per minute:** $58K/min (top 10) to $44K/min (all)

## Example: Full Send Workflow

```bash
# 1. Check pipeline health
python3 tools/pipeline-snapshot.py

# 2. Preview top 10
python3 tools/send-service-messages.py --top 10 --dry-run

# 3. Send top 10
python3 tools/send-service-messages.py --top 10

# 4. Track responses (manual)
python3 tools/response-tracker.py add eigenlayer "interested, wants call"
```

## Notes

- This tool is the **execution layer** of the service outreach pipeline
- Build phase creates "ready" messages
- This tool converts them to "sent" messages
- Response handling is separate (use `response-tracker.py`)

## Version History

- **2026-02-03:** Created (execution engine for service outreach)
