# velocity-calc.py — Work Block Metrics

Quickly calculate velocity metrics from your diary.md work blocks.

## What It Does

 Parses your diary.md for `[WORK BLOCK X — timestamp]` entries and calculates:
- Total work blocks completed
- Duration (first to last block)
- Velocity (blocks per hour)
- Average block time

## Usage

```bash
# Today's metrics (all blocks in diary)
python3 tools/velocity-calc.py

# Last 7 days only
python3 tools/velocity-calc.py --week
```

## Example Output

```
📊 Velocity Metrics

Total Work Blocks: 527
Duration: 7214 minutes
Velocity: 4.4 blocks/hour
Avg Block Time: 13.7 minutes

First Block: 2026-02-01 09:07
Last Block: 2026-02-02 12:30
```

## Why It Matters

Velocity is your productivity pulse. Track it to:
- Spot slowdowns (decision fatigue, blockers)
- Compare days (what worked better?)
- Calibrate estimates (how long will X take?)
- Celebrate progress (500 blocks = ~50 hours of focused work)

## Integration

Used by: `self-improvement-loop.py` for automated velocity tracking and insights.

## See Also

- `block-counter.py` — Raw block count
- `diary-digest.py` — Daily summaries
- `self-improvement-loop.py` — Automated velocity + insights
