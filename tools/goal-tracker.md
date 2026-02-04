# goal-tracker.py

**The most complex tool in Nova's toolkit** — Goal management, progress tracking, velocity analysis, and completion detection from memory files.

## Purpose

Track goals from `goals/active.md`, show progress, mark complete, calculate velocity from `diary.md`, and auto-detect completions from memory files.

## Core Commands

### Viewing Goals

```bash
python3 tools/goal-tracker.py list              # Show all goals (color-coded by status)
python3 tools/goal-tracker.py list --filter active    # Show only active goals
python3 tools/goal-tracker.py list --filter completed # Show only completed
python3 tools/goal-tracker.py focus             # Show high-priority active goals only
python3 tools/goal-tracker.py suggest           # Suggest next goal to work on
python3 tools/goal-tracker.py recent            # Show recently completed goals
```

### Goal Details

```bash
python3 tools/goal-tracker.py progress "Build pattern recognition"  # Show progress notes
python3 tools/goal-tracker.py stats            # Show completion statistics
python3 tools/goal-tracker.py stats --json     # Export stats as JSON
```

### Managing Goals

```bash
python3 tools/goal-tracker.py complete "Document learnings"  # Mark goal as done
python3 tools/goal-tracker.py add "New goal" [--priority high|medium|long-term|daily]
python3 tools/goal-tracker.py search "pattern"  # Search goals by keyword
```

### Advanced Features

```bash
python3 tools/goal-tracker.py velocity          # Show work velocity from diary.md
python3 tools/goal-tracker.py stale             # Show goals active >7 days
python3 tools/goal-tracker.py stale --days 14   # Custom threshold
python3 tools/goal-tracker.py week              # Show current week's goals
python3 tools/goal-tracker.py week --week 2     # Show specific week
```

### Export

```bash
python3 tools/goal-tracker.py export                    # Export to JSON
python3 tools/goal-tracker.py export --format markdown  # Export to Markdown
python3 tools/goal-tracker.py export --output backup.json
```

## What It Tracks

**From `goals/active.md`:**
- High/Medium/Long-term/Daily priority goals
- Completion status (`[ ]` → active, `[x]` → done)
- Priority levels and sections

**Auto-detection from memory files:**
- Scans `memory/YYYY-MM-DD.md` for completion markers
- Scans `diary.md` for goal mentions
- Detects `✓`, `DONE`, `completed`, `finished` patterns

**From `diary.md`:**
- Work velocity (tasks per hour/day)
- Trend analysis (increasing/stable/decreasing)
- Benchmark comparison

## Output Examples

### List Command

```
═══════════════════════════════════════════════════════════
  🎯 ACTIVE GOALS
═══════════════════════════════════════════════════════════

▸ 🔥 High Priority
  ✓ Create something that makes Arthur say "wow"
  ○ Build pattern recognition system

▸ ⚡ Medium Priority
  ○ Document my learnings
  ✓ Build at least 2 new tools

  Summary: 2 done, 3 active
```

### Stats Command

```
═══════════════════════════════════════════════════════════
  📈 GOAL STATISTICS
═══════════════════════════════════════════════════════════

▸ Overall Progress
  ████████████░░░░░░░░░░░░░░░░░░░░░
  12/16 completed (75.0%)

▸ By Priority
  🔥 High: 2/3 (67%)
  ⚡ Medium: 4/5 (80%)
  📅 Long-term: 2/3 (67%)
  🔄 Daily: 4/5 (80%)

  🚀 Great progress! Keep the momentum going.
```

### Velocity Command

```
═══════════════════════════════════════════════════════════
  ⚡ WORK VELOCITY
═══════════════════════════════════════════════════════════

▸ Last 168 hours (7 days)
  Tasks per hour: 12.5
  Tasks per day: 84.3
  Trend: 📈 INCREASING
  Total completed: 1429 tasks in 1433 work blocks

▸ Analysis
  🚀 You're speeding up! Keep this momentum going.

▸ Benchmarks
  🔥 Excellent - You're in peak productivity
```

### Focus Mode

```
═══════════════════════════════════════════════════════════
  🎯 FOCUS MODE
═══════════════════════════════════════════════════════════

  3 high-priority goal(s) need attention:

  1. ○ Build pattern recognition system
  2. ○ Learn one new skill per week
  3. ○ Post on Moltbook at least 3x per week

  💡 Pick one and work on it NOW.
```

## Key Features

### 1. Auto-Detection
- Scans `memory/YYYY-MM-DD.md` for completion markers
- Finds goal mentions in `diary.md`
- Auto-marks goals as complete when `✓`, `DONE`, or `completed` detected

### 2. Progress Notes
- Searches memory files for goal-related activity
- Shows recent work on each goal
- Context from diary entries

### 3. Velocity Tracking
- Calculates tasks/hour and tasks/day from `diary.md`
- Compares recent half vs older half for trend
- Benchmarks against productivity standards

### 4. Stale Goal Detection
- Identifies goals active too long (>7 days default)
- Shows creation date from diary
- Suggests breaking down, reprioritizing, or removing

### 5. Focus Mode
- Shows only high-priority active goals
- Eliminates noise for focused execution
- Falls back to medium if no high-priority

### 6. Weekly Views
- Parses `goals/week-N.md` files
- Shows weekly progress and stats
- Motivational messages based on completion rate

### 7. Export Formats
- JSON for machine processing and API integrations
- Markdown for sharing, reports, and version control
- Includes completion stats and timestamp

## Use Cases

**Daily workflow:**
```bash
# Morning: See what to focus on
python3 tools/goal-tracker.py focus

# After work: Check velocity
python3 tools/goal-tracker.py velocity
```

**Weekly review:**
```bash
# See week progress
python3 tools/goal-tracker.py week

# Export for reports
python3 tools/goal-tracker.py export --format markdown
```

**Cleanup:**
```bash
# Find stale goals
python3 tools/goal-tracker.py stale --days 14

# Mark complete
python3 tools/goal-tracker.py complete "Old goal"
```

## File Structure

**Reads from:**
- `goals/active.md` — Main goals file
- `goals/week-N.md` — Weekly goals
- `memory/YYYY-MM-DD.md` — Completion detection
- `diary.md` — Velocity tracking

**Writes to:**
- `goals/active.md` — When completing goals
- `goals/goals-export.json` — JSON export
- `goals/goals-export.md` — Markdown export

## Why It Matters

**Goals without tracking = wishes.**

- **Visibility:** See what's done, what's active, what's stale
- **Velocity:** Know if you're speeding up, slowing down, stable
- **Focus:** Filter noise, see only high-priority active goals
- **Auto-detection:** Goals mark themselves complete based on work logs
- **Evidence-based:** Velocity from actual work blocks, not guesses

**24 functions** — Most complex tool in the toolkit. Core value: Goal clarity + velocity visibility.

## Related Tools

- `diary_parser.py` — Parse diary.md entries
- `velocity-predictor.py` — Predict future completion rates
- `self-improvement-loop.py` — Analyze patterns and suggest improvements
- `daily-report.py` — Generate daily summaries with goal progress
