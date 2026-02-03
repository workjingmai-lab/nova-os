# velocity-calc.py — Work Block Velocity Calculator

## What It Does

Calculates performance metrics from your work block history:
- Total work blocks completed
- Duration covered
- Velocity (blocks per hour)
- Average time per block
- First/last block timestamps

## When to Use It

- **Daily check-ins:** See today's velocity at a glance
- **Weekly reviews:** Track velocity trends over time
- **Performance analysis:** Identify productivity patterns

## Installation

No dependencies needed. Uses Python stdlib only.

```bash
# Already in workspace/tools/
chmod +x tools/velocity-calc.py
```

## Usage

```bash
# All-time metrics (default)
python3 tools/velocity-calc.py

# Last 7 days only
python3 tools/velocity-calc.py --week

# Total summary
python3 tools/velocity-calc.py --total
```

## Output Format

```
📊 Velocity Metrics

Total Work Blocks: 670
Duration: 2832 minutes
Velocity: 14.2 blocks/hour
Avg Block Time: 4.2 minutes

First Block: 2026-01-31 09:00
Last Block: 2026-02-02 18:54
```

## How It Works

1. **Parses diary.md** for work block entries: `[WORK BLOCK N — timestamp]`
2. **Filters by timeframe** (all-time, weekly, daily)
3. **Calculates metrics:**
   - Total blocks: Count of matched entries
   - Duration: Time span from first to last block
   - Velocity: `blocks / (duration / 60)`
   - Avg block time: `duration / blocks`
4. **Formats output** with clean, readable layout

## Data Sources

- **Input:** `diary.md` (your daily work log)
- **Output:** Formatted metrics to stdout
- **Pattern:** `[WORK BLOCK (\d+) — ([^\]]+)\]`

## Metric Definitions

- **Velocity:** Work blocks completed per hour (higher = faster)
- **Avg Block Time:** Minutes per work block (lower = faster)
- **Duration:** Time span from first to last block in dataset

## Integration Examples

```bash
# Track weekly velocity trends
echo "=== Weekly Velocity ===" >> weekly-report.txt
python3 tools/velocity-calc.py --week >> weekly-report.txt

# Daily performance check
alias vcheck="python3 tools/velocity-calc.py"
vcheck  # Quick status

# Compare with goals
TARGET=30
ACTUAL=$(python3 tools/velocity-calc.py --week | grep "Velocity:" | awk '{print $2}')
if (( $(echo "$ACTUAL < $TARGET" | bc -l) )); then
  echo "⚠️ Below target velocity"
fi
```

## Error Handling

- Gracefully handles missing diary.md
- Skips malformed work block entries
- Returns zero values if no blocks found

## Performance Notes

- Parses entire diary.md on each run
- Efficient regex extraction
- Suitable for daily use, not real-time monitoring

## Maintenance Notes

- **Last updated:** 2026-02-02
- **Dependencies:** None (stdlib only)
- **Pattern:** Matches `[WORK BLOCK N — timestamp]` format
- **Timezone:** Handles UTC (Z suffix) and naive datetimes

## See Also

- `self-improvement-loop.py` — Advanced velocity analysis with insights
- `goal-tracker.py` — Progress tracking against targets
- `pattern-analyzer.py` — Trend detection across metrics

---

**Created:** 2026-02-02
**Category:** Analytics
**Status:** ✅ Production-ready
