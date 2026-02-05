# Blocker ROI Calculator

## Overview
Calculates the return-on-investment for unblocking tasks. Helps prioritize which blockers to clear first based on value/time ratio.

## Usage
```bash
./tools/blocker-roi-calculator.sh <unblocked_value> <time_minutes>
```

## Examples
```bash
# Gateway restart: $50K bounties in 1 minute
./tools/blocker-roi-calculator.sh 50000 1

# GitHub auth: $130K grants in 8 minutes
./tools/blocker-roi-calculator.sh 130000 8

# Combined: $180K in 6 minutes (both blockers)
./tools/blocker-roi-calculator.sh 180000 6
```

## Output
- **Per-second ROI:** Instant value rate
- **Per-minute ROI:** Standardized comparison metric
- **Per-hour ROI:** Annualized perspective
- **Priority rating:** Urgent/High/Medium/Low
- **Decision guidance:** Execute now vs schedule
- **Investment perspective:** Multiple on minimum wage

## Key Insight
> **Blocker ROI = Priority** — $30K/min tasks should be done before $1K/min tasks.

## Created
- **Date:** 2026-02-04
- **Work block:** #1507
- **Context:** Week 2 revenue pivot — prioritizing gateway restart and GitHub auth

## Related Tools
- `revenue-tracker.py` — Track pipeline value
- `blocker-tracker.md` — Log current blockers
- `priority-sorter.sh` — Sort tasks by ROI
