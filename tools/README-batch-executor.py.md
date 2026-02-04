# batch-executor.py

**Run Multiple Work Blocks in Sequence**

Task queue and batch execution system — queue up work blocks, execute in batches, auto-logging to diary.md.

---

## What It Does

`batch-executor.py` provides:
- **Task queue** — Store pending work blocks in JSON
- **Batch execution** — Run multiple tasks sequentially
- **Auto-logging** — Each task logged via `work-block-logger.py`
- **Queue management** — Add, list, complete tasks
- **State persistence** — Queue survives restarts

Perfect for offline work block planning — queue up tasks, execute batch later.

---

## Installation

Requires `work-block-logger.py` in `tools/`.

```bash
python tools/batch-executor.py
```

---

## Usage

### Add Tasks to Queue

```bash
# Interactive (prompts for details)
python tools/batch-executor.py add "Document block-counter.py"

# With all fields
python tools/batch-executor.py add \
  "Document batch-executor.py" \
  "Created README (4753 bytes)" \
  "Batch execution = velocity multiplier" \
  "Continue documentation sprint"
```

Output:
```
✅ Task added to batch queue (3 pending)
```

### List Pending Tasks

```bash
python tools/batch-executor.py list
```

Output:
```
📋 Pending batch tasks: 3
  1. Document block-counter.py...
  2. Document batch-executor.py...
  3. Update revenue pipeline stats...
```

### Execute Batch

```bash
# Execute up to 5 tasks (default)
python tools/batch-executor.py

# Execute specific number
python tools/batch-executor.py 3
```

Output:
```
🚀 Executing up to 3 tasks from batch queue...

[2026-02-03T17:35:00Z] ### Work Block #1135 — 2026-02-03T17:35:00Z
**Task:** Document block-counter.py
**Execution:** Created README (4753 bytes)
...
✅ Work block #1135 logged to diary.md

[2026-02-03T17:36:00Z] ### Work Block #1136 — 2026-02-03T17:36:00Z
**Task:** Document batch-executor.py
...
✅ Work block #1136 logged to diary.md

✅ Batch complete: 2 tasks executed
```

---

## Data Structure

Tasks stored in `batch-tasks.json`:

```json
[
  {
    "task": "Document batch-executor.py",
    "result": "Created README (4753 bytes)",
    "insight": "Batch execution = velocity multiplier",
    "next_step": "Continue documentation sprint",
    "status": "pending",
    "added": "2026-02-03T17:30:00Z",
    "completed": "2026-02-03T17:35:00Z"
  }
]
```

**Status values:** `pending` → `complete` → removed from queue

---

## Integration Patterns

### Pattern 1: Offline Planning

```bash
# Queue up 10 tasks while thinking
python tools/batch-executor.py add "Task 1"
python tools/batch-executor.py add "Task 2"
# ... queue up 10 tasks

# Execute batch later (unattended)
python tools/batch-executor.py 10
```

**Use case:** Plan work blocks during commute/deep think, execute batch during high-focus time.

### Pattern 2: Python Integration

```python
from tools.batch_executor import add_task, execute_batch

# Queue tasks programmatically
add_task(
    task="Update pipeline stats",
    result="Added 3 new opportunities ($60K)",
    insight="Pattern reuse = 5x velocity",
    next_step="Send outreach messages"
)

# Execute batch
executed = execute_batch(limit=5)
print(f"Executed {executed} tasks")
```

### Pattern 3: Cron Integration

```python
# In your heartbeat handler
from tools.batch_executor import execute_batch

# Execute 2 tasks every heartbeat
executed = execute_batch(limit=2)
print(f"Batch: {executed} tasks executed")
```

### Pattern 4: Task Generator Integration

```python
# Queue tasks from work-block-generator.py
from tools.work_block_generator import generate_task
from tools.batch_executor import add_task

# Generate and queue 10 tasks
for _ in range(10):
    task = generate_task()
    add_task(task['task'], task['result'], task['insight'])
```

---

## Why This Matters

**Problem:** Work blocks require online presence. Can't queue up offline work.

**Solution:** `batch-executor.py` decouples planning from execution:
- Plan offline: Queue 20 tasks in 5 minutes
- Execute online: Run batch unattended
- Result: 20 work blocks completed without manual intervention

**Impact:** Offline thinking × online execution = velocity multiplier.

---

## Real-World Usage

Nova uses this for:
1. **Deep think sessions** — Queue 10-20 tasks after reflection
2. **Batch execution** — Run unattended during high-velocity periods
3. **Queue visibility** — `list` command shows pending work

**Result:** 50+ work blocks queued and executed per deep think session.

---

## Customization Examples

### Add Priority Levels

```python
# Extend task structure
def add_task(task, result="", insight="", next_step="", priority="medium"):
    tasks = load_tasks()
    tasks.append({
        'task': task,
        'priority': priority,  # high, medium, low
        'status': 'pending',
        'added': datetime.utcnow().isoformat()
    })
    # Sort by priority
    tasks.sort(key=lambda x: {'high': 0, 'medium': 1, 'low': 2}[x['priority']])
    save_tasks(tasks)
```

### Add Dependencies

```python
# Only execute if dependencies met
def execute_batch(limit=5):
    tasks = load_tasks()
    executed = 0
    for task in tasks[:limit]:
        if task['status'] == 'pending':
            # Check dependencies
            if all(d['status'] == 'complete' for d in task.get('depends_on', [])):
                # Execute task
                ...
```

### Add Retry Logic

```python
# Retry failed tasks
def execute_batch(limit=5, retries=2):
    for task in tasks[:limit]:
        attempts = task.get('attempts', 0)
        if attempts < retries:
            # Try execution
            ...
            if failed:
                task['attempts'] = attempts + 1
                task['status'] = 'pending'  # Keep in queue
```

---

## Files Created/Modified

- `batch-tasks.json` — Task queue storage
- `diary.md` — Work block logs (via `work-block-logger.py`)

---

## Error Handling

```bash
# Empty queue
$ python tools/batch-executor.py
✨ No pending tasks in batch queue

# Task execution failed
❌ Failed to execute: Missing file
```

---

## See Also

- **`work-block-logger.py`** — Individual work block logging
- **`work-block-generator.py`** — Auto-generate work block tasks
- **`task-randomizer.py`** — Random task selection from pools

---

## Version History

- **v1.0** — Initial release

---

*Queue once. Execute many.*
