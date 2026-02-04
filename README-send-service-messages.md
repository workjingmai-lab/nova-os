# send-service-messages.py

## What It Does

Executes service outreach message sends based on Arthur's strategic choice.

## Usage

```bash
# Send top 10 by value (Tiered rollout - Option 3)
python3 tools/send-service-messages.py --top 10

# Send all ready messages (Batch send - Option 2)
python3 tools/send-service-messages.py --all

# Send specific batch
python3 tools/send-service-messages.py --batch 16

# Dry run (preview without sending)
python3 tools/send-service-messages.py --top 10 --dry-run
```

## How It Works

1. **Loads messages** from `service-outreach-tracker.json`
2. **Filters** for status="ready"
3. **Sorts** by value (high to low) if using --top
4. **Sends** each message via configured channel
5. **Updates** tracker with "sent" status and timestamp
6. **Reports** results (sent, failed, total value)

## Execution Options (from EXECUTE-PHASE-READY.md)

### Option 1: Manual Review & Send
Arthur reviews messages in `tmp/`, approves targets, Nova sends approved.

### Option 2: Batch Send (All 103)
```bash
python3 tools/send-service-messages.py --all
```
Sends all 103 messages in sequence.

### Option 3: Tiered Rollout (Recommended)
```bash
python3 tools/send-service-messages.py --top 10
```
Send top 10 first ($340K), monitor response rate, scale to remaining 93.

## Output

- Sends messages via configured channel (Telegram, Signal, email, etc.)
- Updates `service-outreach-tracker.json`:
  - status: "ready" → "sent"
  - sentAt: ISO timestamp
  - totalReady: Decrements
  - totalSent: Increments
- Prints summary: sent count, failed count, total value

## Notes

⚠️ **This script is a framework.** Actual sending logic depends on:
- Channel configuration (how to reach each prospect)
- Message routing (email vs. DM vs. contact form)
- Rate limiting (don't trigger spam filters)

Current implementation simulates sending. Real integration requires:
1. Channel setup (e.g., SMTP for email, API for DMs)
2. Prospect contact mapping (prospect → contact method)
3. Rate limiting (e.g., 1 message per minute)

## Arthur's Action

Before using this script:
1. ✅ Review `EXECUTE-PHASE-READY.md`
2. ✅ Choose execution option (1/2/3)
3. ✅ Give greenlight
4. ✅ (Optional) Configure channel settings
5. ✅ Run this script

## Example Output

```
📊 Loading messages...
   Total messages: 103
   Ready to send: 103
   Sending top 10: 10 messages
   - Ethereum Foundation: $40K
   - Fireblocks: $35K
   - Base (Coinbase L2): $30K
   - Coinbase: $30K
   - Uniswap Labs: $30K
   ... and 5 more

   Total value: $340K

⚠️  Ready to send!
   Type 'yes' to confirm: yes

🚀 Sending 10 messages...
[1/10]   📧 Sending to: Ethereum Foundation
[2/10]   📧 Sending to: Fireblocks
...
  ✅ Tracker updated

✅ Done!
   Sent: 10
   Failed: 0
```

## Related Tools

- `service-batch-send.py` — Alternative batch send implementation
- `service-outreach-tracker.py` — Track and manage pipeline
- `pipeline-snapshot.py` — Quick pipeline status view
- `EXECUTE-PHASE-READY.md` — Strategic decision document
