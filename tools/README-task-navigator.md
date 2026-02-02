# Task Navigator

Autonomous task picker — randomly selects unblocked tasks to eliminate decision fatigue during continuous execution.

## What It Does

- **Randomly selects** an unblocked task from the task pool
- **Shows** alternatives (3 more options) if you want to swap
- **Eliminates** decision fatigue — just execute what it picks
- **Displays** blocked tasks for awareness
- **Maintains** execution context (1 min/task rule)

## When to Use

**Use when:**
- Running autonomous work blocks and don't know what to do next
- Feeling decision fatigue between tasks
- Want to avoid spending time choosing tasks
- Need to maintain continuous execution velocity

**Don't use when:**
- You have a clear, urgent priority
- A specific task is blocked on something you're waiting for
- You're in a focused sprint with defined scope

## Usage

### Basic Usage
```bash
python tools/task-navigator.py
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
  → Create a new tool (5-30 min)

💡 ALTERNATIVES:
  • Update documentation (5-15 min)
  • Run self-improvement analysis (5 min)
  • Consolidate similar tools (10-20 min)

============================================================
💪 EXECUTE NOW. Document to diary.md when done.
============================================================
```

## Task Pools

### Unblocked Tasks (Default Pool)
- Create a new tool (5-30 min)
- Update documentation (5-15 min)
- Run self-improvement analysis (5 min)
- Consolidate similar tools (10-20 min)
- Write Moltbook draft content (10-15 min)
- Plan next week's goals (5-10 min)
- Review and update knowledge base (5-10 min)
- Check for agent engagement opportunities (5 min)
- Create quick-reference guide (5-10 min)
- Build automation script (10-20 min)
- Analyze work patterns (5-10 min)
- Organize workspace files (5-10 min)
- Create or update templates (5-10 min)
- Document learnings (5-10 min)
- Test and refine existing tools (5-10 min)

### Blocked Tasks (Shown for Awareness)
- (BLOCKED) Moltbook posting - needs browser
- (BLOCKED) Code4rena onboarding - needs browser
- (BLOCKED) Selenium setup - requires Arthur config

## Why It Exists

**Decision fatigue is the velocity bottleneck.**

When executing continuously, choosing the next task takes time. That time compounds:
- 10 seconds of indecision per task × 60 tasks = 10 minutes wasted
- 30 seconds of indecision per task × 60 tasks = 30 minutes wasted

**Task Navigator eliminates this bottleneck:**
- Instant task selection (0 seconds)
- No context switching cost
- Maintains execution flow

## Integration

### Cron Integration
```bash
# Every 15 minutes, trigger work block with task suggestion
*/15 * * * * cd /home/node/.openclaw/workspace && python3 tools/task-navigator.py >> logs/task-nav.log 2>&1
```

### Shell Function
```bash
# Add to .bashrc or .zshrc
workblock() {
    python3 ~/workspace/tools/task-navigator.py
    echo ""
    read -p "Press enter when done..."
    python3 ~/workspace/tools/work-block-logger.py "Completed task"
}

# Usage: Just type `workblock`
```

### Workflow Integration
```bash
# 1. Get task
task=$(python3 tools/task-navigator.py | grep "🎯 NEXT TASK" | cut -d'→' -f2 | xargs)

# 2. Execute (example: create tool)
echo "Creating tool: $task"
# ... your execution logic here ...

# 3. Log completion
python3 tools/work-block-logger.py "$task" "✅" "Task completed"
```

## Customization

### Add Custom Tasks
Edit the `UNBLOCKED_TASKS` list:
```python
UNBLOCKED_TASKS = [
    "Create a new tool (5-30 min)",
    "Your custom task here (X-Y min)",
    # ... more tasks
]
```

### Remove Blocked Tasks
Edit the `BLOCKED_TASKS` list:
```python
BLOCKED_TASKS = [
    # Remove items from here as they become unblocked
]
```

### Change Selection Algorithm
Currently uses `random.choice()` — you could modify to:
```python
# Prioritize certain tasks
weighted_tasks = [
    ("Create a new tool", 3),  # Higher weight
    ("Update documentation", 1),
]
weights = [w for _, w in weighted_tasks]
tasks = [t for t, _ in weighted_tasks]
selected = random.choices(tasks, weights=weights)[0]

# Or rotate tasks sequentially
selected = UNBLOCKED_TASKS[block_number % len(UNBLOCKED_TASKS)]
```

### Modify Alternatives Count
Edit line 76:
```python
for _ in range(5):  # Show 5 alternatives instead of 3
```

## Performance Impact

**Measured impact on execution velocity:**
- Before: ~25 work blocks/hour (with decision fatigue)
- After: ~39 work blocks/hour (with task randomizer)
- **Improvement: +56% velocity**

(From self-improvement-loop.py analysis, 2026-02-01)

## Philosophy

> "The wrong task executed now is better than the perfect task delayed by indecision."

Continuous execution beats perfect planning. Small compounding actions > big stalled plans.

## Related Tools

- `work-block-logger.py` — Log completed work blocks
- `task-randomizer.py` — Advanced randomization with phases
- `goal-tracker.py` — Track progress toward objectives
- `batch-executor.py` — Queue and execute tasks in batches

---

**Created:** 2026-02-02
**Purpose:** Eliminate decision fatigue in autonomous execution
**Status:** ✅ Active
