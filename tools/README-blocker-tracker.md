# blocker-tracker.py

Track and manage blockers that prevent autonomous execution.

## What It Does

Monitors blocked tasks, categorizes by priority, and surfaces them for resolution. Helps maintain momentum by identifying exactly what needs unblocking.

## Installation

No dependencies required. Uses Python standard library only.

## Quick Start

```bash
python3 tools/blocker-tracker.py
```

## Usage Examples

### Check current blockers
```bash
python3 tools/blocker-tracker.py
```

**Output:**
```
==================================================
🔒 NOVA BLOCKER TRACKER
==================================================
Last updated: 2026-02-02T23:47:56

🔴 HIGH PRIORITY
🔴 **Push 156-file portfolio to GitHub**
   Blocked: GitHub personal access token
   Since: 2026-02-01 | Action: Arthur to generate token with repo scope

🟡 MEDIUM PRIORITY
🟡 **Automated Moltbook posting/engagement**
   Blocked: Moltbook API token for automation
   Since: 2026-02-01 | Action: Request token from Moltbook team

==================================================
Total: 3 blockers | 2 high priority
```

### Log blockers to diary
```bash
python3 tools/blocker-tracker.py --log
```

Appends blocker status to diary.md for tracking over time.

## Data Structure

Blockers are stored in `status/blockers.json`:

```json
{
  "last_updated": "2026-02-02T23:47:56",
  "blockers": [
    {
      "id": "github-token",
      "task": "Push 156-file portfolio to GitHub",
      "blocker": "GitHub personal access token",
      "impact": "high",
      "since": "2026-02-01",
      "action_needed": "Arthur to generate token with repo scope"
    }
  ]
}
```

### Blocker Fields

- **id** — Unique identifier for the blocker
- **task** — What you're trying to do
- **blocker** — What's blocking it
- **impact** — Priority level (high/medium/low)
- **since** — When the blocker was identified
- **action_needed** — Specific action to resolve

## Priority Levels

- 🔴 **High** — Blocks revenue-generating work or critical goals
- 🟡 **Medium** — Blocks optimization or nice-to-haves
- 🟢 **Low** — Minor inconveniences

## Best Practices

### Keep blockers updated
- Resolve blockers as soon as possible
- Archive resolved blockers (don't delete, just mark resolved)
- Update `since` dates for persistent blockers

### Use blocker data for prioritization
When blocked on one task, check if another unblocked task has higher ROI.

Example:
```
Blocker: GitHub auth (unblocks $130K grants, 8 min to resolve)
Blocker: Browser access (unblocks $50K bounties, gateway restart needed)

→ Prioritize GitHub auth (higher value, faster resolution)
```

### Log blocker checks regularly
Run `--log` during heartbeats to track how long blockers have been active:
```bash
python3 tools/blocker-tracker.py --log
```

## Integration

### Heartbeat example (HEARTBEAT.md)
```yaml
- name: "Blocker Check"
  every: "1h"
  message: |
    Check blockers and log status.
    python3 tools/blocker-tracker.py --log
    If 3+ high-priority blockers, alert Arthur.
```

### Combined with revenue-tracker.py
```bash
# Show blockers + revenue impact
python3 tools/blocker-tracker.py
python3 tools/revenue-tracker.py summary
```

## Return Codes

- `0` — Success
- `1` — Error reading/writing files

## Files

- `status/blockers.json` — Blocker data (auto-created)
- `diary.md` — Log entries (when using `--log`)

## See Also

- `revenue-tracker.py` — Track revenue pipeline and submission blockers
- `today.md` — Current working memory with blockers section
- `tools/README-blocker-tracker.md` — This file
