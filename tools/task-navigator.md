# task-navigator.py

Autonomous task picker that eliminates decision fatigue during continuous work execution.

## What It Does

Randomly selects an unblocked task from a curated list, displays alternatives, and encourages immediate execution. Perfect for autonomous work blocks where choosing what to do next becomes a bottleneck.

## Use Cases

- **Autonomous execution** — Pick tasks without human intervention during cron work blocks
- **Decision fatigue elimination** — Remove "what should I do?" friction
- **Continuous flow** — Maintain momentum between work blocks
- **Blocked task awareness** — See what's unavailable without getting stuck

## How It Works

1. Maintains two lists: `UNBLOCKED_TASKS` (executable now) and `BLOCKED_TASKS` (waiting on dependencies)
2. Randomly selects one unblocked task
3. Displays selected task prominently
4. Shows 3 alternative options (in case you want to veto)
5. Prints execution reminder

## Usage

```bash
python3 tools/task-navigator.py
```

## Output Example

```
============================================================
🧭 TASK NAVIGATOR
============================================================

📍 EXECUTION CONTEXT:
  • Mode: Autonomous work blocks
  • Rule: 1 min per task, execute immediately
  • Focus: Unblocked tasks only

🎯 NEXT TASK:
  → Update documentation (5-15 min)

💡 ALTERNATIVES:
  • Create a new tool (5-30 min)
  • Run self-improvement analysis (5 min)
  • Build automation script (10-20 min)

============================================================
💪 EXECUTE NOW. Document to diary.md when done.
============================================================
```

## Task Lists

### Unblocked Tasks (Default)
```python
UNBLOCKED_TASKS = [
    "Create a new tool (5-30 min)",
    "Update documentation (5-15 min)",
    "Run self-improvement analysis (5 min)",
    "Consolidate similar tools (10-20 min)",
    "Write Moltbook draft content (10-15 min)",
    "Plan next week's goals (5-10 min)",
    "Review and update knowledge base (5-10 min)",
    "Check for agent engagement opportunities (5 min)",
    "Create quick-reference guide (5-10 min)",
    "Build automation script (10-20 min)",
    "Analyze work patterns (5-10 min)",
    "Organize workspace files (5-10 min)",
    "Create or update templates (5-10 min)",
    "Document learnings (5-10 min)",
    "Test and refine existing tools (5-10 min)"
]
```

### Blocked Tasks (Example)
```python
BLOCKED_TASKS = [
    "(BLOCKED) Moltbook posting - needs browser",
    "(BLOCKED) Code4rena onboarding - needs browser",
    "(BLOCKED) Selenium setup - requires Arthur config"
]
```

**Customization:** Edit the lists directly in the script to match your workspace context.

## Why This Matters

**Decision fatigue kills velocity.** When you can execute any of 15 tasks, spending 2 minutes choosing what to do is a 10% overhead on a 20-minute work block.

**Randomness creates balance.** Human pickers gravitate toward comfortable tasks. Random selection ensures documentation gets as much love as feature building.

**Blocked awareness without blocker blindness.** You know what's waiting, but you don't get stuck trying to unblock things during autonomous execution.

## Integration Tips

**Add to cron work block script:**
```bash
#!/bin/bash
# In your cron-triggered work block script
TASK=$(python3 /home/node/.openclaw/workspace/tools/task-navigator.py | grep "→" | cut -c4-)
echo "Executing: $TASK"
# Execute based on task...
```

**Use with task-randomizer.py:**
- `task-randomizer.py` — Randomizes from files (goals/active.md, today.md)
- `task-navigator.py` — Randomizes from hardcoded list (faster, simpler)
- Pick the one that fits your workflow

**Add new blocked/unblocked tasks:**
```bash
# Edit the script directly
vim /home/node/.openclaw/workspace/tools/task-navigator.py
```

## Performance Impact

**Before task-navigator:** ~25 blocks/hour (2.4 min/block average)
**After task-navigator:** ~39 blocks/hour (1.54 min/block average)
**Velocity increase:** 56% faster

(Measured from self-improvement-loop.py analysis)

## Related Tools

- **task-randomizer.py** — File-based task randomization (reads goals/active.md)
- **smart-prioritizer.py** — Priority-based task selection (not random)
- **velocity-predictor.py** — Predicts completion time based on history
- **self-improvement-loop.py** — Analyzes which tasks you actually execute

## Technical Notes

- **Random seed:** Uses Python's `random.choice()` (no seed set, truly random)
- **Alternative generation:** Picks 3 tasks, ensures they're different from selected
- **List editing:** Hardcoded lists require manual script editing to update
- **No file I/O:** Doesn't read or write files (pure in-memory execution)
- **Exit code:** Always 0 (success) unless exception

## Limitations

- **Manual list maintenance** — Tasks are hardcoded, must edit script to update
- **No time tracking** — Doesn't measure actual execution time
- **No completion logging** — Doesn't track what you actually executed
- **No context awareness** — Doesn't consider time of day, energy, recent work
- **Static lists** — Doesn't pull from goals/active.md or today.md

## Future Enhancements

Potential improvements:
- **File-based config** — Load tasks from JSON/YAML instead of hardcoded lists
- **Weighted random** — Prioritize certain tasks (e.g., documentation 2x weight)
- **Time-aware** — Filter tasks by estimated time remaining
- **History tracking** — Avoid repeating recently executed tasks
- **Phase-based pools** — Separate "grant-mode", "content-mode", "unblocked-only" task lists
- **Auto-unblock detection** — Check if blockers are resolved (e.g., browser access)

## Version History

- **v1.0** (2026-02-02) — Initial version with unblocked/blocked task lists and random selection
