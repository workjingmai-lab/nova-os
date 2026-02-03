# win-streak.py

**Purpose:** Gamify productivity by tracking consecutive days with 10+ work blocks.

## What It Does

Analyzes your diary.md to find:
- **Current streak** — Consecutive days with 10+ work blocks
- **Daily totals** — Work blocks per day (last 7 days)
- **Status indicators** — 🔥 for qualifying days, blank for non-qualifying

## Usage

```bash
python3 tools/win-streak.py
```

## Output

```
🔥 WIN STREAK TRACKER
==================================================

🎯 Current Streak: 7 consecutive days with 10+ work blocks

🔥 ON FIRE! Keep it going!

Recent Daily Totals:
--------------------------------------------------
🔥 2026-02-02: 85 work blocks
🔥 2026-02-01: 132 work blocks
🔥 2026-01-31: 98 work blocks
...
```

## Threshold

**10+ work blocks = "win"**

Adjustable in code (`threshold = 10`).

## Why It Matters

**Gamification works.** Streaks create:
- **Momentum** — Don't break the chain!
- **Visibility** — See consistency at a glance
- **Motivation** — Push for 10+ even on low-energy days

**Pro tip:** Use with goal-tracker.py for full goal + streak visibility.

## Category

Analytics / Motivation / Gamification
