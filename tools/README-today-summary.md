# today-summary.py

Generate human-readable summary of today's work for Arthur.

## What It Does

- Extracts today's diary entries
- Lists completed tasks (last 5)
- Shows metrics: tools built, posts made, goal progress
- Highlights current blockers

## Usage

```bash
python3 tools/today-summary.py
```

## Output

- Prints summary to stdout
- Saves to `reports/today-summary.md`

## Sections

1. **What Got Done** — Completed tasks from diary
2. **By the Numbers** — Tools built, posts, totals
3. **Goals Status** — Week progress
4. **Current Blockers** — What's blocking execution

## Why This Matters

Visibility = trust. Arthur sees what Nova accomplished without digging through diary.md.

---

**Work Block:** #962
**Created:** 2026-02-03T06:07Z
