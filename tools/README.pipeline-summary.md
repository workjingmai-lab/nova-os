# pipeline-summary.py

**Quick revenue pipeline overview**

---

## What It Does

Shows your $302K revenue pipeline at a glance with one command.

---

## Usage

```bash
python3 tools/pipeline-summary.py
```

---

## Output Example

```
============================================================
💰 REVENUE PIPELINE SUMMARY
============================================================

Total Pipeline: $302,000
Last Updated: 2026-02-03T02:10:00Z

📊 Breakdown:

  GRANTS:
    Amount: $130,000
    Status: ready
    Blocker: GitHub auth needed (Arthur action)
    ROI: $16,250/min (8 min auth → $130K unblocked)

  SERVICES:
    Amount: $122,000
    Status: tracking

  BOUNTIES:
    Amount: $50,000
    Status: setup
    Blocker: Browser access needed (Code4rena onboarding)
    ROI: $50,000/min (1 min restart → $50K unblocked)

📈 Metrics:
  Work Blocks Today: 851
  Work Blocks Week 2: 706
  Velocity: ~42 blocks/hour sustained
  Next Action: Submit 5 grants ($130K ready), send 15 service messages ($122K)

============================================================
```

---

## Why It Exists

Revenue pipeline data in `revenue-pipeline.json` is powerful but hard to read as raw JSON.

This script converts that data into a clean, human-readable summary.

**One command = full pipeline visibility.**

---

## Data Source

Reads from: `/home/node/.openclaw/workspace/revenue-pipeline.json`

Updated by: `revenue-tracker.py` and manual updates

---

## Use Cases

- **Morning check:** See what's ready to execute
- **Priority decisions:** Identify highest-ROI blockers
- **Status reviews:** Share pipeline with Arthur
- **Tracking:** Monitor pipeline growth over time

---

## Created By

Nova — 2026-02-03 (Work block 856)

**Part of:** Nova's Toolkit — 87+ tools for autonomous agents
