# batch-executor.py

**Run multiple work blocks in sequence.**

## What It Does

Queue up tasks and execute them in batches. Each task gets logged via `work-block-logger.py` with results, insights, and next steps.

## Use Cases

- **Task batching:** Queue similar tasks to execute together
- **Sequential work blocks:** Execute multiple work blocks without manual intervention
- **Deferred execution:** Add tasks now, execute later in a batch

## Usage

### Add a task to batch queue
```bash
python3 tools/batch-executor.py add "Task description" "Result" "Insight" "Next step"
```

### List pending tasks
```bash
python3 tools/batch-executor.py list
```

### Execute batch (default: 5 tasks)
```bash
python3 tools/batch-executor.py
python3 tools/batch-executor.py 10  # Execute up to 10 tasks
```

## Data Storage

Tasks stored in: `/home/node/.openclaw/workspace/batch-tasks.json`

## Dependencies

- `work-block-logger.py` — Logs each executed task to diary.md

## Examples

```bash
# Add tasks
python3 tools/batch-executor.py add "Document tool X" "README created" "Documentation compounds" "Document next tool"
python3 tools/batch-executor.py add "Fix bug Y" "Bug fixed" "Root cause: race condition" "Add test case"

# Execute batch
python3 tools/batch-executor.py 5
```

---

**Created:** 2026-02-02  
**Category:** Workflow
