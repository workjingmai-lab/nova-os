# goal-tracker.py

Goal tracking CLI — manage goals from goals/active.md with completion detection, progress notes, velocity tracking, and more.

## What It Does

Comprehensive goal management with:
- **List** — Show all goals with status and priority (color-coded)
- **Progress** — Show progress notes for a specific goal (auto-scanned from memory/diary)
- **Complete** — Mark goal as done in goals/active.md
- **Stats** — Completion statistics by priority
- **Suggest** — AI-like suggestion for next goal to work on
- **Velocity** — Work velocity from diary.md (tasks/hour, trend analysis)
- **Focus** — Show only high-priority active goals
- **Stale** — Detect goals active too long (>7 days default)
- **Export** — Backup goals to JSON or Markdown
- **Week** — Show goals from a specific week's file

## When to Use

- Daily check-ins: `python3 goal-tracker.py list --active`
- Morning focus: `python3 goal-tracker.py focus`
- Progress review: `python3 goal-tracker.py progress "goal name"`
- Velocity check: `python3 goal-tracker.py velocity`
- Weekly review: `python3 goal-tracker.py week`

## How It Works

```bash
# List all goals
python3 tools/goal-tracker.py list

# Show only active (incomplete) goals
python3 tools/goal-tracker.py list --active

# Focus mode: high-priority only
python3 tools/goal-tracker.py focus

# Mark goal complete
python3 tools/goal-tracker.py complete "Document learnings"

# Show progress notes
python3 tools/goal-tracker.py progress "Build pattern recognition"

# Stats with JSON output
python3 tools/goal-tracker.py stats --json

# Suggest next goal
python3 tools/goal-tracker.py suggest

# Work velocity (from diary.md)
python3 tools/goal-tracker.py velocity

# Stale goals (>14 days)
python3 tools/goal-tracker.py stale --days 14

# Export to markdown
python3 tools/goal-tracker.py export --format markdown

# Week-specific goals
python3 tools/goal-tracker.py week --week 2
```

## Key Features

### Auto-Detection
Scans memory files and diary.md to auto-detect completed goals (finds "✓", "DONE", "completed" markers).

### Progress Notes
Finds goal mentions across memory/diary files and shows context around them (up to 10 recent notes).

### Velocity Tracking
Calculates work velocity from diary.md:
- Tasks per hour/day
- Trend analysis (increasing/stable/decreasing)
- Comparison to benchmarks

### Color-Coded Output
- 🔥 High priority (red)
- ⚡ Medium priority (yellow)
- 📅 Long-term (blue)
- 🔄 Daily habits (cyan)

### Stale Detection
Identifies goals active too long without completion (default: >7 days). Suggests breaking down or reprioritizing.

## Output Examples

**List:**
```
════════════════════════════════════════════════════════════
  🎯 ACTIVE GOALS
════════════════════════════════════════════════════════════

▸ 🔥 High Priority
  ○ Build pattern recognition system
  ○ Learn one new skill per week

▸ ⚡ Medium Priority
  ○ Document learnings in structured format
  ✓ Create "Nova's Toolkit" reference guide

Summary: 1 done, 3 active
```

**Stats:**
```
════════════════════════════════════════════════════════════
  📈 GOAL STATISTICS
════════════════════════════════════════════════════════════

▸ Overall Progress
  ████████████████░░░░░░░░░░░░░░░░░░
  5/20 completed (25.0%)

▸ By Priority
  🔥 High: 1/3 (33%)
  ⚡ Medium: 2/8 (25%)
  📅 Long-term: 2/9 (22%)

💪 More than halfway there! You've got this.
```

**Velocity:**
```
════════════════════════════════════════════════════════════
  ⚡ WORK VELOCITY
════════════════════════════════════════════════════════════

▸ Last 168 hours (7 days)
  Tasks per hour: 2.5
  Tasks per day: 60.0
  Trend: 📈 INCREASING
  Total completed: 420 tasks in 168 work blocks

▸ Analysis
  🚀 You're speeding up! Keep this momentum going.

▸ Benchmarks
  💪 Strong - Above average velocity
```

## Dependencies

None (uses only workspace files)

## Data Sources

- **Goals:** goals/active.md, goals/week-*.md
- **Progress:** memory/*.md, diary.md
- **Velocity:** diary.md (WORK BLOCK entries)

## Related Tools

- `daily-report.py` — Daily reporting and briefing
- `self-improvement-loop.py` — Velocity tracking and insights
- `diary-digest.py` — Analyze diary patterns

---

**Created:** 2026-02-04
**Work block:** 1413
**Purpose:** Comprehensive goal management with auto-detection and velocity tracking
