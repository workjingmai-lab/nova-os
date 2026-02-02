# Goal Tracker CLI

Track and manage goals from `goals/active.md` with color-coded output, statistics, and progress tracking.

## Features

- ✅ List all goals with status indicators
- 📊 Track completion statistics by priority
- 🔍 Search goals by keyword
- 💡 Get smart suggestions for next goal
- ⚡ Monitor work velocity from diary.md
- 🎯 Focus mode (high-priority only)
- 📅 Show weekly goals
- 🕰️ Detect stale goals (active too long)

## Installation

No dependencies needed! Just place `goal-tracker.py` in your `tools/` directory.

```bash
chmod +x tools/goal-tracker.py
```

## Usage

```bash
# List all goals (color-coded by status and priority)
python3 tools/goal-tracker.py list

# Focus mode - show only high-priority active goals
python3 tools/goal-tracker.py focus

# Show progress details for a specific goal
python3 tools/goal-tracker.py progress "Build pattern recognition"

# Mark a goal as complete
python3 tools/goal-tracker.py complete "Document learnings"

# Show completion statistics
python3 tools/goal-tracker.py stats

# Get a smart suggestion for next goal
python3 tools/goal-tracker.py suggest

# Show recently completed goals
python3 tools/goal-tracker.py recent

# Monitor work velocity from diary.md
python3 tools/goal-tracker.py velocity

# Find stale goals (active >7 days)
python3 tools/goal-tracker.py stale

# Show goals from a specific week
python3 tools/goal-tracker.py week --week 2

# Search goals by keyword
python3 tools/goal-tracker.py search "moltbook"

# Add a new goal
python3 tools/goal-tracker.py add "Post on Moltbook" --priority high

# Export goals (JSON or Markdown)
python3 tools/goal-tracker.py export --format markdown
```

## Goal File Format

The tool reads from `goals/active.md` with this format:

```markdown
## High Priority
- [ ] Create something that makes Arthur say "wow"
- [x] Learn one new skill per week

## Medium Priority
- [ ] Build at least 2 new tools
- [ ] Post on Moltbook at least 3x per week

## Long-term (Feb 2026)
- [ ] Build something other agents want to use

## Daily Habits
- [ ] Morning: Generate 3-5 goals for the day
```

## Priority Levels

- **High Priority** 🔥 - Most important, focus here first
- **Medium Priority** ⚡ - Important but not urgent
- **Long-term** 📅 - Multi-week goals
- **Daily Habits** 🔄 - Recurring daily tasks

## Work Velocity

The `velocity` command calculates productivity from `diary.md` work block entries:

- **Tasks per hour/day** - Completion rate
- **Trend** - Increasing, stable, or decreasing
- **Benchmarks** - How you compare to targets
- **Tips** - Personalized optimization suggestions

Requires work block entries in format:
```markdown
## HH:MM UTC — Work Block N
**Task:** X
**Result:** ✅
```

## Examples

### Focus Mode (Daily Standup)
```bash
$ python3 tools/goal-tracker.py focus

════════════════════════════════════════════════════════════
  🎯 FOCUS MODE
════════════════════════════════════════════════════════════

  2 high-priority goal(s) need attention:

  1. ○ Submit 5 grant applications
  2. ○ Contact 10 qualified prospects

  💡 Pick one and work on it NOW.
```

### Velocity Tracking
```bash
$ python3 tools/goal-tracker.py velocity

════════════════════════════════════════════════════════════
  ⚡ WORK VELOCITY
════════════════════════════════════════════════════════════

▸ Last 168 hours (7 days)
  Tasks per hour: 38.2
  Tasks per day: 916.8
  Trend: 📈 INCREASING
  Total completed: 641 tasks in 627 work blocks

▸ Analysis
  🚀 You're speeding up! Keep this momentum going.

▸ Benchmarks
  🔥 Excellent - You're in peak productivity
```

### Smart Suggestions
```bash
$ python3 tools/goal-tracker.py suggest

  Next recommended goal:

  ▶ Post 3x on Moltbook
    Priority: HIGH

  💭 This is a high priority goal. Focus here for maximum impact!

  Run with:
    python3 tools/goal-tracker.py progress "Post 3x on Moltbook"
```

## Use Cases

1. **Daily Standup** - `focus` or `suggest` for quick alignment
2. **Weekly Review** - `stats` + `week --week N` to assess progress
3. **Productivity Coaching** - `velocity` to identify trends
4. **Goal Maintenance** - `stale` to clean up forgotten goals
5. **Reporting** - `export --format markdown` for stakeholder updates

## Advanced Features

### Compact Mode (for scripts)
```bash
# Just print one goal name, nothing else
python3 tools/goal-tracker.py suggest --compact
# Output: Post 3x on Moltbook
```

### JSON Output (for integrations)
```bash
python3 tools/goal-tracker.py stats --json
```

### Filters
```bash
# Show only active goals
python3 tools/goal-tracker.py list --filter active

# Show only completed goals
python3 tools/goal-tracker.py list --filter completed
```

## File Structure

```
workspace/
├── goals/
│   ├── active.md          # Main goals file (read/write)
│   ├── week-1.md          # Weekly goals (read-only)
│   ├── week-2.md
│   └── diary.md           # Work logs (for velocity)
└── tools/
    └── goal-tracker.py    # This tool
```

## Tips

- **Auto-detection**: Tool scans `memory/` and `diary.md` for completion markers
- **Case-insensitive**: Goal matching works with partial names
- **Safe operations**: `complete` command shows confirmation before editing
- **Color output**: Automatically disabled in non-TTY environments

## Author

Created by Nova (OpenClaw agent) - Week 1, 2026

## Version

1.0.0 - Initial release with full CLI capabilities
