# pipeline-summary.py

**Revenue pipeline visibility at a glance.**

Shows your entire $302K revenue pipeline with breakdowns, blockers, and metrics in one command.

## What It Does

- Reads `revenue-pipeline.json` and displays a formatted summary
- Shows total pipeline value, category breakdowns, and status
- Displays metrics: work blocks, velocity, next action
- Highlights blockers with ROI calculations

## Usage

```bash
python3 tools/pipeline-summary.py
```

## Output Example

```
============================================================
💰 REVENUE PIPELINE SUMMARY
============================================================

Total Pipeline: $302,000
Last Updated: 2026-02-03T05:00:00Z

📊 Breakdown:

  GRANTS:
    Amount: $130,000
    Status: Ready to submit
    Blocker: GitHub CLI auth required
    ROI: $16,250/min

  SERVICES:
    Amount: $122,000
    Status: 13/13 messages ready

  BOUNTIES:
    Amount: $50,000
    Status: Setup pending
    Blocker: Browser access
    ROI: $50,000/min

📈 Metrics:
  Work Blocks Today: 34
  Work Blocks Week 2: 938
  Velocity: ~44 blocks/hour
  Next Action: GitHub auth to unblock $130K grants

============================================================
```

## Dependencies

- `revenue-pipeline.json` (created/updated by `revenue-tracker.py`)

## Use Cases

- **Morning check:** See what's ready to execute
- **Pre-execution:** Verify pipeline status before submitting grants/sending messages
- **Blocker prioritization:** ROI sorting shows highest-impact unblocking
- **Metrics review:** Track velocity and work block progress

## Why It Matters

**Pipeline visibility = execution clarity.**

You can't improve what you can't see. This tool creates a single source of truth for your revenue pipeline, ensuring every opportunity is tracked and nothing falls through the cracks.

---

**Created:** 2026-02-02
**Status:** Active ✅
**Related:** `revenue-tracker.py`, `service-outreach-tracker.py`
