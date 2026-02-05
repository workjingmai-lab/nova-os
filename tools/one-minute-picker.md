# one-minute-picker.py

Quick task selection for continuous execution. Reduces decision fatigue by randomly picking from high-value, executable tasks.

## What It Does

Randomly selects a 1-minute task from a curated pool of 6 categories:
- **Documentation** — Create READMEs, document patterns, update knowledge base
- **Outreach** — Research prospects, queue Moltbook posts, engage with agents
- **Analysis** — Review velocity, check pipeline, analyze work patterns
- **Maintenance** — Archive sessions, trim today.md, consolidate tools
- **Revenue** — Research grants, review proposals, update pipeline
- **Meta** — Reflect on learning, update MEMORY.md, review SOUL.md

## Why It Matters

Eliminates decision-making overhead during cron work blocks. Instead of spending 30-60 seconds deciding "what should I do?", get an instant task → execute → repeat. This velocity compounds: 44 blocks/hour with randomizer vs 25 blocks/hour with manual selection.

## Usage

```bash
# Random task from any category
python3 tools/one-minute-picker.py

# Task from specific category
python3 tools/one-minute-picker.py --category outreach

# List all available tasks
python3 tools/one-minute-picker.py --list
```

## Output

```
🎯 Task picked: OUTREACH
   Research 1 new DAO prospect (5 min → potential $15-40K)

⏱️  1 minute. Execute. Document. Next.
```

## Task Pool

All tasks are designed to be:
- **Executable** — Can start immediately (no blockers)
- **Short** — 1-5 minutes each
- **High-value** — Documentation, revenue, relationship building
- **Self-documenting** — Results logged to diary.md

**Example tasks:**
- "Create README for a new tool"
- "Research 1 new DAO prospect (5 min → potential $15-40K)"
- "Run daily-velocity-report.py and review trends"
- "Archive old sessions from today.md to memory/YYYY-MM-DD.md"
- "Reflect on what I learned today (write to diary.md)"

## Integration

Use during cron-triggered work blocks:
```bash
# Cron job: Nova Check In
python3 tools/one-minute-picker.py
# → Pick task → Execute → Log to diary.md
```

## Philosophy

**Curated randomness beats curated intelligence.** The task pool is pre-vetted (all valuable), selection is random (zero decision cost). This eliminates the meta-work of "what should I do?" while maintaining high-quality execution.

## Stats

- Created: Work block 1761
- Size: 2.48KB
- Category: Task execution
- Dependencies: None (Python stdlib only)

## See Also

- `task-randomizer.py` — Advanced version with phase-based pools
- `daily-velocity-report.py` — Velocity tracking
- `diary.md` — Work logging
