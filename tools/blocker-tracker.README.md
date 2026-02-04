# blocker-tracker.py

**Monitor blocked tasks and surface them for resolution.**

## What It Does

Tracks blockers that prevent task execution, displays current status with priority levels, and logs blocker checks to diary.md.

**Value:** Prevents "silent blockers" from stalling work. Makes blockers visible, prioritized, and actionable.

## Usage

### Show Current Blockers
```bash
python3 tools/blocker-tracker.py
```

### Show Blockers + Log to Diary
```bash
python3 tools/blocker-tracker.py --log
```

## Output Example

```
==================================================
🔒 NOVA BLOCKER TRACKER
==================================================
Last updated: 2026-02-03 14:00

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

==================================================
Total: 3 blockers | 2 high priority

💡 Run with --log to append to diary.md
```

## Blocker Structure

Each blocker in `status/blockers.json`:
```json
{
  "id": "github-token",
  "task": "Push 156-file portfolio to GitHub",
  "blocker": "GitHub personal access token",
  "impact": "high",
  "since": "2026-02-01",
  "action_needed": "Arthur to generate token with repo scope"
}
```

## Priority Levels

| Level | Emoji | Description |
|-------|-------|-------------|
| high | 🔴 | Blocks revenue or critical path (e.g., $130K grants) |
| medium | 🟡 | Slows progress but workarounds exist |
| low | 🟢 | Minor inconvenience, low impact |

## How It Works

1. **Load blockers** — Reads `status/blockers.json`
2. **Display by priority** — Shows high priority first, then medium
3. **Log if requested** — Appends blocker check to diary.md with timestamp
4. **Auto-initialize** — If no blockers file exists, loads default blockers

## Default Blockers

The tool includes default blockers from today.md:
- **sepolia-eth** — Testnet deployment blocked (0.05-0.1 ETH needed)
- **github-token** — Portfolio push blocked (PAT with repo scope needed)
- **moltbook-token** — Automation blocked (API token needed)

## Dependencies

- Python 3.x
- No external packages required (stdlib only: json, os, datetime, pathlib)
- **Data file:** `status/blockers.json` (auto-created)
- **Log file:** `diary.md` (appends if `--log` flag used)

## Related Tools

- `blocker-roi-calculator.py` — Calculate ROI of unblocking specific blockers
- `revenue-tracker.py` — Track revenue pipeline impacted by blockers
- `task-navigator.py` — Find unblocked tasks to execute

## Why This Matters

**Invisible blockers stall progress.**

Without tracking:
- "I can't push to GitHub" → forgotten, never resolved
- "Need Sepolia ETH" → deprioritized, loses momentum
- $130K grant submission blocked → no revenue generated

With tracking:
- Blockers are visible, prioritized, actionable
- Arthur sees exact blockers and actions needed
- High-impact blockers ($50K/min ROI) surfaced first
- Diary logs create historical record

**Nova's use case:** Tracks 3 blockers (2 high), logs status to diary, continues autonomous work until blockers resolved.

---

**Last updated:** 2026-02-03
**Category:** System
**Status:** Core tool — blocker visibility and prioritization
