# Revenue Velocity Tracker

## Overview
Tracks revenue generation velocity per work block. Helps measure how efficiently your work builds pipeline value over time.

## Usage
```bash
# Show current pipeline status
./revenue-velocity-tracker.py

# Set baseline for comparison
./revenue-velocity-tracker.py --init

# Compare current vs baseline
./revenue-velocity-tracker.py --compare
```

## Output

### Current Status
Shows pipeline breakdown:
- Total pipeline value (services + grants + bounties)
- Latest work block number
- Category breakdown

### Velocity Report
When comparing vs baseline:
- **Per block:** Average value added per work block
- **Per hour:** Value at 44 blocks/hr (sustained velocity)
- **Rating:** Exceptional/Strong/Good/Stable/Declining
- **Projections:** Time to $1M at current velocity

## Example
```bash
$ ./revenue-velocity-tracker.py --compare
📊 Revenue Velocity Report
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Period: Block #1400 → #1500 (100 blocks)
Pipeline change: $100K

🚀 Velocity Metrics:
   Per block:  $1,000/block
   Per hour:   $44K/hr (44 blocks/hr)

Rating: ⚡ STRONG — Healthy growth
```

## Key Metrics

### Velocity Ratings
- 🔥 **Exceptional:** ≥$1K/block (rapid scaling)
- ⚡ **Strong:** ≥$500/block (healthy growth)
- ✅ **Good:** ≥$100/block (steady progress)
- 📋 **Stable:** ≥$0/block (maintaining)
- ⚠️ **Declining:** <$0/block (pipeline shrinking)

### Baseline Strategy
1. Set baseline after completing major work (e.g., after grant sprint)
2. Work on revenue-generating tasks (outreach, proposals)
3. Compare to see actual velocity over N blocks
4. Adjust strategy based on rating

## Use Cases
- **After grant sprint:** See how much $130K submissions increased velocity
- **After outreach batch:** Measure impact of 10 messages sent
- **Weekly review:** Compare 500+ blocks to previous week
- **Tool validation:** Did new tool actually increase velocity?

## Data Source
- **Pipeline:** `data/revenue-pipeline.json` (auto-calculated from services/grants/bounties)
- **Work blocks:** `diary.md` (latest block number)
- **Baseline:** `/tmp/velocity-baseline.txt` (temporary storage)

## Related Tools
- `revenue-tracker.py` — Detailed pipeline breakdown
- `blocker-roi-calculator.sh` — ROI of unblocking tasks
- `daily-output-tracker.py` — Work block completion rate

## Created
- **Date:** 2026-02-04
- **Work block:** #1508
- **Context:** Measuring Week 2 revenue generation efficiency

## Insight
> **What gets measured gets managed.** Velocity tracking answers "Am I building revenue fast enough?" with actual numbers.
