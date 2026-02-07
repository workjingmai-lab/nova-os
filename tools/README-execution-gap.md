# execution-gap.py — Execution Gap Calculator

**Purpose:** Calculate and display the gap between POTENTIAL (ready to send) and KINETIC (actually sent) revenue.

## What It Does

Makes the invisible cost of waiting visible by calculating:
- Total revenue ready to send
- Total revenue actually sent
- Execution gap (dollar amount and percentage)
- ROI per minute for closing the gap
- Opportunity cost per hour of waiting

## Usage

```bash
python3 tools/execution-gap.py
```

## Output Example

```
============================================================
💸 EXECUTION GAP ANALYZER
============================================================

POTENTIAL (Ready to Send):
  Total ready: $734.5K

KINETIC (Actually Sent):
  Total sent: $5.0K

------------------------------------------------------------
EXECUTION GAP:
  Gap amount: $729.5K
  Gap percent: 99.3%

THE MATH:
  Time to close gap: 15 minutes
  ROI per minute: $48.6K
  Opportunity cost/hour: $2.92M

ACTION:
  Run: bash tools/send-everything.sh full
  Time: 15 minutes
  Result: $729.5K sent
```

## How It Works

1. Reads `revenue-pipeline.json` for current pipeline data
2. Calculates total ready amount across all categories
3. Calculates total submitted amount
4. Computes gap metrics (amount, percentage, ROI)
5. Displays critical alert if gap ≥ 90%

## Data Source

- **File:** `revenue-pipeline.json`
- **Format:** JSON with categories (grants, services, bounties)
- **Fields:** `amount`, `ready`, `submitted`, `won`

## Key Metrics

- **Gap Amount:** Dollar difference between ready and sent
- **Gap Percentage:** (Gap / Ready) × 100
- **ROI Per Minute:** Gap / 15 minutes (time to send everything)
- **Opportunity Cost:** ROI × 60 (cost per hour of waiting)

## When to Use

- **Daily check:** Track execution gap over time
- **Before sending:** Understand the ROI of closing the gap
- **Motivation:** See the cost of waiting in concrete numbers

## Integration

Use with other revenue tools:
- `revenue-tracker.py` — Track individual items
- `lead-prioritizer.py` — Prioritize high-ROI leads
- `service-batch-send.py` — Send service messages
- `grant-batch-submit.py` — Submit grant applications

## Created

- **Date:** 2026-02-06
- **Work block:** 2809
- **Context:** Making execution gap visible to drive action

## Insight

> "The execution gap isn't a technical problem — it's a choice. $729.5K ready but not sent = $2.92M/hour left on table. Every minute waited = $48.6K not pursued."

The math is brutal. The tool makes it visible.
