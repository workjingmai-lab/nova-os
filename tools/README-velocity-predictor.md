# velocity-predictor.py

**Forecast near-term work block output based on historical velocity.**

## Overview

Analyzes diary.md work block history to calculate velocity (blocks/hour) and project future output. Quick-and-dirty forecasting for momentum awareness, not statistical precision.

## Usage

```bash
# Basic: Last 24h baseline, forecast next 24h
python3 tools/velocity-predictor.py

# Custom baseline window (e.g., last 6 hours)
python3 tools/velocity-predictor.py --hours 6

# Custom forecast horizon (e.g., next 12 hours)
python3 tools/velocity-predictor.py --next 12

# Both combined
python3 tools/velocity-predictor.py --hours 6 --next 12
```

## Output

```
📈 Velocity Predictor
Baseline window: last 24h
Recent blocks: 287 (from #1152 to #1438)
Estimated velocity: 44.23 blocks/hour
Forecast horizon: next 24h
Projected blocks: 1061.5
```

## How It Works

1. **Parses diary.md** — Extracts `[WORK BLOCK <n> — <iso8601>]` headers
2. **Calculates baseline** — Blocks in window / duration (hours)
3. **Projects future** — Velocity × forecast horizon = expected blocks

## Data Requirements

- `diary.md` must contain work blocks with ISO-8601 timestamps
- Minimum 2 blocks in baseline window for velocity calculation
- Handles both `Z` suffix (UTC) and naive timestamps (treated as UTC)

## Examples

```bash
# What's my velocity right now?
python3 tools/velocity-predictor.py --hours 1

# Can I hit 2000 blocks by tomorrow? (currently at 1500)
python3 tools/velocity-predictor.py --hours 24 --next 24
# If projected blocks > 500, you're on track

# Weekend planning — use last 7 days as baseline
python3 tools/velocity-predictor.py --hours 168 --next 48
```

## Notes

- **Velocity fluctuates** — Short windows (1-6h) are noisy; use 12-24h for stable baseline
- **Assumes consistent pace** — Doesn't account for breaks, priority shifts, or context switching
- **Quick reference only** — For rigorous forecasting, use work-pattern-analyzer.py

## Related Tools

- **block-counter.py** — Instant count of today's blocks
- **work-pattern-analyzer.py** — Deep dive into patterns, trends, anomalies
- **velocity-calc.py** — Calculate velocity for custom time ranges

## File Location

`/home/node/.openclaw/workspace/tools/velocity-predictor.py`
