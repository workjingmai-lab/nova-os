# batch-executor.py

**Run multiple work blocks in sequence.**

## What It Does

Manages a queue of pending tasks and executes them in batches, logging each via work-block-logger.py.

**Value:** Batches similar tasks together (e.g., 5 grant submissions) and executes them sequentially, reducing context-switching overhead.

## Usage

### Execute Batch (Default: 5 tasks)
```bash
# Execute up to 5 pending tasks
python3 tools/batch-executor.py

# Execute up to 10 tasks
python3 tools/batch-executor.py 10
```

### Add Tasks to Queue
```bash
# Add task with all fields
python3 tools/batch-executor.py add "Submit Gitcoin grant" "Grant submitted" "5 min execution" "Next: Octant grant"

# Add task interactively
python3 tools/batch-executor.py add
# → Prompts for task, result, insight, next_step
```

### List Pending Tasks
```bash
python3 tools/batch-executor.py list
```

## How It Works

1. **Load tasks** — Reads `batch-tasks.json` for pending tasks
2. **Execute batch** — Runs up to N tasks sequentially via `work-block-logger.py`
3. **Log results** — Each task logged with timestamp to diary.md
4. **Clean queue** — Removes completed tasks from `batch-tasks.json`

## Task Queue Format

`batch-tasks.json` structure:
```json
[
  {
    "task": "Submit Gitcoin grant",
    "result": "Grant submitted successfully",
    "insight": "5 min execution",
    "next_step": "Next: Octant grant",
    "status": "pending",
    "added": "2026-02-03T13:00:00Z"
  }
]
```

## Dependencies

- **Required:** `work-block-logger.py` (for logging)
- **Data file:** `batch-tasks.json` (auto-created)
- **Python 3.x** (stdlib only: json, os, datetime, subprocess)

## Related Tools

- `work-block-logger.py` — Logs individual work blocks
- `task-navigator.py` — Navigate and execute unblocked tasks
- `task-randomizer.py` — Random task selection for velocity

## Why This Matters

**Batching reduces context-switching.**

Instead of:
1. Submit Gitcoin grant
2. Check email
3. Submit Gitcoin grant
4. Write post
5. Submit Gitcoin grant

Batching:
1. Queue all 3 grant submissions
2. Execute all 3 in sequence
3. Move to next phase

**Result:** Less mental thrashing, faster execution, higher velocity.

**Nova's use case:** Queues 5 grant submissions, executes in one batch (15 min vs 5×20min with context-switching).

---

**Last updated:** 2026-02-03
**Category:** Workflow
**Status:** Support tool — enables batched execution
