# revenue-tracker.py - Revenue Opportunity Pipeline

Track all revenue opportunities (grants, services, bounties) in one centralized system.

## Why It Matters

**Revenue visibility = execution clarity.** Without a single source of truth, opportunities leak through the cracks. This tool creates a $2,237K pipeline tracker that shows:
- What's ready to execute (green = go)
- What's blocked (needs unblocking)
- What's submitted (in progress)
- What's won/lost (conversion tracking)

## Usage

### Add a Revenue Opportunity

```bash
# Add a grant opportunity
python tools/revenue-tracker.py add grant --name "Gitcoin" --potential 5000 --status "ready"

# Add a service lead
python tools/revenue-tracker.py add service --name "Quick Automation" --potential 2000 --status "lead" --notes "Website contact form"

# Add a bounty
python tools/revenue-tracker.py add bounty --name "Code4rena Audit" --potential 5000 --status "lead"
```

**Status values:** `lead` | `ready` | `submitted` | `won` | `lost`

### List Opportunities

```bash
# List all opportunities
python tools/revenue-tracker.py list

# Filter by category
python tools/revenue-tracker.py list --category grants

# Filter by status
python tools/revenue-tracker.py list --status ready
```

### Show Summary

```bash
python tools/revenue-tracker.py summary
```

**Output:**
```
💰 REVENUE PIPELINE SUMMARY
============================================================

GRANTS:
  Total items: 5
  Potential: $130,000
  Ready to submit: $130,000
  Submitted: $0
  Won: $0

SERVICES:
  Total items: 25
  Potential: $2,057,000
  Ready to submit: $2,057,000
  Submitted: $0
  Won: $0

============================================================
TOTAL PIPELINE: $2,237,000
WON: $0
Conversion rate: 0.0%
```

## Data Storage

Pipeline data stored in: `data/revenue-pipeline.json`

Format:
```json
{
  "grants": [
    {
      "name": "Gitcoin",
      "potential": 5000,
      "status": "ready",
      "notes": "",
      "created": "2026-02-04T06:00:00",
      "updated": "2026-02-04T06:00:00"
    }
  ],
  "services": [],
  "bounties": []
}
```

## Key Insight

**Pipeline tracking prevents revenue leakage.** Every opportunity is tracked from lead → ready → submitted → won/lost. No more "I forgot about that grant."

## See Also

- `tools/grant-submit-helper.py` - Grant submission templates
- `tools/service-templates/` - Service proposal templates
- `knowledge/1000-work-blocks-milestone.md` - How $302K pipeline was built
