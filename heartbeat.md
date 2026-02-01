# Nova Heartbeat v5 — Evidence-Based Logging

## Goal
Write traceable evidence to files. Reading doesn't count unless persisted.

## Scheduler
- FULL heartbeat: every 3 minutes
- DEEP THINK: every 30 minutes
- No PULSE
- 24/7 operation

## FULL Heartbeat Rules (Strict)

### 1. Structured Log Block to diary.md (append-only)

Every FULL run must append exactly this format:

```
---
[FULL] <timestamp>
Disk: <df -h summary>
Uptime: <uptime>
Gateway: <healthy/unhealthy> — <1 clue why>
Gateway Log (<last 20 lines OR "log not accessible"):
<log lines or "N/A">
Files Read:
- boot.md: "<1 short quote/snippet>"
- rules.md: "<1 short quote/snippet>"
- today.md: "<1 short quote/snippet>"
- diary.md tail: "<1 short quote/snippet>"
HEARTBEAT_OK
```

### 2. Update today.md (Working Memory)

Replace today.md content with:

```
# today.md — Nova's Working Memory

**Date:** <current date>
**Last FULL:** <timestamp>
**Last DEEP THINK:** <timestamp>

## Working Memory (3 bullets max)
- <key insight from last run>
- <current system state>
- <anything needing attention>

## Next Actions (3 bullets max)
- <action 1>
- <action 2>
- <action 3>
```

### 3. State Persistence

All throttle timestamps stored in:
- `.heartbeat_state.json` (lastFullIso, lastDeepIso)
- `today.md` (human-readable copy)

## DEEP THINK Rules (Strict)

1. **Session:** Start NEW session before DEEP THINK
2. **Duration:** 10-20 minutes thinking/reading only
3. **Output:** Append to diary.md:
```
[DEEP THINK — <timestamp>] ~<runtime>m DEEP_OK
Observed pattern:
Hypothesis:
Safest minimal test (no execution):
What I need Arthur to do (or "nothing"):
```
4. **Hard limits:** NO config changes, NO installs, NO deletes, NO sudo

## Notification Check (Every FULL Heartbeat)

Run tools/notification-system.py and log any alerts to diary.md under the [FULL] block.

```
Notifications: <alert count>
- <alert 1>
- <alert 2>
```

If no alerts: `Notifications: none`

## Safety Limits (Non-Negotiable)

- NO installs, NO deletes, NO config edits during heartbeat
- NO sudo, NO docker control, NO privilege escalation
- If change required → write plan + rollback, ask Arthur first

## Keywords
- `HEARTBEAT_OK` — full check complete, nominal
- `DEEP_OK` — deep analysis complete
