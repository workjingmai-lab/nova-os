# growth-predictor.md — Predict Growth Trends & Milestones

**Version:** 1.0  
**Category:** Analytics / Forecasting  
**Created:** 2026-02-01

---

## What It Does

Predicts future milestones based on current velocity: work blocks, tools, documentation coverage, and more.

### Features

- Linear extrapolation from current data
- Milestone prediction (when will I hit X?)
- Velocity trend analysis
- Goal completion forecasting
- Scenario modeling (optimistic/pessimistic)
- Export predictions to reports

---

## Usage

```bash
# Predict when 1000 work blocks will be reached
python3 tools/growth-predictor.py work-blocks 1000

# Predict documentation completion
python3 tools/growth-predictor.py docs 112

# Show all predictions
python3 tools/growth-predictor.py all

# Optimistic scenario (20% faster)
python3 tools/growth-predictor.py work-blocks 1000 --scenario optimistic

# Generate report
python3 tools/growth-predictor.py report
```

---

## Prediction Types

| Type | Metric | Example |
|------|--------|---------|
| `work-blocks` | Total work blocks | When will I hit 1000? |
| `docs` | Documentation coverage | When will 112 tools be documented? |
| `tools` | Tools created | When will I have 150 tools? |
| `goals` | Goal completion | When will Week 2 be complete? |

---

## Scenarios

| Scenario | Velocity | Description |
|----------|----------|-------------|
| `current` | Current velocity | Based on last 7 days |
| `optimistic` | +20% | Best-case acceleration |
| `pessimistic` | -20% | Slowing down |
| `historical` | 30-day avg | Long-term trend |

---

## Output Example

```bash
$ python3 tools/growth-predictor.py work-blocks 1000

📊 GROWTH PREDICTION
────────────────────────────────────────────────────────────

Metric: Work Blocks
Current: 736 blocks
Target: 1000 blocks
Remaining: 264 blocks

Velocity (current): 38 blocks/hour
Prediction (current velocity): 6.9 hours

Scenarios:
  • Optimistic (+20%): 5.8 hours
  • Current: 6.9 hours
  • Pessimistic (-20%): 8.6 hours

Confidence: High (stable velocity)

Milestone: Feb 2, 2026 at 03:45 UTC (current velocity)
```

---

## Dependencies

- Python 3.7+
- `diary.md` for historical data
- `today.md` for current metrics

---

## Prediction Method

Uses linear extrapolation:
1. Calculate current velocity (metric/time)
2. Apply scenario modifier
3. Extrapolate to target: `remaining / velocity`

---

## Integration

- Pair with `velocity-calc.py` for velocity data
- Use `self-improvement-loop.py` to compare predictions vs. actual
- Feed into goal planning for realistic targets

---

## Tips

1. Use `historical` scenario for long-term predictions
2. Monitor prediction accuracy to refine models
3. Set targets based on realistic velocities
4. Re-run predictions weekly as velocity changes
5. Celebrate milestone achievements when predictions hit
