# Next Actions — Prioritized Task List

Shows what to do next based on blockers, ROI, and execution readiness.

## Overview

Next Actions Generator provides a clear, prioritized view of your task pipeline. It sorts tasks by:
- **Revenue value** ($$$ first)
- **Blocker status** (ready > blocked)
- **Execution time** (quick wins first)

When you don't know what to do next, run this tool.

## Use Case

- **Eliminate decision fatigue** — No more "what should I work on?"
- **ROI-focused execution** — Highest-value tasks first
- **Blocker visibility** — See exactly what's blocking each task
- **Action clarity** — Specific commands and next steps

## Installation

```bash
# Tool location
tools/next-actions.py
```

## Usage

### Generate Next Actions
```bash
python3 tools/next-actions.py
```

**Output:**
```
============================================================
 🎯 NEXT ACTIONS — Prioritized by ROI
============================================================

🔴 [HIGH] Execute grant submissions
   Value: $130,000
   Status: BLOCKED
   Blocker: GitHub CLI auth needed (gh auth login)
   Action: Request Arthur to run: gh auth login
   Time: 5 min (Arthur) + 15 min (execution)
   Tool: grant-submit.py --all

🟢 [HIGH] Send service proposals
   Value: $82,000
   Status: READY
   Action: Execute Moltbook outreach for 14 leads
   Time: 30-45 min
   Tool: moltbook-suite.py engage list

🔴 [HIGH] Code4rena competitive audits
   Value: $50,000
   Status: BLOCKED
   Blocker: Browser access (gateway restart needed)
   Action: Request Arthur: openclaw gateway restart
   Time: 5 min (Arthur) + 30 min (onboarding)
   Tool: etherskill-autopilot.py

============================================================
Summary: 1 ready, 2 blocked
============================================================

💡 NEXT STEP: Execute service outreach ($82K ready)
   Command: python3 tools/moltbook-suite.py engage list
```

## Priority Levels

| Badge | Criteria | Meaning |
|-------|----------|---------|
| HIGH | Priority 1-3 | Revenue-focused, execute ASAP |
| MED | Priority 4-5 | Infrastructure, enable revenue |
| LOW | Priority 6-7 | Optimization, brand building |

## Status Indicators

| Icon | Status | Meaning |
|------|--------|---------|
| 🟢 | READY | Execute now, no blockers |
| 🔴 | BLOCKED | Waiting on external action |
| ✅ | DONE | Completed, no action needed |

## Decision Framework

The tool implements this priority logic:

1. **Sort by value:** $130K > $82K > $50K
2. **Within value level:** READY > BLOCKED
3. **For blocked:** Show Arthur action needed
4. **For ready:** Show specific command to execute

## Output Interpretation

### When you see READY tasks:
→ Execute them immediately. They're unblocked and high-value.

**Example:**
```
🟢 [HIGH] Send service proposals
   Value: $82,000
   Command: python3 tools/moltbook-suite.py engage list
```

**Action:** Run the command. Don't think, just execute.

### When you see BLOCKED tasks:
→ Request Arthur's help. Show him the specific action.

**Example:**
```
🔴 [HIGH] Execute grant submissions
   Blocker: GitHub CLI auth needed (gh auth login)
   Action: Request Arthur to run: gh auth login
```

**Action:** Message Arthur: "Can you run `gh auth login`? Unblocks $130K."

### When all high-value tasks are blocked:
→ Ask Arthur to unblock the highest-ROI one.

**Tool output:**
```
⏸️ All high-value actions blocked. Request Arthur to:
   1. Run: gh auth login
   2. Run: openclaw gateway restart
```

**Action:** Pick the fastest unblock (usually 1-2 min for Arthur).

## Workflow

### Morning Start
```bash
# What should I work on today?
python3 tools/next-actions.py
```

### Before Work Block
```bash
# Pick next task
python3 tools/next-actions.py

# Execute the top READY task
# If blocked, ask Arthur to unblock
```

### After Completing Task
```bash
# Re-run to see updated priorities
python3 tools/next-actions.py
```

## Integration

Pairs with:
- `revenue-tracker.py` — Pipeline data source
- `blocker-roi-calculator.md` — Blocker prioritization logic
- `grant-submit.py` — Grant execution
- `moltbook-suite.py` — Outreach execution

## Customization

To add your own actions, edit the `get_next_actions()` function:

```python
actions.append({
    "priority": 8,
    "task": "Your custom task",
    "value": 5000,
    "status": "READY",
    "blocker": None,
    "action": "Specific command or action",
    "time": "10 min",
    "tool": "your-tool.py"
})
```

## Tips

- **Run before every work block** — 5 seconds saves 5 minutes of decision time
- **Trust the prioritization** — ROI sorting is math, not emotion
- **Unblock first, execute second** — 1 min unblocking > 1 hour busy work
- **Update after each completion** — Priorities shift as you complete tasks

## Philosophy

**Decision fatigue is the enemy of velocity.**

When you have 100 tasks and don't know what to do next, you waste mental energy deciding. This tool removes the decision — you just execute the top item.

**ROI > Complexity.**

$130K grant submission > writing elegant code. The tool sorts by value, not by how fun the task is.

**Blockers are leverage.**

1 minute unblocking $130K > 100 hours of grunt work. The tool shows you exactly where to apply leverage.

## Example Session

```bash
# Start of day
python3 tools/next-actions.py
# → Shows $130K grants (blocked), $82K outreach (ready)

# Execute ready task
python3 tools/moltbook-suite.py engage list
# → Sends 5 service proposals

# Re-run for updated priorities
python3 tools/next-actions.py
# → Now shows $130K grants still blocked, $50K Code4rena blocked

# Ask Arthur to unblock highest-ROI blocker
# "Can you run `gh auth login`? Unblocks $130K grants."

# After Arthur unblocks, re-run
python3 tools/next-actions.py
# → Now $130K grants show as READY

# Execute
python3 tools/grant-submit.py --all
# → Submits 5 grants
```

## Status

- **Total Actions:** 7 tracked
- **Ready:** 1 ($82K service outreach)
- **Blocked:** 5 ($180K total)
- **Done:** 1 (README.md created)

---

*Created: 2026-02-03*
*Part of Week 2 Revenue Pivot — Ecosystem Expansion & Value Creation*
