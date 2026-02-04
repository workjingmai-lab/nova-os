# blocker-status.py

Quick visibility into what's blocking revenue execution and the ROI of unblocking.

## What It Does

Checks the status of common blockers (GitHub CLI auth, browser service) and displays:
- Current status (✅/❌)
- Time to fix
- Value unblocked
- ROI per minute
- Command to fix
- What gets unblocked

## When to Use

- Before starting grant submissions
- Before browser automation tasks
- Quick health check (10 seconds)
- Part of heartbeat checklist

## How It Works

```bash
python3 tools/blocker-status.py
```

**Example output:**
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

## Key Insight

**Blocker ROI = Priority** — Fix highest ROI blockers first. $50K/min > $26K/min > everything else.

## Dependencies

- `gh` CLI (GitHub CLI)
- `openclaw` CLI

## Related Tools

- `revenue-tracker.py` — Track the pipeline
- `grant-submit.py` — Submit grants once unblocked
- `service-batch-send.py` — Send service messages

---

**Created:** 2026-02-04
**Work block:** 1411
**Purpose:** Track blockers with ROI clarity
