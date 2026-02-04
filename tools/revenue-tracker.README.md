# revenue-tracker.py — Pipeline Visibility Tool

**Purpose:** Single source of truth for all revenue opportunities across grants, services, and bounties.

## Why This Matters

You can't improve what you don't measure. revenue-tracker creates a clear, JSON-based pipeline that tracks every opportunity from lead → won/lost.

## What It Does

- Tracks revenue across 3 channels: grants, services, bounties
- Records status progression: lead → ready → submitted → won/lost
- Calculates total pipeline value and blockers
- Outputs JSON for programmatic access

## Usage

```bash
python3 tools/revenue-tracker.py
```

## Pipeline JSON Structure

```json
{
  "grants": {
    "total": 130000,
    "opportunities": [
      {
        "name": "Gitcoin",
        "value": 50000,
        "status": "ready",
        "blocker": "GitHub repo not pushed"
      }
    ]
  },
  "services": {
    "total": 2057000,
    "opportunities": [...]
  },
  "bounties": {
    "total": 50000,
    "opportunities": [...]
  }
}
```

## Key Fields

- **name:** Opportunity identifier
- **value:** Dollar amount (USD)
- **status:** lead | ready | submitted | won | lost
- **blocker:** What's preventing execution (if any)

## Real-World Impact

**Nova's Pipeline (Feb 4, 2026):**
- Total: $2,237K tracked
- Services: $2,057K (NO blockers → ready to execute)
- Grants: $130K (blocked: GitHub auth)
- Bounties: $50K (blocked: browser access)

**Visibility = Clarity**
Without this tool: "Some opportunities maybe?"
With this tool: "$2,237K tracked, $2,057K ready, 2 blockers identified"

## Integration

Parses revenue-pipeline.json in workspace root. Update that file to track new opportunities.

## See Also

- `tools/revenue-tracker.py` — Implementation
- `revenue-pipeline.json` — Data store
- `knowledge/revenue-tracking.md` — Methodology docs

---

**Created:** 2026-02-04
**Purpose:** Pipeline visibility = execution clarity
