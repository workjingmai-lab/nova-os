# blocker-tracker.py

Monitor and manage execution blockers.

## Overview

Tracks what's blocking execution and surfaces them for resolution. Prevents silent stagnation by making blockers visible and actionable.

## Features

- **Blocker registry:** JSON-based storage in `status/blockers.json`
- **Priority classification:** High (🔴), Medium (🟡), Low (🟢)
- **Action clarity:** Each blocker has explicit action needed
- **Diary logging:** Optional log to diary.md for tracking
- **Time tracking:** "Since" field shows blocker age

## Usage

### Check Current Blockers

```bash
python tools/blocker-tracker.py
```

Output:
```
==================================================
🔒 NOVA BLOCKER TRACKER
==================================================
Last updated: 2026-02-03 16:50

🔴 HIGH PRIORITY
🔴 **GitHub CLI auth for grant submissions**
   Blocked: gh CLI not authenticated
   Since: 2026-02-01 | Action: Arthur runs `gh auth login`

🟡 MEDIUM PRIORITY
🟡 **Browser access for Code4rena**
   Blocked: Gateway browser control service not responding
   Since: 2026-02-01 | Action: Arthur runs `openclaw gateway restart`

==================================================
Total: 2 blockers | 1 high priority

💡 Run with --log to append to diary.md
```

### Log to Diary

```bash
python tools/blocker-tracker.py --log
```

Appends blocker check to diary.md for historical tracking.

## Blocker Structure

Each blocker in `status/blockers.json`:

```json
{
  "id": "github-auth",
  "task": "GitHub CLI auth for grant submissions",
  "blocker": "gh CLI not authenticated",
  "impact": "high",
  "since": "2026-02-01",
  "action_needed": "Arthur runs `gh auth login`"
}
```

### Fields

| Field | Description | Example |
|-------|-------------|---------|
| `id` | Unique identifier | `github-auth` |
| `task` | What's blocked | "Grant submissions" |
| `blocker` | What's blocking | "gh CLI not authenticated" |
| `impact` | Priority level | `high`, `medium`, `low` |
| `since` | When blocker started | `2026-02-01` |
| `action_needed` | Clear next step | "Arthur runs `gh auth login`" |

## Managing Blockers

### Add New Blocker

Edit `status/blockers.json`:

```json
{
  "blockers": [
    {
      "id": "new-blocker",
      "task": "Task being blocked",
      "blocker": "What's blocking it",
      "impact": "high",
      "since": "2026-02-03",
      "action_needed": "Specific action to resolve"
    }
  ]
}
```

### Resolve Blocker

Remove from `status/blockers.json`:

```bash
# Manually edit status/blockers.json and delete resolved entry
```

Or use script (if added):

```python
# blocker-tracker.py --resolve github-auth
```

## Priority Classification

**🔴 High Impact:**
- Blocks revenue ($1000+ value at stake)
- Prevents critical execution (can't work at all)
- Time-sensitive (opportunity window closing)

**🟡 Medium Impact:**
- Slows velocity but doesn't block
- Affects secondary objectives
- Can work around with effort

**🟢 Low Impact:**
- Nice-to-have improvements
- Optimization opportunities
- No immediate urgency

## Integration

### Heartbeat Checks

Add to HEARTBEAT.md:

```markdown
- Check blockers: `python tools/blocker-tracker.py`
- If high blockers > 2: Alert Arthur
```

### Cron Job

Daily blocker review:

```json
{
  "name": "Daily Blocker Review",
  "schedule": {
    "kind": "cron",
    "expr": "0 9 * * *",
    "tz": "UTC"
  },
  "payload": {
    "kind": "systemEvent",
    "text": "Run blocker-tracker.py --log and review high-priority blockers"
  }
}
```

### With blocker-roi-calculator.py

Calculate ROI for resolving blockers:

```bash
# See which blockers to prioritize
python tools/blocker-roi-calculator.py

# Then check current status
python tools/blocker-tracker.py
```

## Best Practices

1. **Be specific:** "Browser access" > "Can't do stuff"
2. **One action per blocker:** Don't combine multiple blockers
3. **Clear ownership:** Who needs to act? (Arthur, Nova, external)
4. **Age matters:** Old blockers need escalation
5. **Resolve or archive:** Don't let list grow indefinitely

## Example Workflow

1. **Detect blocker:** Try to submit grant → "gh: not logged in"
2. **Add to tracker:** Edit `status/blockers.json` with entry
3. **Calculate ROI:** `python tools/blocker-roi-calculator.py` → $26K/min
4. **Prioritize:** High ROI = high priority
5. **Surface to Arthur:** Add to today.md blockers section
6. **Resolve:** Arthur runs `gh auth login`
7. **Remove from tracker:** Delete entry from JSON

## Anti-Patterns

❌ **Vague blockers:** "Can't work" → "GitHub CLI auth needed"
❌ **Combined blockers:** "GitHub + Browser blocked" → Two separate entries
❌ **No action:** "Blocked" → "Blocked: Arthur runs `gh auth login`"
❌ **Stale data:** Blockers from January in March → Review and archive

## Version

- **v1.0** (2026-02-01): Initial release

## See Also

- `blocker-roi-calculator.py` — Calculate priority by value/time
- `today.md` — Current blockers section (synced with tracker)
- `next-actions.py` — Unblockable tasks to work on while blocked
