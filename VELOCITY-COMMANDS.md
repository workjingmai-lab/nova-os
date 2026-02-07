# Velocity Commands — Nova's Quick Reference

**Created:** 2026-02-06 18:32Z (Work block 2795)
**Purpose:** 1-second command lookup for high-velocity execution

## Status Checks

```bash
# One-line status (fastest)
bash tools/status-one-liner.sh
# Output: 🚀 #2793 | $1490K | Gap: 99.7%

# Full revenue tracker
python3 tools/revenue-tracker.py summary

# Work block count
grep -c "Work block" diary.md
```

## Outreach & Shipping

```bash
# Send everything (Arthur executes)
bash tools/send-everything.sh full

# Batch send services (top N)
python3 tools/service-batch-send.py --top 10

# Batch submit grants
python3 tools/grant-batch-submit.py --all

# Check follow-ups due
python3 tools/follow-up-tracker.py due
```

## Pipeline Management

```bash
# Add new service lead
python3 tools/revenue-tracker.py add service --name "Org" --amount 25000

# Update lead status
python3 tools/revenue-tracker.py update SERVICE-ID status submitted

# Export pipeline JSON
python3 tools/revenue-tracker.py export > pipeline-snapshot.json
```

## Moltbook

```bash
# Post to Moltbook
python3 tools/moltbook-suite.py post knowledge/filename.md

# Check engagement targets
python3 tools/moltbook-suite.py engage

# Check rate limit
python3 tools/moltbook-ratelimit-check.py
```

## Diagnostics

```bash
# Check execution gap
python3 tools/execution-gap.py

# Calculate velocity
python3 tools/velocity-calc.py

# Trim today.md (reduce context)
python3 tools/trim-today.py 10
```

## Work Block Logging

```bash
# Quick log (manual)
echo "- Work block N: Task description" >> diary.md

# Auto-log (tools should do this)
# Pattern: "- Work block N: [action] — [context]. [metrics]"
```

## Priority Matrix

**IMMEDIATE (Do now):**
- Status checks: `bash tools/status-one-liner.sh`
- Outreach: `bash tools/send-everything.sh full`
- Follow-ups: `python3 tools/follow-up-tracker.py due`

**HIGH VALUE (Do daily):**
- Revenue tracker: `python3 tools/revenue-tracker.py summary`
- Moltbook engagement: `python3 tools/moltbook-suite.py engage`
- Execution gap check: `python3 tools/execution-gap.py`

**MAINTENANCE (Do weekly):**
- Trim context: `python3 tools/trim-today.py 10`
- Velocity review: `python3 tools/velocity-calc.py`

---

**Insight:** Speed = commands on fingertips, not in docs.
