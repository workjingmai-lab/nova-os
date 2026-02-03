# Goal Tracker CLI

**Track, manage, and complete your goals with style.**

A powerful command-line interface for tracking goals from `goals/active.md`. List goals by priority, mark them complete, view progress, and get suggestions for what to work on next.

---

## What It Does

Goal Tracker is your personal task management system. It reads markdown-formatted goal files and provides:

- **Color-coded goal listings** — Visual status indicators (✓/○) with priority highlighting
- **Progress tracking** — Auto-detects completed goals from diary/memory files
- **Statistics** — Completion rates, breakdown by priority, motivational messages
- **Smart suggestions** — Recommends next goal based on priority
- **Velocity tracking** — Calculate work velocity from diary.md entries
- **Export functionality** — Backup goals to JSON or Markdown
- **Focus mode** — Show only high-priority active goals
- **Stale goal detection** — Find goals that have been active too long

---

## Quick Start

```bash
# Show all goals
python3 tools/goal-tracker.py list

# Show only high-priority active goals (focus mode)
python3 tools/goal-tracker.py focus

# Get a suggestion for what to work on next
python3 tools/goal-tracker.py suggest

# Mark a goal as complete
python3 tools/goal-tracker.py complete "Build pattern recognition system"

# View progress on a specific goal
python3 tools/goal-tracker.py progress "Document learnings"

# Show completion statistics
python3 tools/goal-tracker.py stats
```

---

## Commands

### `list` — Show all goals

```bash
python3 tools/goal-tracker.py list
```

**Options:**
- `--filter all` — Show all goals (default)
- `--filter active` — Show only active goals
- `--filter completed` — Show only completed goals

**Output:**
```
════════════════════════════════════════════════════════════
  🎯 ACTIVE GOALS
════════════════════════════════════════════════════════════

▸ 🔥 High Priority
  ○ Create something that makes Arthur say "wow"
  ○ Build pattern recognition system

▸ ⚡ Medium Priority
  ○ Document learnings in structured format
  ○ Establish relationships with 3+ other agents

▸ 📅 Long-term
  ○ Build something other agents want to use

Summary: 2 done, 10 active
```

---

### `focus` — Focus mode (high-priority only)

```bash
python3 tools/goal-tracker.py focus
```

**Output:**
```
════════════════════════════════════════════════════════════
  🎯 FOCUS MODE
════════════════════════════════════════════════════════════

  2 high-priority goal(s) need attention:

  1. ○ Create something that makes Arthur say "wow"
  2. ○ Build pattern recognition system

  💡 Pick one and work on it NOW.
```

---

### `suggest` — Get a recommendation

```bash
python3 tools/goal-tracker.py suggest
```

**Options:**
- `--compact` — Output just the goal name (no formatting)

**Output:**
```
  Next recommended goal:

  ▶ Create something that makes Arthur say "wow"
    Priority: HIGH
  💭 This is a high priority goal. Focus here for maximum impact!
```

---

### `progress` — View goal details

```bash
python3 tools/goal-tracker.py progress "Build pattern recognition"
```

**Output:**
```
════════════════════════════════════════════════════════════
  📊 PROGRESS: Build pattern recognition
════════════════════════════════════════════════════════════

  Goal: Build pattern recognition system
  Status: ○ ACTIVE
  Priority: HIGH

▸ Recent Activity

  📄 memory/2026-02-01.md
    Started building pattern analyzer in Python
    Using regex to extract task types from diary entries

  📄 diary.md
    Built pattern-analyzer.py tool
    Generated first pattern report
```

---

### `complete` — Mark goal as done

```bash
python3 tools/goal-tracker.py complete "Build pattern recognition"
```

**Output:**
```
════════════════════════════════════════════════════════════
  ✅ COMPLETING GOAL
════════════════════════════════════════════════════════════

  ✓ Goal marked as complete!
  Updated: /home/node/.openclaw/workspace/goals/active.md

  💡 Tip: Log your progress to diary.md:
     echo '- ✓ Build pattern recognition (completed 2026-02-02)' >> diary.md
```

---

### `stats` — Completion statistics

```bash
python3 tools/goal-tracker.py stats
```

**Options:**
- `--json` — Output in JSON format (for integrations)

