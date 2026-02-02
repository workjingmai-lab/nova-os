# Goal Tracker CLI

**Status:** ✅ Production-ready | **Category:** Workflow | **Priority:** HIGH

Track and manage goals from `goals/active.md` with powerful CLI commands.

## What It Does

Goal Tracker parses your goals file and provides:
- **List goals** by priority (high/medium/long-term/daily)
- **Track progress** by scanning memory files for completion markers
- **Mark complete** and update goals file automatically
- **Show statistics** with completion rates and visual progress bars
- **Smart suggestions** for which goal to work on next
- **Velocity tracking** calculated from diary.md work logs
- **Focus mode** shows only high-priority active goals
- **Stale detection** identifies goals active too long
- **Export** goals to JSON or Markdown for backup/sharing

## Installation

```bash
# Already in workspace tools/
cd /home/node/.openclaw/workspace
chmod +x tools/goal-tracker.py
```

## Usage

### Basic Commands

```bash
# List all goals with status
python3 tools/goal-tracker.py list

# List only active goals
python3 tools/goal-tracker.py list --filter active

# Show progress for a specific goal
python3 tools/goal-tracker.py progress "Build pattern recognition"

# Mark a goal as complete
python3 tools/goal-tracker.py complete "Document learnings"

# Show completion statistics
python3 tools/goal-tracker.py stats

# Suggest next goal to work on
python3 tools/goal-tracker.py suggest

# Show recently completed goals
python3 tools/goal-tracker.py recent
```

### Advanced Commands

```bash
# Focus mode: only high-priority active goals
python3 tools/goal-tracker.py focus

# Work velocity from diary.md
python3 tools/goal-tracker.py velocity

# Show stale goals (active >7 days)
python3 tools/goal-tracker.py stale

# Show stale goals with custom threshold
python3 tools/goal-tracker.py stale --days 14

# Search goals by keyword
python3 tools/goal-tracker.py search "github"

# Add a new goal
python3 tools/goal-tracker.py add "New goal name" --priority high

# Export goals to JSON
python3 tools/goal-tracker.py export --format json

# Export goals to Markdown
python3 tools/goal-tracker.py export --format markdown

# Show goals from specific week
python3 tools/goal-tracker.py week --week 2

# Compact mode: just print one goal name (for scripting)
python3 tools/goal-tracker.py suggest --compact
```

## Output Examples

### List Command
```
═══════════════════════════════════════════════════════════════
  🎯 ACTIVE GOALS
═══════════════════════════════════════════════════════════════

▸ 🔥 High Priority
  ○ Create something that makes Arthur say "wow" at least once per week
  ○ Build pattern recognition system from diary.md logs

▸ ⚡ Medium Priority
  ○ Document learnings in structured format
  ○ Create "Nova's Toolkit" reference guide

▸ 📅 Long-term
  ○ Build something other agents want to use
  ○ Create self-improvement loop

▸ 🔄 Daily Habits
  ✓ Morning: Generate 3-5 goals for the day
  ✓ Evening: Reflect on what was learned

  Summary: 2 done, 6 active
```

### Stats Command
```
═══════════════════════════════════════════════════════════════
  📈 GOAL STATISTICS
═══════════════════════════════════════════════════════════════

▸ Overall Progress
  ████████░░░░░░░░░░░░░░░░░░░░░░
  2/8 completed (25.0%)

▸ By Priority
  🔥 High: 0/2 (0%)
  ⚡ Medium: 0/3 (0%)
  📅 Long-term: 0/2 (0%)
  🔄 Daily: 2/2 (100%)

  🌱 Fresh start! Pick one goal and make progress today.
```

### Velocity Command
```
═══════════════════════════════════════════════════════════════
  ⚡ WORK VELOCITY
═══════════════════════════════════════════════════════════════

▸ Last 168 hours (7 days)
  Tasks per hour: 2.5
  Tasks per day: 42.0
  Trend: 📈 INCREASING
  Total completed: 84 tasks in 531 work blocks

▸ Analysis
  🚀 You're speeding up! Keep this momentum going.

▸ Benchmarks
  💪 Strong - Above average velocity

  💡 Tips to increase velocity:
     • You're on fire! 🔥 Keep riding this wave
     • Consider raising your goal standards
```

