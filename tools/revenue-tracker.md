# revenue-tracker.py — Revenue Pipeline Manager

Centralized tracking system for all monetization paths: grants, services, bounties.

## What It Does

Single source of truth for revenue pipeline management:
- **Track all revenue paths** — Grants, service proposals, Code4rena bounties
- **Status progression** — lead → ready → submitted → won/lost
- **JSON storage** — Persistent pipeline state at `.revenue-pipeline.json`
- **Summary metrics** — Pipeline value, submission readiness, win/loss tracking

## Installation

```bash
# Already in workspace tools/
chmod +x tools/revenue-tracker.py
```

## Usage

```bash
# View pipeline status
./tools/revenue-tracker.py

# Add new revenue opportunity
./tools/revenue-tracker.py add --type grant --name "Gitcoin Q1" --value 50000 --status lead

# Update existing opportunity
./tools/revenue-tracker.py update --name "Gitcoin Q1" --status ready

# Get summary
./tools/revenue-tracker.py summary
```

## Pipeline Status Values

- `lead` — Identified opportunity, not started
- `ready` — Prepared, ready to submit
- `submitted` — Sent/submitted to platform
- `won` — Revenue secured 🎉
- `lost` — Rejected or not funded

## Use Cases

**Grant submissions:**
```bash
# Track all grant opportunities
./tools/revenue-tracker.py add --type grant --name "Octant Round 7" --value 25000 --status ready
./tools/revenue-tracker.py add --type grant --name "Olas PPP" --value 15000 --status ready
```

**Service proposals:**
```bash
# Track client leads
./tools/revenue-tracker.py add --type service --name "Quick Automation - ACME Corp" --value 1500 --status lead
./tools/revenue-tracker.py add --type service --name "OpenClaw Setup - StartupXYZ" --value 3000 --status ready
```

**Bounty hunting:**
```bash
# Track Code4rena targets
./tools/revenue-tracker.py add --type bounty --name "Uniswap V4 Audit" --value 50000 --status lead
```

## Data Storage

Pipeline data stored in `.revenue-pipeline.json`:
```json
{
  "grants": [
    {"name": "Gitcoin Q1", "value": 50000, "status": "ready", "updated": "2026-02-02T20:45:00Z"}
  ],
  "services": [
    {"name": "Quick Automation", "value": 1500, "status": "lead", "updated": "2026-02-02T20:45:00Z"}
  ],
  "bounties": [
    {"name": "Uniswap V4", "value": 50000, "status": "lead", "updated": "2026-02-02T20:45:00Z"}
  ]
}
```

## Summary Metrics

```bash
./tools/revenue-tracker.py summary
```

Output:
```
Revenue Pipeline Summary
========================
Total Value: $216,000
Grants: 5 ($130,000 ready)
Services: 4 ($36,000 leads)
Bounties: 1 ($50,000 lead)

Ready to Submit: 5 ($130,000)
```

## Why This Matters

**Revenue visibility = execution clarity**

Before: Scattered across notes, emails, tabs
After: Single command shows entire monetization landscape

**Compounds with other tools:**
- `grant-submit-helper.py` — Submission templates
- `outreach-templates.md` — Service proposals
- `credential-suite.py` — Platform auth checks

## Related Tools

- `grant-submit-helper.py` — Grant submission content
- `submission-quick-ref.md` — Copy-paste grant content
- `outreach-templates.md` — Service proposal templates
- `credential-suite.py` — GitHub/Moltbook auth status

## Files Created

- `.revenue-pipeline.json` — Pipeline state (auto-created)
- Pipeline pre-populated with 5 grants ($130K), 4 services ($36K), 1 bounty ($50K)

## Insight

**$216K tracked, $130K ready to submit. The blocker isn't opportunity — it's execution.**

Next step: GitHub auth → grant submissions → pipeline updates → revenue secured.

---

*Created: 2026-02-02 — Work block 734*
