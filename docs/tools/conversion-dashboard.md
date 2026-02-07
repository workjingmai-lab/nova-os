# Conversion Dashboard — Pipeline Funnel Visualization

Visual conversion funnel showing pipeline stages (ready → sent → response → call → won) with conversion rates and blockers.

## What It Does

- Displays full conversion funnel from ready to won/lost
- Shows conversion rates between each stage
- Tracks execution gap (ready but not sent)
- Lists active blockers preventing pipeline movement
- Allows manual updates to stage values/counts

## Usage

```bash
# Display dashboard
python3 tools/conversion-dashboard.py

# Update a stage
python3 tools/conversion-dashboard.py --update sent 10000 5
python3 tools/conversion-dashboard.py --update response 5000 2
python3 tools/conversion-dashboard.py --update won 25000 1
```

## Output Example

```
============================================================
  🎯 CONVERSION FUNNEL — $739,500 Pipeline
============================================================

READY    $   734,500  (39 msgs)
         Ready to send

SENT     $     5,000  (1 msgs) → 0.7% conv
         Messages delivered

RESPONSE $         0  (0 msgs) → 0.0% conv
         Replies received

CALL     $         0  (0 msgs)
         Calls scheduled

WON      $         0  (0 msgs)
         Deals closed

============================================================
  Overall Conversion: 0.0%
  Execution Gap: 99.3%
  Last Updated: 2026-02-06T14:50:00Z

  🚧 Active Blockers:
     • Gateway restart (1 min → $50K bounties)
     • GitHub auth (5 min → $125K grants)
============================================================
```

## Pipeline Stages

| Stage | Description | Metric |
|-------|-------------|--------|
| **READY** | Messages ready to send | $734,500 (39 msgs) |
| **SENT** | Messages delivered | $5,000 (1 msg) |
| **RESPONSE** | Replies received | $0 (0 msgs) |
| **CALL** | Calls scheduled | $0 (0 msgs) |
| **WON** | Deals closed | $0 (0 msgs) |

## Conversion Metrics

**Stage-to-stage conversion:**
```
READY → SENT:     0.7% ($5K / $734.5K)
SENT → RESPONSE: 0.0% ($0 / $5K)
RESPONSE → CALL:  — (no responses yet)
CALL → WON:       — (no calls yet)
```

**Overall conversion:**
```
WON / READY = 0.0%
```

**Execution gap:**
```
(READY - SENT) / READY = 99.3%
$729.5K sitting ready but not sent
```

## Data Storage

Saves to `data/conversion-funnel.json`:

```json
{
  "stages": {
    "ready": {"value": 734500, "count": 39, "description": "Ready to send"},
    "sent": {"value": 5000, "count": 1, "description": "Messages delivered"},
    "response": {"value": 0, "count": 0, "description": "Replies received"},
    "call": {"value": 0, "count": 0, "description": "Calls scheduled"},
    "won": {"value": 0, "count": 0, "description": "Deals closed"}
  },
  "last_updated": "2026-02-06T14:50:00Z",
  "blockers": [
    "Gateway restart (1 min → $50K bounties)",
    "GitHub auth (5 min → $125K grants)"
  ]
}
```

## When to Use

- **Daily check:** See current pipeline health
- **Before sending:** Check execution gap (why is 99.3% unsent?)
- **After responses:** Update stage values to track conversion
- **Blocker review:** See what's preventing pipeline movement
- **Revenue planning:** Forecast potential revenue based on funnel

## Updating Stages

When messages move between stages:

```bash
# After sending a batch
python3 tools/conversion-dashboard.py --update sent 25000 10

# After receiving responses
python3 tools/conversion-dashboard.py --update response 10000 4

# After scheduling calls
python3 tools/conversion-dashboard.py --update call 5000 2

# After closing deals
python3 tools/conversion-dashboard.py --update won 15000 1
```

## Blockers

Active blockers are listed in the dashboard:
- **Gateway restart** — Blocks $50K bounties (1 min to fix)
- **GitHub auth** — Blocks $125K grants (5 min to fix)

Remove blockers when resolved:
```json
"blockers": []  // Empty = no blockers
```

## Related Tools

- `revenue-tracker.py` — Track individual pipeline items
- `follow-up-tracker.py` — Track follow-ups after sent
- `action-recommender.py` — Prioritize actions based on funnel state

## Key Metrics to Watch

| Metric | Good | Warning | Critical |
|--------|------|---------|----------|
| Execution gap | <20% | 20-50% | >50% |
| Response rate | >10% | 5-10% | <5% |
| Overall conversion | >5% | 1-5% | <1% |

## Created

2026-02-06 — Week 3, pipeline visibility for conversion tracking
