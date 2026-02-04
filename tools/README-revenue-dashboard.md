# revenue-dashboard.py

**Visualize your entire revenue pipeline in one command.**

---

## What It Does

Displays an ASCII dashboard showing all revenue opportunities (grants, services, bounties) with:
- Total pipeline value
- Ready-to-execute vs. pending amounts
- Category breakdown (grants, services, bounties)
- Top 5 opportunities by value
- Visual progress bar

**Current pipeline:** $302K (as of 2026-02-03)

---

## Installation

Already in `tools/`. Requires `data/revenue-pipeline.json` (auto-created if missing).

---

## Usage

```bash
# View your revenue dashboard
python3 tools/revenue-dashboard.py
```

**Output example:**
```
============================================================
          💰 REVENUE PIPELINE DASHBOARD
============================================================

  TOTAL PIPELINE: $302K
  Ready to execute: $130K

  Pipeline Status:
  [████████████████████░░░░░░░░░░░░░░░]
   $130K ready $172K pending

  By Category:
  ┌─ Grants:    $130K (5 opportunities)
  │  └─ Ready:  $130K
  ├─ Services:  $122K (10 leads)
  │  └─ Ready:  $0K
  └─ Bounties:  $50K (1 opportunity)
     └─ Ready:  $0K

  Top 5 Opportunities:
  1. ✅ Optimism RPGF                  $150K
  2. ✅ Gitcoin Grant                  $50K
  3. ⏸️ Quick Automation (Stripe)      $10K
  4. ⏸️ Quick Automation (Supabase)    $10K
  5. ⏸️ Multi-Agent System (Notion)    $25K

  Last updated: 2026-02-03T03:00:00Z
============================================================
```

---

## Data Source

Reads from `data/revenue-pipeline.json`:

```json
{
  "grants": [
    {
      "name": "Optimism RPGF",
      "potential": 150000,
      "status": "ready",
      "deadline": "2026-02-15"
    }
  ],
  "services": [
    {
      "name": "Quick Automation (Stripe)",
      "potential": 10000,
      "status": "tracked",
      "contact": "N/A"
    }
  ],
  "bounties": [
    {
      "name": "Code4rena",
      "potential": 50000,
      "status": "blocked",
      "blocker": "Browser access"
    }
  ],
  "last_updated": "2026-02-03T03:00:00Z"
}
```

**Update the pipeline:** Edit `data/revenue-pipeline.json` directly, or use `revenue-tracker.py`.

---

## Why It Matters

**Revenue visibility = execution clarity.**

Before this tool, opportunities were scattered across different files and systems. Now you have:
- Single source of truth for all revenue
- Quick visual of what's ready to execute
- Prioritization by opportunity size
- Status tracking (ready, tracked, blocked)

**The $302K pipeline** (grants + services + bounties) is now visible in one command.

---

## Integration

**Best used with:**
- `revenue-tracker.py` — Update pipeline data
- `service-outreach-tracker.py` — Track service messages
- `grant-submit.md` — Execute grant submissions

**Add to your workflow:**
1. Run `revenue-dashboard.py` every morning
2. Pick top opportunity to execute
3. Update status when complete
4. Repeat

---

## Examples

```bash
# Check pipeline before starting work
python3 tools/revenue-dashboard.py

# After completing a submission, update JSON
vim data/revenue-pipeline.json

# Verify update
python3 tools/revenue-dashboard.py
```

---

## Created

**2026-02-03** — Week 2, revenue pivot focus

**Insight:** "Can't improve what you can't see. Revenue dashboard makes $302K visible and actionable."
