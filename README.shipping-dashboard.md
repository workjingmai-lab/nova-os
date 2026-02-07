# shipping-dashboard.py — Shipping Phase Dashboard

**Purpose:** One-command overview of everything needed for shipping phase

**Usage:**
```bash
python3 tools/shipping-dashboard.py
```

**What it shows:**
- Pipeline totals (ready, submitted, won)
- Execution gap (potential vs kinetic)
- Conversion rate (submitted → won)
- Blockers with ROI/min
- Next actions prioritized by value/time
- Quick command reference

**Data sources:**
- `data/revenue-pipeline.json` — Pipeline data (nested JSON structure with grants/services/bounties arrays)
- Calculates execution gap from pipeline: gap = ready - submitted

**Latest fix (Work block 2288):**
- Original issue: Dashboard looked for non-existent `execution-gap-data.json` file
- Solution: Calculate gap from pipeline data directly (potential = ready, kinetic = submitted)
- Result: Now correctly shows $732K gap (99.3%)

**Example output:**
```
PIPELINE OVERVIEW
  Total Pipeline:     $920K
  Ready to Send:      $737K
  Submitted:          $5K
  Won:                $0

EXECUTION GAP
  Potential (Ready):  $737K
  Kinetic (Shipped):  $5K
  Gap:                $732K
  Gap Size:           99.3%
```

**Why this matters:**
Shipping phase requires high visibility into what's ready and what's blocking. This dashboard is the first command to run — shows everything at a glance.

**Related tools:**
- `execution-gap.py` — Detailed gap breakdown
- `revenue-tracker.py` — Pipeline management
- `response-tracker.py` — Response tracking

**Created:** 2026-02-05 (Work block 2248)
**Last updated:** 2026-02-05 (Work block 2288 — gap calculation fix)
