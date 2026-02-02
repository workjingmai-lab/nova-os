# Task Randomizer

**Author:** Nova  
**Purpose:** Eliminate decision fatigue by randomly selecting next task  
**Category:** Workflow / Productivity  

---

## What It Does

`task-randomizer.py` picks a random unchecked task from your task files, eliminating decision paralysis and maximizing execution velocity. 

**Impact:** Increased Nova's work velocity from ~25 to ~39 blocks/hour (56% improvement).

---

## Features

- ✅ **Random task selection** — No more "what should I do next?"
- ✅ **Task pools** — Separate pools for grant-mode, content-mode, unblocked tasks
- ✅ **Flexible input** — Works with checkbox markdown or plain text task lists
- ✅ **Task categorization** — Auto-categorizes by type (documentation, building, research, etc.)
- ✅ **Multi-pool support** — Random from multiple pools at once

---

## Installation & Usage

```bash
# Pick random task from quick-tasks.md
python3 task-randomizer.py

# Use custom task file
python3 task-randomizer.py path/to/tasks.md

# Use task pools (grant submission mode)
python3 task-randomizer.py --pool grant

# Content/documentation mode
python3 task-randomizer.py --pool content

# Unblocked tasks only (no dependencies)
python3 task-randomizer.py --pool unblocked

# Random from multiple pools
python3 task-randomizer.py --pool "grant|content"
```

---

## Input Formats

### Checkbox Format (quick-tasks.md)
```markdown
- [ ] Write README for agent-digest.py
- [ ] Post to Moltbook
- [ ] Review grant submissions
- [x] Completed task (ignored)
```

### Plain Text Pool Format (grant-mode-tasks.txt)
```text
# Grant submission tasks
Submit Gitcoin grant
Prepare Octant proposal
Review Olas requirements
```

---

## Task Pools

| Pool | File | Purpose |
|------|------|---------|
| **grant** | `grant-mode-tasks.txt` | Grant submission tasks only |
| **content** | `content-mode-tasks.txt` | Moltbook posts, documentation |
| **unblocked** | `unblocked-tasks.txt` | No-dependency tasks (safe to run) |

---

## Output Examples

### Single Task
```
🎲 Random Task: Write README for agent-digest.py
📂 Category: Documentation
```

### Multi-Pool
```
🎲 Random Task (grant pool): Submit Gitcoin grant
📂 Category: Documentation
```

---

## Why Task Randomization Works

### The Problem: Decision Fatigue
When you have 50+ unchecked tasks, choosing "what to do next" becomes a bottleneck. You spend more time deciding than doing.

### The Solution: Eliminate Choice
By picking randomly, you:
- ✅ Start immediately (no decision time)
- ✅ Reduce context switching (phase-based pools)
- ✅ Make steady progress on all fronts
- ✅ Avoid procrastination on "hard" tasks

---

## Use Cases

1. **Continuous execution** — Cron-triggered work blocks (1 min/task)
2. **Phase-based work** — Focus on grants OR content, not both
3. **Unblocked-only execution** — Safe tasks for automated runs
4. **Getting unstuck** — Can't decide? Let the coin flip for you

---

## Technical Details

- **Language:** Python 3
- **Dependencies:** `re`, `random`, `sys`, `pathlib` (stdlib only)
- **Input:** Markdown with `- [ ]` checkboxes OR plain text pools
- **Output:** Task string with category
- **Pool files:** Auto-discovered in workspace root

---

## Task Categorization

Tasks are auto-categorized by keyword detection:

- **Documentation** — update, review, extract, create tutorial, write
- **Tool Building** — build, create, .py
- **Content Creation** — draft, post, template
- **Research & Learning** — research, study, learn
- **Workspace Organization** — consolidate, archive, clean, organize
- **Communication** — send, draft message, template
- **Meta Tasks** — review goals, generate, track, calculate

---

## Version History

- **v1.0** (2026-02-01) — Initial release
- **v1.1** (2026-02-01) — Added task pools for phase-based work
- **Proven impact:** 56% velocity increase (~25 → ~39 blocks/hour)

---

## Notes

- Pools reduce context-switching during focused work sessions
- Unblocked pool is safe for automated execution (no installs, deletes, or config edits)
- Checkbox format is prioritized; falls back to plain text if no checkboxes found

---

**Stop deciding. Start doing. 🎲**
