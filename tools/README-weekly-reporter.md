# weekly-reporter.py

Automated week-in-review generator. Creates structured reports from diary.md and goal files.

## What It Does

- Parses diary.md for work blocks and achievements (last 7 days)
- Categorizes entries: task, heartbeat, deep_think, log
- Calculates velocity (tasks per day)
- Generates JSON + Markdown reports

## Usage

```bash
python3 tools/weekly-reporter.py
```

## Output

Reports saved to `reports/`:
- `week-N-progress.json` — Machine-readable metrics
- `week-N-progress.md` — Human-readable summary

## Metrics Tracked

- **Work Blocks Completed:** Tasks executed this week
- **Velocity:** Tasks per day (avg)
- **Total Entries:** All diary activity
- **Achievements:** Top 5 wins (✅ or COMPLETE markers)

## Entry Types Detected

- `task` — Work blocks (WORK BLOCK / CRON)
- `heartbeat` — FULL heartbeat markers
- `deep_think` — DEEP THINK sessions
- `log` — General diary entries

## Why This Matters

Weekly reviews = pattern recognition. See what's working, double down on wins.

---

**Work Block:** #961
**Created:** 2026-02-03T06:06Z
