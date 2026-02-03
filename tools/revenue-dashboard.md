# revenue-dashboard.py

**Visualize your entire revenue pipeline at a glance.**

## What It Does

Displays an ASCII dashboard showing:
- Total pipeline value (grants + services + bounties)
- Ready-to-execute opportunities vs pending
- Visual bar chart of pipeline status
- Category breakdowns with counts
- Top 5 highest-value opportunities

## How to Use

```bash
python tools/revenue-dashboard.py
```

## Data Source

Reads from `data/revenue-pipeline.json` (populated by `revenue-tracker.py`).

## Output Example

```
============================================================
              💰 REVENUE PIPELINE DASHBOARD
============================================================

  TOTAL PIPELINE: $302K
  Ready to execute: $130K

  Pipeline Status:
  [████████████████████████░░░░░░░░░░░░░░░]
   $130K ready $172K pending

  By Category:
  ┌─ Grants:    $130K (5 opportunities)
  │  └─ Ready:  $130K
  ├─ Services:  $122K (25 leads)
  │  └─ Ready:  $0
  └─ Bounties:  $50K (1 opportunity)
     └─ Ready:  $0

  Top 5 Opportunities:
  1. ✅ Gitcoin Grant                         $50K
  2. ✅ Optimism RPGF                         $40K
  3. ⏸️ Code4rena Audit                       $50K
  ...
```

## Why It Matters

**Pipeline visibility = execution clarity.**

Without a dashboard, $300K of opportunities is invisible noise. With it, you see:
- What's ready to execute now (unblock these first!)
- What's worth pursuing (top 5 = 80% of value)
- Category balance (are you over-indexed on grants?)

## Related Tools

- `revenue-tracker.py` — Add/update opportunities
- `grant-submit.py` — Execute grant submissions
- `service-outreach-tracker.py` — Track service leads

## Metrics

- Created: Week 2 (Revenue Pivot)
- Usage: Daily (heartbeat visibility)
- Impact: Single source of truth for $302K pipeline
