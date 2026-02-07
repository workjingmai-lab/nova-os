# conversion-tracker.py

Track outreach conversion rates through the entire funnel.

## Purpose

Week 4 tool: Optimize conversion, not just pipeline. Tracks leads from "sent" through "closed_won" or "closed_lost".

## Usage

```bash
# Add a new lead
python3 conversion-tracker.py add "Ethereum Foundation" --value 40000 --source "cold-outreach"

# Update lead stage
python3 conversion-tracker.py update "Ethereum Foundation" --stage call_booked

# Show funnel stats
python3 conversion-tracker.py stats

# List all leads
python3 conversion-tracker.py list
```

## Conversion Funnel

1. **sent** — Message sent
2. **opened** — Message opened (if tracked)
3. **replied** — Prospect replied
4. **call_booked** — Meeting scheduled
5. **proposal_sent** — Proposal delivered
6. **closed_won** — Deal won
7. **closed_lost** — Deal lost

## Data File

Stores data in `data/conversions.json`:
```json
{
  "version": "1.0",
  "last_updated": "2026-02-07T10:45:00",
  "leads": [...],
  "totals": {...},
  "rates": {...}
}
```

## Why This Matters

Pipeline value is meaningless without conversion tracking. This tool answers:
- What's our reply rate?
- What stage do we lose most leads?
- Which source has best conversion?

## Created

2026-02-07 — Work block 3264
