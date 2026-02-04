# pipeline-health-check.py — Unified Pipeline Overview

**Purpose:** Complete pipeline health in one command — combines pipeline snapshot, blocker status, today's metrics, and revenue tracker into a single view.

**When to use:** Quick status check before making decisions or starting work.

---

## What It Does

**Orchestrates 4 health checks:**

1. **Pipeline snapshot** — Messages, value, status breakdown
2. **Blocker status** — Top blocker with ROI calculation
3. **Today's metrics** — Work blocks, velocity, target progress
4. **Revenue tracker** — Pipeline summary ($2M+ tracked)

**Plus recommendations** — What to do next based on current state.

---

## Usage

### Text Output (Default)

```bash
python3 tools/pipeline-health-check.py
```

**Example output:**
```
================================================================================
🔍 PIPELINE HEALTH CHECK
================================================================================

📊 PIPELINE STATUS:
--------------------------------------------------------------------------------
Total: $2,237,000
Services: $2,057,000 (92%)
Grants: $130,000 (6%)
Bounties: $50,000 (2%)

Status breakdown:
- Ready to execute: $2,057,000
- Blocked (Arthur): $130,000
- Blocked (Browser): $50,000

🚧 BLOCKERS:
--------------------------------------------------------------------------------
🔥 TOP PRIORITY: Gateway restart (browser access)
   Time: 1 min → Value: $50,000 → ROI: $50,000/min

📈 TODAY'S METRICS:
--------------------------------------------------------------------------------
Work blocks completed: 1418
Target: 300 blocks (24 hours)
Velocity: ~44 blocks/hour sustained

💰 REVENUE TRACKER:
--------------------------------------------------------------------------------
Run `python3 tools/revenue-tracker.py summary` for full details

💡 RECOMMENDATION:
--------------------------------------------------------------------------------
Top priority: Unblock highest ROI item first
   Arthur approval: $1,028,500/min → $2,057K services
   GitHub auth: $26,000/min → $130K grants
   Gateway restart: $50,000/min → $50K bounties

Next action:
   1. Review blockers: python3 tools/blocker-roi-calculator.py
   2. Check pipeline: python3 tools/pipeline-snapshot.py
   3. Pick goal: python3 tools/goal-tracker.py focus

================================================================================
✅ Health check complete
================================================================================
```

### JSON Export

```bash
python3 tools/pipeline-health-check.py --json
```

**Exports to:** `tmp/health-check.json`

```json
{
  "timestamp": "2026-02-04T05:25:00Z",
  "work_blocks": 1418,
  "status": "HEALTHY",
  "recommendation": "Unblock highest ROI item first"
}
```

---

## Components

**Runs these tools internally:**

| Tool | Output | Purpose |
|------|--------|---------|
| `pipeline-snapshot.py` | Pipeline status ($2M+ tracked) | What's in the pipeline |
| `blocker-roi-calculator.py` | Top blocker with ROI | What's blocking execution |
| `revenue-tracker.py` | Revenue summary | Breakdown by type |
| `diary.md` | Work blocks, velocity | Today's progress |

---

## Why It Matters

**Decision support in one command:**

- **Arthur checks in** → "How's everything?" → Run `pipeline-health-check.py`
- **Starting work** → "What should I do?" → Recommendations section
- **Status sync** → "What's the pipeline value?" → $2M+ breakdown
- **Blocker review** → "What's blocking?" → Top blocker with ROI

**Before:** Run 4 separate commands, stitch together output
**After:** One command, complete picture

---

## Key Metrics

**Pipeline health indicators:**

- **Total value** — $2M+ tracked (grants, services, bounties)
- **Ready vs blocked** — What can execute now vs needs unblocking
- **Work blocks** — Today's output vs 300 target
- **Velocity** — Blocks per hour (sustained ~44)
- **Top blocker** — Highest ROI unblock (time → value)

---

## Recommendations

**Generated based on current state:**

1. **Services NO blockers** → $2,057K ready (Arthur approval: 2 min → $2M)
2. **Grants: GitHub auth** → $130K ready (5 min → $26K/min)
3. **Bounties: Gateway restart** → $50K ready (1 min → $50K/min)

**Next actions:**
- Review blockers: `blocker-roi-calculator.py`
- Check pipeline: `pipeline-snapshot.py`
- Pick goal: `goal-tracker.py focus`

---

## Dependencies

- Python 3.6+
- Standard library only (`subprocess`, `json`, `sys`, `pathlib`, `re`)
- **Required tools:** pipeline-snapshot.py, blocker-roi-calculator.py, revenue-tracker.py

---

## Automation

**Heartbeat integration:**

Can be run via cron or heartbeat to generate periodic status reports.

```yaml
# Example: Daily pipeline health report
- name: "Daily Pipeline Health"
  schedule: "0 9 * * *"  # 9 AM daily
  message: |
    Run pipeline-health-check.py and export to tmp/daily-health.json
```

---

## Created

2026-02-03 — Work block ~1100 (pipeline orchestration)
