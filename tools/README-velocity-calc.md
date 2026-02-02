# Velocity Calculator

Quick work block metrics — measure your execution velocity in blocks per hour.

## Features

- **Instant metrics** — Current velocity from diary.md logs
- **Multiple views** — Today, weekly, or all-time summaries
- **Core metrics** — Blocks per hour, avg block time, duration
- **Timezone-aware** — Handles UTC timestamps correctly

## Usage

```bash
# Show all-time metrics
python3 tools/velocity-calc.py

# Weekly summary
python3 tools/velocity-calc.py --week

# Total (same as default)
python3 tools/velocity-calc.py --total
```

## Example Output

```
📊 Velocity Metrics

Total Work Blocks: 576
Duration: 3456 minutes
Velocity: 10.0 blocks/hour
Avg Block Time: 6.0 minutes

First Block: 2026-01-26 08:00
Last Block: 2026-02-02 13:19
```

## Metrics Explained

- **Total Work Blocks** — Total blocks logged in diary.md
- **Duration** — Time span from first to last block (minutes)
- **Velocity** — Blocks completed per hour (throughput)
- **Avg Block Time** — Average time per block (inverse of velocity)

## Use Cases

1. **Daily check-ins** — Track today's velocity
2. **Weekly reviews** — Compare weekly averages
3. **Optimization** — Identify peak velocity periods
4. **Goal tracking** — Correlate velocity with goal completion

## Data Source

Reads from `diary.md` and parses entries in this format:

```
[WORK BLOCK 500 — 2026-02-02T13:20Z]
```

## Integration

Pairs with:
- `velocity-check.py` — For detailed velocity analysis
- `self-improvement-loop.py` — For velocity trends over time
- `diary-digest.py` — For pattern analysis

## Created

2026-02-02 — Core metric tool for continuous improvement
