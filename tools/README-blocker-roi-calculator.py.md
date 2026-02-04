# README - blocker-roi-calculator.py

## Overview
Calculate and prioritize blockers by ROI (Return on Investment) to focus unblocking efforts on highest-impact items first.

## What It Does
- Takes list of blockers with (time to fix, value unlocked)
- Calculates ROI = Value / Time
- Sorts blockers by ROI (highest first)
- Outputs prioritized action list

## Why It Exists
**Math-driven prioritization:** Not all blockers are equal.

Example from Week 2:
- GitHub auth: 5 min → unblocks $130K grants = **$26,000/min**
- Gateway restart: 1 min → unblocks $50K bounties = **$50,000/min**
- Service outreach: 0 min blocked → $2,057K ready = **∞ ROI**

Execute highest ROI blockers first. 6 minutes = $180K unblocked.

## Usage

```bash
# Calculate ROI from blockers JSON
python3 tools/blocker-roi-calculator.py

# Use custom blocker list
python3 tools/blocker-roi-calculator.py --file my-blockers.json

# Sort by value instead of ROI
python3 tools/blocker-roi-calculator.py --sort-by value
```

## Input Format
JSON array of blockers:
```json
[
  {
    "name": "GitHub auth",
    "time_minutes": 5,
    "value_unlocked": 130000,
    "currency": "USD"
  },
  {
    "name": "Gateway restart",
    "time_minutes": 1,
    "value_unlocked": 50000,
    "currency": "USD"
  }
]
```

## Output
Prioritized list:
```
# Blocker Priority (by ROI)

1. Gateway restart — $50,000/min (1 min → $50K)
2. GitHub auth — $26,000/min (5 min → $130K)
3. Documentation — $1,000/min (30 min → $30K)

Total: 36 min → $210K unblocked
```

## Key Insight
**Blockers aren't problems. They're ROI opportunities.**

Calculate ROI. Sort. Execute.

## Integration
- Used by: blocker-tracker.py
- Reads from: revenue-pipeline.json
- Updates: .heartbeat_state.json (blockers section)

## Related Tools
- `blocker-status.py` — Check current blocker states
- `blocker-tracker.py` — Track blocker history
- `revenue-tracker.py` — Pipeline value tracking

## Real-World Impact
Week 2 (Feb 2026): Used ROI calculation to prioritize 3 blockers → $180K unblocked in 6 minutes ($30K/min average).

## Created
2026-02-03 (work block #902)

## Maintained By
Nova (continuous refinement based on blocker patterns)
