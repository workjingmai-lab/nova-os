# task-queue.py

Simple FIFO task queue for work blocks — designed for cron-driven execution and autonomous sessions.

## What It Does

Manages a queue of small tasks with priorities, tracking pending/in-progress/completed states. Perfect for:
- Cron-triggered work sessions ("give me the next task")
- Autonomous execution without user prompts
- Tracking completion history and metrics

## Installation

No dependencies required. Uses Python standard library only.

## Quick Start

### Add a task
```bash
python3 tools/task-queue.py add "Update revenue pipeline" --priority high
python3 tools/task-queue.py add "Write tool README" --priority normal
python3 tools/task-queue.py add "Organize workspace" --priority low
```

### Get next task (for cron)
```bash
python3 tools/task-queue.py next
# Output:
# 🎯 WORK BLOCK TASK:
#    Update revenue pipeline
#
#    When done, run: python3 task-queue.py complete 'result summary'
```

### Complete current task
```bash
python3 tools/task-queue.py complete "Updated pipeline.json, added blocker ROI"
```

### Check status
```bash
python3 tools/task-queue.py status
```

**Output:**
```
📋 Task Queue Status
========================================
🔄 IN PROGRESS: Update revenue pipeline

⏳ Pending: 2
   🟡 Write tool README
   🟢 Organize workspace

✅ Completed today: 5
📊 Total completed: 127
```

## Commands

### add
Add a new task to the queue.
```bash
python3 tools/task-queue.py add "description" [--priority high|normal|low] [--source cron|manual]
```

**Options:**
- `--priority`: Task priority (default: normal). High-priority tasks execute first.
- `--source`: Task source (default: manual). Useful for tracking where tasks came from.

**Example:**
```bash
python3 tools/task-queue.py add "Submit Gitcoin grant" --priority high --source manual
# ✅ Added: Submit Gitcoin grant
```

### next
Get the next task from queue and mark as in-progress.
```bash
python3 tools/task-queue.py next
```

**Behavior:**
- Sorts pending tasks by priority (high → normal → low)
- Moves first task to "in_progress" state
- Returns task details for execution

### complete
Mark the current in-progress task as complete.
```bash
python3 tools/task-queue.py complete ["result summary"]
```

**Example:**
```bash
python3 tools/task-queue.py complete "Grant submitted, awaiting confirmation"
# ✅ Completed: Submit Gitcoin grant
```

### skip
Skip the current task and return it to the pending queue.
```bash
python3 tools/task-queue.py skip
```

**Use case:** Task is blocked or not ready — re-queue for later.

### status
Show current queue status and metrics.
```bash
python3 tools/task-queue.py status
```

### list
List all pending tasks.
```bash
python3 tools/task-queue.py list
```

### work-block
Convenience command for cron sessions — gets next task with minimal output.
```bash
python3 tools/task-queue.py work-block
```

**Output:**
```
🎯 WORK BLOCK TASK:
   Update revenue pipeline

   When done, run: python3 tools/task-queue.py complete 'result summary'
```

## Data Files

- `.task_queue.json` — Current queue state (pending/in-progress/completed)
- `.task_history.json` — Completion history (last 100 tasks)

**Queue structure:**
```json
{
  "pending": [
    {
      "id": "task_20260203_030400_0",
      "description": "Update revenue pipeline",
      "priority": "high",
      "source": "manual",
      "added_at": "2026-02-03T03:04:00Z"
    }
  ],
  "in_progress": null,
  "completed": [...]
}
```

## Use Cases

### 1. Cron-Driven Work Sessions
Add tasks in advance, let cron pull the next one automatically:
```yaml
# HEARTBEAT.md
- name: "Work Block"
  every: "1m"
  message: |
    python3 tools/task-queue.py work-block
    # Execute task, then:
    python3 tools/task-queue.py complete "Done"
```

### 2. Priority-Based Execution
Add high-priority tasks (grant submissions, blockers) that execute first:
```bash
python3 tools/task-queue.py add "Submit Gitcoin grant" --priority high
python3 tools/task-queue.py add "Write README" --priority normal
python3 tools/task-queue.py add "Organize files" --priority low
```

### 3. Tracking Completion Metrics
View how many tasks completed today vs. total:
```bash
python3 tools/task-queue.py status
# ✅ Completed today: 47
# 📊 Total completed: 892
```

### 4. Skipping Blocked Tasks
If a task is blocked (browser down, API timeout), skip and re-queue:
```bash
python3 tools/task-queue.py skip
# ⏭️ Skipped: Check Code4rena bounties
```

## Return Codes

- `0` — Success
- `1` — Error (no task in progress, queue empty)

## Examples

### Batch Add Tasks
```bash
python3 tools/task-queue.py add "Update revenue pipeline" --priority high
python3 tools/task-queue.py add "Create tool README" --priority normal
python3 tools/task-queue.py add "Post to Moltbook" --priority normal
python3 tools/task-queue.py add "Organize workspace" --priority low
```

### Work Block Session
```bash
# Cron triggers every minute
$ python3 tools/task-queue.py next
🎯 WORK BLOCK TASK:
   Update revenue pipeline

   When done, run: python3 tools/task-queue.py complete 'result summary'

# ... execute task ...

$ python3 tools/task-queue.py complete "Updated $302K pipeline, blocker ROI calculated"
✅ Completed: Update revenue pipeline
```

### Check Progress
```bash
$ python3 tools/task-queue.py status
📋 Task Queue Status
========================================

⏳ Pending: 3
   🔴 Write tool README
   🟡 Post to Moltbook
   🟢 Organize workspace

✅ Completed today: 12
📊 Total completed: 156
```

## Integration

### With goal-tracker.py
```bash
# Add weekly goals as tasks
python3 tools/task-queue.py add "Complete 5 grant submissions" --priority high --source goal-tracker
python3 tools/task-queue.py add "Send 15 service messages" --priority high --source goal-tracker
```

### With moltbook-suite.py
```bash
# Queue content creation
python3 tools/task-queue.py add "Post achievement to Moltbook" --priority normal --source moltbook
python3 tools/task-queue.py add "Engage with 3 agents" --priority normal --source moltbook
```

### With revenue-tracker.py
```bash
# Queue revenue tasks
python3 tools/task-queue.py add "Submit Gitcoin grant ($5K)" --priority high --source revenue
python3 tools/task-queue.py add "Submit Octant grant ($15K)" --priority high --source revenue
```

## Design Philosophy

**Simple FIFO with priority sorting.**

No complex dependencies, no scheduling, no recurring tasks. Just:
1. Add tasks
2. Pull next task (sorted by priority)
3. Complete or skip
4. Track history

This simplicity makes it perfect for:
- Cron-driven autonomous sessions
- Quick decision-free task execution
- High-volume work block tracking

## See Also

- `task-randomizer.py` — Random task selection (eliminates decision fatigue)
- `goal-tracker.py` — Long-term goal tracking
- `diary-digest.py` — Analyze completion patterns
- `quick-wins.md` — 30+ 1-minute task ideas
