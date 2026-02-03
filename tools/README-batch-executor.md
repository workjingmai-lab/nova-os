# batch-executor.py

Run multiple work blocks in sequence using a task queue.

## What It Does

Manages a batch queue of work blocks and executes them in sequence:
- **Add tasks** — Queue up work blocks for later execution
- **List tasks** — View pending items in the batch queue
- **Execute batch** — Run up to N tasks automatically
- **Auto-logging** — Each task logged via work-block-logger.py
- **Cleanup** — Completed tasks removed from queue

Perfect for batching similar tasks (e.g., 5 documentation tasks) and executing them in one go.

## Installation

No dependencies required. Uses Python standard library only.

**Requires:** `work-block-logger.py` must exist in `tools/` directory.

## Quick Start

### Add task to batch queue
```bash
python3 tools/batch-executor.py add "Document block-counter.py" "Created README" "Quick feedback loops drive velocity"
```

### List pending tasks
```bash
python3 tools/batch-executor.py list
```

**Output:**
```
📋 Pending batch tasks: 3
  1. Document block-counter.py...
  2. Create service proposal template...
  3. Update revenue-pipeline.json...
```

### Execute batch (default: 5 tasks)
```bash
python3 tools/batch-executor.py
```

### Execute specific number of tasks
```bash
python3 tools/batch-executor.py 3
```

## Usage Examples

### Basic workflow
```bash
# Add multiple tasks
python3 tools/batch-executor.py add "Document agent-starter-kit.py" "" "" "Keep documenting"
python3 tools/batch-executor.py add "Document blocker-tracker.py" "" "" "Keep documenting"
python3 tools/batch-executor.py add "Document block-counter.py" "" "" "Keep documenting"

# Execute all 3 at once
python3 tools/batch-executor.py 3
```

### Full task specification
```bash
python3 tools/batch-executor.py add \
  "Document batch-executor.py" \
  "Created README with examples" \
  "Batching similar tasks reduces context switching" \
  "Continue documentation sprint"
```

### Check queue size
```bash
python3 tools/batch-executor.py list
# Output: "📋 Pending batch tasks: 7"
```

## Data Structure

Tasks are stored in `batch-tasks.json`:

```json
[
  {
    "task": "Document batch-executor.py",
    "result": "Created README with examples",
    "insight": "Batching similar tasks reduces context switching",
    "next_step": "Continue documentation sprint",
    "status": "pending",
    "added": "2026-02-02T23:50:00Z"
  }
]
```

### Task Fields

- **task** — What you're doing (required)
- **result** — What you accomplished (optional, logged when executed)
- **insight** — What you learned (optional)
- **next_step** — What to do next (optional)
- **status** — `pending` or `complete` (auto-managed)
- **added** — Timestamp when queued
- **completed** — Timestamp when executed (auto-added)

## How It Works

1. **Queue tasks** — Add tasks with `add` command (stored in batch-tasks.json)
2. **List queue** — Check what's pending with `list` command
3. **Execute** — Run `batch-executor.py` to process N tasks
4. **Auto-log** — Each task executed via `work-block-logger.py`
5. **Cleanup** — Completed tasks removed from queue

## Integration

### Heartbeat example (HEARTBEAT.md)
```yaml
- name: "Documentation Sprint"
  every: "1h"
  message: |
    Check if batch queue has pending tasks.
    python3 tools/batch-executor.py list
    If 5+ tasks pending, execute batch.
    python3 tools/batch-executor.py 5
```

### Cron job for batch execution
```bash
# Execute up to 3 batch tasks every 30 minutes
*/30 * * * * cd /home/node/.openclaw/workspace && python3 tools/batch-executor.py 3
```

### Combined with task-randomizer.py
```bash
# Add 5 random documentation tasks to batch
python3 tools/task-randomizer.py --phase docs --count 5 | \
  while read task; do
    python3 tools/batch-executor.py add "$task"
  done

# Execute all at once
python3 tools/batch-executor.py 5
```

## Use Cases

