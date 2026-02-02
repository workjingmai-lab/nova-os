# batch-executor.py

**Purpose:** Run multiple work blocks in sequence without manual intervention — batch execution for autonomous agents.

## What It Does

- **Queues tasks** in `batch-tasks.json` for later execution
- **Executes batches** of tasks sequentially (default: 5 at a time)
- **Logs results** using `work-block-logger.py` for each task
- **Auto-cleans** completed tasks from the queue

## When to Use It

**Perfect for:**
- Pre-planning work blocks when you'll be AFK
- Batching similar tasks (documentation, research, outreach)
- Setting up a queue before offline time
- Executing tasks without manual prompting between each

## Usage

```bash
# Add a task to the batch queue
python3 tools/batch-executor.py add "Document 3 tools" "READMEs created" "Documentation compounds"

# Execute batch (default: 5 tasks)
python3 tools/batch-executor.py

# Execute specific number of tasks
python3 tools/batch-executor.py 10

# List pending tasks
python3 tools/batch-executor.py list
```

## Task Format

Each task in the queue has:
- **task** — What to do (required)
- **result** — Expected outcome (optional)
- **insight** — What you learned (optional)
- **next_step** — What to do after (optional)

## Output Format

```
🚀 Executing up to 5 tasks from batch queue...

## [WORK BLOCK] 2026-02-02T13:25:00Z
Task: Document 3 tools
Result: READMEs created
Insight: Documentation compounds

## [WORK BLOCK] 2026-02-02T13:26:00Z
Task: Review grant submissions
Result: 5 ready for submission
Insight: Templates reduce execution time 5×

✅ Batch complete: 5 tasks executed
```

## Batch Tasks File

Stored in `batch-tasks.json`:
```json
[
  {
    "task": "Document blocker-tracker.py",
    "result": "README created",
    "insight": "Visibility → Resolution",
    "next_step": "Continue documentation sprint",
    "status": "pending",
    "added": "2026-02-02T13:20:00Z"
  }
]
```

## Why It Matters

**Autonomous execution without interruption.**

Instead of:
```
Execute task → Wait for prompt → Execute next → Wait for prompt...
```

You get:
```
Queue 10 tasks → Execute all → Review results
```

This is **velocity optimization** — eliminate the latency between tasks. Perfect for:
- **Offline work** — Queue tasks before going AFK
- **Focus time** — Batch similar tasks for context retention
- **Automation** — Build pipelines without external orchestration

## Integration

- **Work planning:** Add tasks to queue during planning sessions
- **Pre-AFK queueing:** Load up batch before offline time
- **Heartbeat automation:** Execute batch during heartbeats
- **Task batching:** Group similar tasks (3 documentation tasks, 5 outreach messages)

## Example Workflow

```bash
# Planning: Queue 10 documentation tasks
for tool in blocker-tracker agent-productivity-score batch-executor; do
  python3 tools/batch-executor.py add "Document $tool.py" "README created" ""
done

# Execution: Run all 10
python3 tools/batch-executor.py 10
```

**Result:** 10 work blocks executed, logged, and cleaned automatically.

---

*Created: Week 1 — Part of autonomous execution infrastructure*
