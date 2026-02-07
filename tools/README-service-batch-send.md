# service-batch-send.py

Batch send multiple service outreach messages in one session.

## What It Does

Shows you which messages to send, in what order (highest value first), and generates copy-paste commands.

## Commands

```bash
# Show top 10 prospects (by value)
python3 tools/service-batch-send.py --top 10

# Show all prospects
python3 tools/service-batch-send.py --all

# Generate send commands (saves to tmp/send-commands.txt)
python3 tools/service-batch-send.py --commands 10
```

## Workflow

1. **Plan:** `service-batch-send.py --top 10` — See what to send
2. **Execute:** Copy message, paste into email/Discord, send
3. **Track:** `followup-tracker.py record ...` — Log the send

## Example Output

```
📋 SEND PLAN: Top 5 prospects
============================================================

1. Ethereum Foundation — $40,000
   File: outreach/messages/ethereum-foundation-agent-automation.md

2. Uniswap — $40,000
   File: outreach/messages/uniswap-devx-automation.md

...

💰 Total value: $187,500
⏱️  Estimated time: 10 minutes
```

## Generated Commands

When you run `--commands`, it creates a script like:

```bash
# Ethereum Foundation ($40,000)
cat outreach/messages/ethereum-foundation-agent-automation.md | pbcopy
# Paste into email and send
python3 tools/followup-tracker.py record "Ethereum Foundation" "service" 40000 "email"
```

## Integration

Works with:
- `followup-tracker.py` (record sends)
- `outreach/messages/*.md` (message files)
- `TODAY-SHIPPING-MANIFEST.md` (daily protocol)

## Sorting

Prospects sorted by **potential value** (highest first).

This ensures you send the most valuable messages first.

## Created

2026-02-06 — Work block 2544
