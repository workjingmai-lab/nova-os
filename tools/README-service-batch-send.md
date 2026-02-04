# service-batch-send.py — Execute Revenue Pipeline

## What It Does

Batch send your service outreach messages in one command:
- Top N prospects by value
- Tiered rollout (test → analyze → scale)
- Send entire pipeline at once
- Dry-run mode for testing

## Usage Examples

**Send top 10 prospects:**
```bash
python3 tools/service-batch-send.py --top 10
# Sends $305K worth of pipeline (top 10 by value)
```

**Tiered rollout (safe approach):**
```bash
python3 tools/service-batch-send.py --tiered
# Phase 1: Send top 25 ($585K)
# Wait 24h, analyze responses
# Phase 2: Send remaining 75 ($1,394K)
```

**Send all at once (bold):**
```bash
python3 tools/service-batch-send.py --all
# Sends 100 messages ($1,979K pipeline)
```

**Dry-run (preview mode):**
```bash
python3 tools/service-batch-send.py --top 10 --dry-run
# Shows what would be sent without sending
```

## Requirements

**Before sending:**
1. ✅ Pipeline populated (`revenue-pipeline.json`)
2. ✅ Messages ready (`tmp/service-outreach/*.md`)
3. ✅ Status = "ready" (not "sent" or "responded")
4. ✅ Send mechanism configured

**Verify pipeline:**
```bash
python3 tools/pipeline-snapshot.py
# Check: 100 ready → $1,979K → good to send
```

## Send Strategies

### Strategy 1: Top 10 ($305K)
**Best for:** Testing waters, low risk
```bash
python3 tools/service-batch-send.py --top 10
```
- Sends: Ethereum Foundation, Fireblocks, Alchemy, Infura, Circle, ConsenSys, Polygon, Solana, Arbitrum, Optimism
- Value: $305K
- Expected: 1-2 responses → 0-1 deals

### Strategy 2: Tiered Rollout ($585K → $1,979K)
**Best for:** Measured expansion, data-driven
```bash
python3 tools/service-batch-send.py --tiered
# Phase 1: Top 25 ($585K)
# Wait 24h, analyze responses
# Phase 2: Remaining 75 ($1,394K) if response rate > 10%
```

### Strategy 3: Send All ($1,979K)
**Best for:** Maximum pipeline, confident in quality
```bash
python3 tools/service-batch-send.py --all
```
- Sends: 100 messages
- Value: $1,979K
- Expected: 10-15 responses → 1-3 deals → $5K-$45K revenue

## Workflow

**Pre-send checklist:**
```bash
# 1. Verify pipeline
python3 tools/pipeline-snapshot.py

# 2. Preview what will be sent
python3 tools/service-batch-send.py --top 10 --dry-run

# 3. Send!
python3 tools/service-batch-send.py --top 10
```

**Post-send tracking:**
```bash
# Log responses as they arrive
python3 tools/response-tracker.py add --msg 001 --response interested

# Check response rates
python3 tools/response-tracker.py stats

# Review pipeline health
python3 tools/pipeline-snapshot.py
```

## ROI Math

| Strategy | Time | Pipeline | ROI/min |
|----------|------|----------|---------|
| Top 10 | 5 min | $305K | $61K/min |
| Tiered (Phase 1) | 12 min | $585K | $49K/min |
| All | 45 min | $1,979K | $44K/min |

**Blocker removal** (if needed):
- GitHub CLI auth: 5 min → $130K grants unlocked ($26K/min)
- Gateway restart: 1 min → $50K bounties unlocked ($50K/min)

## Integration

**Works with:**
- `pipeline-snapshot.py` — Pre-send verification
- `response-tracker.py` — Post-send tracking
- `outreach-tracker.py` — Lead management
- `revenue-pipeline.json` — Pipeline data

## Error Handling

**Exit codes:**
- `0` — Success
- `1` — Missing files or config
- `2` — No ready messages found
- `3` — Send failed (check logs)

**Common issues:**
- ❌ "No ready messages" → Check `revenue-pipeline.json` for `status: "ready"`
- ❌ "Missing file" → Verify message files exist in `tmp/service-outreach/`
- ❌ "Send failed" → Check message channel configuration

## Why This Matters

**Execution is where revenue happens.**
- 1,204 work blocks building → $0 (until now)
- 5-45 minutes sending → $1,979K pipeline activated

Build phase is preparation. Execute phase is activation.

**This tool = the activation button.**

---

**Created:** Work block 1176  
**Last updated:** 2026-02-03  
**Related tools:** pipeline-snapshot.py, response-tracker.py, outreach-tracker.py
