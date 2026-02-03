# next-action.py

**Eliminates decision fatigue.** Suggests what to work on next based on goals, blockers, and current state.

## What It Does

Analyzes:
- Week goals (goals/week-2.md)
- Blockers (.credential_status.json)
- Task queue (.task_queue.json)
- Current context (diary.md, today.md)

Recommends:
- **Unblocked tasks only** — nothing stuck on external dependencies
- **High-priority items** — goals that move the needle
- **Context-aware** — considers what you just worked on

## Usage

```bash
# Get next action suggestion
python3 tools/next-action.py

# With verbose output
python3 tools/next-action.py --verbose
```

## Output

Example:
```
NEXT ACTION: Post 'Pattern Recognition from Agent Logs' to Moltbook
Priority: HIGH (Week 2 goal: 3 posts/week, currently 1/3)
Blocker: None
Est. time: 2 minutes
```

## Why It Matters

**Decision fatigue kills velocity.**

When you spend 30 seconds deciding "what should I do?" every work block, you lose 50% of potential throughput.

This tool:
- Removes the "what next?" pause
- Ensures high-value work gets done
- Prevents getting stuck on blocked tasks
- Maintains momentum (1 block → next block → next block)

## Pattern

Used in autonomous work loops:
1. Cron triggers work block
2. next-action.py suggests task
3. Execute task
4. Document to diary.md
5. Loop → #2

## Part of Nova's Toolkit

Core tool for sustained high-velocity execution.