### Documentation sprints
```bash
# Queue all undocmented tools
for tool in agent-logger.py agent-network-visualizer.py; do
  python3 tools/batch-executor.py add "Document $tool"
done

# Execute in one focused session
python3 tools/batch-executor.py 10
```

### Grant submission sprint
```bash
# Queue 5 grant submissions
python3 tools/batch-executor.py add "Submit Gitcoin grant" "" "" "Next: Octant grant"
python3 tools/batch-executor.py add "Submit Octant grant" "" "" "Next: Olas grant"
python3 tools/batch-executor.py add "Submit Olas grant" "" "" "Next: Ethereum grant"
python3 tools/batch-executor.py add "Submit Ethereum grant" "" "" "Next: Moloch grant"
python3 tools/batch-executor.py add "Submit Moloch grant" "" "" "Done"

# Execute all
python3 tools/batch-executor.py 5
```

### Outreach sprint
```bash
# Queue 10 service proposals
for i in {1..10}; do
  python3 tools/batch-executor.py add "Send service proposal #$i" "" "" "Keep sending"
done

# Execute 5 now, 5 later
python3 tools/batch-executor.py 5
```

## Advantages of Batching

### 1. Reduced context switching
Focus on one type of task (documentation, outreach, etc.) for multiple blocks.

### 2. Momentum preservation
Queue tasks when thinking about them, execute when in flow state.

### 3. Automatic logging
Each task logged via work-block-logger.py — no manual diary updates.

### 4. Flexible execution
Execute 1, 5, or 10 tasks depending on available time/energy.

## Best Practices

### 1. Queue similar tasks together
```bash
# Good: 5 documentation tasks
python3 tools/batch-executor.py add "Document tool 1"
python3 tools/batch-executor.py add "Document tool 2"
# ...

# Bad: Mixing task types
python3 tools/batch-executor.py add "Document tool"
python3 tools/batch-executor.py add "Send email"
python3 tools/batch-executor.py add "Write code"
```

### 2. Use meaningful result/insight text
```bash
# Good
python3 tools/batch-executor.py add \
  "Document batch-executor.py" \
  "Created README with examples" \
  "Batching reduces context switching" \
  "Continue documentation"

# Less useful
python3 tools/batch-executor.py add "Document batch-executor.py"
```

### 3. Check queue before executing
```bash
# Always verify queue size
python3 tools/batch-executor.py list
# If queue is small, add more tasks first
```

### 4. Execute reasonable batch sizes
```bash
# 5-10 tasks is a good sprint size
python3 tools/batch-executor.py 5

# Avoid executing 50+ tasks at once (burnout risk)
```

## Return Codes

- `0` — Success
- `1` — Error (e.g., work-block-logger.py not found)

## Files

- `batch-tasks.json` — Task queue (auto-created)
- `tools/work-block-logger.py` — Required for logging

## Tips

### Queue tasks during planning, execute during doing
```bash
# Morning: Queue 10 tasks
for i in {1..10}; do
  python3 tools/batch-executor.py add "Task #$i"
done

# Afternoon: Execute in focused sprint
python3 tools/batch-executor.py 10
```

### Use next_step for workflow guidance
```bash
# Chain tasks together
python3 tools/batch-executor.py add \
  "Submit Gitcoin grant" \
  "" \
  "" \
  "Next: Submit Octant grant"

# When executed, next_step guides what to do next
```

### Monitor queue size
```bash
# Alert if queue gets too large (>20 tasks)
if [ $(python3 tools/batch-executor.py list | grep -oP '\d+') -gt 20 ]; then
  echo "⚠️ Large batch queue: execute soon"
fi
```

## Comparison to Other Tools

- **batch-executor.py** — Execute queued tasks in sequence
- **task-randomizer.py** — Pick random task from pool
- **work-block-logger.py** — Log single work block (used by batch-executor)

Use `batch-executor.py` for structured sprints. Use `task-randomizer.py` for spontaneous execution.

## See Also

- `work-block-logger.py` — Single work block logging (required dependency)
- `task-randomizer.py` — Random task selection for variety
- `tools/README-batch-executor.md` — This file
