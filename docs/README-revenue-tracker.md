# README-revenue-tracker.md

## revenue-tracker.py

Centralized revenue pipeline tracker. Manages grants, services, and bounties with status tracking from lead → ready → submitted → won/lost.

### Usage

```bash
# Add opportunities
python3 tools/revenue-tracker.py add grant --name "Gitcoin" --potential 5000 --status ready
python3 tools/revenue-tracker.py add service --name "Quick Automation" --potential 2000 --status lead
python3 tools/revenue-tracker.py add bounty --name "Code4rena" --potential 10000 --status ready

# Update status
python3 tools/revenue-tracker.py update grants --name "Gitcoin" --status submitted

# View pipeline
python3 tools/revenue-tracker.py list
python3 tools/revenue-tracker.py summary
```

### Status Values

| Status | Icon | Meaning |
|--------|------|---------|
| lead | 🔵 | Identified but not ready |
| ready | 🟢 | Ready to submit/send |
| submitted | 🟡 | Sent, awaiting response |
| won | ✅ | Closed successfully |
| lost | ❌ | Closed unsuccessfully |

### Commands

#### `add <category>`
Add new opportunity to a category.

**Categories:** `grant`, `service`, `bounty`

**Options:**
- `--name`: Opportunity name
- `--potential`: Dollar amount ($)
- `--status`: One of lead/ready/submitted/won/lost
- `--notes`: Optional notes

#### `update <category>`
Update existing opportunity status.

**Options:**
- `--name`: Opportunity name (exact match)
- `--status`: New status
- `--potential`: Update amount
- `--notes`: Update notes

#### `list`
Display all opportunities by category, sorted by potential (highest first).

#### `summary`
Display pipeline totals and conversion metrics.

```
REVENUE PIPELINE SUMMARY
========================

GRANTS ($50,000)
  🟢 Ready:      $25,000 (50.0%)
  🟡 Submitted:  $25,000 (50.0%)

SERVICES ($200,000)
  🟢 Ready:      $150,000 (75.0%)
  🟡 Submitted:  $50,000 (25.0%)

TOTAL PIPELINE: $250,000
```

### Data File

Stored at: `data/revenue-pipeline.json`

```json
{
  "grants": [...],
  "services": [...],
  "bounties": [...]
}
```

### Pipeline Flow

```
lead → ready → submitted → won
                    ↓
                  lost
```

### Integration

- Used by `operator-status.py` for pipeline checks
- Used by `conversion-pulse.py` for funnel metrics
- Creates `data/revenue-pipeline.json` if missing

### Dependencies

- Python 3.6+
- Standard library (json, argparse, datetime, pathlib)

### Created

Work block ~1700 — Week 2 revenue pivot toolkit
