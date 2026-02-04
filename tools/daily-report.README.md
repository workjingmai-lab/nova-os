# daily-report.py

Unified daily reporting tool — consolidates daily-summary.py, daily-briefing.py, and daily-snapshot.py into one tool with multiple modes.

## What It Does

Generates three types of reports from workspace data:
- **summary** — Full daily report (goals, grants, activity, heartbeat stats)
- **briefing** — Auto-generate today.md from incomplete goals
- **snapshot** — Quick status at a glance

## When to Use

- Morning briefing: `python3 daily-report.py briefing` (generates today.md)
- End-of-day summary: `python3 daily-report.py summary`
- Quick status check: `python3 daily-report.py snapshot`
- Historical analysis: `python3 daily-report.py summary --date 2026-02-01`

## How It Works

```bash
# Default: full daily summary
python3 daily-report.py summary

# Generate today.md from goals
python3 daily-report.py briefing

# Quick status snapshot
python3 daily-report.py snapshot

# With options
python3 daily-report.py summary --date 2026-02-01 --format json --output reports/summary.md
```

## Data Sources

- **Goals:** goals/active.md, goals/week-2.md
- **Activity:** diary.md (WORK BLOCK entries)
- **Grants:** grants/tracker.md
- **Blockers:** today.md
- **Heartbeat:** heartbeat/*.jsonl files

## Consolidation Story

Replaced 3 tools:
- daily-summary.py (409 lines)
- daily-briefing.py (312 lines)
- daily-snapshot.py (287 lines)

→ daily-report.py (450 lines, 38% code reduction, same functionality)

## Output Examples

**Summary:**
```markdown
# 📊 Nova's Daily Summary — 2026-02-04

**Generated:** 2026-02-04 12:00:00 UTC

## 🎯 Goals Progress
- Completed: 12/20 (60%)

## 💰 Funding Pipeline
- Grant drafts ready: 5
- Applications submitted: 2

## 📝 Today's Activity
- WORK BLOCK #1411: Documentation gap analysis...
```

**Briefing:** Generates today.md with working memory, next actions, blockers.

**Snapshot:**
```markdown
# 📊 Daily Snapshot — 2026-02-04 12:00 UTC

**Status:** 🟢 On Track

## 🎯 Goals Progress
- 12/20 complete (60%)

## 📝 Activity Today
- 25 work blocks
- 112 tools in workspace
```

## Dependencies

None (uses only workspace files)

## Related Tools

- `diary-digest.py` — Analyze diary patterns
- `goal-tracker.py` — Track goal completion
- `self-improvement-loop.py` — Velocity tracking

---

**Created:** 2026-02-04
**Work block:** 1412
**Purpose:** Unified daily reporting (3→1 consolidation, 38% code reduction)
