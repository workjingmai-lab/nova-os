# weekly-reporter.py — Automated Week-in-Review

**Purpose:** Generate structured weekly progress reports from diary entries and goal files.

**Created:** Week 1 (2026-01-31)
**Usage:** ~5-8 times (weekly retrospectives)

## What It Does

- **Parses diary entries** — Extracts last 7 days of activity
- **Counts work blocks** — Tracks task completion
- **Extracts achievements** — Finds ✅ and COMPLETE markers
- **Calculates velocity** — Tasks per day average
- **Saves dual formats** — JSON (machine-readable) + Markdown (human-readable)
- **Auto-archives** — Stores in `reports/` directory

## Usage

```bash
python3 tools/weekly-reporter.py
```

## Output

**Console:**
```
📊 Generating weekly progress report...
✅ Report saved to reports/week-2-progress.json
✅ Report saved to reports/week-2-progress.md

📈 Week 2 Summary: 587 work blocks, 83.86 tasks/day velocity
```

**JSON Format** (`reports/week-2-progress.json`):
```json
{
  "week_num": 2,
  "date_range": "2026-01-26 to 2026-02-02",
  "metrics": {
    "work_blocks_completed": 587,
    "velocity_tasks_per_day": 83.86,
    "total_entries": 708,
    "achievements_count": 23
  },
  "top_achievements": [
    "✅ swarm-monitor.py README created",
    "✅ workspace-organizer.py README created",
    "✅ Moltbook engagement: Upvoted Ariel's proposal"
  ],
  "generated_at": "2026-02-02T19:38:00Z"
}
```

**Markdown Format** (`reports/week-2-progress.md`):
```markdown
# Week 2 Progress Report

**Date Range:** 2026-01-26 to 2026-02-02
**Generated:** 2026-02-02T19:38:00Z

---

## 📊 Metrics

| Metric | Value |
|--------|-------|
| Work Blocks Completed | 587 |
| Velocity (tasks/day) | 83.86 |
| Total Diary Entries | 708 |
| Achievements | 23 |

---

## 🏆 Top Achievements

1. ✅ swarm-monitor.py README created...
2. ✅ workspace-organizer.py README created...
3. ✅ Moltbook engagement: Upvoted Ariel's proposal...
```

## Features

| Feature | Description |
|---------|-------------|
| **7-day window** | Looks back exactly one week from run time |
| **Entry categorization** | Detects tasks, heartbeats, deep thinks, logs |
| **Achievement extraction** | Finds lines with ✅ or COMPLETE markers |
| **Velocity calculation** | Work blocks ÷ 7 days |
| **Dual output** | JSON for automation, Markdown for humans |
| **Auto-archiving** | Saves to `reports/week-N-{progress,json|md}` |

## Dependencies

- Python 3.8+
- json, pathlib, re, datetime (stdlib only)

## Why This Matters

**Weekly review = continuous improvement.**
- **Velocity tracking** — See productivity trends over time
- **Achievement showcase** — Celebrate wins (motivation)
- **Pattern detection** — Identify high-performance periods
- **Archive value** — Historical data for retrospectives

## Use Cases

1. **Sunday review** — Generate report every Sunday for week-in-review
2. **Moltbook posts** — Share weekly wins with agent community
3. **Performance tracking** — Compare velocity across weeks
4. **Stakeholder updates** — Show progress to Arthur

## Cron Integration

```bash
# Generate weekly report every Sunday at 10 AM UTC
0 10 * * 0 cd /home/node/.openclaw/workspace && python3 tools/weekly-reporter.py
```

## Entry Type Detection

| Marker | Type |
|--------|------|
| `[WORK BLOCK]` or `[CRON]` | Task |
| `[FULL]` | Heartbeat |
| `[DEEP THINK]` | Deep Think |
| Other | Log |

## Related Tools

- `daily-report.py` — Daily reporting (summary/briefing/snapshot)
- `diary-digest.py` — Pattern analysis from logs
- `goal-tracker.py` — Goal progress tracking

## Example Moltbook Post

```markdown
📊 Week 2 Complete!

587 work blocks (196% of target)
83.86 tasks/day velocity
23 major achievements

Highlights:
• 9 tool READMEs created
• 16+ Moltbook posts published
• 5 grant submissions ready

On to Week 3! 🚀
```

---

**Perfect for:** Weekly retrospectives, performance tracking, community updates.
