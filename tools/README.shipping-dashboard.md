# shipping-dashboard.py

One-stop dashboard for the shipping phase. Shows everything Arthur needs to know in a single command.

## What It Does

- **Pipeline overview:** Ready, submitted, won totals
- **Execution gap:** Potential vs kinetic revenue
- **Conversion rate:** Submitted → won percentage
- **Blockers:** Current blockers with ROI/min
- **Next actions:** Prioritized by ROI
- **Quick commands:** Fast access to key tools

## Usage

```bash
python3 tools/shipping-dashboard.py
```

That's it. One command, complete visibility.

## Example Output

```
============================================================
  🚢 SHIPPING DASHBOARD
============================================================
  Generated: 2026-02-05 19:05 UTC

📊 PIPELINE OVERVIEW
------------------------------------------------------------
  Total Pipeline:     $920K
  Ready to Send:      $435K
  Submitted:          $5K
  Won:                $0

⚡ EXECUTION GAP
------------------------------------------------------------
  Potential (Ready):  $435K
  Kinetic (Shipped):  $0
  Gap:                $435K
  Gap Size:           100.0%

⚠️  BLOCKERS (Arthur actions required)
============================================================
  • Gateway restart
    Time: 1 min
    Unlocks: $50K
    ROI: $50K/min

  • GitHub CLI auth
    Time: 5 min
    Unlocks: $130K
    ROI: $26K/min

  Total: 6 min → $180K unblocked
  Average ROI: $30K/min

🎯 NEXT ACTIONS (Prioritized by ROI)
============================================================
  1. Send 39 service messages
     Time: 36 min | ROI: $9K/min | Value: $332K
  2. Submit 5 grant applications
     Time: 15 min | ROI: $8K/min | Value: $125K
  3. Gateway restart (bounties)
     Time: 1 min | ROI: $50K/min | Value: $50K
  4. GitHub auth (grants)
     Time: 5 min | ROI: $26K/min | Value: $130K
```

## Why This Tool Exists

**Problem:** During shipping phase, Arthur needs quick answers to:
- What's ready to send?
- What's blocking progress?
- What should I do next?
- What's the ROI of each action?

**Solution:** One command shows everything. No hunting through files. No manual calculation. Just run and see.

## Data Sources

- `data/revenue-pipeline.json` — Pipeline totals (nested structure: grants/services/bounties arrays)
- `execution-gap-data.json` — Gap metrics (optional, shows $0 if missing)
- Hardcoded blockers list — Arthur-specific actions

**Note (Work block 2282):** Fixed JSON parser to correctly read nested pipeline structure. Dashboard now shows accurate totals ($920K total, $737K ready, $5K submitted).

## Integration with Other Tools

- **execution-gap.py** — Shows detailed gap analysis
- **revenue-tracker.py** — Updates pipeline status
- **response-tracker.py** — Tracks responses after sending
- **NOW.md** — 5-second action summary
- **STATUS-FOR-ARTHUR.md** — Full execution context

## When to Use

1. **Daily shipping sessions** — Run before starting to see current state
2. **Mid-session check** — Run after completing actions to see updated gap
3. **Weekly review** — Run to assess progress and plan next week

## Key Metrics Explained

- **Potential** — Revenue ready to send but not yet sent
- **Kinetic** — Revenue actually submitted/out the door
- **Gap** — Difference (what's left on the table)
- **Conversion Rate** — Submitted → Won (only appears after submissions)

## Arthur's 57-Min Plan

The dashboard shows the complete plan:
1. **Unblock (6 min):** Gateway restart ($50K) + GitHub auth ($130K)
2. **Ship (51 min):** Send 39 service messages ($332K) + Submit 5 grants ($125K)
3. **Total:** 57 min → $637K ROI = $11,193/min

---

**Tool created:** 2026-02-05 (Work block 2248)
**Purpose:** Single source of truth for shipping phase
**Status:** Ready for Arthur's use immediately
