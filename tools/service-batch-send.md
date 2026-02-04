# service-batch-send.py

## What It Does

Batch sends service outreach messages to prospects. Loads ready messages from the pipeline, sorts by value, and sends them in batches with safety controls (dry-run, tiered rollout, resume capability).

## How It Works

1. **Load pipeline** from `service-outreach-tracker.json`
2. **Filter ready** — Only messages with `status="ready"`
3. **Sort by value** — Highest pipeline value first
4. **Load message files** from `tmp/service-outreach/` directory
5. **Send in batches** — Top N, tiered rollout, or all at once
6. **Update tracker** — Change status from `ready` → `sent`

## Usage

```bash
# Send top 10 messages (highest value)
python3 tools/service-batch-send.py --top 10

# Send top 25 messages (tiered rollout)
python3 tools/service-batch-send.py --tiered

# Send all ready messages
python3 tools/service-batch-send.py --all

# Dry run (show what would be sent)
python3 tools/service-batch-send.py --top 10 --dry-run

# Resume from message N (after interruption)
python3 tools/service-batch-send.py --top 10 --from 5
```

## Output Modes

**Top N:**
```
📊 Ready messages: 25/100
💰 Top 10 by value: $305K total

📤 Sending to: Acme Corp ($50K)
   File: tmp/service-outreach/acme-corp.md
   Status: ✅ Sent

📤 Sending to: TechStart ($30K)
   File: tmp/service-outreach/techstart.md
   Status: ✅ Sent
[...]
✅ Sent 10/10 messages successfully
```

**Tiered Rollout:**
```
📊 Tiered Rollout Plan
────────────────────────────────────────────────────────────
Batch 1 (now):     25 messages  → $305K
Batch 2 (24h):     25 messages  → $280K  (after response analysis)
Batch 3 (48h):     Remaining    → $1,394K

Sending Batch 1...
✅ Sent 25/25 messages successfully
⏰ Next batch in 24 hours (analyze responses first)
```

**Dry Run:**
```
📊 Ready messages: 25/100
💰 Top 10 by value: $305K total

📤 [DRY-RUN] Would send to: Acme Corp ($50K)
📤 [DRY-RUN] Would send to: TechStart ($30K)
[...]
✅ Dry run complete — 10 messages ready to send
```

## Safety Features

- **Dry-run mode** — Preview what would be sent without actually sending
- **Tiered rollout** — Send 25 → wait 24h → analyze responses → send remaining
- **Resume capability** — `--from N` resumes from message N if interrupted
- **Value sorting** — Highest value prospects first
- **Status tracking** — Updates tracker from `ready` → `sent`

## Requirements

- **Pipeline tracker:** `service-outreach-tracker.json` must exist
- **Ready messages:** Messages must have `status="ready"`
- **Message files:** Each message must have a file in `tmp/service-outreach/`
- **Send mechanism:** Message channel configured (integration TODO in script)

## Exit Codes

- `0` — Success (all messages sent)
- `1` — Missing files or configuration
- `2` — No ready messages found
- `3` — Send failed (one or more messages failed to send)

## Batch Strategy

**Top N (recommended):**
- Send top 10-25 highest-value prospects first
- Monitor response rate for 24-48h
- Adjust messaging based on feedback
- Continue with next batch

**Tiered Rollout (cautious):**
- Batch 1: 25 messages now
- Wait 24h, analyze response rate
- If response rate > 20%, send Batch 2
- If response rate < 10%, adjust messaging first

**All At Once (aggressive):**
- Send all ready messages simultaneously
- Highest velocity, lowest control
- Recommended only after messaging is validated

## Message File Format

Each message file (`tmp/service-outreach/prospect-name.md`):
```markdown
# Outreach Message for Prospect

## Pain Point
[Specific pain point identified]

## Solution
[How Nova's services solve it]

## Proof
[Case studies, examples]

## Pricing
[Price range]

## CTA
[Call to action]
```

## Tracker Format

`service-outreach-tracker.json`:
```json
{
  "messages": [
    {
      "prospect": "Acme Corp",
      "status": "ready",
      "pipeline_value": 50,
      "file": "tmp/service-outreach/acme-corp.md",
      "created": "2026-02-03T10:00:00Z"
    }
  ]
}
```

## When to Use It

- **Weekly outreach campaigns** — Send batch of 10-25 messages
- **Pipeline execution** — Send all ready messages (0 blockers = $2,057K)
- **A/B testing** — Send small batch, analyze, iterate
- **Response rate optimization** — Tiered rollout with analysis between batches

## Integration

```bash
# 1. Generate messages (outreach-tracker.py)
python3 tools/outreach-tracker.py --generate

# 2. Review and edit message files
# Edit files in tmp/service-outreach/

# 3. Set status to "ready" in tracker
python3 tools/outreach-tracker.py --set-ready acme-corp

# 4. Send batch
python3 tools/service-batch-send.py --top 10

# 5. Monitor responses
python3 tools/execution-dashboard.py
```

## Next Actions After Sending

1. **Monitor response rate** — Use `execution-dashboard.py`
2. **Update tracker** — Change `sent` → `responded` when replies arrive
3. **Adjust messaging** — If response rate < 10%, revise templates
4. **Send next batch** — Wait 24-48h, then send next 10-25

## See Also

- `outreach-tracker.py` — Generate and track outreach messages
- `execution-dashboard.py` — Monitor response rates
- `revenue-tracker.py` — Track all revenue opportunities
- `next-actions.py` — ROI-ranked task list (services = $2,057K ready)
