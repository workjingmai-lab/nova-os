# growth-predictor.py — Velocity & Trend Forecasting

**Purpose:** Predict growth trajectories based on historical work patterns

## Quick Start

```bash
# Predict week completion based on current velocity
python3 tools/growth-predictor.py week

# Show 7-day trend forecast
python3 tools/growth-predictor.py trend --days 7

# Estimate milestone reach date
python3 tools/growth-predictor.py milestone --target 1000

# Compare actual vs predicted
python3 tools/growth-predictor.py compare
```

## Metrics Tracked

- **Work block velocity** — Blocks per hour/day
- **Week completion** — Progress toward weekly goals
- **Milestone projection** — When will target be reached?
- **Trend analysis** — Acceleration or deceleration

## Output Examples

```
📊 Week Forecast (Feb 2-8)
Current: 523/300 (174%)
Velocity: 38 blocks/hour
Predicted: ~1,040 blocks by week end
Trend: 📈 Accelerating (+12% vs last week)
```

## Data Sources

- `diary.md` — Historical work logs
- `.heartbeat_state.json` — Velocity checkpoints
- `goals/week-*.md` — Target metrics

---

**Created:** 2026-02-02
**Usage:** Part of Nova's analytics toolkit
