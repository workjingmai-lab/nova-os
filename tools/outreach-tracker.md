# outreach-tracker.py — Lead & Proposal Management

**Purpose:** Track outreach leads, proposals sent, and follow-ups

## Quick Start

```bash
# Add a new lead
python3 tools/outreach-tracker.py add "Company X" --type "service" --value "5K"

# List all leads
python3 tools/outreach-tracker.py list

# Show leads by status
python3 tools/outreach-tracker.py status "contacted"

# Update proposal status
python3 tools/outreach-tracker.py update <lead-id> --status "proposed"

# Show pipeline value
python3 tools/outreach-tracker.py pipeline
```

## Lead Types

- **service** — Consulting/automation services ($1K-$25K)
- **grant** — Grant opportunities ($5K-$150K)
- **partnership** — Collaboration opportunities
- **audit** — Security audit engagements (Code4rena)

## Pipeline Stages

1. **identified** — Lead discovered
2. **contacted** — Initial outreach sent
3. **proposed** — Proposal delivered
4. **negotiating** — Terms discussion
5. **closed** — Deal won/lost

## Data Storage

`data/outreach/leads.json` — All lead records and history

---

**Created:** 2026-02-02
**Usage:** Part of Nova's revenue generation pipeline
