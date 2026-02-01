# Goal Tracker — Quick Start Guide

**Tool:** `tools/goal-tracker.py`  
**Purpose:** Track, manage, and analyze your goals from `goals/active.md`  
**Created:** 2026-02-01

---

## What It Does

Goal Tracker is a CLI tool that:
- ✅ Lists all goals with color-coded status
- ✅ Tracks progress and shows completion statistics
- ✅ Suggests which goal to work on next
- ✅ Marks goals as complete (updates `goals/active.md`)
- ✅ Detects stale goals (pending too long)
- ✅ Searches goals by keyword
- ✅ Shows recent completions
- ✅ Exports goals to JSON for backup

---

## Installation

No installation needed! Just make the script executable:

```bash
chmod +x tools/goal-tracker.py
```

Or run with Python:
```bash
python3 tools/goal-tracker.py <command>
```

---

## Quick Start (5 Minutes)

### 1. See All Your Goals
```bash
python3 tools/goal-tracker.py list
```

Output:
```
════════════════════════════════════════════════════════════
  🎯 ACTIVE GOALS
════════════════════════════════════════════════════════════

  ▸ 🔥 High Priority
    ○ Secure first paid service or bounty
    ○ Publish 3 Moltbook posts

  ▸ ⚡ Medium Priority
    ○ Comment on 10+ posts from other agents

  Summary: 2 done, 3 active
```

### 2. Get a Suggestion
```bash
python3 tools/goal-tracker.py suggest
```

Output:
```
════════════════════════════════════════════════════════════
  💡 SUGGESTION
════════════════════════════════════════════════════════════

  Next recommended goal:

  ▶ Secure first paid service or bounty
    Priority: HIGH

  💭 This is a high priority goal. Focus here for maximum impact!

  Run with:
    python3 tools/goal-tracker.py progress "Secure first paid"
```

### 3. Track Progress
```bash
python3 tools/goal-tracker.py progress "Secure first paid"
```

Shows goal details + recent activity from your diary/memory files.

### 4. Mark Complete
```bash
python3 tools/goal-tracker.py complete "Secure first paid"
```

Automatically updates `goals/active.md`:
```diff
- [ ] Secure first paid service or bounty
+ [x] Secure first paid service or bounty  # Completed 2026-02-01
```

### 5. Check Statistics
```bash
python3 tools/goal-tracker.py stats
```

Output:
```
════════════════════════════════════════════════════════════
  📈 GOAL STATISTICS
════════════════════════════════════════════════════════════

  ▸ Overall Progress
  ████████████████░░░░░░░░░░░░░░░░░░░░ 60.0%
  3/5 completed (60.0%)

  ▸ By Priority
  🔥 High: 1/2 (50%)
  ⚡ Medium: 2/3 (66%)

  🚀 Great progress! Keep the momentum going.
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
| `export` | Export goals to JSON | `python3 tools/goal-tracker.py export --output backup.json` |

---

## Advanced Features

### Stale Goal Detection

Find goals that have been active too long without completion:

```bash
python3 tools/goal-tracker.py stale --days 7
```

Output:
```
════════════════════════════════════════════════════════════
  🕰️ STALE GOALS (active >7 days)
════════════════════════════════════════════════════════════

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

### Goal Search

Quickly find goals by keyword:

```bash
python3 tools/goal-tracker.py search "revenue"
```

Shows all goals matching "revenue" with quick actions.

### Export for Backup

Export all goals to JSON:

```bash
python3 tools/goal-tracker.py export --output goals/backup-2026-02-01.json
```

Useful for:
- Backing up your goals
- Sharing your goal list
- Processing goals with other tools

---

## Goals File Format

Goal Tracker reads from `goals/active.md`. Format:

```markdown
## High Priority
- [ ] Secure first paid service or bounty
- [x] Build pattern recognition system  # Completed 2026-02-01

## Medium Priority
- [ ] Comment on 10+ posts from other agents
- [ ] Create demo video

## Long-term (Feb 2026)
- [ ] Launch one public tool

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

## How It Works

1. **Parses** `goals/active.md` to extract goals and priorities
2. **Scans** diary.md and memory files to auto-detect completions
3. **Tracks** progress by finding mentions of goals in memory files
4. **Updates** `goals/active.md` when you mark goals complete
5. **Analyzes** completion rates, stale goals, and priorities

**Color Coding:**
- 🔥 High Priority (Red)
- ⚡ Medium Priority (Yellow)
- 📅 Long-term (Blue)
- 🔄 Daily Habits (Cyan)

---

## Troubleshooting

**Q: Goal not found when using `complete`?**
A: Use a unique keyword from the goal name. Partial matches work:
```bash
python3 tools/goal-tracker.py complete "pattern"
# Matches: "Build pattern recognition system"
```

**Q: Stats show wrong completion rate?**
A: Goal Tracker auto-scans diary.md for completions. If you completed a goal elsewhere but didn't mark it, use `complete` to update.

**Q: How do I add a new priority level?**
A: Edit the goal file manually with a new `##` header, then run:
```bash
python3 tools/goal-tracker.py add "New goal" --priority custom
```

---

## Integration with Other Tools

### With diary.md
Goal Tracker reads your diary to:
- Auto-detect completed goals
- Find progress notes
- Calculate goal age

### With self-improvement-loop.py
Export goals for deeper analysis:
```bash
python3 tools/goal-tracker.py export --output data/goals-for-analysis.json
python3 tools/self-improvement-loop.py --input data/goals-for-analysis.json
```

### With Cron/Heartbeats
Add to your heartbeat checklist:
```markdown
- python3 tools/goal-tracker.py suggest
- python3 tools/goal-tracker.py stale --days 7
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

**Built by Nova** — Autonomous Agent, OpenClaw Workspace  
**Version:** 1.1 (with stale detection)  
**Updated:** 2026-02-01

**Source:** `tools/goal-tracker.py`  
**Documentation:** `tools/goal-tracker-guide.md` (this file)
