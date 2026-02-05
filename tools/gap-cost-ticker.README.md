# gap-cost-ticker.py

## What

Shows real-time cost of the execution gap — makes the invisible visible.

## Why

The execution gap is abstract ($14K/min, $20M/day). This tool makes it concrete:
- Days since gap was identified
- Revenue at risk
- Opportunity cost per minute/hour/day
- Total cost to date

**Urgency needs to be seen to be felt.**

## Usage

```bash
python3 tools/gap-cost-ticker.py
```

## Output Example

```
╔════════════════════════════════════════════════════════════╗
║         🚨 EXECUTION GAP COST TICKER 🚨                    ║
╚════════════════════════════════════════════════════════════╝

⏱️  Days Waiting:        0 days
💰 Revenue at Risk:     $435K

💸 Opportunity Cost:
   • Per minute:         $14K/min
   • Per hour:           $842K/hr
   • Per day:            $435K/day

📉 Total Cost to Date:   $0

⚡  Close the gap: 31 minutes → $435K submitted
   Run: python3 tools/execution-gap.py
```

## Related Tools

- `execution-gap.py` — Shows gap between POTENTIAL and KINETIC revenue
- `revenue-tracker.py` — Tracks full pipeline status
- `DAILY-GAP-REMINDER.md` — Manual daily check-in

## Created

Work block 1840 — 2026-02-05
