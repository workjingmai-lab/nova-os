# next-action.py — Highest ROI Next Action

## What
Shows the single highest-ROI action Arthur can take RIGHT NOW to convert pipeline to revenue.

## Why
99.5% execution gap = $920K ready, $5K shipped. Decision paralysis kills velocity. This tool answers "What should I do?" in 30 seconds with data-driven ROI ranking.

## How
Reads revenue-pipeline.json, calculates ROI (value/time) for all ready opportunities, ranks by highest ROI, shows blockers and execution gap.

## Commands
```bash
python3 tools/next-action.py
```

## Example Output
```
============================================================
🎯 NEXT ACTION — Highest ROI Move
============================================================

Gateway restart (1 min → $50,000 bounties unblocked)

💰 Value: $50,000
⏱️  Time: 1 min
📈 ROI: $50,000/min

============================================================

📊 Execution Gap: $920,000 ready, $5,000 submitted
   Gap: 99.5% — Time to ship! 🚀

🚧 Blockers:
   Grants: GitHub CLI auth needed (5 min → $125K unblocked)
   Services: ✅ NO BLOCKERS
   Bounties: Browser access (needs gateway restart)
```

## Workflow
1. Run `python3 tools/next-action.py`
2. See highest-ROI action (sorted by value/time)
3. Execute immediately
4. Repeat until gap closed

## Data Sources
- `revenue-pipeline.json` — pipeline status, blockers, ready amounts
- ROI calculation = value ÷ time (minutes)

## Key Features
- **30-second clarity**: No decision paralysis, just "do this"
- **Data-driven ranking**: Ranks by ROI, not gut feel
- **Blocker visibility**: Shows exactly what's blocking each category
- **Gap tracking**: Shows execution gap percentage

## Created
Work block 2551 (2026-02-06 08:33Z)

## Part of Shipping Phase Infrastructure
- TODAY-SHIPPING-MANIFEST.md — What to send today
- followup-tracker.py — Post-shipping workflow
- service-batch-send.py — Batch sending tool
- next-action.py — THIS — Highest-ROI prioritizer
