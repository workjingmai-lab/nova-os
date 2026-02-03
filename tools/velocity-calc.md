# velocity-calc.md — Calculate Work Block Velocity

**Version:** 1.0  
**Category:** Analytics / Metrics  
**Created:** 2026-02-01

---

## What It Does

Calculates work block velocity: blocks per hour, per day, and trends over time.

### Features

- Real-time velocity calculation
- Hourly/daily/weekly metrics
- Trend detection (accelerating/decelerating)
- Peak productivity windows
- Comparison to targets
- Historical data storage

---

## Usage

```bash
# Calculate current velocity
python3 tools/velocity-calc.py

# Show velocity by hour
python3 tools/velocity-calc.py --hourly

# Show weekly trend
python3 tools/velocity-calc.py --weekly

# Compare to target
python3 tools/velocity-calc.py --target 40

# Export historical data
python3 tools/velocity-calc.py --export velocity-2026-02-02.json
```

---

## Metrics

| Metric | Description | Formula |
|--------|-------------|---------|
| **Current Velocity** | Blocks/hour (last hour) | blocks_last_hour |
| **Daily Velocity** | Blocks/day (today) | blocks_today / hours_today |
| **Weekly Velocity** | Blocks/day (7-day avg) | blocks_week / 7 |
| **Trend** | Acceleration | (velocity_now - velocity_yesterday) |
| **Peak Window** | Most productive hour | hour with max blocks |

---

## Output Example

```bash
$ python3 tools/velocity-calc.py

📊 VELOCITY METRICS
────────────────────────────────────────────────────────────

Current Velocity: 38 blocks/hour
Daily Average: 32 blocks/hour
Weekly Average: 29 blocks/hour

Trend: ↗️ +6 from yesterday (accelerating)

Peak Window: 14:00-16:00 UTC (45 blocks/hour)

Target: 40 blocks/hour
Status: 95% of target

Historical:
  Feb 1: 28 blocks/hour
  Feb 2: 32 blocks/hour
  Today: 38 blocks/hour
```

---

## Dependencies

- Python 3.7+
- `diary.md` for work block timestamps

---

## Data Storage

Historical velocity stored in `.velocity-history.json`:

```json
{
  "2026-02-02": {
    "hourly": [30, 35, 40, 38, 42],
    "daily_avg": 37,
    "peak_hour": 14
  }
}
```

---

## Integration

- Pair with `agent-productivity-score.py` for composite metrics
- Use `work-block-miner.py` for pattern analysis
- Feed into `self-improvement-loop.py` for trend insights

---

## Tips

1. Track velocity at different times to find your peak
2. Use trend data to adjust daily schedules
3. Set realistic targets based on weekly averages
4. Monitor for burnout (sustained low velocity)
5. Celebrate velocity milestones (40+ blocks/hour)
