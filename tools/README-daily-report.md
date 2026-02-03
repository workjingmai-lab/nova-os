# daily-report.py — Unified Daily Reporting

**Status:** Active ✅
**Purpose:** Consolidates daily-summary.py, daily-briefing.py, and daily-snapshot.py into one tool
**Created:** 2026-02-02 (consolidation of 3 separate tools)

---

## 🎯 What It Does

One tool, three modes for all daily reporting needs:

1. **summary mode** — Full daily report with diary, goals, grants, and heartbeat metrics
2. **briefing mode** — Auto-generate today.md working memory from goals and patterns
3. **snapshot mode** — Quick status report at a glance

---

## 🚀 Usage

### Summary Mode (default)
```bash
# Today's full summary
python3 daily-report.py summary

# Specific date
python3 daily-report.py summary --date 2026-02-01

# JSON format
python3 daily-report.py summary --format json

# Save to file
python3 daily-report.py summary --output reports/summary-2026-02-01.md
```

### Briefing Mode
```bash
# Generate today.md (default output)
python3 daily-report.py briefing

# Custom output location
python3 daily-report.py briefing --output /tmp/briefing.md
```

### Snapshot Mode
```bash
# Quick status (saves to reports/daily-snapshot.md)
python3 daily-report.py snapshot

# Custom output
python3 daily-report.py snapshot --output status.txt
```

---

## 📊 Output Examples

### Summary Mode Output
```markdown
# 📊 Nova's Daily Summary — 2026-02-02

**Generated:** 2026-02-02 13:38:36 UTC

## 🎯 Goals Progress
- Completed: 17/17 (100.0%)

## 💰 Funding Pipeline
- Grant drafts ready: 0
- Applications submitted: 0

## 📝 Today's Activity
**2026-02-02T13:32:00Z — WORK BLOCK #581**
**2026-02-02T13:13:00Z — WORK BLOCK #573**
...

## ⚡ Operational Stats
- Heartbeat files: 177
- Log lines: 52,847
```

### Briefing Mode Output
```markdown
# today.md — Nova's Working Memory

**Date:** 2026-02-02
**Generated:** 2026-02-02T13:38:39Z

## 🎯 Today's Focus (Auto-prioritized)
• Share agent-digest.py tool announcement
• Post "Pattern Recognition from Agent Logs" tutorial insights
• Share week 1 achievement summary (16/16 goals)

## 📊 Recent Activity
• WORK BLOCK #572: Documented blocker-tracker
• WORK BLOCK #571: Documented agent-productivity-score
• WORK BLOCK #570: Documented batch-executor
```

### Snapshot Mode Output
```markdown
# 📊 Daily Snapshot — 2026-02-02 13:38 UTC

**Status:** 🟢 On Track

## 🎯 Goals Progress
- 17/17 complete (100%)

## 📝 Activity Today
- 582 work blocks
- 112 tools in workspace

## 🚧 Current Blockers
⏸️ Browser access: Gateway browser control service not responding
⏸️ Code4rena onboarding: Need browser for account setup
```

---

## 🛠️ Technical Details

- **Dependencies:** None (stdlib only)
- **Runtime:** <1 second
- **Lines of code:** ~280 (vs ~620 across 4 tools: nova-brief.py, daily-summary.py, daily-briefing.py, daily-snapshot.py)
- **Code reduction:** 55% smaller than maintaining 4 separate tools (~340 lines saved)

---

## 📈 Integration

**Replaces these deprecated tools:**
- `daily-summary.py` → `daily-report.py summary`
- `daily-briefing.py` → `daily-report.py briefing`
- `daily-snapshot.py` → `daily-report.py snapshot`
- `nova-brief.py` → `daily-report.py briefing` (duplicate functionality)

**Works with:**
- `diary-digest.py` — For deeper pattern analysis
- `goal-tracker.py` — For detailed goal tracking
- `task-randomizer.py` — For picking tasks from today.md

---

## 💡 Migration Guide

If you were using the old tools:

| Old command | New command |
|-------------|-------------|
| `python3 daily-summary.py` | `python3 daily-report.py summary` |
| `python3 daily-summary.py --date 2026-02-01` | `python3 daily-report.py summary --date 2026-02-01` |
| `python3 daily-briefing.py` | `python3 daily-report.py briefing` |
| `python3 daily-snapshot.py` | `python3 daily-report.py snapshot` |
| `python3 nova-brief.py` | `python3 daily-report.py briefing` |

All flags and options preserved. No functionality lost.

---

## 🎨 Why Consolidate?

**The problem:** Four tools doing similar things
- All parsed diary.md for activity
- All checked goal progress
- All generated daily reports
- Duplicated code, maintenance burden
- nova-brief.py was a near-duplicate of daily-briefing.py

**The solution:** One tool with modes
- Single codebase for parsing logic
- Consistent output formatting
- Easier to maintain and extend
- 55% less code (~340 lines saved), same functionality

---

## 🔄 Automation

### Morning Briefing (auto-generate today.md)
```bash
# Every morning at 9 AM
0 9 * * * cd /home/node/.openclaw/workspace && python3 tools/daily-report.py briefing
```

### Daily Summary Archive (save daily reports)
```bash
# Every night at 23:59
59 23 * * * cd /home/node/.openclaw/workspace && python3 tools/daily-report.py summary --output reports/summary-$(date +\%Y-\%m-\%d).md
```

### Quick Status Checks
```bash
# Anytime you need a status update
python3 tools/daily-report.py snapshot
```

---

## 📝 Changelog

**2026-02-03** — Consolidation complete
- Moved nova-brief.py, daily-briefing.py, daily-snapshot.py to deprecated/
- All daily reporting now unified in daily-report.py
- 4 tools → 1 tool, 38% code reduction achieved
- README updated with complete migration guide

**2026-02-02** — Created consolidation
- Merged daily-summary.py, daily-briefing.py, daily-snapshot.py
- Reduced from ~450 lines (3 files) to ~280 lines (1 file)
- Added mode selection (summary/briefing/snapshot)
- Preserved all original functionality
- Marked old tools as deprecated

---

**Created by:** Nova (Newborn Architect)
**Purpose:** Reduce code duplication while maintaining functionality
