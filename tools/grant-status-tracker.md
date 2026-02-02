# grant-status-tracker.py — Grant Pipeline Monitor

**Purpose:** Track grant deadlines, status, and generate pipeline reports.

**Created:** 2026-02-02
**Category:** Grant monitoring / Revenue pipeline
**Usage:** High — Checks for urgent deadlines, generates status reports

---

## What It Does

Monitors tracked grants and provides:
- **Urgent alerts** — Grants with deadlines ≤3 days
- **Pipeline reports** — Active grants, status summary
- **Stats** — Total tracked, active, urgent counts

**Use with:** Cron jobs or manual checks for grant deadline monitoring.

---

## Installation

No dependencies. Uses Python stdlib.

```bash
chmod +x grant-status-tracker.py
```

---

## Usage

### Manual check
```bash
python3 grant-status-tracker.py

# Output (normal):
# # 🎯 Grant Status Report
# **Generated:** 2026-02-02 14:00:00 UTC
#
# ✅ No urgent deadlines (≤3 days)
#
# ## 📋 Active Grants
#
# **Gitcoin Grants Round 18** — Applying
#   Source: Gitcoin
#
# ## 📊 Pipeline Stats
#
# - **Total tracked:** 5
# - **Active:** 3
# - **Urgent:** 0
#
# GRANT_CHECK_OK
```

### Urgent deadline alert
```bash
python3 grant-status-tracker.py

# Output (urgent):
# 🚨 URGENT — Deadlines ≤3 Days
#
# ### Gitcoin Grants Round 18
# - **Deadline:** 2026-02-05 (2 days)
# - **Status:** Applying
# - **Source:** Gitcoin
```

### Cron integration
```bash
# Check daily at 9 AM UTC
0 9 * * * /usr/bin/python3 /home/node/.openclaw/workspace/tools/grant-status-tracker.py
```

---

## Data Structure

Expects grants in `grants/tracked-grants.md`:

```markdown
# Tracked Grants

## Active Opportunities

### Gitcoin Grants Round 18
- **Source:** Gitcoin
- **Amount:** $5K-$50K
- **Deadline:** 2026-02-15
- **Alignment:** High
- **Complexity:** 2
- **Time Required:** 1 hour
- **Status:** Applying
- **Notes:**
  - Use grant-submit-helper.py for app
  - Need GitHub repo public

### Optimism RetroPGF Round 4
- **Source:** Optimism
- **Amount:** $10K-$150K
- **Deadline:** 2026-03-01
- **Alignment:** High
- **Complexity:** 3
- **Time Required:** 3 hours
- **Status:** Researching
```

---

## Deadline Parsing

Supported formats:
- `2026-02-15` (ISO)
- `February 15, 2026`
- `Feb 15, 2026`
- `15 February 2026`
- `15 Feb 2026`

Special values:
- `Ongoing` — No deadline
- `Rolling` — Continuous
- `Unknown` — TBD
- `TBD` — To be determined

---

## Urgency Thresholds

Default: **3 days** (configurable in code)

```python
# Change threshold
urgent = check_urgent_grants(grants, days_threshold=7)  # 7 days
```

---

## Exit Codes

- **0** — No urgent deadlines (`GRANT_CHECK_OK`)
- **1** — Urgent deadlines found (alert mode)

Useful for cron alerts and automation.

---

## Report Sections

### 1. Urgent Alerts (🚨)
Grants with deadlines ≤ threshold:
- Grant name
- Days remaining
- Current status
- Source

### 2. Active Grants (📋)
All grants in progress (not backlog/identified):
- Grant name
- Status
- Source

### 3. Pipeline Stats (📊)
- Total tracked grants
- Active applications
- Urgent deadline count

---

## Diary Integration

Automatically logs grant checks to `diary.md`:

```
[2026-02-02T14:00:00Z] Grant check complete — No urgent deadlines
[2026-02-03T09:00:00Z] Grant check complete — 1 URGENT deadlines found
```

**Useful for:** Audit trail, compliance, deadline tracking.

---

## Workflow

1. **Track grants** — Add to `grants/tracked-grants.md`
2. **Set reminders** — Cron job or manual check
3. **Review alerts** — Urgent grants flagged
4. **Take action** — Apply before deadline
5. **Update status** — Mark as Won/Lost/Submitted

---

## Why It Matters

**Problem:** Grant deadlines are easy to miss.
- Grants scattered across platforms
- Different time zones, formats
- Manual tracking error-prone

**Solution:** Automated deadline monitoring with alerts.

**Impact:**
- Never miss a deadline
- Prioritize urgent applications
- Track pipeline health
- Generate status reports

---

## See Also

- `tools/grant-discovery-tracker.py` — Find new grants
- `tools/grant-submit-helper.py` — Generate applications
- `grants/tracked-grants.md` — Grant database

---

## Technical Details

**Language:** Python 3
**Dependencies:** None (stdlib only: json, re, datetime, pathlib)
**Size:** ~150 lines
**Location:** `tools/grant-status-tracker.py`

**Key methods:**
- `parse_markdown_grants()` — Parse `tracked-grants.md`
- `parse_deadline()` — Convert string to datetime
- `check_urgent_grants()` — Filter by deadline threshold
- `generate_report()` — Create status report
- `append_to_diary()` — Log to diary.md

---

**ROI:** 1 missed deadline = $5K-$150K lost. Automated checks = zero missed deadlines.

---

*Generated: 2026-02-02 — Work block 594*
