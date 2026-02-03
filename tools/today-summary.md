# today-summary.py — Human-Readable Daily Summary

**Purpose:** Generate a concise, human-friendly summary of today's work for Arthur to quickly review Nova's accomplishments.

**Created:** Week 1 (2026-01-31)
**Usage:** ~5-10 times (daily status reports)

## What It Does

- **Extracts today's diary entries** — Parses diary.md for current date
- **Counts completed tasks** — Looks for task completion markers
- **Tracks activity metrics** — Tools built, posts made, files created
- **Shows goals progress** — Pulls completion status from active.md
- **Lists blockers** — Extracts current blockers from today.md
- **Saves report** — `reports/today-summary.md`

## Usage

```bash
python3 tools/today-summary.py
```

## Output

**Console + File:**
```markdown
# 📋 Nova's Day in Review — February 02, 2026

## ✅ What Got Done (12 tasks)
- swarm-monitor.py README created
- workspace-organizer.py README created
- daily-output-tracker.py README created
- credential-suite.py README created
- daily-summary.py README created (DEPRECATED)
- Moltbook engagement: Upvoted Ariel's humanAI Community proposal
...

## 📊 By the Numbers
- **Tools built today:** ~6 new files
- **Total tools in arsenal:** 112
- **Social posts:** 3

## 🎯 Goals Status
- **Week 1 Progress:** 16/16 complete (100%)

## ⚡ Current Blockers
- Browser access: Gateway browser control service not responding
- GitHub push: Pending Arthur action

---
*Generated at 19:35 UTC | Run `./tools/today-summary.py` for fresh data*
```

## Features

| Feature | Description |
|---------|-------------|
| **Task extraction** | Finds completed tasks from diary entries |
| **Tool counting** | Scans `tools/` directory for `.py` files |
| **Social tracking** | Counts Moltbook posts and social engagement |
| **Goals parsing** | Reads completion checkboxes from active.md |
| **Blocker detection** | Pulls current blockers from today.md |

## Dependencies

- Python 3.8+
- pathlib, re, datetime (stdlib only)

## Why This Matters

**Human-AI alignment requires visibility.**
- Arthur can quickly scan accomplishments without reading 1000+ diary lines
- Communication bridge between agent activity and human oversight
- Creates sense of progress and momentum

## Use Cases

1. **Daily standup** — Arthur runs it each morning to see what happened overnight
2. **Weekly review** — Archive reports for retrospective analysis
3. **Stakeholder updates** — Share progress summaries with others

## Task Detection Patterns

```python
# Looks for these patterns in diary entries:
- "**Task XXX COMPLETE**"
- "- Built ..."
- "- Created ..."
- "- Wrote ..."
- "- Fixed ..."
- "- Deployed ..."
```

## Related Tools

- `daily-report.py` — Comprehensive daily reporting (multiple modes)
- `diary-digest.py` — Pattern analysis from logs
- `goal-tracker.py` — Goal progress tracking

## Example Integration with Cron

```bash
# Generate daily summary at 6 AM UTC
0 6 * * * cd /home/node/.openclaw/workspace && python3 tools/today-summary.py
```

---

**Perfect for:** Operators who want quick visibility into agent activity without deep-diving into raw logs.
