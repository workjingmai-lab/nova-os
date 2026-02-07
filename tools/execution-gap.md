# execution-gap.py

Measure the gap between potential revenue (ready to send) and actual submissions.

## Quick Start

```bash
python3 tools/execution-gap.py
```

## Output Example

```
══════════════════════════════════════════════════════════════════
                    EXECUTION GAP ANALYSIS
══════════════════════════════════════════════════════════════════

READY TO SEND:                    $734,500
ACTUALLY SUBMITTED:                 $5,000
══════════════════════════════════════════════════════════════════

EXECUTION GAP: 99.3%

INTERPRETATION:
  ⚠️  CRITICAL: You have $734.5K ready but haven't sent it.

TIME TO CLOSE GAP: ~15 minutes
(35 items × 0.5 min average send time)

ROI: $48,966 per minute of execution

══════════════════════════════════════════════════════════════════
```

## Why This Exists

The execution gap is the difference between what you COULD do (everything ready) and what you've actually DONE (submitted). A high gap means:

- Pipeline built but not activated
- Revenue left on the table
- Opportunity cost mounting

## How It Works

1. Reads `data/revenue-pipeline.json`
2. Sums all items with status "ready" or "ready_to_submit"
3. Sums all items with status "submitted"
4. Calculates gap percentage: `(ready - submitted) / total`

## Using the Gap to Drive Action

**Gap > 90%:**
- Problem: Not executing
- Solution: Block time, start sending

**Gap 50-90%:**
- Problem: Inconsistent execution
- Solution: Daily checklist, routine

**Gap < 50%:**
- Status: Good execution velocity
- Focus: Follow-ups, closing

**Gap < 20%:**
- Status: Excellent
- Focus: Pipeline replenishment

## Related

- Dashboard: `tools/conversion-dashboard.py` (full pipeline view)
- Tracker: `tools/revenue-tracker.py` (update statuses)
- Checklist: `knowledge/daily-execution-checklist.md` (close the gap)

## Run Frequency

- **Daily:** Morning standup to see current gap
- **After sends:** Verify gap is shrinking
- **Weekly:** Track gap trend over time
