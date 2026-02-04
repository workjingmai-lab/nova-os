# Wins Tracker

## What

A simple accomplishment logger. Track small wins, review progress, maintain momentum.

## Why

Motivation through visible progress. Seeing wins accumulate creates momentum.

## Usage

```bash
# Add a win
python3 tools/wins.py add "Submitted 5 grant proposals"

# List all wins
python3 tools/wins.py list

# Today's wins
python3 tools/wins.py today

# Recent wins (last 10)
python3 tools/wins.py recent
```

## Data

Stored in `.wins.json` (workspace root).

## Integration

- Hook into `diary.md` updates
- Add to daily reflection routine
- Use for morale during low-velocity periods

## Metrics

- Total wins logged
- Wins per day/week
- Streak tracking (manual)

---

**Created:** 2026-02-03
**Category:** Productivity / Motivation
