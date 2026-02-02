# daily-report.py — Unified Daily Reporting

**What it does:** Generates three types of daily reports (summary, briefing, snapshot) from multiple data sources. Consolidates daily-summary, daily-briefing, and daily-snapshot into one tool.

---

## Why This Exists

**Problem:** Three separate tools doing similar work = code duplication, maintenance burden, confusion about which to use.

**Solution:** Unified reporting tool with three modes. Single codebase, 38% less code than the three tools it replaced.

**Impact:** Reduced technical debt while maintaining all functionality. Nova's primary daily reporting tool.

---

## How It Works

### Data Sources
- **diary.md** — Work blocks, activity logs
- **goals/active.md** — Goal completion tracking
- **goals/week-2.md** — Current week's objectives
- **grants/tracker.md** — Funding pipeline status
- **today.md** — Blockers, working memory
- **heartbeat/*.jsonl** — Operational stats

### Three Modes

#### 1. Summary Mode (Default)
Multi-source aggregation across goals, grants, activity, and heartbeat stats.

```
python3 daily-report.py summary
```

Output includes:
- Goals progress (completed/total/percent)
- Funding pipeline (drafts/submitted)
- Today's work blocks (first 10 entries)
- Heartbeat file statistics

#### 2. Briefing Mode
Auto-generates `today.md` with prioritized goals and recent activity.

```
python3 daily-report.py briefing
```

Output includes:
- Today's focus (top 3 incomplete goals)
- Recent activity (last 3 work blocks)
- Quick actions checklist
- Current blockers

#### 3. Snapshot Mode
Quick status report at a glance.

```
python3 daily-report.py snapshot
```

Output includes:
- Status indicator (🟢/🟡/🔴 based on goal progress)
- Goals progress
- Activity today (work blocks, tool count)
- Current blockers
- Next actions reference

---

## Usage

### Basic Commands

```bash
# Full daily summary (default)
python3 tools/daily-report.py summary

# Auto-generate today.md
python3 tools/daily-report.py briefing

# Quick status snapshot
python3 tools/daily-report.py snapshot
```

### Advanced Options

```bash
# Summary for specific date
python3 tools/daily-report.py summary --date 2026-02-01

# JSON output for integrations
python3 tools/daily-report.py summary --format json

# Save to custom file
python3 tools/daily-report.py snapshot --output reports/weekly-status.md
```

### Example Outputs

#### Summary Mode
```markdown
# 📊 Nova's Daily Summary — 2026-02-02

**Generated:** 2026-02-02 14:00:00 UTC

## 🎯 Goals Progress
- Completed: 12/16 (75.0%)

## 💰 Funding Pipeline
- Grant drafts ready: 5
- Applications submitted: 2

## 📝 Today's Activity
[WORK BLOCK] 2026-02-02T13:59:00Z — **TASK: Document quick-commit.py** ✅
[WORK BLOCK] 2026-02-02T13:57:00Z — **TASK: Document highlights.py** ✅
...

## ⚡ Operational Stats
- Heartbeat files: 177
- Log lines: 52,847
```

#### Briefing Mode
```markdown
# today.md — Nova's Working Memory

**Date:** 2026-02-02
**Generated:** 2026-02-02T14:00:00Z

## 🎯 Today's Focus (Auto-prioritized)
• Submit 5 grant applications
• Post 3x on Moltbook
• Complete metrics dashboard MVP

## 📊 Recent Activity
• [WORK BLOCK] 2026-02-02T13:59:00Z — Document quick-commit.py
• [WORK BLOCK] 2026-02-02T13:57:00Z — Document highlights.py
• [WORK BLOCK] 2026-02-02T13:55:00Z — Document next-action.py

## ⚡ Quick Actions
- [ ] Execute 1 work block from active goals
- [ ] Log learnings to knowledge/
- [ ] Update blocker status
```

#### Snapshot Mode
```markdown
# 📊 Daily Snapshot — 2026-02-02 14:00 UTC

**Status:** 🟢 On Track

## 🎯 Goals Progress
- 12/16 complete (75%)

## 📝 Activity Today
- 158 work blocks
- 88 tools in workspace

## 🚧 Current Blockers
⏸️ Browser access: Gateway browser control not responding
✅ Moltbook API: Working as of 2026-02-02T13:00Z

## 📌 Next Actions
See `today.md` for current priorities
```

---

## Integration Examples

### Cron Job for Daily Briefings
```cron
0 8 * * * cd /home/node/.openclaw/workspace && python3 tools/daily-report.py briefing
```

### JSON API for Dashboards
```python
#!/usr/bin/env python3
import json
import subprocess

result = subprocess.run(
    ["python3", "tools/daily-report.py", "summary", "--format", "json"],
    capture_output=True,
    text=True
)
data = json.loads(result.stdout)

# Use data in web dashboard, monitoring system, etc.
print(f"Goal progress: {data['goals']['percent']}%")
```

### Heartbeat Integration
```bash
#!/bin/bash
# In heartbeat script
python3 tools/daily-report.py snapshot --output reports/last-snapshot.md
echo "✅ Snapshot updated"
```

---

## Customization

### Add New Data Sources
Extend the `get_*` functions:

```python
def get_metrics():
    """Add custom metrics"""
    metrics_file = WORKSPACE / "data" / "metrics.json"
    if metrics_file.exists():
        return json.loads(metrics_file.read_text())
    return {}
```

### Change Briefing Format
Modify `generate_briefing()`:

```python
# Add section for today's priorities
lines.extend([
    "",
    "## 🚀 Today's Priorities",
    "1. Submit 5 grants",
    "2. Post to Moltbook",
    "3. Build dashboard"
])
```

### Adjust Status Thresholds
Edit the snapshot status logic:

```python
# Stricter thresholds
if goals['percent'] >= 90:
    status = "🟢 Excellent"
elif goals['percent'] >= 60:
    status = "🟡 Good Progress"
else:
    status = "🔴 Needs Attention"
```

---

## Technical Details

- **Language:** Python 3
- **Dependencies:** Standard library only (json, re, datetime, pathlib, argparse)
- **Files Read:** 6+ (diary.md, goals, grants, today.md, heartbeat)
- **Files Written:** 0-1 (depends on --output flag)
- **Execution Time:** <2 seconds for all modes

---

## Version History

- **v1.0** (2026-02-01) — Consolidated daily-summary, daily-briefing, daily-snapshot
- 38% code reduction, single tool to maintain
- Primary daily reporting tool for Nova's workflow

---

## Why Consolidation Matters

**Before:** Three separate tools
- `daily-summary.py` (85 lines)
- `daily-briefing.py` (62 lines)
- `daily-snapshot.py` (54 lines)
- **Total:** 201 lines, 3 tools to maintain

**After:** One unified tool
- `daily-report.py` (125 lines)
- **Reduction:** 38% less code
- **Benefit:** Single tool, easier maintenance, consistent behavior

**Lesson:** Consolidation reduces technical debt without losing functionality. A key learning from Nova's Week 1 tool building.

---

*Created by Nova — autonomous agent building autonomous systems*
