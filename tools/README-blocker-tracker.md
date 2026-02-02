# blocker-tracker.py

Monitor and track blocked tasks that require external resolution.

## Overview

`blocker-tracker.py` helps Nova identify and manage tasks that can't proceed without external action (Arthur's intervention, API tokens, resources, etc.). It maintains a persistent list of blockers with impact levels and required actions.

**Use case:** When autonomous execution hits a hard blocker (GitHub auth, API tokens, infrastructure access), this tool ensures nothing gets forgotten and surfaces what needs attention.

---

## Features

- **Persistent blocker storage** — JSON file tracks all active blockers
- **Impact levels** — High/medium/low priority classification
- **Action tracking** — What's needed to resolve each blocker
- **Diary logging** — Append blocker status to diary.md with `--log`
- **Timestamp tracking** — When each blocker was identified
- **Auto-initialization** — Default blockers loaded on first run

---

## Installation

```bash
# Already in tools/ directory
cd /home/node/.openclaw/workspace/tools
chmod +x blocker-tracker.py
```

---

## Quick Start

```bash
# Check current blockers
python3 blocker-tracker.py

# Log blocker status to diary.md
python3 blocker-tracker.py --log
```

---

## Usage Examples

### View all blockers
```bash
python3 blocker-tracker.py
```

Output:
```
==================================================
🔒 NOVA BLOCKER TRACKER
==================================================
Last updated: 2026-02-02 11:00

🔴 HIGH PRIORITY
🔴 **Push 156-file portfolio to GitHub**
   Blocked: GitHub personal access token
   Since: 2026-02-01 | Action: Arthur to generate token with repo scope

🟡 MEDIUM PRIORITY
🟡 **Automated Moltbook posting/engagement**
   Blocked: Moltbook API token for automation
   Since: 2026-02-01 | Action: Request token from Moltbook team

==================================================
Total: 2 blockers | 1 high priority
```

### Log blocker status to diary
```bash
python3 blocker-tracker.py --log
```

Adds a timestamped entry to `diary.md` with current blocker count and summary.

---

## Data Structure

Blockers are stored in `status/blockers.json`:

```json
{
  "last_updated": "2026-02-02T11:00:00Z",
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

### Blocker fields

- **id** — Unique identifier (kebab-case)
- **task** — What task is blocked
- **blocker** — What's preventing execution
- **impact** — Priority level: "high", "medium", "low"
- **since** — When blocker was identified (YYYY-MM-DD)
- **action_needed** — Specific resolution steps

---

## Best Practices

### 1. Document blockers immediately
When you hit a hard blocker, add it to blockers.json right away:
```bash
python3 blocker-tracker.py --log
```

### 2. Categorize by impact
- **High** — Blocks $1K+ pipeline or critical execution (GitHub auth, browser access)
- **Medium** — Blocks value-add features but not critical path (API tokens, optional integrations)
- **Low** — Nice-to-haves, optimizations

### 3. Include specific action steps
Don't just say "auth needed" — say "Arthur to run `gh auth login`". Specificity unblocks faster.

### 4. Review blockers weekly
Run blocker-tracker during weekly review to:
- Remove resolved blockers
- Escalate long-standing high-priority items
- Update action steps if context changed

---

## Integration Ideas

### Cron job blocker checks
Add to HEARTBEAT.md for periodic blocker review:
```yaml
- name: "Blocker Review"
  every: "4h"
  message: |
    Run python3 blocker-tracker.py
    If high-priority blockers exist >24h, escalate to Arthur
```

### Auto-resolve with conditionals
Extend blocker-tracker to auto-check resolution:
```python
def check_resolution(blocker):
    if blocker["id"] == "github-token":
        result = run_command("gh auth status")
        if "Logged in" in result:
            return "RESOLVED"
    return "STILL_BLOCKED"
```

### Dashboard integration
Use blocker data in a status dashboard:
```python
blockers = load_blockers()
high_count = sum(1 for b in blockers["blockers"] if b["impact"] == "high")
print(f"🔴 {high_count} blockers")
```

---

## Troubleshooting

### Blockers not loading
- Check `status/blockers.json` exists and is valid JSON
- Verify file permissions (readable)

### New blockers not showing
- Ensure JSON structure is correct (comma-separated, valid syntax)
- Run `python3 blocker-tracker.py` to load and validate

### Diary logging fails
- Check `diary.md` is writable
- Verify working directory is `/home/node/.openclaw/workspace`

---

## Related Tools

- **self-improvement-loop.py** — Analyzes execution velocity and recommends blocker resolution
- **task-randomizer.py** — Picks unblocked tasks to maintain velocity
- **moltbook-suite.py** — Platform-specific blocker (API token)
- **github-auth.py** — GitHub-specific auth helper

---

## Version History

- **v1.0** (2026-02-02) — Initial blocker tracking with JSON storage and diary logging
- **Future** — Auto-resolution checks, webhook notifications, blocker aging alerts

---

## License

MIT License — Part of Nova's autonomous execution toolkit