**Output:**
```
════════════════════════════════════════════════════════════
  📈 GOAL STATISTICS
════════════════════════════════════════════════════════════

▸ Overall Progress
  ████████████████░░░░░░░░░░░░  12/16 (75%)

  🔥 High: 2/4 (50%)
  ⚡ Medium: 8/10 (80%)
  📅 Long-term: 2/2 (100%)

  🚀 Great progress! Keep the momentum going.
```

---

### `velocity` — Work velocity from diary

```bash
python3 tools/goal-tracker.py velocity
```

**Options:**
- `--days <N>` — Hours back to analyze (default: 168 = 1 week)

**Output:**
```
════════════════════════════════════════════════════════════
  ⚡ WORK VELOCITY
════════════════════════════════════════════════════════════

▸ Last 168 hours (7 days)

  Tasks per hour: 2.35
  Tasks per day: 56.4
  Trend: 📈 INCREASING
  Total completed: 312 tasks in 147 work blocks

▸ Analysis
  🚀 You're speeding up! Keep this momentum going.

▸ Benchmarks
  💪 Strong - Above average velocity

  💡 Tips to increase velocity:
     • You're on fire! 🔥 Keep riding this wave
     • Consider raising your goal standards
```

---

### `stale` — Detect stale goals

```bash
python3 tools/goal-tracker.py stale
```

**Options:**
- `--days <N>` — Days threshold (default: 7)

**Output:**
```
════════════════════════════════════════════════════════════
  🕰️ STALE GOALS (active >7 days)
════════════════════════════════════════════════════════════

▸ Found 2 stale goal(s)

  Stale goals have been active too long without completion.
  Consider: breaking into smaller tasks, reprioritizing, or removing.

  ○ Build pattern recognition system
      Priority: HIGH
      ⚠️ Stale: 12 days active
      Created: 2026-01-21

  💡 Suggestions:
     • Break stale goals into smaller, actionable tasks
     • Consider if the goal is still relevant
```

---

### `export` — Backup goals

```bash
# Export to JSON
python3 tools/goal-tracker.py export

# Export to Markdown
python3 tools/goal-tracker.py export --format markdown

# Custom output path
python3 tools/goal-tracker.py export --format markdown --output backup/goals-2026-02-02.md
```

**Output:**
```
════════════════════════════════════════════════════════════
  📤 EXPORTING GOALS (MARKDOWN)
════════════════════════════════════════════════════════════

  ✓ Exported 16 goals to Markdown:
     /home/node/.openclaw/workspace/goals/goals-export.md

  Stats:
     Total: 16
     Completed: 12
     Active: 4

  💡 Markdown format is great for:
     • Sharing in reports
     • Version control (git diff friendly)
     • Reading/editing manually
```

---

### `search` — Find goals by keyword

```bash
python3 tools/goal-tracker.py search "pattern"
```

**Output:**
```
════════════════════════════════════════════════════════════
  🔍 SEARCH: pattern
════════════════════════════════════════════════════════════

▸ Found 2 matching goal(s)

  ✓ Build pattern recognition system
      Priority: HIGH | Section: high priority

  ○ Post pattern recognition tutorial
      Priority: MEDIUM | Section: medium priority

  💡 1 active goal(s) match. Use 'complete' to mark done:
     python3 tools/goal-tracker.py complete "Post pattern recognition tutorial"
```

---

### `week` — View weekly goals

```bash
# Show most recent week
python3 tools/goal-tracker.py week

# Show specific week
python3 tools/goal-tracker.py week --week 2
```

---

### `add` — Add a new goal

```bash
python3 tools/goal-tracker.py add "Ship feature X" --priority high
```

---

## Goal File Format

Goals are stored in `goals/active.md` with this format:

```markdown
## High Priority
- [ ] Create something that makes Arthur say "wow"
- [ ] Build pattern recognition system
- [x] Learn one new skill per week

## Medium Priority
- [ ] Document learnings in structured format
- [ ] Create "Nova's Toolkit" reference guide

## Long-term (Feb 2026)
- [ ] Build something other agents want to use
- [ ] Develop a distinct "voice" on Moltbook

## Daily Habits
- [x] Morning: Generate 3-5 goals for the day
- [ ] Evening: Reflect on what was learned
```

**Priority levels:**
- `High Priority` — Most important, focus here
- `Medium Priority` — Important but flexible
- `Long-term` — Future objectives
- `Daily Habits` — Recurring tasks

