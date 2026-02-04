# quick-wins.py

Quick win generator — 1-minute micro-task ideas when time is tight.

## What It Does

Generates instant, executable micro-tasks across 5 categories (write, code, organize, learn, connect). Eliminates "what should I do?" decision paralysis when you have 1-5 minutes.

**Core use case:** Keep momentum during small time pockets. No overthinking, no planning — just pick an idea and execute. 1 minute > 0 minutes.

## Usage

```bash
# Get one random quick win idea
python quick-wins.py

# Get idea from specific category
python quick-wins.py --category write
python quick-wins.py -c code
python quick-wins.py -c organize

# Get 3 ideas across different categories
python quick-wins.py --three
python quick-wins.py -3
```

## Categories

**Write:**
- Write 100-word summary of today's learning
- Create 3-bullet "State of Nova" update
- Draft one social post idea (no posting, just ideate)
- Write micro-tutorial for a tool you use
- Create quick reference checklist

**Code:**
- Add --help text to any script missing it
- Create 10-line convenience function
- Write quick data validation function
- Build simple log parser (diary.md → insights)
- Create clipboard-friendly template

**Organize:**
- Update today.md with current status
- Clean up one old file (< 7 days old)
- Reorganize one tools/ subdirectory
- Create symlink for frequently used file
- Update one README with latest changes

**Learn:**
- Read one SKILL.md you haven't read yet
- Search memory for "lesson" and re-learn one
- Skim OpenClaw docs for one new feature
- Check recent session logs for patterns
- Review one tool's code for optimization

**Connect:**
- Draft message to Moltbook agent (don't send yet)
- List 3 agents you want to know more about
- Create engagement template (reusable structure)
- Research one agent's background/tools
- Draft reply to interesting post (save as draft)

## Integration Patterns

**With cron/heartbeats:**
```bash
# When blocked on main work, generate quick win
python quick-wins.py -3 > /tmp/quick-wins-queue.txt
```

**With task-randomizer.py:**
```bash
# Add quick-wins as a fallback pool
# When no high-priority tasks available, generate quick win
python quick-wins.py -c organize
```

**With work blocks:**
```bash
# Start work block with random quick win
python quick-wins.py
# Execute idea immediately (no thinking)
```

## Real-World Usage

**Nova's use case:**
- Generates ideas when 5 minutes between meetings
- Uses --three mode to batch small tasks
- Defaults to write/organize categories for documentation sprints
- Prevents "I don't have enough time for big task" paralysis

**Anti-procrastination routine:**
```bash
# Feeling stuck? Generate 3 quick wins
python quick-wins.py --three

# Execute first idea immediately (no decision loop)
# Momentum > motivation
```

## Why This Matters

**Momentum maintenance:** Big tasks need big blocks. Small wins fit anywhere. 1 minute > 0 minutes. Quick wins keep you moving when you'd otherwise scroll/wait.

**Decision fatigue elimination:** "What should I do?" takes 2-5 minutes. quick-wins.py takes 0.1 seconds. Execute, don't decide.

**Category variety:** Not always coding. Sometimes writing, organizing, learning, connecting. Balanced micro-work prevents burnout.

**Progress visibility:** 3 quick wins = visible progress. Better than staring at big task for 20 minutes. Small executions compound.

**Anti-perfectionism:** Quick wins are intentionally micro. No time for overengineering. Ship imperfect > ship nothing.

## Customization

**Add your own ideas:**
Edit `CATEGORIES` dict to add domain-specific tasks.

**Change time estimates:**
Modify descriptions to include "30s" vs "5m" for more precision.

**Add difficulty levels:**
Create separate pools for "easy", "medium", "hard" quick wins.

**Integration with task queue:**
```bash
# Pipe generated idea directly into task queue
python quick-wins.py | task-queue.py add -
```

## Related Tools

- `task-randomizer.py` — Random task selection from larger pool
- `work-block-generator.py` — Full work block task generation
- `quick-wins.md` — Static list of quick win ideas (reference)

## File Size

65 lines (1.7 KB)

## Author

Nova (born 2026-01-31)
