# velocity-predictor.py

Forecast near-term work block output based on recent velocity.

## What It Does

`velocity-predictor.py` analyzes your recent work block rate and projects how many blocks you'll complete in the next N hours. Quick-and-dirty forecasting, not statistical rigor.

## Usage

```bash
# Default: 24h baseline, 24h forecast
python3 tools/velocity-predictor.py

# Custom baseline (last 6 hours)
python3 tools/velocity-predictor.py --hours 6

# Custom forecast horizon (next 12 hours)
python3 tools/velocity-predictor.py --next 12

# Both: last 12h baseline, predict next 48h
python3 tools/velocity-predictor.py --hours 12 --next 48
```

## Example Output

```bash
$ python3 tools/velocity-predictor.py

📈 Velocity Predictor
Baseline window: last 24h
Recent blocks: 142 (from #586 to #728)
Estimated velocity: 5.92 blocks/hour
Forecast horizon: next 24h
Projected blocks: 142.1
```

## How It Works

1. **Parse diary.md** — Extract `[WORK BLOCK N — ISO8601]` headers
2. **Filter baseline window** — Only blocks in last N hours
3. **Calculate velocity** — Blocks ÷ hours between first and last block
4. **Project output** — Velocity × forecast horizon

## Diary Format Required

Expects work blocks in this format:

```markdown
[WORK BLOCK 728 — 2026-02-02T20:10Z]
```

Timestamps must be ISO-8601 (with or without trailing `Z`).

## Use Cases

- **Goal planning** — "Can I hit 300 blocks this week?"
- **Deadline estimation** — "When will I finish the documentation sprint?"
- **Reality check** — Is current velocity sustainable?
- **Schedule optimization** — How much can I get done by Friday?

## Why This Matters

**Forecasting beats guessing.**

Instead of "I think I can do it," you have data: "At 5.9 blocks/hour, I'll finish in 24 hours." This helps:

- **Set realistic goals** — Based on actual output, not hopes
- **Detect velocity changes** — Compare 6h vs 24h vs 48h windows
- **Plan ahead** — Know what's achievable in the next day/week

## Limitations

- **Linear projection** — Assumes constant velocity (no burnout, no flow states)
- **Requires data** — Needs 2+ blocks in baseline window
- **No time-of-day awareness** — Doesn't account for peak hours
- **Quick-and-dirty** — Not statistically rigorous

## Better Together

Pair with other analytics tools:

- `work-pattern-analyzer.py` — Find your peak hours
- `self-improvement-loop.py` — Velocity tracking with insights
- `goal-tracker.py` — Set goals based on realistic projections

## Tips

- **Use shorter baselines (6-12h)** for recent velocity changes
- **Use longer baselines (24-48h)** for stable, long-term estimates
- **Compare multiple windows** (`--hours 6` vs `--hours 24`) to detect trends

## See Also

- `self-improvement-loop.py` — Advanced velocity tracking
- `work-block-miner.py` — Extract insights from work patterns
- `velocity-check.py` — Quick count of today's completed tasks

---

**Version:** 1.0  
**Created:** 2026-02-01  
**Category:** Analytics / Forecasting
