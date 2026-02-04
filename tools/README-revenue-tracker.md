# Revenue Tracker — Pipeline Visibility Tool

Track all revenue opportunities (grants, services, bounties) in one centralized system.

## What It Does

**Revenue Tracker** gives you single-source-of-truth visibility into your entire revenue pipeline:
- **Track opportunities** across 3 categories: grants, services, bounties
- **Status workflow**: lead → ready → submitted → won/lost
- **Pipeline metrics**: total potential, ready to submit, submitted, won
- **Conversion tracking**: calculate win rates automatically

## Why It Matters

Without tracking = "How much is in the pipeline?"
With tracking = "$2,180K total (grants $130K + services $2,007K + bounties $43K), 103 opportunities, 5 won"

Revenue = numbers game. Tracking = control.

## Commands

### Add Opportunity
```bash
python tools/revenue-tracker.py add grant --name "Gitcoin" --potential 5000 --status "ready"
python tools/revenue-tracker.py add service --name "Quick Automation" --potential 2000 --status "lead"
python tools/revenue-tracker.py add bounty --name "Code4rena" --potential 10000 --status "submitted"
```

**Options:**
- `--name`: Opportunity name (required)
- `--potential`: Potential value in dollars (required)
- `--status`: lead | ready | submitted | won | lost (default: lead)
- `--notes`: Additional context (optional)

### List Opportunities
```bash
# List all
python tools/revenue-tracker.py list

# Filter by category
python tools/revenue-tracker.py list --category grants
python tools/revenue-tracker.py list --category services

# Filter by status
python tools/revenue-tracker.py list --status ready
python tools/revenue-tracker.py list --status submitted
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
  Total items: 95
  Potential: $2,007,000
  Ready to submit: $2,007,000
  Submitted: $0
  Won: $0

BOUNTIES:
  Total items: 3
  Potential: $43,000
  Ready to submit: $43,000
  Submitted: $0
  Won: $0

============================================================
TOTAL PIPELINE: $2,180,000
WON: $0
Conversion rate: 0.0%
```

## Data File

**Location:** `~/.openclaw/workspace/data/revenue-pipeline.json`

**Structure:**
```json
{
  "grants": [
    {
      "name": "Gitcoin",
      "potential": 5000,
      "status": "ready",
      "notes": "Round 19 open",
      "created": "2026-02-01T10:00:00",
      "updated": "2026-02-01T10:00:00"
    }
  ],
  "services": [...],
  "bounties": [...]
}
```

## Status Icons

- 🔵 **Lead**: Identified but not qualified
- 🟢 **Ready**: Qualified, ready to execute
- 🟡 **Submitted**: Proposal sent, awaiting response
- ✅ **Won**: Revenue realized
- ❌ **Lost**: Opportunity closed

## Workflow Integration

### Grant Submissions
```bash
# 1. Add discovered grant
python tools/revenue-tracker.py add grant --name "Octant" --potential 50000 --status "lead"

# 2. Mark ready when submission prepared
# Edit JSON or add new entry with status "ready"

# 3. Mark submitted
python tools/revenue-tracker.py add grant --name "Octant" --potential 50000 --status "submitted"

# 4. Update to won/lost when decided
python tools/revenue-tracker.py add grant --name "Octant" --potential 50000 --status "won"
```

### Service Pipeline
```bash
# Track service opportunities through funnel
python tools/revenue-tracker.py add service --name "Quick Automation" --potential 2000 --status "lead"
python tools/revenue-tracker.py add service --name "Multi-Agent System" --potential 25000 --status "ready"
```

### Bounty Hunting
```bash
# Track competitive audit bounties
python tools/revenue-tracker.py add bounty --name "Code4rena" --potential 5000 --status "submitted"
```

## Related Tools

- **service-outreach-tracker.py** — Track service outreach messages (lead → contacted → responded → closed)
- **response-tracker.py** — Track incoming responses to sent messages
- **pipeline-snapshot.py** — Quick snapshot of entire pipeline
- **roi-scenario-calculator.py** — Calculate realistic revenue scenarios

## Usage Tips

1. **Add early**: Track opportunities when discovered (lead status)
2. **Update frequently**: Change status as opportunities progress
3. **Review weekly**: Check conversion rates, focus on high-value ready items
4. **Backup data**: JSON file is your single source of truth

## Example Pipeline Evolution

**Week 1:**
```
TOTAL PIPELINE: $50,000
- 2 leads, 1 ready
```

**Week 2:**
```
TOTAL PIPELINE: $2,180,000
- 103 opportunities, 103 ready
- BUILD phase complete
```

**Week 4:**
```
TOTAL PIPELINE: $2,180,000
WON: $15,000
Conversion rate: 0.7%
- 5 submitted, 2 won, 3 lost
```

## Quick Reference

```bash
# Add grant
python tools/revenue-tracker.py add grant --name "NAME" --potential 5000 --status "ready"

# Add service
python tools/revenue-tracker.py add service --name "NAME" --potential 2000 --status "lead"

# Add bounty
python tools/revenue-tracker.py add bounty --name "NAME" --potential 10000 --status "submitted"

# List all
python tools/revenue-tracker.py list

# Summary
python tools/revenue-tracker.py summary
```

---

**Created:** 2026-02-03
**Category:** Revenue Execution
**Dependencies:** None (pure Python)
**Data:** `data/revenue-pipeline.json`
