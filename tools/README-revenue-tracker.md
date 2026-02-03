# Revenue Tracker Tools

Nova has TWO revenue tracking tools for different purposes:

## 1. `revenue-tracker.py` (workspace root)

**Purpose:** Quick pipeline status viewer

**Usage:**
```bash
python3 revenue-tracker.py
```

**Features:**
- Reads `revenue-pipeline.json` from workspace root
- Displays formatted snapshot of $285K pipeline
- Shows blockers and next actions
- No arguments needed — just run it

**Output:**
- Total pipeline value
- Category breakdown (grants, services, bounties)
- Blocker visibility
- Metrics (work blocks, velocity)
- Prioritized next actions

**Use when:** You need a quick status check on the pipeline

---

## 2. `tools/revenue-tracker.py` (CLI tool)

**Purpose:** Full pipeline management system

**Usage:**
```bash
# Add opportunities
python tools/revenue-tracker.py add grant --name "Gitcoin" --potential 5000 --status "ready"
python tools/revenue-tracker.py add service --name "Quick Automation" --potential 2000 --status "lead"

# List opportunities
python tools/revenue-tracker.py list
python tools/revenue-tracker.py list --category grants --status ready

# Show summary
python tools/revenue-tracker.py summary
```

**Features:**
- Add/list revenue opportunities
- Track status progression (lead → ready → submitted → won/lost)
- Filter by category and status
- Conversion rate tracking
- Saves to `data/revenue-pipeline.json`

**Use when:** You need to manage individual opportunities, track submissions, or analyze conversion rates

---

## Data Files

The tools use different data files:

| Tool | Data File | Purpose |
|------|-----------|---------|
| `revenue-tracker.py` | `revenue-pipeline.json` (root) | High-level pipeline snapshot |
| `tools/revenue-tracker.py` | `data/revenue-pipeline.json` | Detailed item tracking |

**Note:** These are separate files. The root-level file is for quick status viewing; the data/ file is for detailed tracking.

---

## Current Pipeline (as of 2026-02-02T23:40Z)

- **Total:** $285,000
- **Grants:** $130,000 (ready, blocked by GitHub auth)
- **Services:** $105,000 (13 proposals ready, 0 sent)
- **Bounties:** $50,000 (setup, blocked by browser access)

---

## Next Actions

1. **UNBLOCK GRANTS** ($130K): GitHub auth needed (Arthur action)
2. **SEND PROPOSALS**: 13 service messages ready to send
3. **UNBLOCK BOUNTIES** ($50K): Browser access needed (gateway restart)

---

*Created: 2026-02-02T23:45Z — Work block 771*
