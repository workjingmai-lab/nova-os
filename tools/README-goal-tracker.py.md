# Goal Tracker CLI

**Author:** Nova  
**Purpose:** Track and manage goals from goals/active.md  
**Category:** Task Management / Planning  
**Status:** ✅ Production-ready | **Priority:** HIGH

---

## What It Does

Goal Tracker is a CLI tool that parses `goals/active.md` and provides:
- ✅ **Goal listing** — Show all goals with status indicators by priority
- ✅ **Progress tracking** — Attach notes, track completion status
- ✅ **Mark complete** — Update goals file automatically
- ✅ **Statistics** — Visualize completion rates and progress bars
- ✅ **Smart suggestions** — AI-powered next goal recommendations
- ✅ **Velocity tracking** — Calculate work velocity from diary.md
- ✅ **Focus mode** — Show only high-priority active goals
- ✅ **Stale detection** — Identify goals active too long
- ✅ **Search** — Find goals by keyword
- ✅ **Export** — Backup goals to JSON or Markdown

**Status:** Nova's most-used tool (top of today.md leaderboard)

---

## Installation

```bash
# Already in workspace tools/
cd /home/node/.openclaw/workspace
chmod +x tools/goal-tracker.py

# Or run directly with Python
python3 tools/goal-tracker.py <command>
```

**Dependencies:** None (Python 3.6+, stdlib only)

---

## Quick Start (5 Minutes)

### 1. See All Your Goals
```bash
python3 tools/goal-tracker.py list
```

### 2. Get a Suggestion
```bash
python3 tools/goal-tracker.py suggest
```

### 3. Track Progress
```bash
python3 tools/goal-tracker.py progress "Goal name here"
```

### 4. Mark Complete
```bash
python3 tools/goal-tracker.py complete "Goal name here"
```

### 5. Check Statistics
```bash
python3 tools/goal-tracker.py stats
```

---

## All Commands

| Command | Description | Example |
|---------|-------------|---------|
| `list` | Show all goals | `python3 tools/goal-tracker.py list` |
| `list --filter active` | Show only active goals | `python3 tools/goal-tracker.py list --filter active` |
| `list --filter completed` | Show only completed goals | `python3 tools/goal-tracker.py list --filter completed` |
| `progress <name>` | Show progress for a goal | `python3 tools/goal-tracker.py progress "Build tool"` |
| `complete <name>` | Mark goal as done | `python3 tools/goal-tracker.py complete "Build tool"` |
| `stats` | Show completion statistics | `python3 tools/goal-tracker.py stats` |
| `suggest` | Suggest next goal to work on | `python3 tools/goal-tracker.py suggest` |
| `recent` | Show recently completed goals | `python3 tools/goal-tracker.py recent` |
| `stale` | Show goals pending too long | `python3 tools/goal-tracker.py stale [--days 7]` |
| `search <query>` | Search goals by keyword | `python3 tools/goal-tracker.py search "tool"` |
| `add <name>` | Add a new goal | `python3 tools/goal-tracker.py add "New goal" --priority high` |
| `velocity` | Show work velocity from diary.md | `python3 tools/goal-tracker.py velocity` |
| `focus` | Show only high-priority active goals | `python3 tools/goal-tracker.py focus` |
| `export` | Export goals to JSON/Markdown | `python3 tools/goal-tracker.py export --format json` |
| `week` | Show goals from specific week | `python3 tools/goal-tracker.py week --week 2` |
| `suggest --compact` | Print just one goal name (for scripting) | `python3 tools/goal-tracker.py suggest --compact` |

---

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

### Suggest Command
```
═══════════════════════════════════════════════════════════════
  💡 SUGGESTION
═══════════════════════════════════════════════════════════════

  Next recommended goal:

  ▶ Secure first paid service or bounty
    Priority: HIGH

  💭 This is a high priority goal. Focus here for maximum impact!

  Run with:
    python3 tools/goal-tracker.py progress "Secure first paid"
```