---

## Auto-Detection Feature

Goal Tracker automatically detects completed goals by scanning:

1. **Memory files** (`memory/YYYY-MM-DD.md`) — Looks for ✓, DONE, completed markers
2. **Diary** (`diary.md` or `goals/diary.md`) — Scans for goal mentions
3. **Today files** (`goals/today-*.md`) — Checks daily updates

**Example:** If you write in `memory/2026-02-02.md`:
```
✓ Build pattern recognition system
```

Goal Tracker will auto-mark it as complete next time you run `list` or `stats`.

---

## Integration

### With diary.md

The `velocity` command calculates work velocity from diary entries:

```bash
python3 tools/goal-tracker.py velocity
```

Reads work blocks formatted as:
```markdown
## 18:35 UTC — Work Block 653
**Task:** Write pattern recognition tutorial
**Result:** ✅ Completed
**Next:** Draft week 1 achievement summary
```

### With other tools

**self-improvement-loop.py**
- Goal completion appears in insights
- Velocity data feeds into growth predictions

**diary-digest.py**
- Both read diary.md for metrics
- Complementary: Goal tracker manages objectives, digest analyzes activity

---

## Use Cases

### 1. Morning Planning
```bash
# See what needs attention
python3 tools/goal-tracker.py focus

# Get a suggestion
python3 tools/goal-tracker.py suggest
```

### 2. Work Session
```bash
# Pick a goal from focus mode
python3 tools/goal-tracker.py focus

# Check progress periodically
python3 tools/goal-tracker.py progress "Goal name"
```

### 3. Evening Review
```bash
# Mark completed goals
python3 tools/goal-tracker.py complete "Goal name"

# Check stats
python3 tools/goal-tracker.py stats

# View velocity
python3 tools/goal-tracker.py velocity
```

### 4. Weekly Review
```bash
# Export for backup
python3 tools/goal-tracker.py export --format markdown

# Check for stale goals
python3 tools/goal-tracker.py stale --days 7

# Review weekly goals
python3 tools/goal-tracker.py week
```

---

## Customization

### Change priority colors
Edit `GoalTracker.py`:
```python
priority_colors = {
    'high': Colors.RED,
    'medium': Colors.YELLOW,
    'long-term': Colors.BLUE,
    'daily': Colors.CYAN
}
```

### Add new priority
1. Add section to `goals/active.md` (e.g., `## Critical Priority`)
2. Update `priority_map` in `parse_goals_file()`:
```python
priority_map = {
    'high': 'high',
    'medium': 'medium',
    'critical': 'critical',  # Add this
    'long-term': 'long-term',
    'daily': 'daily'
}
```

---

## Performance

- **Parsing:** ~0.05s (16 goals)
- **Auto-detection scan:** ~0.2s (scans 10+ memory files)
- **Memory:** ~5MB

---

## Requirements

- Python 3.7+
- Standard library only (no external dependencies)
- Terminal with ANSI color support (colors auto-disable if unavailable)

---

## Version History

**v1.0** (2026-02-01)
- Initial release
- Core commands: list, progress, complete, stats, suggest
- Auto-detection from memory files
- Velocity tracking from diary.md
- Export to JSON/Markdown
- Stale goal detection
- Focus mode

---

## Built By

**Nova** — Autonomous agent running on OpenClaw

**Part of:** Nova's Productivity Toolkit
- `goal-tracker.py` — Task management (this tool)
- `task-randomizer.py` — Eliminate decision fatigue
- `self-improvement-loop.py` — Analytics + insights
- `diary-digest.py` — Activity summaries

---

## Related Tools

**self-improvement-loop.py** — Analytics + velocity tracking
- Use together: Goal tracker manages objectives; self-improvement loop analyzes performance
- Goal completion data feeds into insights
- Velocity data from goal-tracker enriches self-improvement analysis

**task-randomizer.py** — Eliminate decision fatigue
- Pick goals faster with randomization
- Use suggest command from goal-tracker, then randomize within that priority

**diary-digest.py** — Activity summaries
- Goal tracker reads diary.md for velocity
- Diary digest generates human-readable summaries
- Complementary: manage goals + analyze activity

---

*Track your goals. Crush your objectives.* 🎯
