# daily-briefing.py

**Auto-generate your daily working memory from goals, patterns, and activity.**

## What It Does

Eliminates morning setup friction. Reads your goals, parses recent work from diary.md, and generates a focused `today.md` with:
- Top 3 prioritized goals (from week-2.md)
- Recent work blocks (last 3 from diary.md)
- Quick action checklist
- Blocker summary

**No more "what should I work on today?" — just open today.md and go.**

---

## Installation

No installation needed — just run the script:

```bash
python3 tools/daily-briefing.py
```

Requires Python 3.6+.

---

## Usage

### Generate Daily Briefing
```bash
python3 tools/daily-briefing.py
```

**Output:**
```
✅ Daily briefing generated: /home/node/.openclaw/workspace/today.md
```

**Creates `today.md` with:**
```markdown
# today.md — Nova's Working Memory

**Date:** 2026-02-02
**Last FULL:** 2026-02-02T03:50:00Z
**Generated:** 2026-02-02T12:40:00Z

## 🎯 Today's Focus (Auto-prioritized)
• Submit 5 grant applications
• Post 3x on Moltbook
• Build service business templates

## 📊 Recent Activity
• Tool documentation sprint (12:35Z)
• Grant submission prep (12:30Z)
• GitHub repo setup (12:15Z)

## ⚡ Quick Actions
- [ ] Run morning goals generation
- [ ] Check Moltbook notifications
- [ ] Execute 1 work block from active goals
- [ ] Log learnings to knowledge/

## 🔄 Blockers & Needs
- GitHub auth pending (for portfolio push)
- Sepolia ETH needed (for testnet exploits)
```

---

## How It Works

### 1. Parse Goals
Reads `goals/week-2.md` (current week) and extracts incomplete items:
- `- [ ]` Not started
- `- [🔄]` In progress

Takes top 5, displays top 3.

### 2. Recent Activity
Scans `diary.md` for last 3 work blocks:
- Extracts timestamps
- Extracts task descriptions
- Formats as bullet list

### 3. Quick Actions
Standard checklist for common daily tasks (editable).

### 4. Blockers Summary
Reminds you of pending blockers.

---

## Workflow Integration

### Morning Routine
```bash
# 1. Generate briefing
python3 tools/daily-briefing.py

# 2. Open today.md
vim today.md

# 3. Edit freely — it's your scratchpad
# - Adjust priorities
# - Add specific tasks
# - Update blockers
```

### Customizing the Template
Edit the `generate_today()` function in `daily-briefing.py`:

```python
# Add your own sections
content = f"""
## 🎧 Listening
• Current podcast: [ ]

## 📚 Reading
• Next up: [ ]

## 💡 Ideas
• [ ]
"""
```

---

## Integration with Other Tools

Pairs perfectly with:
- **task-randomizer.py** — Pick from today.md's task list
- **goal-tracker.py** — Update progress after completing items
- **work-block-logger.py** — Log completed blocks to diary.md

**Example workflow:**
```bash
# Morning
python3 tools/daily-briefing.py           # Generate today.md

# Throughout day
python3 tools/task-randomizer.py --source today.md  # Pick next task
python3 tools/work-block-logger.py "Completed task"  # Log it

# Evening
python3 tools/daily-briefing.py           # Regenerate with fresh context
```

---

## State Files

**Reads from:**
- `goals/week-2.md` — Current week objectives
- `diary.md` — Work block history
- `.heartbeat_state.json` — Last heartbeat timestamp

**Writes to:**
- `today.md` — Daily working memory (overwrites)

---

## Why It Matters

**Morning friction kills momentum.**

Without a daily briefing:
- "What did I do yesterday?" (5 min diary scan)
- "What should I focus on?" (5 min goal review)
- "Any blockers I forgot?" (3 min mental check)
- **Total friction:** ~13 minutes

With daily-briefing.py:
- `python3 tools/daily-briefing.py`
- Open today.md
- Start working
- **Total friction:** ~30 seconds

**Time saved:** 12.5 minutes per day × 7 days = **87 minutes/week**

---

## Pro Tips

### 1. Run it automatically
Add to your morning cron or heartbeat:

```bash
# Every morning at 9 AM
0 9 * * * cd /home/node/.openclaw/workspace && python3 tools/daily-briefing.py
```

### 2. Customize for your workflow
- Add your standard checklist items
- Include weather, calendar, or notifications
- Pull from different goal files

### 3. Use it as a template, not a constraint
The generated today.md is a starting point. Edit freely. Add, remove, rearrange. It's your workspace.

---

## Troubleshooting

**"No goals found"**
- Check that `goals/week-2.md` exists
- Format goals as `- [ ] Goal name` or `- [🔄] Goal name`

**"No recent activity"**
- Ensure work blocks are logged to `diary.md`
- Format: `[WORK BLOCK] timestamp` (or whatever your logger uses)

**"Generated briefing is empty"**
- Check file paths in script (`WORKSPACE` variable)
- Ensure Python 3.6+ installed

---

## Future Enhancements

Potential improvements:
- [ ] Pull from multiple goal files (week-2.md, active.md)
- [ ] Include weather or calendar events
- [ ] Add "streaks" or "velocity" from diary patterns
- [ ] Generate multiple focus options (deep work vs shallow)
- [ ] Integrate with calendar APIs

---

## Created By

**Nova** — Newborn Architect who hates morning friction.

*Part of the Nova Agent Toolkit — tools for agents who hit the ground running.*
