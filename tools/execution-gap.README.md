# Execution Gap Calculator

Shows the difference between what you have READY and what you've actually SUBMITTED.

## What It Does

The execution gap is the chasm between POTENTIAL revenue (opportunities identified) and KINETIC revenue (money actually pursued).

**Example output:**
```
⚡ EXECUTION GAP REPORT
============================================================

📊 PIPELINE SUMMARY
  Total Potential: $435,000
  Ready to Send:  $435,000 (100.0%)
  Submitted:      $0 (0.0%)
  Won:            $0 (0.0%)

🚨 EXECUTION GAP
  Ready → Submitted: $435,000 (not sent)
```

## Usage

```bash
python3 tools/execution-gap.py
```

## What It Tells You

- **Potential Pipeline:** Total value of all identified opportunities
- **Ready to Send:** Value of opportunities with messages/proposals prepared
- **Submitted:** Value of opportunities actually sent/submitted
- **Execution Gap:** The difference between ready and submitted

## Key Insight

A large execution gap means you're PREPARING but not EXECUTING.

**$435K ready, $0 submitted = 100% execution gap.**

The gap is not capability or preparation — it's SHIPPING.

## Data Source

Reads from `revenue-pipeline.json` — your single source of truth for all revenue opportunities.

## Related Tools

- `revenue-tracker.py` — Track individual submissions
- `service-batch-send.py` — Send service outreach messages
- `grant-batch.py` — Submit grant applications

---

*Created: 2026-02-05 — Work block 1835*
*Purpose: Make the execution gap visible*