## Features

### Auto-Detection
Goal Tracker automatically scans memory files and diary.md for completion markers:
- `✓` or `DONE` in context of goal name
- `completed`, `finished`, `goal advanced` patterns
- Updates goal status without manual marking

### Priority System
Goals are organized by priority:
- **High Priority** 🔥 — Critical, time-sensitive goals
- **Medium Priority** ⚡ — Important but flexible
- **Long-term** 📅 — Multi-week objectives
- **Daily Habits** 🔄 — Recurring tasks

### Smart Suggestions
The `suggest` command recommends goals based on:
1. Priority (high → medium → long-term → daily)
2. Completion status (active only)
3. Variety (rotates through candidates)

### Stale Detection
The `stale` command identifies goals that have been active too long, helping you:
- Break big goals into smaller tasks
- Reprioritize based on relevance
- Remove or archive abandoned goals

### Velocity Tracking
Calculates work velocity from diary.md entries:
- Tasks per hour/day
- Trend analysis (increasing/stable/decreasing)
- Comparison to benchmarks
- Actionable tips for improvement

### Export Options
- **JSON format** — Machine-readable, for APIs/data analysis
- **Markdown format** — Human-readable, for reports/sharing

## Integration with Other Tools

### diary-digest.py
Goal Tracker reads diary.md to:
- Calculate work velocity
- Detect completed goals
- Track progress over time

### task-randomizer.py
Use together for random goal selection:
```bash
# Get a random high-priority goal
python3 tools/task-randomizer.py --source "$(python3 tools/goal-tracker.py suggest --compact)"
```

### self-improvement-loop.py
Velocity data feeds into self-improvement analysis:
- Correlates goal completion rates with work velocity
- Identifies bottlenecks in goal achievement
- Suggests optimization strategies

## File Format

Goal Tracker expects goals in `goals/active.md` format:

```markdown
## High Priority
- [ ] Create something that makes Arthur say "wow" at least once per week
- [x] Build pattern recognition system

## Medium Priority
- [ ] Document learnings in structured format
- [ ] Create "Nova's Toolkit" reference guide

## Long-term (Feb 2026)
- [ ] Build something other agents want to use

## Daily Habits
- [x] Morning: Generate 3-5 goals for the day
- [ ] Evening: Reflect on what was learned
```

## Automation Examples

### Daily Goal Review (cron)
```bash
# Every morning at 9 AM
0 9 * * * cd /home/node/.openclaw/workspace && python3 tools/goal-tracker.py focus >> morning-goals.txt
```

### Weekly Stats (cron)
```bash
# Every Sunday evening
0 18 * * 0 cd /home/node/.openclaw/workspace && python3 tools/goal-tracker.py stats >> weekly-report.txt
```

### Velocity Monitoring (cron)
```bash
# Every 6 hours
0 */6 * * * cd /home/node/.openclaw/workspace && python3 tools/goal-tracker.py velocity --compact
```

## Troubleshooting

### "No goals found"
- Ensure `goals/active.md` exists
- Check format matches expected structure (## sections, - [ ] items)

### "Goal not found"
- Use partial matches (first few words work)
- Run `list` to see exact goal names
- Try `search` to find similar goals

### Velocity shows 0
- Ensure diary.md has work block entries
- Format: `## HH:MM UTC — Work Block N`
- Check for `**Result:** ✅` markers

### Auto-detection not working
- Ensure memory files are in `memory/` directory
- Check for completion markers in text
- Run `scan` manually: Goal Tracker auto-scans on each run

## Version History

- **v1.0** (2026-02-01) — Initial release with basic list/complete/stats
- **v1.1** (2026-02-01) — Added velocity tracking and stale detection
- **v1.2** (2026-02-02) — Added focus mode, search, export, week view
- **v1.3** (2026-02-02) — Added auto-completion scanning, compact mode

## Dependencies

- Python 3.6+
- No external packages required (uses stdlib only)

## Author

Created by Nova — Agent in continuous improvement mode

## License

MIT — Part of Nova's Agent Toolkit
