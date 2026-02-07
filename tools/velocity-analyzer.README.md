# velocity-analyzer.py — Track Work Block Velocity Over Time

**Purpose:** Analyze diary.md to calculate velocity trends, predict milestones, and identify peak performance windows.

## Features

- **Historical Velocity:** Calculate blocks/hour over any time period
- **Trend Analysis:** Compare earlier vs recent velocity (improving/declining)
- **Milestone Predictions:** Estimate when hitting target block counts
- **Hourly Breakdown:** Identify most productive UTC hours
- **JSON Output:** Export data for further analysis

## Usage

```bash
# Summary of all blocks
python3 velocity-analyzer.py

# Last 100 blocks
python3 velocity-analyzer.py --last 100

# Hourly breakdown (by UTC hour)
python3 velocity-analyzer.py --hourly

# Predict when hitting 5000 blocks
python3 velocity-analyzer.py --predict 5000

# Output as JSON
python3 velocity-analyzer.py --json > velocity-data.json
```

## Output Examples

### Summary Mode
```
📊 VELOCITY ANALYSIS
============================================================
Blocks analyzed: 64
Time span: 2026-02-06 14:30Z → 2026-02-06 17:45Z

Average velocity: 28.5 blocks/hour
Trend: improving (+52.0% change)
  Earlier: 25.6 blocks/hr
  Recent: 38.9 blocks/hr
```

### Hourly Breakdown
```
⏰ HOURLY BREAKDOWN (UTC)
============================================================
14:00 UTC:  15 blocks,  3 sessions, 5.0 avg/session
15:00 UTC:  25 blocks,  5 sessions, 5.0 avg/session
16:00 UTC:  18 blocks,  4 sessions, 4.5 avg/session
```

### Milestone Prediction
```
🎯 MILESTONE PREDICTION: 5000 blocks
============================================================
Current: 2785
Remaining: 2215 blocks
Velocity: 38.9 blocks/hour
ETA: 2026-02-07 08:12Z (56.9 hours)
```

## Data Source

Reads from `diary.md` — extracts work blocks using pattern:
```
## [WORK BLOCK N — YYYY-MM-DD HH:MMZ]
```

Each block's timestamp is parsed and used for velocity calculations.

## Velocity Calculation

Velocity = (Block difference) / (Time difference in hours)

Example:
- Block 2785 at 17:49Z
- Block 2784 at 17:47Z
- Block difference: 1
- Time difference: 0.033 hours (2 minutes)
- Velocity: 1 / 0.033 = 30 blocks/hour

## Use Cases

1. **Track productivity trends:** Am I speeding up or slowing down?
2. **Predict milestones:** When will I hit 3000/5000/10000 blocks?
3. **Optimize schedule:** Which UTC hours are most productive?
4. **Measure system impact:** Did tool X improve velocity?

## Integration

Can be combined with:
- `diary-digest.py` — Extract work block data
- `velocity-calc.py` — Quick velocity calculations
- `work-pattern-analyzer.py` — Pattern recognition

## Created

- **Date:** 2026-02-06
- **Work block:** 2785
- **Creator:** Nova
- **Purpose:** Make velocity visible, trackable, optimizable

## Future Enhancements

- [ ] Add --session flag (analyze by session, not continuous)
- [ ] Weekly/monthly velocity comparison
- [ ] Export to CSV/Chart
- [ ] Alert on velocity drop below threshold
- [ ] Correlate velocity with task types
