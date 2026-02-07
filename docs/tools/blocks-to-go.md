# Blocks To Go — Milestone Progress Check

Quick progress check showing blocks remaining to 2000 milestone with ETA projections at different velocities.

## What It Does

- Reads diary.md to find current work block count
- Calculates blocks remaining to 2000 milestone
- Shows ETA at 3 velocities: sustained (44/hr), burst (55/hr), current (67/hr)

## Usage

```bash
python3 tools/blocks-to-go.py
```

## Output Example

```
🎯 2000-Block Milestone Progress
==================================================
Current: 2860 blocks (143.00%)
Target: 2000 blocks
Remaining: -860 blocks

📊 Velocity Scenarios:
  Sustained (44/hr): -19.5hr → ~00:10 UTC
  Burst (55/hr):     -15.6hr → ~04:05 UTC
  Current (67/hr):   -12.8hr → ~06:53 UTC

💪 Keep going! -860 blocks to milestone!
```

## Data Source

Reads from `/home/node/.openclaw/workspace/diary.md` and looks for pattern:
```
WORK BLOCK NNNN —
```
Uses the most recent (highest) block number found.

## Velocities

| Velocity | Type | Description |
|----------|------|-------------|
| 44 blocks/hr | Sustained | Proven long-term average |
| 55 blocks/hr | Burst | Task randomizer + focus |
| 67 blocks/hr | Current | Cron session velocity |

**Note:** Current velocity (67/hr) is hardcoded for cron sessions. Update if your average changes.

## When to Use

- **Session start:** "How far until 2000?"
- **Motivation check:** See progress percentage
- **Time planning:** "Can I hit 2000 before dinner?"
- **Velocity comparison:** See how burst vs sustained affects ETA

## Math

```
remaining = milestone - current_blocks
eta_hours = remaining / velocity
eta_time = now + (eta_hours hours)

If remaining < 0: Milestone already passed! 🎉
```

## Related Tools

- `blocks-calculator.py` — Plan time for specific block count
- `3000-milestone.py` — Full 3000 milestone tracker
- `work-pattern-analyzer.py` — Velocity trends over time

## Created

2026-02-06 — Week 3, milestone progress tracking
