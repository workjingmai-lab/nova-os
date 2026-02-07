# Daily Revenue Dashboard

One-command revenue pipeline health check for operators.

## What It Does

Shows your entire revenue pipeline status at a glance:
- Total pipeline value
- Ready vs submitted amounts
- Execution gap percentage
- Category breakdown (grants, services, bounties)
- Active blockers
- Next actions

## Usage

```bash
# Full dashboard (pretty-printed)
python3 tools/daily-revenue-dashboard.py

# Mini dashboard (one-line status)
python3 tools/daily-revenue-dashboard.py --mini
python3 tools/daily-revenue-dashboard.py -m
```

## Output Examples

### Full Mode
```
╔══════════════════════════════════════════════════════════╗
║          DAILY REVENUE DASHBOARD                      ║
╚══════════════════════════════════════════════════════════╝
📅 2026-02-06 23:20Z | 🧱 2897 work blocks

💰 PIPELINE OVERVIEW
──────────────────────────────────────────────────────────
  Total Pipeline:     $1.5M
  Ready to Submit:    $734K
  Submitted:          $5K
  Execution Gap:      99.3%

📊 CATEGORY BREAKDOWN
──────────────────────────────────────────────────────────

  GRANTS ($130K)
    Status: ready
    Ready: $125K | Sent: $5K
    ⚠️  Blocker: GitHub CLI auth needed (5 min → $125K unblocked)

  SERVICES ($1.3M)
    Status: ready
    Ready: $610K | Sent: $0

  BOUNTIES ($50K)
    Status: blocked
    Ready: $0 | Sent: $0
    ⚠️  Blocker: Browser access (needs gateway restart)

🎯 NEXT ACTIONS
──────────────────────────────────────────────────────────
  ⚠️  High execution gap! Run: bash tools/send-everything.sh full
  🔓 Unblock grants: GitHub CLI auth needed (5 min → $125K unblocked)
  📈 Track: python3 tools/revenue-tracker.py status
  📝 Diary: cat diary.md | tail -20

✨ Small executions compound. Keep building.
```

### Mini Mode
```
📊 2917 blocks | $1,490,065 pipeline | 734,500 ready | 5,000 sent | 99.3% gap
```

## Data Sources

- `revenue-pipeline.json` — Pipeline data
- `diary.md` — Work block count (extracts latest block number)

## Metrics Explained

### Execution Gap
Percentage of "ready to submit" revenue that hasn't been sent yet.

Formula: `((Ready - Submitted) / Ready) × 100`

- **< 20%**: Healthy, good shipping velocity
- **20-50%**: Room for improvement
- **> 50%**: Critical zone, prioritize sending

### Category Status
- **ready**: No blockers, can send immediately
- **blocked**: Has active blocker preventing execution
- **submitted**: Sent, awaiting response

## Integration

Add to your daily routine:
```bash
# Morning check
python3 tools/daily-revenue-dashboard.py

# Before sending messages
python3 tools/daily-revenue-dashboard.py && bash tools/send-everything.sh full

# Quick status between tasks
python3 tools/daily-revenue-dashboard.py -m
```

## Why It Matters

**Builders** focus on: "How much pipeline can I build?"
**Operators** focus on: "How much pipeline can I ship?"

This dashboard is for operators. It answers the question:
"What's my revenue right now, and what's blocking me from shipping more?"

## Related Tools

- `revenue-tracker.py` — Detailed pipeline tracking and management
- `send-everything.sh` — Batch send all ready messages
- `execution-gap.py` — Calculate execution gap percentage

## Created

Work block 2915 — 2026-02-06 23:22Z
