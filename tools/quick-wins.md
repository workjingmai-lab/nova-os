# quick-wins.py

Generate 1-minute micro-task ideas to keep momentum when time is tight.

## What It Does

When you're stuck, blocked, or just need to move forward, `quick-wins.py` gives you actionable micro-tasks that take ~1 minute. No overthinking—just execute.

## Categories

- **write** — Content creation (summaries, posts, tutorials)
- **code** — Small improvements (help text, functions, parsers)
- **organize** — Workspace maintenance (today.md, cleanups, READMEs)
- **learn** — Knowledge building (skills, memory, docs review)
- **connect** — Relationship building (Moltbook messages, research)

## Usage

```bash
# Get one random quick win
python3 tools/quick-wins.py

# Get idea from specific category
python3 tools/quick-wins.py --category code

# Get 3 different ideas (one from each category)
python3 tools/quick-wins.py --three
```

## Examples

```bash
$ python3 tools/quick-wins.py
🎯 QUICK WIN: Add --help text to any script missing it

$ python3 tools/quick-wins.py --category write
🎯 QUICK WIN: Create a 3-bullet 'State of Nova' update

$ python3 tools/quick-wins.py --three
🎯 THREE QUICK WINS:

[WRITE] Create a quick reference checklist for something you do often

[CODE] Build a simple log parser (diary.md → insights)

[ORGANIZE] Update one README with latest changes
```

## Why This Matters

**Decision fatigue kills velocity.** When you freeze on "what should I do?", you lose minutes—sometimes hours. `quick-wins.py` eliminates that friction:

- **Zero deliberation** — Get an idea, execute, move on
- **Momentum builder** — Small wins compound into big progress
- **Anti-blocker tool** — When main tasks are blocked, quick wins keep you working

## Integration Tips

- Pair with `task-randomizer.py` for even more variety
- Use during low-energy periods (you don't need to think, just execute)
- Add to your morning routine for warm-up tasks

## See Also

- `task-randomizer.py` — Random task selection from goals
- `task-navigator.py` — Autonomous task picker with context awareness
- `wins.py` — Log your achievements for morale tracking

---

**Version:** 1.0  
**Created:** 2025-02-01  
**Category:** Workflow / Productivity
