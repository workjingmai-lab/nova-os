# Batch Executor

Task queue system for running multiple work blocks in sequence. Queue tasks, then execute them in batches.

## What It Does

- **Queue** tasks for later execution (add to batch-tasks.json)
- **Execute** pending tasks in batches (default: 5 at a time)
- **Log** each task using work-block-logger.py
- **Clean up** completed tasks automatically
- **List** pending tasks in the queue

## When to Use

**Use when:**
- You have multiple small tasks that can be batched
- Want to queue tasks now, execute later
- Running work blocks programmatically (cron, scripts)
- Need to track pending tasks across sessions

**Don't use when:**
- Task requires immediate attention (execute directly)
- Task is complex or time-consuming (>1 min)
- You're actively working in real-time (just execute directly)

## Usage

### Add Tasks to Queue
```bash
# Interactive
python tools/batch-executor.py add "Task description"

# With all fields
python tools/batch-executor.py add "Task description" "Expected result" "Insight" "Next step"
```

### List Pending Tasks
```bash
python tools/batch-executor.py list
```

### Execute Batch
```bash
# Execute up to 5 tasks (default)
python tools/batch-executor.py

# Execute up to N tasks
python tools/batch-executor.py 10
```

## Workflow

### Queue → Execute Pattern
```bash
# 1. Queue multiple tasks
python tools/batch-executor.py add "Write README for tool X"
python tools/batch-executor.py add "Review grant submissions"
python tools/batch-executor.py add "Check Moltbook API"

# 2. List pending
python tools/batch-executor.py list

# 3. Execute batch
python tools/batch-executor.py 3
```

### Programmatic Use
```bash
# Cron job to execute queued tasks hourly
0 * * * * cd /home/node/.openclaw/workspace && python tools/batch-executor.py 5 >> logs/batch.log 2>&1
```

## Data Storage

Tasks are stored in `batch-tasks.json`:
```json
[
  {
    "task": "Write README for tool X",
    "result": "README created",
    "insight": "Documentation enables ecosystem adoption",
    "next_step": "Continue documentation",
    "status": "pending",
    "added": "2026-02-02T13:00:00Z"
  }
]
```

## Output Example

### Adding Tasks
```
✅ Task added to batch queue (3 pending)
```

### Listing Tasks
```
📋 Pending batch tasks: 3
  1. Write README for tool X...
  2. Review grant submissions...
  3. Check Moltbook API...
```

### Executing Batch
```
🚀 Executing up to 5 tasks from batch queue...

**2026-02-02T13:01:00Z — WORK BLOCK #561**
**Task:** Write README for tool X
**Result:** ✅ Complete — README-tool-x.md created
...

✅ Batch complete: 3 tasks executed
```

## Features

### Automatic Logging
Each task is logged via `work-block-logger.py` with:
- Timestamp
- Task description
- Result/insight
- Next step

### Auto-Cleanup
Completed tasks are removed from `batch-tasks.json` after execution.

### Flexible Limits
Execute any number of tasks per batch:
- Small batches (3-5) for focused work
- Large batches (10+) for clearing backlog

## Integration

**Works with:**
- `work-block-logger.py` — Logs each executed task
- `diary.md` — Where work blocks are written
- Any tool or script that needs task queuing

## Use Cases

### 1. Offline Task Generation
Generate tasks when you don't have time to execute:
```bash
# Quick brain dump
batch-executor.py add "Fix bug in script X"
batch-executor.py add "Test new feature"
# Later...
batch-executor.py 2  # Execute both
```

### 2. Scheduled Batch Execution
Queue tasks during the day, execute at night:
```bash
# During work hours
python tools/batch-executor.py add "Review PR #123"

# Nightly cron job
0 2 * * * python tools/batch-executor.py 10
```

### 3. Parallel Agent Work
Multiple agents can queue tasks, one executor:
```bash
# Agent 1
python tools/batch-executor.py add "Update docs"

# Agent 2
python tools/batch-executor.py add "Run tests"

# Executor (cron)
0 * * * * python tools/batch-executor.py 5
```

## Dependencies

- Python 3.7+
- `work-block-logger.py` (for logging executed tasks)
- No external packages (stdlib only)

## Related Tools

- `work-block-logger.py` — Logs individual work blocks
- `block-counter.py` — Count completed blocks
- `task-randomizer.py` — Random task selection

---

**Created:** 2026-02-02
**Purpose:** Task queueing for batched execution
**Status:** ✅ Active
