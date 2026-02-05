# velocity-calc.py

**Calculate and predict work block velocity metrics.**

## What It Does

Parses diary.md to extract work block history, calculates velocity (blocks/day, blocks/hour), and predicts when you'll hit milestones.

## Quick Start

```bash
python3 tools/velocity-calc.py
```

## Output Example

```
📊 Work Block Velocity
========================================
Current blocks: 1804
Avg blocks/day: 1804.0 (last 1 days)
Blocks/hour: 78.4
Trend: +0% (recent vs overall)

🎯 Milestone Predictions
========================================
2000 blocks: ~2 hours
2500 blocks: ~8 hours
5000 blocks: ~1 days
10000 blocks: ~4 days
```

## Metrics

- **Current blocks:** Latest block count from heartbeat state or max in diary
- **Avg blocks/day:** Average blocks per day (last 7 days or available)
- **Blocks/hour:** Assuming 23 workable hours/day (1 hour rest/maintenance)
- **Trend:** Percent change (recent 3 days vs overall 7 days)

## Milestones Predicted

- 2000 blocks (~2 hours from 1804)
- 2500 blocks (~8 hours)
- 5000 blocks (~1 day)
- 10000 blocks (~4 days)

## Use Cases

1. **Track progress** — See if velocity is increasing or decreasing
2. **Predict milestones** — Know when you'll hit 5K, 10K blocks
3. **Optimize schedule** — Adjust work hours based on actual velocity
4. **Motivation** — Visualize progress toward goals

## Data Source

Reads from:
- `diary.md` — Work block history by date
- `.heartbeat_state.json` — Current block count

## Integration

Run daily or weekly to track velocity trends:
```bash
# Daily check
python3 tools/velocity-calc.py

# Log to diary
python3 tools/velocity-calc.py >> diary.md
```

## Technical Notes

- Parses diary.md using regex: `## YYYY-MM-DD` and `Work Block NNNN`
- Calculates moving average (last 7 days)
- Trend compares last 3 days to overall 7-day average
- Assumes 23 workable hours/day (1 hour for rest/maintenance)

## Related Tools

- `revenue-tracker.py` — Revenue pipeline metrics
- `goal-tracker.py` — Goal completion tracking
- `daily-output-tracker.py` — Daily output visualization
