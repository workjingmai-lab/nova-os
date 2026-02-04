# blocker-status.py

Quick visibility into what's blocking revenue execution.

## Purpose

See what's blocking, the ROI of fixing it, and the exact command to unblock.

## Usage

```bash
python3 tools/blocker-status.py
```

## What It Checks

- **GitHub CLI Auth** — Required for grant submissions ($130K pipeline)
- **Browser Service** — Required for Code4rena bounties ($50K pipeline)

## Output

Shows blockers sorted by ROI (value/time):
- ✅ Status (green/red)
- Time to fix
- Value unblocked
- ROI per minute
- Exact command to run
- What it unblocks

## Example

```
🚧 BLOCKER STATUS
==================================================

❌ GitHub CLI NOT authenticated

❌ Browser service NOT running

==================================================
🔥 UNBLOCKERS (sorted by ROI):
==================================================

1. Gateway Restart
   Time: 1 min | Value: $50K | ROI: $50K/min
   Command: openclaw gateway restart
   Unblocks: Code4rena bounties + browser automation

2. GitHub CLI Auth
   Time: 5 min | Value: $130K | ROI: $26K/min
   Command: gh auth login
   Unblocks: 5 grant submissions
```

## Why It Matters

**Blocker ROI = Priority.**

Highest ROI unblockers first:
- Gateway restart → $50K/min
- GitHub auth → $26K/min

6 minutes = $180K unblocked. Execute highest value blockers first.

## Related Tools

- `blocker-tracker.py` — Track blockers over time
- `blocker-roi-calculator.py` — Calculate ROI for any blocker
- `revenue-tracker.py` — Full pipeline visibility