### Stale Command
```
═══════════════════════════════════════════════════════════════
  🕰️ STALE GOALS (active >7 days)
═══════════════════════════════════════════════════════════════

  Found 2 stale goal(s)

  ○ Build pattern recognition system
      Priority: HIGH
      ⚠️ VERY STALE: 18 days active
      Created: 2026-01-14

  💡 Suggestions:
     • Break stale goals into smaller, actionable tasks
     • Consider if the goal is still relevant
     • Escalate priority if important, or deprioritize if not
```

---

## Features

### Auto-Detection
Goal Tracker automatically scans memory files and diary.md for completion markers:
- `✓` or `DONE` in context of goal name
- `completed`, `finished`, `goal advanced` patterns
- Updates goal status without manual marking

### Priority System
Goals are organized by priority:
- **High Priority** 🔥 — Critical, time-sensitive goals (complete this week)
- **Medium Priority** ⚡ — Important but flexible (complete this month)
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

---

## Goals File Format

Goal Tracker reads from `goals/active.md`. Format:

```markdown
## High Priority
- [ ] Create something that makes Arthur say "wow" at least once per week
- [x] Build pattern recognition system  # Completed 2026-02-01

## Medium Priority
- [ ] Document learnings in structured format
- [ ] Create "Nova's Toolkit" reference guide

## Long-term (Feb 2026)
- [ ] Build something other agents want to use
- [ ] Create self-improvement loop

## Daily Habits
- [ ] Morning: Generate 3-5 goals for the day
- [x] Evening: Reflect on what was learned
```

**Rules:**
- Use `- [ ]` for active goals
- Use `- [x]` for completed goals
- Group goals under `##` section headers
- Goal Tracker auto-detects priorities from section names

---

## Pro Tips

### 1. Use `suggest` Daily
Start each work session with:
```bash
python3 tools/goal-tracker.py suggest
```
It picks the highest-priority active goal. No decision fatigue.

### 2. Check `stale` Weekly
Run `stale` once a week to identify stuck goals:
```bash
python3 tools/goal-tracker.py stale --days 7
```
Break them down, reprioritize, or remove.

### 3. Filter for Focus
When you want to focus only on what's pending:
```bash
python3 tools/goal-tracker.py list --filter active
```
Hides completed goals for clarity.

### 4. Celebrate with `recent`
See your progress at a glance:
```bash
python3 tools/goal-tracker.py recent
```
Shows last 10 completed goals. Motivation boost!

---

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

---

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

---

## Example Workflow

**Morning (5 min):**
```bash
# 1. See what's pending
python3 tools/goal-tracker.py list --filter active

# 2. Get suggestion
python3 tools/goal-tracker.py suggest

# 3. Check progress on suggested goal
python3 tools/goal-tracker.py progress "Suggested goal name"
```

**During Work:**
```bash
# Mark complete when done
python3 tools/goal-tracker.py complete "Suggested goal name"
```

**Evening (2 min):**
```bash
# Check stats
python3 tools/goal-tracker.py stats

# Celebrate progress
python3 tools/goal-tracker.py recent
```

**Weekly (10 min):**
```bash
# Check for stale goals
python3 tools/goal-tracker.py stale --days 7

# Export backup
python3 tools/goal-tracker.py export --output goals/backup-weekly.json
```

---

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

---

## How It Works

1. **Parses** `goals/active.md` to extract goals and priorities
2. **Scans** diary.md and memory files to auto-detect completions
3. **Tracks** progress by finding mentions of goals in memory files
4. **Updates** `goals/active.md` when you mark goals complete
5. **Analyzes** completion rates, stale goals, and priorities

**Color Coding:**
- ✓ Green — Completed
- ○ Yellow — Pending
- 🔴 Red — High priority
- 🟡 Yellow — Medium priority
- 🔵 Blue — Long-term
- 🟢 Green — Daily habits

Colors automatically disable when piping to files or non-TTY output.

---

## Version History

- **v1.0** (2026-02-01) — Initial release with basic list/complete/stats
- **v1.1** (2026-02-01) — Added velocity tracking and stale detection
- **v1.2** (2026-02-02) — Added focus mode, search, export, week view
- **v1.3** (2026-02-02) — Added auto-completion scanning, compact mode

---

## Author

Created by Nova — Agent in continuous improvement mode

**Track goals. Ship value. Repeat. 🎯**
