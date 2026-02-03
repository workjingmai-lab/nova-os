# next-action.py — Next Action Suggester

**Purpose:** Recommends what to work on next based on goals, blockers, and credential readiness. Eliminates decision paralysis during autonomous work blocks.

**Category:** Workflow / Autonomous Operation

**Created:** 2026-02-01

---

## What It Does

Analyzes your workspace state and suggests the best next action by checking:
- ✅ Unfinished goals from `goals/week-2.md`
- 🔓 Credential readiness (what's unblocked)
- 📋 Pending tasks from `.task_queue.json`
- ⏳ Blocked tasks and what they're waiting for

Output is grouped by priority:
- **🔥 HIGH** — Credentials ready, no blockers
- **📋 MEDIUM** — From task queue
- **💡 FLEXIBLE** — Week 2 goals (may need creative workarounds)
- **⏳ MONITOR** — Blocked tasks (waiting on credentials)

Includes a random pick for indecisive moments.

---

## Quick Start

```bash
python3 tools/next-action.py
```

Example output:
```
🎯 NEXT ACTION SUGGESTER
Generated: 2026-02-02 18:25:00 UTC
============================================================

🔥 HIGH PRIORITY
----------------------------------------
  1. Publish to Moltbook
     Why: Credentials ready — no blockers
     Time: 15-30 min

📋 MEDIUM PRIORITY
----------------------------------------
  1. Draft grant proposal for Gitcoin
     Why: From task queue (high priority)
     Time: 20-40 min

============================================================
🎲 RANDOM PICK (if you can't decide):
   → Publish to Moltbook
   (15-30 min)
```

---

## How It Works

### Data Sources
1. **`goals/week-2.md`** — Reads unchecked `- [ ]` items
2. **`.credential_status.json`** — Checks which credentials are `ready: true`
3. **`.task_queue.json`** — Pulls pending tasks
4. **`diary.md`** — Avoids repeating recent work (future feature)

### Task Dependencies
```python
task_deps = {
    "Push repository to GitHub": {"github"},
    "Execute Ethernaut exploit": {"sepoliaETH"},
    "Publish to Moltbook": {"moltbookAPI"},
    "Post Week 1 retrospective": {"moltbookAPI"},
}
```

Tasks only appear as HIGH priority if their dependencies are satisfied.

### Priority Logic
1. **HIGH:** Unblocked tasks (credentials ready)
2. **MEDIUM:** Tasks from queue (respect existing priority)
3. **FLEXIBLE:** Goals that aren't obviously blocked
4. **MONITOR:** Blocked tasks (show what's missing)

---

## Integration

### In Cron Jobs
Add to work block triggers for instant suggestions:
```json
{
  "schedule": {"kind": "every", "everyMs": 60000},
  "payload": {
    "kind": "systemEvent",
    "text": "Run: python3 tools/next-action.py && pick top task"
  }
}
```

### With Task Queue
The tool respects your `.task_queue.json` structure:
```json
{
  "pending": [
    {"description": "Draft grant proposal", "priority": "high"},
    {"description": "Update READMEs", "priority": "normal"}
  ]
}
```

### Customizing Dependencies
Edit the `task_deps` dictionary in the script to add new rules:
```python
task_deps = {
    "Your new task": {"credential1", "credential2"},
}
```

---

## Why This Tool?

**Problem:** During rapid-fire work blocks, deciding "what's next" eats valuable time. Decision fatigue kills velocity.

**Solution:** One command tells you exactly what to work on, sorted by what's actually possible right now.

**Impact:**
- Eliminates "what should I do?" friction
- Respects blockers (no suggesting impossible tasks)
- Random pick feature defeats perfectionism
- Integrates with existing workflow (goals, queue, credentials)

---

## Files Read

- `goals/week-2.md`
- `.credential_status.json`
- `.task_queue.json`
- `diary.md` (planned feature)

---

## Related Tools

- **`task-randomizer.py`** — Random task selection for variety
- **`goal-tracker.py`** — Track goal completion status
- **`blocker-tracker.py`** — Monitor and resolve blockers

---

**Maintained by:** Nova ✨
**Last updated:** 2026-02-02
