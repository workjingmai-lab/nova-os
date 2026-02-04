# win-streak.py — Track Productivity Streaks

**Gamify your productivity by tracking consecutive days with 10+ work blocks.**

## What It Does

- Scans `diary.md` for WORK BLOCK entries
- Counts work blocks per day
- Calculates your current streak (consecutive days with 10+ blocks)
- Shows recent daily totals with fire emoji 🔥 for qualifying days

## Usage

```bash
python tools/win-streak.py
```

## Output

```
🔥 WIN STREAK TRACKER
==================================================

🎯 Current Streak: 5 consecutive days with 10+ work blocks

🔥 ON FIRE! Keep it going!

Recent Daily Totals:
--------------------------------------------------
🔥 2026-02-03: 47 work blocks
🔥 2026-02-02: 312 work blocks
🔥 2026-02-01: 250 work blocks
🔥 2026-01-31: 89 work blocks
🔥 2026-01-30: 15 work blocks
  2026-01-29: 3 work blocks
```

## How It Works

1. Parses diary.md for `WORK BLOCK ### — YYYY-MM-DD` pattern
2. Counts blocks per date
3. Calculates streak (consecutive days with ≥10 blocks)
4. Stops counting at first day below threshold

## Dependencies

- Python 3.7+
- `diary.md` in workspace root

## Why 10 Blocks?

10 work blocks = ~10 minutes of focused execution. It's achievable but requires showing up and doing the work. The streak gamifies consistency over intensity.

**Maintain the fire. 🔥**
