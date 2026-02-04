# Pipeline Summary — Quick Revenue Overview

See your entire revenue pipeline at a glance: grants, services, bounties, metrics.

## Overview

Pipeline Summary provides a quick, formatted view of your revenue pipeline. No raw JSON, no parsing — just clear, readable output showing:
- **Total pipeline value** ($302K+)
- **Breakdown by category** (grants, services, bounties)
- **Status and blockers** for each category
- **Metrics** (work blocks, velocity, next action)

## Use Case

- **Quick pipeline check** — See what's in the funnel
- **Status at a glance** — Blocked vs. ready categories
- **Metrics dashboard** — Velocity and work block counts
- **Before decisions** — Know your pipeline before choosing next task

## Installation

```bash
# Tool location
tools/pipeline-summary.py

# Data source
revenue-pipeline.json
```

## Usage

### View Pipeline
```bash
python3 tools/pipeline-summary.py
```

**Output:**
```
============================================================
💰 REVENUE PIPELINE SUMMARY
============================================================

Total Pipeline: $302,000
Last Updated: 2026-02-03T02:00:00Z

📊 Breakdown:

  GRANTS:
    Amount: $130,000
    Status: Ready to submit
    Blocker: GitHub repo must be public
    ROI: $16,250/min (8 min auth = $130K unblocked)

  SERVICES:
    Amount: $122,000
    Status: 10 messages ready, 0 sent
    Blocker: None
    ROI: $8,133/min (15 min to send 10 messages)

  BOUNTIES:
    Amount: $50,000
    Status: Setup needed
    Blocker: Browser access (gateway restart)
    ROI: $50,000/min (1 min restart = $50K unblocked)

📈 Metrics:
  Work Blocks Today: 300
  Work Blocks Week 2: 878
  Velocity: ~42 blocks/hour
  Next Action: Submit 5 grants, send 15 service messages, unblock Code4rena

============================================================
```

## Pipeline Categories

| Category | Amount | Status | Next Action |
|----------|--------|--------|-------------|
| **Grants** | $130K | Ready | GitHub auth → Submit |
| **Services** | $122K | Ready | Send 10 messages |
| **Bounties** | $50K | Blocked | Browser restart → Setup |

## Data Structure

Reads from `revenue-pipeline.json`:

```json
{
  "totalPipeline": 302000,
  "lastUpdated": "2026-02-03T02:00:00Z",
  "categories": {
    "grants": {
      "amount": 130000,
      "status": "Ready to submit",
      "blocker": "GitHub repo must be public",
      "blockerROI": "$16,250/min"
    },
    "services": {
      "amount": 122000,
      "status": "10 messages ready, 0 sent"
    },
    "bounties": {
      "amount": 50000,
      "status": "Setup needed",
      "blocker": "Browser access (gateway restart)",
      "blockerROI": "$50,000/min"
    }
  },
  "metrics": {
    "workBlocksToday": 300,
    "workBlocksWeek2": 878,
    "velocity": "~42 blocks/hour",
    "nextAction": "Submit 5 grants, send 15 service messages"
  }
}
```

## Workflow

### Morning Pipeline Check
```bash
# What's in my funnel?
python3 tools/pipeline-summary.py

# → Shows total $302K, what's blocked, what's ready
```

### Before Work Block
```bash
# See pipeline context
python3 tools/pipeline-summary.py

# Then check next actions
python3 tools/next-actions.py

# Execute highest-ROI task
```

### After Pipeline Update
```bash
# Update pipeline
python3 tools/revenue-tracker.py update

# Check new summary
python3 tools/pipeline-summary.py
```

## Integration

Pairs with:
- `revenue-tracker.py` — Pipeline data source, updates
- `next-actions.py` — Prioritized task list based on pipeline
- `service-outreach-tracker.py` — Service pipeline detail
- `grant-submit.py` — Grant execution

## Use Cases

### Decision Support
```bash
# Should I focus on grants or services?
python3 tools/pipeline-summary.py

# → Shows grants: $130K blocked (16K/min ROI)
# → Shows services: $122K ready (8K/min ROI)
# → Decision: Unblock grants first (higher ROI)
```

### Pipeline Health Check
```bash
# Is my pipeline growing or shrinking?
python3 tools/pipeline-summary.py

# → Total $302K (up from $224K yesterday)
# → Velocity: 42 blocks/hour
# → Status: Pipeline healthy, growing
```

### Blocker Visibility
```bash
# What's blocking revenue?
python3 tools/pipeline-summary.py

# → Grants: GitHub auth ($16K/min ROI)
# → Bounties: Browser restart ($50K/min ROI)
# → Decision: Restart browser first (highest ROI)
```

## Tips

- **Run daily** — Pipeline changes fast, stay current
- **Pair with next-actions** — Summary shows what, next-actions shows how
- **Track trends** — Is pipeline growing or shrinking week over week?
- **ROI focus** — Use blocker ROI to prioritize unblocking

## Philosophy

**Pipeline clarity = execution clarity.**

When you can see your entire funnel at a glance, you make better decisions. $130K blocked vs. $122K ready → Unblock $130K first.

**Blockers are leverage.**

1 minute unblocking $50K > 1 hour of grunt work. The summary shows you exactly where leverage exists.

**Metrics drive improvement.**

Velocity, work blocks, pipeline value — track these weekly. If velocity drops, investigate. If pipeline shrinks, add more leads.

## Metrics to Track

Weekly:
- **Pipeline value** — Total $ in funnel
- **Conversion rate** — Ready → Submitted → Won
- **Blocker resolution time** — How fast you unblock
- **Velocity** — Work blocks per hour

## Example Session

```bash
# Morning check
python3 tools/pipeline-summary.py
# → $302K total, $130K blocked (grants), $122K ready (services)

# Check next actions
python3 tools/next-actions.py
# → Shows grant submission as #1 priority (but blocked)

# Unblock highest-ROI task
# Ask Arthur: "Can you run `gh auth login`? Unblocks $130K."

# After unblock, re-check
python3 tools/pipeline-summary.py
# → $130K now ready to execute

# Execute
python3 tools/grant-submit.py --all
```

## Status

- **Total Pipeline:** $302,000
- **Categories:** 3 (grants, services, bounties)
- **Blocked Value:** $180,000 (grants + bounties)
- **Ready Value:** $122,000 (services)

---

*Created: 2026-02-03*
*Part of Week 2 Revenue Pivot — Ecosystem Expansion & Value Creation*
