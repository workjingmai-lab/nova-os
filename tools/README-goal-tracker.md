# Goal Tracker

**Track and manage goals from `goals/active.md` with a powerful CLI.**

---

## 🎯 What It Does

Goal Tracker reads your goals from `goals/active.md` (or weekly goal files) and provides:
- **List goals** with status filtering (all, pending, completed)
- **Mark goals complete** with automatic ✅ updates
- **Show progress notes** extracted from `diary.md`
- **Statistics** on completion rates and velocity
- **Smart suggestions** for what to work on next
- **Export goals** to JSON/Markdown
- **Velocity tracking** from diary work blocks

---

## 📦 Installation

No installation needed — just run:

```bash
python3 tools/goal-tracker.py [command]
```

**Requirements:** Python 3.7+, standard library only (no external deps)

---

## 🚀 Quick Start

### 1. List all goals
```bash
python3 tools/goal-tracker.py list
```

Output:
```
Active Goals - February 2026

High Priority
  ○ Create something that makes Arthur say "wow" (high)
  ○ Build pattern recognition system (high)

Medium Priority
  ✓ Document my learnings (medium)
  ○ Create Nova's Toolkit guide (medium)

Stats: 1/4 completed (25%)
```

### 2. Mark a goal as complete
```bash
python3 tools/goal-tracker.py complete "Create Nova's Toolkit guide"
```

Automatically updates `goals/active.md` with ✅.

### 3. Show progress for a goal
```bash
python3 tools/goal-tracker.py progress "Build pattern recognition system"
```

Scans `diary.md` for work blocks related to this goal.

### 4. Get suggestions
```bash
python3 tools/goal-tracker.py suggest
```

Recommends the next high-priority incomplete goal.

### 5. Check velocity
```bash
python3 tools/goal-tracker.py velocity
```

Shows work blocks per hour from your `diary.md`.

---

## 📚 All Commands

| Command | Description | Example |
|---------|-------------|---------|
| `list` | Show all goals with status | `goal-tracker.py list` |
| `list --pending` | Show only incomplete goals | `goal-tracker.py list --pending` |
| `list --completed` | Show only completed goals | `goal-tracker.py list --completed` |
| `progress <name>` | Show progress notes from diary | `goal-tracker.py progress "Build tool"` |
| `complete <name>` | Mark goal as done | `goal-tracker.py complete "Learn skill"` |
| `stats` | Show completion statistics | `goal-tracker.py stats --json` |
| `suggest` | Suggest next goal to work on | `goal-tracker.py suggest` |
| `recent` | Show recently completed goals | `goal-tracker.py recent --limit 5` |
| `export` | Export goals to file | `goal-tracker.py export --format json` |
| `week <num>` | Show specific week goals | `goal-tracker.py week 2` |
| `stale` | Show inactive goals | `goal-tracker.py stale --days 7` |
| `focus` | Show current priority goal | `goal-tracker.py focus` |
| `velocity` | Show work velocity | `goal-tracker.py velocity` |

---

## 📊 File Format

Goal Tracker expects goals in this format (Markdown):

```markdown
# Active Goals - February 2026

## High Priority
- [ ] Create something that makes Arthur say "wow"
- [ ] Build pattern recognition system

## Medium Priority
- [x] Document my learnings
- [ ] Create Nova's Toolkit guide

## Long-term
- [ ] Build something other agents want to use
```

**Supported syntax:**
- `[ ]` or `- [ ]` → Incomplete
- `[x]` or `- [x]` → Completed
- Sections: `## High Priority`, `## Medium Priority`, `## Long-term`, `## Daily Habits`

---

## 🔧 Advanced Usage

### Velocity Tracking
Calculate work blocks per hour from diary.md:
```bash
python3 tools/goal-tracker.py velocity --hours 24
```

Output:
```
Velocity (last 24 hours):
  Work blocks: 47
  Time span: 23.5 hours
  Rate: 2.0 blocks/hour
```

### Export for Reporting
Export goals to JSON for integrations:
```bash
python3 tools/goal-tracker.py export --format json --output goals-export.json
```

Export to Markdown for sharing:
```bash
python3 tools/goal-tracker.py export --format markdown --output goals-summary.md
```

### Weekly Goal Files
Work with specific week files:
```bash
python3 tools/goal-tracker.py week 2
```

Reads from `goals/week-2.md` instead of `goals/active.md`.

---

## 🎨 Color Output

Goal Tracker uses terminal colors for readability:
- 🟢 Green = Completed goals
- 🔴 Red = High priority
- 🟡 Yellow = Medium priority
- 🔵 Blue = Info headers

Disable colors with `NO_COLOR=1`:
```bash
NO_COLOR=1 python3 tools/goal-tracker.py list
```

---

## 🔍 Progress Note Extraction

When you run `progress <goal>`, Goal Tracker scans `diary.md` for:
- Work blocks mentioning the goal name
- "Outcome:" or "Result:" sections
- Timestamps within the last 7 days

Example:
```bash
$ goal-tracker.py progress "Build pattern recognition system"

Progress: Build pattern recognition system

[2026-02-01T14:23Z] Created pattern analyzer
  → Built tools/pattern-analyzer.py
  → Generated reports/patterns-2026-02-01.md
  → Status: Testing phase

[2026-02-01T16:45Z] Enhanced with anomaly detection
  → Added statistical anomaly detection
  → Output: 3 anomalies found in last 100 blocks
```

---

## 🚫 Limitations

- **Goal name matching:** Fuzzy matching — use unique substrings
- **File paths:** Expects `goals/` and `diary.md` in workspace root
- **Markdown format:** Only supports `##` sections and `[ ]` checklist items
- **Progress notes:** Only scans `diary.md`, not other files

---

## 📈 Integration with Other Tools

### with diary-digest.py
```bash
# Show velocity + recent work
python3 tools/goal-tracker.py velocity
python3 tools/diary-digest.py --today
```

### with task-randomizer.py
```bash
# Get suggestion, then randomize if undecided
python3 tools/goal-tracker.py suggest
python3 tools/task-randomizer.py
```

### with self-improvement-loop.py
```bash
# Check stats, then run improvement analysis
python3 tools/goal-tracker.py stats --json
python3 tools/self-improvement-loop.py
```

---

## 🤝 Contributing

This tool is part of Nova's autonomous toolkit. Built for:
- Personal productivity tracking
- Goal completion visualization
- Velocity measurement

**Created:** 2026-01-31
**Maintained:** Nova (autonomous agent)
**License:** MIT

---

## 📝 Changelog

### v1.2 (2026-02-01)
- Added `velocity` command for diary.md tracking
- Added `export` with JSON/Markdown formats
- Enhanced fuzzy matching for goal names

### v1.1 (2026-01-31)
- Added `progress` command with diary.md scanning
- Added `suggest` for next goal recommendation
- Added color output for readability

### v1.0 (2026-01-30)
- Initial release
- Basic list/complete/stats commands
- Support for goals/active.md

---

*For more tools, see `tools/TOOL-INVENTORY.md`*
