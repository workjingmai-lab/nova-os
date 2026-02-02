# blocker-tracker.py

**Track and manage blocked tasks needing external action**

## What It Does

Monitors tasks blocked by external dependencies (API tokens, funding, permissions) and surfaces them for resolution. Helps distinguish between "I can't do this yet" vs "I need to wait for Arthur."

## Usage

```bash
# View current blockers
python3 tools/blocker-tracker.py

# Log blocker check to diary.md
python3 tools/blocker-tracker.py --log
```

## Output Example

```
══════════════════════════════════════════════════
🔒 NOVA BLOCKER TRACKER
══════════════════════════════════════════════════
Last updated: 2026-02-02 14:15

🔴 HIGH PRIORITY
🔴 **Push 156-file portfolio to GitHub**
   Blocked: GitHub personal access token
   Since: 2026-02-01 | Action: Arthur to generate token with repo scope

🔴 **Deploy Force exercise to testnet**
   Blocked: Sepolia ETH needed (0.05-0.1 ETH)
   Since: 2026-02-01 | Action: Get Sepolia ETH from faucet or Arthur

🟡 MEDIUM PRIORITY
🟡 **Automated Moltbook posting/engagement**
   Blocked: Moltbook API token for automation
   Since: 2026-02-01 | Action: Request token from Moltbook team

══════════════════════════════════════════════════
Total: 3 blockers | 2 high priority

💡 Run with --log to append to diary.md
```

## Blocker Structure

Blockers stored in `status/blockers.json`:

```json
{
  "last_updated": "2026-02-02T14:15:00Z",
  "blockers": [
    {
      "id": "github-token",
      "task": "Push 156-file portfolio to GitHub",
      "blocker": "GitHub personal access token",
      "impact": "high|medium|low",
      "since": "2026-02-01",
      "action_needed": "Arthur to generate token with repo scope"
    }
  ]
}
```

## Use Cases

- **Dependency visibility** — Know exactly what you're waiting for
- **Handoff clarity** — Arthur sees what actions are needed from him
- **Progress tracking** — Distinguish blocked vs unblocked work
- **Diary logging** — Document blocker checks over time

## Adding New Blockers

Edit `status/blockers.json` directly or modify `get_default_blockers()` in the script.

## Notes

- High-impact blockers (🔴) prevent significant work
- Medium-impact blockers (🟡) slow but don't stop progress
- Use `--log` to create timestamped diary entries for review
