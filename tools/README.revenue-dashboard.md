# revenue-dashboard.py — Revenue Pipeline Visualizer

## What It Does

Displays your entire revenue pipeline in an ASCII dashboard with:
- Total pipeline value (ready vs pending)
- Category breakdown (grants, services, bounties)
- Top 5 opportunities ranked by value
- Visual bar chart for pipeline status
- Status indicators (✅ ready, ⏸️ pending)

## Usage

```bash
python3 tools/revenue-dashboard.py
```

## Output Example

```
============================================================
                💰 REVENUE PIPELINE DASHBOARD                
============================================================

  TOTAL PIPELINE: $216.0K
  Ready to execute: $130.0K

  Pipeline Status:
  [████████████████████████░░░░░░░░░░░░░░░░]
  $130.0K ready $86.0K pending

  By Category:
  ┌─ Grants:    $130.0K (5 opportunities)
  │  └─ Ready:  $130.0K
  ├─ Services:  $36.0K (4 leads)
  │  └─ Ready:      $0
  └─ Bounties:  $50.0K (1 opportunities)
     └─ Ready:      $0

  Top 5 Opportunities:
  1. ✅ Olas                                $50.0K
  2. ✅ Optimism RPGF                       $50.0K
  3. ⏸️ Code4rena                           $50.0K
  4. ⏸️ Multi-Agent System                  $25.0K
  5. ✅ Octant                              $15.0K

  Last updated: Never
============================================================
```

## Data Source

Reads from `data/revenue-pipeline.json` (created by `revenue-tracker.py`)

JSON structure:
```json
{
  "grants": [
    {"name": "Gitcoin", "potential": 5000, "status": "ready", "notes": "..."}
  ],
  "services": [
    {"name": "Quick Automation", "potential": 2000, "status": "lead", "notes": "..."}
  ],
  "bounties": [
    {"name": "Code4rena", "potential": 50000, "status": "lead", "notes": "..."}
  ]
}
```

## Features

1. **Instant overview** — See entire pipeline at a glance
2. **Visual status** — Bar chart shows ready vs pending ratio
3. **Category tracking** — Separate tracking for grants, services, bounties
4. **Top opportunities** — Rankings by value (high-impact focus)
5. **Status icons** — Quick visual scan (✅ ready, ⏸️ pending)

## Metrics Calculated

- **Total pipeline:** Sum of all opportunities
- **Ready to execute:** Sum of items with status="ready"
- **By category:** Breakdown by type (grants/services/bounties)
- **Ready %:** Visual bar shows proportion ready to execute

## Use Cases

- **Daily check-in** — Run to see pipeline status
- **Before outreach** — Confirm which leads are ready
- **Priority setting** — Focus on top opportunities first
- **Arthur visibility** — Quick snapshot of revenue potential

## Dependencies

- Python 3.6+
- `data/revenue-pipeline.json` (created by revenue-tracker.py)

## Related Tools

- `revenue-tracker.py` — Pipeline data management
- `grant-submission-generator.py` — Grant application templates
- Service proposal templates in `outreach/`

## Why It Matters

**Visualization = clarity.**

Without a dashboard, revenue pipeline is just numbers in JSON. With a dashboard, Arthur sees:
- Where the money is ($216K total)
- What's ready to execute ($130K grants)
- What needs work ($86K in leads)
- Top priorities (Olas $50K, Optimism RPGF $50K, Code4rena $50K)

This transforms "someday" into "next action."

---

**Created:** 2026-02-02
**Author:** Nova
**Part of:** Revenue generation toolkit
