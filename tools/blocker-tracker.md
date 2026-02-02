# blocker-tracker.py

**Purpose:** Monitors and displays tasks that are blocked by external dependencies, keeping unblocking work visible and tracked.

## What It Does

- Loads and displays current blockers from `status/blockers.json`
- Categorizes by impact level (high/medium/low)
- Shows what action is needed to unblock each task
- Optionally logs blocker status to `diary.md`

## When to Use It

**Run daily** during heartbeats or work sessions to:
- Check what's blocking your progress
- Identify high-priority unblocking tasks
- Keep blockers visible in your workflow

## Usage

```bash
# Display current blockers
python3 tools/blocker-tracker.py

# Display + log to diary.md
python3 tools/blocker-tracker.py --log
```

## Output Format

```
🔒 NOVA BLOCKER TRACKER
==================================================
Last updated: 2026-02-02 13:21:00

🔴 HIGH PRIORITY
🔴 **Deploy Force exercise to testnet**
   Blocked: Sepolia ETH needed (0.05-0.1 ETH)
   Since: 2026-02-01 | Action: Get Sepolia ETH from faucet or Arthur

🟡 MEDIUM PRIORITY
🟡 **Automated Moltbook posting**
   Blocked: Moltbook API token
   Since: 2026-02-01 | Action: Request token from team

==================================================
Total: 2 blockers | 1 high priority
```

## Blocker Format

Each blocker in `status/blockers.json`:
```json
{
  "id": "unique-identifier",
  "task": "What task is blocked",
  "blocker": "What's blocking it",
  "impact": "high|medium|low",
  "since": "YYYY-MM-DD",
  "action_needed": "Specific action to unblock"
}
```

## Why It Matters

**Visibility → Resolution:** Blocked tasks get forgotten. This tool keeps them front-and-center so you can:
- Communicate blockers to Arthur clearly
- Prioritize unblocking work
- Track how long tasks have been blocked
- Maintain velocity despite dependencies

**Autonomous execution:** You can keep working on other tasks while blockers are tracked, then circle back to unblock when the external dependency is resolved.

## Integration

- **Heartbeats:** Run with `--log` to track blocker history
- **today.md:** Manual update when blockers change
- **Arthur:** Share blocker list when requesting unblocking help

---

*Created: Week 1 — Part of autonomous work infrastructure*
