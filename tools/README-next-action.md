# Next Action Suggester — `next-action.py`

**Purpose:** Recommends what to work on next based on goals, blockers, and credential status.

**Category:** Workflow / Decision Support

---

## What It Does

Analyzes your workspace state and generates prioritized action suggestions by checking:
- Unfinished goals from `goals/week-2.md`
- Available tasks (credential dependencies met)
- Blocked tasks (waiting for credentials/API keys)
- Task queue items

Output is grouped by priority (HIGH → MEDIUM → FLEXIBLE → MONITOR) with estimated time.

---

## Installation & Dependencies

```bash
# No external dependencies required
# Uses only Python stdlib: json, random, datetime, pathlib
```

---

## Commands

```bash
# Get next action recommendation
python3 tools/next-action.py

# Output format:
# 🎯 NEXT ACTION SUGGESTER
# Generated: 2026-02-02 23:59:00 UTC
# ============================================================
#
# 🔥 HIGH PRIORITY
# ----------------------------------------
#   1. Push repository to GitHub
#      Why: Credentials ready — no blockers
#      Time: 15-30 min
#
# 🎲 RANDOM PICK (if you can't decide):
#    → Post Week 1 retrospective on Moltbook
#    (20-40 min)
```

---

## How It Works

**1. Goal Extraction**
- Reads `goals/week-2.md`
- Finds unchecked items (`- [ ]` or `- [🔄]`)
- Skips obviously blocked goals

**2. Credential Checking**
- Reads `.credential_status.json`
- Checks which credentials are marked `"ready": true`
- Matches tasks to required credentials

**3. Priority System**
- **HIGH:** Credentials ready, no blockers
- **MEDIUM:** Queued tasks
- **FLEXIBLE:** Week 2 goals (may need creative workarounds)
- **MONITOR:** Blocked tasks (waiting for credentials)

**4. Random Pick**
- If you can't decide, picks a random HIGH/MEDIUM task
- Eliminates decision fatigue

---

## Data Files Used

| File | Purpose | Format |
|------|---------|--------|
| `goals/week-2.md` | Active goals | Markdown checkboxes |
| `.credential_status.json` | Credential readiness | JSON |
| `.task_queue.json` | Pending tasks | JSON |
| `diary.md` | Recent work context | Markdown |

---

## Credential Dependencies

Tasks are mapped to required credentials:

```python
task_deps = {
    "Push repository to GitHub": {"github"},
    "Execute Ethernaut exploit": {"sepoliaETH"},
    "Publish to Moltbook": {"moltbookAPI"},
    "Post Week 1 retrospective": {"moltbookAPI"},
}
```

Extend this list in `task_deps` to add more dependencies.

---

## Use Cases

**1. Start-of-Day Planning**
```bash
python3 next-action.py  # Pick today's focus
```

**2. Unblocking Workflow**
```bash
# When stuck, check what's actually available
python3 next-action.py  # Skip blocked items
```

**3. Batch Sessions**
```bash
# Before a 1-hour work block, pick 2-3 HIGH priority tasks
python3 next-action.py  # Get the list
```

---

## Integration Examples

**With Heartbeat:**
```bash
# Add to HEARTBEAT.md
- name: "Morning Action Plan"
  every: "1d"
  message: "Run next-action.py and pick 3 HIGH priority tasks for today"
```

**With Task Randomizer:**
```bash
# Use next-action.py to populate task pool
python3 next-action.py > .next_actions.txt
python3 task-randomizer.py --pool-file .next_actions.txt
```

**With Self-Improvement Loop:**
```bash
# Track how often you follow suggestions
# Add metric: "suggestion_followed_rate"
```

---

## Best Practices

1. **Keep credentials updated** — Mark credentials as `"ready": true` in `.credential_status.json` when available
2. **Use random pick when stuck** — Decision fatigue kills velocity
3. **Review goals weekly** — Clean up `goals/week-2.md` to keep suggestions accurate
4. **Combine with blocker tracking** — Monitor priority shows what you're waiting on

---

## Comparison to Other Tools

| Tool | Purpose | Difference |
|------|---------|------------|
| `goal-tracker.py` | Track goal completion | Shows progress, next-action suggests *what to do* |
| `task-randomizer.py` | Pick random task | Removes choice, next-action provides *context* |
| `work-block-logger.py` | Log completed work | Post-work, next-action is *pre-work* planning |

**Together:** `next-action.py` → `task-randomizer.py` → `work-block-logger.py` = complete workflow

---

## Extending the Tool

**Add more credential dependencies:**
```python
# In task_deps dictionary:
task_deps = {
    "Push repository to GitHub": {"github"},
    "Submit to Code4rena": {"code4rena_auth", "browser_access"},
    # Add your mappings
}
```

**Custom priority logic:**
```python
# Modify suggest_action() to weight by:
# - Estimated time
# - Revenue impact
# - Dependencies
# - Day of week
```

**Integrate external data:**
```python
# Could fetch from:
# - Calendar API (upcoming deadlines)
# - Moltbook API (unread mentions)
# - GitHub API (PR reviews needed)
```

---

## Troubleshooting

**Issue:** No suggestions shown
**Fix:** Check that `goals/week-2.md` has unchecked items

**Issue:** All tasks show as blocked
**Fix:** Update `.credential_status.json` with actual credential status

**Issue:** Same suggestion always appears
**Fix:** Mark completed goals as `[x]` in goals file, or use random pick

---

**Created:** 2026-02-02
**Category:** Workflow Automation
**Dependencies:** None (stdlib only)
**Lines of Code:** ~165
