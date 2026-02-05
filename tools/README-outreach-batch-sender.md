# Outreach Batch Sender — Quick Reference

**Purpose:** Rapidly review and send prepared outreach messages in batches

**When to use:**
- Service outreach campaigns (42 messages, $424.5K ready)
- Prioritizing HIGH/MEDIUM/LOW leads
- Batch sending (5-10 messages per session)

---

## Quick Start

```bash
# List all messages (grouped by priority)
python3 tools/outreach-batch-sender.py

# Show HIGH priority only
python3 tools/outreach-batch-sender.py --high

# Show MEDIUM priority only
python3 tools/outreach-batch-sender.py --medium

# Show in batches of 5
python3 tools/outreach-batch-sender.py --batch 5

# Interactive mode (read each message)
python3 tools/outreach-batch-sender.py --interactive
```

---

## Priority Levels

**HIGH** ($115K total):
- Ethereum Foundation ($40K)
- Uniswap DevX ($40K)
- Fireblocks Security ($35K)

**MEDIUM** ($190K total):
- Alchemy, Infura, Lido, Compound, Aave, Optimism, etc.

**LOW/DAOs** ($117.5K total):
- Balancer, Curve, Yearn, Gitcoin, etc.

---

## Execution Workflow

### Step 1: Review Messages
```bash
python3 tools/outreach-batch-sender.py --high
```
→ See all HIGH priority messages with values

### Step 2: Read Message Content
```bash
python3 tools/outreach-batch-sender.py --interactive
```
→ Read each message in full, press Enter to continue

### Step 3: Send Messages
1. Open message file: `outreach/messages/ethereum-foundation-agent-automation.md`
2. Customize lightly (add specific context)
3. Send via appropriate platform (email, Discord, Telegram)
4. Track in revenue-tracker.py

### Step 4: Track Submission
```bash
python3 tools/revenue-tracker.py update --category services --status submitted --name "Ethereum Foundation" --message "Sent via email"
```

---

## Expected Results

**Input:** 42 messages sent
**Expected:** 28% response rate → 12 responses
**Conversion:** 10-20% → 2-3 contracts
**Revenue:** $40K-$115K

---

## Integration with Revenue Tracker

After sending, update the pipeline:
```bash
python3 tools/revenue-tracker.py update \
  --category services \
  --status submitted \
  --name "Ethereum Foundation" \
  --message "Sent outreach to ecosystem-support@ethereum.org"
```

---

## Common Mistakes

❌ **Send all at once** — Spread out over 2-3 days
❌ **No customization** — Add 1-2 specific insights per message
❌ **Forget tracking** — Update revenue-tracker.py immediately
❌ **One-and-done** — Follow up on Day 3/7/14/21

---

## Files

- Tool: `tools/outreach-batch-sender.py`
- Messages: `outreach/messages/*.md` (42 files)
- Tracker: `data/revenue-pipeline.json`

---

*Created: 2026-02-05 — Work block 1788*
*Pipeline: $424.5K services ready | 42 messages | 28% expected response*
