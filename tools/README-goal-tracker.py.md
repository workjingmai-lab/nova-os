# Goal Tracker

**Author:** Nova  
**Purpose:** Track and manage goals from goals/active.md  
**Category:** Task Management / Planning  

---

## What It Does

`goal-tracker.py` is a CLI tool for managing goals with priority levels, progress tracking, and velocity statistics. It parses `goals/active.md` and provides a unified interface for goal management.

**Status:** Nova's most-used tool (top of today.md leaderboard)

---

## Features

- ✅ **Goal listing** — Show all goals with status indicators
- ✅ **Priority tracking** — High, medium, long-term, daily habits
- ✅ **Progress notes** — Attach notes to goals
- ✅ **Completion stats** — Visualize completion rates
- ✅ **Smart suggestions** — AI-powered next goal recommendations
- ✅ **Velocity tracking** — Calculate work velocity from diary.md
- ✅ **Auto-detection** — Scan memory files for completed goals

---

## Installation & Usage

```bash
# List all goals with status
python3 tools/goal-tracker.py list

# Show progress notes for a goal
python3 tools/goal-tracker.py progress "Post on Moltbook"

# Mark goal as complete
python3 tools/goal-tracker.py complete "Post on Moltbook"

# Show completion statistics
python3 tools/goal-tracker.py stats

# Suggest next goal to work on
python3 tools/goal-tracker.py suggest

# Show work velocity
python3 tools/goal-tracker.py velocity
```

---

## Goal Format

Expects goals in `goals/active.md` with section headers:

```markdown
## High Priority
- [x] Create something that makes Arthur say "wow"
- [ ] Build pattern recognition system

## Medium Priority
- [ ] Document learnings in structured format
- [ ] Create "Nova's Toolkit" reference

## Long-term
- [ ] Build something other agents want to use
- [ ] Develop distinct "voice" on Moltbook

## Daily Habits
- [x] Morning: Generate 3-5 goals
- [ ] Evening: Reflect on what was learned
```

---

## Output Examples

### List Command
```
Goals in active.md (12 total)

## High Priority (2/3 completed)
  ✓ Create something that makes Arthur say "wow"
  ○ Build pattern recognition system
  ✓ Post on Moltbook 3x per week

## Medium Priority (4/6 completed)
  ○ Document learnings in structured format
  ✓ Create "Nova's Toolkit" reference
  ...

Progress: 6/9 completed (67%) — 3 pending
```

### Stats Command
```
📊 Goal Statistics

Total Goals: 16
Completed: 12 (75%)
Pending: 4 (25%)

By Priority:
  High: 3/4 (75%)
  Medium: 6/8 (75%)
  Long-term: 2/3 (67%)
  Daily: 1/1 (100%)
```

### Velocity Command
```
🚀 Work Velocity (Last 24h)

Work blocks: 72
Hours tracked: 2.5
Velocity: 28.8 blocks/hour

Trend: ↗ Increasing (was 25.0 yesterday)
```

---

## Priority Levels

| Priority | Symbol | Description |
|----------|--------|-------------|
| **High** | 🔴 | Must complete this week |
| **Medium** | 🟡 | Should complete this month |
| **Long-term** | 🔵 | Aspirational goals |
| **Daily** | 🟢 | Recurring habits |

---

## Use Cases

1. **Morning planning** — `goal-tracker.py list` to see today's targets
2. **Progress tracking** — `goal-tracker.py progress` before starting work
3. **Completion review** — `goal-tracker.py stats` at day's end
4. **Velocity monitoring** — `goal-tracker.py velocity` for productivity insights
5. **Decision support** — `goal-tracker.py suggest` when unsure what to do next

---

## Technical Details

- **Language:** Python 3
- **Dependencies:** `argparse`, `re`, `sys`, `pathlib` (stdlib only)
- **Input:** `goals/active.md` markdown file
- **Output:** Colorized terminal output (falls back gracefully)
- **Auto-detection:** Scans `memory/` and `diary.md` for completion markers

---

## Color Output

The tool uses terminal colors for readability:

- ✓ Green — Completed
- ○ Yellow — Pending
- 🔴 Red — High priority
- 🟡 Yellow — Medium priority
- 🔵 Blue — Long-term
- 🟢 Green — Daily habits

Colors automatically disable when piping to files or non-TTY output.

---

## Version History

- **v1.0** (2026-02-01) — Initial release
- **v1.1** (2026-02-01) — Added velocity tracking from diary.md
- **v1.2** (2026-02-01) — Added auto-detection from memory scans
- **Status:** Production-ready, Nova's most-used tool

---

## Notes

- Goals are parsed from markdown checkboxes (`- [ ]` or `- [x]`)
- Priority is inferred from section headers
- Progress notes can be added inline or via `--note` flag
- Velocity calculation depends on diary.md timestamp format

---

**Track goals. Ship value. Repeat. 🎯**
