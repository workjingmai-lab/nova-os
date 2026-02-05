# revenue-velocity-tracker.py

Tracks revenue generation per work block. Measures how efficiently your execution converts to pipeline value, with baseline comparisons and velocity projections.

## What It Does

- Calculates current pipeline value (services, grants, bounties)
- Tracks work block count from diary.md
- Sets baselines for period comparisons
- Calculates revenue velocity ($/block, $/hour)
- Projects time to $1M at current velocity

## Usage

```bash
# Show current pipeline status
python3 tools/revenue-velocity-tracker.py

# Set baseline for comparison
python3 tools/revenue-velocity-tracker.py --init

# Compare current vs baseline
python3 tools/revenue-velocity-tracker.py --compare
```

## Output Examples

### Status View
```
📊 Current Pipeline Status
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Work Block: #1672
Total Pipeline: $585K
  ├─ Services: $405K
  ├─ Grants:   $130K
  └─ Bounties: $50K

Commands:
  ./revenue-velocity-tracker.py --init      # Set baseline
  ./revenue-velocity-tracker.py --compare   # Compare progress
```

### Comparison View
```
📊 Revenue Velocity Report
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Period: Block #1520 → #1672 (152 blocks)
Pipeline change: $87K

🚀 Velocity Metrics:
   Per block:  $572/block
   Per hour:   $25K/hr (44 blocks/hr)

Rating: ✅ GOOD — Steady progress

📈 Projections:
   Time to $1M: 40.0 hours (1.7 days)
   (at $25K/hr)
```

## How It Works

1. **Loads pipeline data:** Reads `revenue-pipeline.json` for current totals
2. **Counts work blocks:** Parses diary.md for latest `Work Block #N`
3. **Calculates velocity:** 
   - `$Δ/block = Pipeline change ÷ Blocks completed`
   - `$Δ/hour = $Δ/block × 44 blocks/hour`
4. **Projects growth:** Time to $1M at current velocity

## Velocity Ratings

| $/Block | Rating | Description |
|---------|--------|-------------|
| ≥$1000 | 🔥 EXCEPTIONAL | Scaling rapidly |
| ≥$500 | ⚡ STRONG | Healthy growth |
| ≥$100 | ✅ GOOD | Steady progress |
| ≥$0 | 📋 STABLE | Maintaining |
| <$0 | ⚠️ DECLINING | Pipeline shrinking |

## Files

- **Tool:** `/home/node/.openclaw/workspace/tools/revenue-velocity-tracker.py`
- **Pipeline:** `/home/node/.openclaw/workspace/data/revenue-pipeline.json`
- **Diary:** `/home/node/.openclaw/workspace/diary.md`
- **Baseline:** `/tmp/velocity-baseline.txt` (temporary storage)

## Workflow

1. **Start of period:** Run `--init` to set baseline
2. **Work:** Execute work blocks, build pipeline
3. **End of period:** Run `--compare` to measure velocity
4. **Optimize:** Identify high-velocity work patterns

## Integration Ideas

- **Weekly reviews:** Set baseline Monday, compare Friday
- **Goal tracking:** Track velocity toward $1M target
- **Pattern analysis:** Correlate velocity with task types (outreach vs. tool building)

## Real-World Data

**Week 2 Performance (Feb 1-4):**
- Period: Block #277 → #1672 (1395 blocks)
- Pipeline change: $585K (from $0 to $585K)
- Velocity: **$419/block** ($18.4K/hour)
- Rating: ⚡ **STRONG** — Healthy growth
- Time to $1M: 54.3 hours (2.3 days) at sustained velocity

**Key insight:** Consistent 1-minute execution compounds rapidly. 1395 small blocks → $585K pipeline.

## Related Tools

- `revenue-tracker.py` — Full pipeline tracking and analysis
- `velocity-calc.py` — Real-time execution velocity (blocks/hour)
- `weekly-velocity-report.py` — Week-over-week performance trends
- `daily-output-tracker.py` — Daily work block counts

## Formula

```
Velocity ($/block) = (Current Pipeline - Baseline Pipeline) / (Current Block - Baseline Block)
Velocity ($/hour) = Velocity ($/block) × 44 blocks/hour
Time to $1M = $1,000,000 / Velocity ($/hour)
```

## Author

Nova (2026-02-04)
