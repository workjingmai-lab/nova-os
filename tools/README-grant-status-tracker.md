# Grant Status Tracker

Automated grant pipeline monitor that scans tracked grants for urgent deadlines and generates status reports.

## What It Does

- **Parses** `grants/tracked-grants.md` to extract grant information
- **Checks** deadlines and identifies urgent grants (≤3 days)
- **Generates** status reports with pipeline stats
- **Logs** results to `diary.md` automatically
- **Exits with code** 1 if urgent deadlines found, 0 otherwise (useful for cron/alerting)

## When to Use

**Use when:**
- Running scheduled grant pipeline checks (cron)
- Need visibility into upcoming deadlines
- Generating status reports before sprint planning
- Want automated alerts for time-sensitive grants

**Don't use when:**
- Discovering new grants (use `grant-discovery-tracker.py`)
- Writing grant submissions (use `grant-submit-helper.py`)

## Usage

### Basic Usage
```bash
python tools/grant-status-tracker.py
```

### Cron Integration (Example)
```bash
# Check grants every 6 hours, alert if urgent
0 */6 * * * cd /home/node/.openclaw/workspace && python tools/grant-status-tracker.py
```

### Exit Codes
- **0:** No urgent deadlines (safe to continue)
- **1:** Urgent deadlines found (action required)

## Input Format

Expects `grants/tracked-grants.md` with this structure:

```markdown
### Gitcoin Round 18

- **Source:** Gitcoin Grants
- **Deadline:** 2026-02-15
- **Status:** Applying
- **Amount:** $50,000
- **Notes:** Quadratic funding, need community support

### Ethereum Foundation DevEx

- **Source:** Ethereum Foundation
- **Deadline:** Rolling
- **Status:** Researching
- **Amount:** $100,000
```

## Output Example

### No Urgent Deadlines
```
# 🎯 Grant Status Report
**Generated:** 2026-02-02 13:00:00 UTC

✅ No urgent deadlines (≤3 days)

## 📋 Active Grants

**Gitcoin Round 18** — Applying
  Source: Gitcoin Grants

## 📊 Pipeline Stats

- **Total tracked:** 5
- **Active:** 3
- **Urgent:** 0

GRANT_CHECK_OK
```

### Urgent Deadlines Found
```
# 🎯 Grant Status Report
**Generated:** 2026-02-02 13:00:00 UTC

## 🚨 URGENT — Deadlines ≤3 Days

### Optimism RPGF Season 4
- **Deadline:** 2026-02-05 (3 days)
- **Status:** Applying
- **Source:** Optimism Collective

---
```

## Features

### Deadline Parsing
Supports multiple date formats:
- `2026-02-15` (ISO)
- `February 15, 2026`
- `Feb 15, 2026`
- `15 February 2026`
- `Rolling`, `Ongoing`, `TBD` (ignored for urgency)

### Automatic Logging
Every run is logged to `diary.md`:
```
[2026-02-02T13:00:00Z] Grant check complete — No urgent deadlines
```

### Pipeline Statistics
Tracks:
- Total grants tracked
- Active grants (not backlog/identified)
- Urgent grants (≤3 days)

## Integration

**Works with:**
- `grant-discovery-tracker.py` — Discover new grants to track
- `grant-submit-helper.py` — Generate submissions for tracked grants
- `grants/tracked-grants.md` — Central grant database

## Workflow

1. **Discover** grants with `grant-discovery-tracker.py`
2. **Log** to `grants/tracked-grants.md`
3. **Monitor** with `grant-status-tracker.py` (scheduled via cron)
4. **Submit** with `grant-submit-helper.py` when deadlines approach

## Customization

Edit these values in the script:
- `days_threshold: int = 3` — Change urgency threshold
- `TRACKED_GRANTS_FILE` — Change source file path
- `DIARY_FILE` — Change log destination

## Dependencies

- Python 3.7+
- No external packages (uses stdlib only)

## Related Tools

- `grant-discovery-tracker.py` — Find and evaluate opportunities
- `grant-submit-helper.py` — Generate submission content
- `grant-submission-generator.py` — Full submission builder

---

**Created:** 2026-02-02
**Purpose:** Week 2 Revenue Generation — Automated grant pipeline monitoring
**Status:** ✅ Active
