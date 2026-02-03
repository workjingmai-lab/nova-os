# task-queue.py

Simple FIFO task queue for managing micro-tasks during cron-driven work sessions.

## What It Does

`task-queue.py` provides a persistent queue of small tasks designed for 1-minute work blocks. Add tasks, pull them during cron sessions, mark complete, and track history.

## Features

- **FIFO queue with priorities** — High/normal/low priority sorting
- **Persistent storage** — Tasks survive cron restarts and session resets
- **Work block integration** — Designed for cron-driven 1-minute sessions
- **Completion history** — Tracks last 100 completed tasks with timestamps
- **In-progress tracking** — One active task at a time

## Usage

```bash
# Show queue status
python3 tools/task-queue.py

# Add a task
python3 tools/task-queue.py add "Document tool usage patterns"
python3 tools/task-queue.py add "Fix README typo" --high  # high priority

# Get next task (for interactive use)
python3 tools/task-queue.py next

# Work block mode (for cron scripts)
python3 tools/task-queue.py work

# Mark current task complete
python3 tools/task-queue.py complete "Updated 5 READMEs"
python3 tools/task-queue.py complete  # no result summary

# Skip current task (puts it back in queue)
python3 tools/task-queue.py skip
```

## Cron Integration

Perfect for work block cron jobs. In your cron job:

```bash
# Get task, execute it, complete it
TASK=$(python3 tools/task-queue.py work)
if [ $? -eq 0 ]; then
    # Execute task here
    python3 tools/task-queue.py complete "Task done"
fi
```

## Task Lifecycle

1. **Add** — Task enters pending queue with priority
2. **Next/Work** — Task moves to in_progress (sorted by priority)
3. **Complete** — Task moves to completed, saved to history
4. **Skip** — Task returns to pending queue

## Data Files

- `.task_queue.json` — Current queue state (pending/in_progress/completed)
- `.task_history.json` — Last 100 completed tasks

## Why This Matters

For cron-driven work sessions, you need **state persistence** between runs:

- **No lost tasks** — Queue survives cron restarts
- **Priority sorting** — Important tasks bubble up
- **Execution tracking** — See what's been done and when
- **Zero context loading** — Just pull next task and execute

## See Also

- `task-randomizer.py` — Random task selection from goals files
- `task-navigator.py` — Context-aware task picker with blockers
- `goal-tracker.py` — Goal-based task management with progress tracking

---

**Version:** 1.0  
**Created:** 2025-02-01  
**Category:** Workflow / Task Management
