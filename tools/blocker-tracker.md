# blocker-tracker.py — ROI-Based Blocker Prioritization

## What It Does

Tracks and prioritizes blockers by ROI/min — execute highest-value unblocks first.

## The Problem

When multiple blockers exist, it's hard to know which to tackle first. This tool quantifies the ROI so you can prioritize: $50K/min > $26K/min > others.

## Usage

```bash
# Add a blocker
python3 blocker-tracker.py add --name "Gateway Restart" --value 50000 --time 1 --action "Run: openclaw gateway restart"

# List all blockers
python3 blocker-tracker.py list

# Show blockers by ROI priority
python3 blocker-tracker.py roi

# Mark a blocker resolved
python3 blocker-tracker.py resolve <id>
```

## ROI Formula

```
ROI/min = Value Unlocked / Time to Resolve (minutes)
```

## Example

Adding GitHub auth as a blocker:
```bash
python3 blocker-tracker.py add \
  --name "GitHub SSH Auth" \
  --value 130000 \
  --time 5 \
  --action "Run: gh auth login; git push origin main"
```

Output:
```
✅ Blocker added: GitHub SSH Auth
   ROI: $26,000/min ($130,000 in 5 min)
```

## Current Blockers (as of 2026-02-04)

1. **Gateway Restart** — $50,000/min ($50K in 1 min)
2. **GitHub SSH Auth** — $26,000/min ($130K in 5 min)

**Total: $180K unblocked in 6 min ($30K/min average)**

## Data Storage

Blockers stored in `data/blockers.json`:
```json
[
  {
    "id": 1,
    "name": "Gateway Restart",
    "value": 50000,
    "time_min": 1,
    "roi_per_min": 50000,
    "action": "Run: openclaw gateway restart",
    "owner": "arthur",
    "status": "active",
    "created": "2026-02-04T08:21:00"
  }
]
```

## Key Insight

**6 minutes = $180K unblocked. That's $30K per minute.**

When blocked, don't wait — quantify the ROI and execute highest-value blockers first.

## Related

- `revenue-tracker.py` — Track revenue pipeline
- `diary.md` — Work block logs
- MEMORY.md — "Blocker ROI = Priority" insight
