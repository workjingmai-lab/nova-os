# blocker-status.py

**Quick visibility into what's blocking revenue execution.**

## What It Does

Checks the two main blockers to revenue pipeline execution:
1. **GitHub CLI auth** - Required for grant submissions ($130K pipeline)
2. **Browser service** - Required for Code4rena and web automation ($50K pipeline)

For each blocker, shows:
- Time to fix
- Value at stake
- ROI ($/min)
- Exact command to run
- What it unblocks

## Usage

```bash
python tools/blocker-status.py
```

## Output

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

**Blocker ROI = Priority.** This tool surfaces exactly what's blocking execution, so you can:
- Fix highest-ROI blockers first ($50K/min for gateway restart)
- See exactly what command to run
- Understand what revenue each blocker unblocks

## Created

2026-02-03 — Part of Week 2 revenue pivot
