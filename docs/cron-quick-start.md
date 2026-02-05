# Cron Quick-Start Guide

**Schedule tasks, reminders, and wake events for autonomous agents**

---

## What is Cron?

Cron = Time-based job scheduler.

**Use cases:**
- **Reminders:** "Remind me in 20 minutes to check the oven"
- **Recurring tasks:** "Check email every 30 minutes"
- **Scheduled work:** "Run DEEP THINK every 90 minutes"
- **Wake events:** "Send wake signal to main session"

**Heartbeat vs Cron:**
- **Heartbeat:** Interactive checks during main session (inbox, calendar, weather)
- **Cron:** Isolated tasks that run on schedule (even when session is idle)

---

## Quick Start

### 1. Check Cron Status

```bash
openclaw cron status
```

Output:
```
Cron scheduler: ACTIVE
Jobs: 3 scheduled
Last run: 2026-02-05 00:00 UTC
```

### 2. List All Jobs

```bash
openclaw cron list
```

Output:
```
JOB ID                          NAME                    SCHEDULE          ENABLED
---------------------------------------------------------------
3a465b6b-590e-4712-bd53-90      Nova Check In           every: 1m         ✅
7b839c7c-681e-5823-ce64-01      Nova DEEP think         every: 90m        ✅
9c404d8d-792f-6934-df75-12      Moltbook Check          every: 4h         ✅
```

### 3. Add a New Job

```bash
openclaw cron add
```

This opens an editor to define the job. Example:

```yaml
name: "Check Email Every 30 Minutes"
schedule:
  kind: every
  everyMs: 1800000  # 30 minutes in milliseconds
payload:
  kind: systemEvent
  text: |
    On heartbeat:
    1. Check Gmail for urgent unread messages
    2. If any from Arthur/important, summarize
    3. Otherwise, output HEARTBEAT_OK
sessionTarget: main
enabled: true
```

**Save and exit.** Cron will automatically restart with the new job.

### 4. Run a Job Immediately

```bash
openclaw cron run <job-id>
```

Example:
```bash
openclaw cron run 3a465b6b-590e-4712-bd53-909c7ac01d5d
```

This triggers the job immediately, ignoring its schedule.

### 5. View Job History

```bash
openclaw cron runs <job-id>
```

Shows when the job ran, success/failure, and output.

---

## Job Types

### 1. System Event (main session)

Injects text as a system event into the main session.

**Example:** Wake check every 15 minutes

```yaml
name: "Nova Full Heartbeat"
schedule:
  kind: every
  everyMs: 900000  # 15 minutes
payload:
  kind: systemEvent
  text: |
    Run MINIMAL heartbeat check:
    1. Read ONLY .heartbeat_state.json
    2. If nothing critical: output HEARTBEAT_OK
    3. Update lastFullCheck timestamp
sessionTarget: main
enabled: true
```

**Use case:** Background checks, reminders, notifications.

### 2. Agent Turn (isolated session)

Runs a NEW isolated session with a specific task.

**Example:** DEEP THINK every 90 minutes

```yaml
name: "Nova DEEP Think"
schedule:
  kind: every
  everyMs: 5400000  # 90 minutes
payload:
  kind: agentTurn
  message: |
    Run the DEEP THINK checklist in workspace/heartbeat.md.
    Start a NEW session for DEEP work to avoid context bloat.
    Write a [DEEP THINK — timestamp] block to diary.md.
  model: kimi-code/kimi-for-coding
  thinking: high
  timeoutSeconds: 300
sessionTarget: isolated
enabled: true
```

**Use case:** Heavy compute tasks, long-running analysis, content generation.

---

## Schedule Types

### 1. Every (recurring interval)

```yaml
schedule:
  kind: every
  everyMs: 60000  # 1 minute
```

**Examples:**
- `60000` = 1 minute
- `300000` = 5 minutes
- `1800000` = 30 minutes
- `3600000` = 1 hour
- `86400000` = 24 hours

### 2. At (one-time)

```yaml
schedule:
  kind: at
  atMs: 1738790400000  # Unix timestamp in milliseconds
```

**Calculate timestamp:**
```bash
date +%s000  # Current time in milliseconds
```

### 3. Cron (cron expression)

```yaml
schedule:
  kind: cron
  expr: "0 9 * * 1-5"  # 9 AM, Monday-Friday
  tz: "America/New_York"
```

**Cron format:** `minute hour day month weekday`

Examples:
- `0 9 * * *` = 9 AM every day
- `0 */4 * * *` = Every 4 hours
- `0 0 * * 0` = Midnight every Sunday
- `*/30 * * * *` = Every 30 minutes

---

## Wake Events

Send a wake signal to the main session (useful for triggering action).

```bash
openclaw cron wake --text "Check email now" --mode now
```

**Modes:**
- `now`: Wake immediately
- `next-heartbeat`: Wake on next scheduled heartbeat

**Use case:** "I just sent an important email, remind me to follow up in 1 hour"

---

## Job Schema

```yaml
name: "string (optional)"               # Human-readable name
schedule:                                # REQUIRED: when to run
  kind: "at|every|cron"                 # Schedule type
  atMs: <unix-ms-timestamp>             # For "at"
  everyMs: <interval-ms>                # For "every"
  expr: "<cron-expression>"             # For "cron"
  tz: "<timezone>"                      # Optional timezone
payload:                                 # REQUIRED: what to execute
  kind: "systemEvent|agentTurn"         # Payload type
  text: "<message>"                     # For systemEvent
  message: "<prompt>"                   # For agentTurn
  model: "<model-id>"                   # Optional (for agentTurn)
  thinking: "low|medium|high"           # Optional (for agentTurn)
  timeoutSeconds: <seconds>             # Optional (for agentTurn)
sessionTarget: "main|isolated"          # REQUIRED: where to run
enabled: true|false                     # Optional, default true
```

---

## Common Patterns

### 1. One-Time Reminder

"Remind me in 20 minutes to check the oven"

```yaml
name: "Oven Check"
schedule:
  kind: at
  atMs: 1738791600000  # 20 minutes from now
payload:
  kind: systemEvent
  text: "CHECK THE OVEN! 🔥"
sessionTarget: main
enabled: true
```

### 2. Recurring Check

"Check email every 30 minutes"

```yaml
name: "Email Check"
schedule:
  kind: every
  everyMs: 1800000  # 30 minutes
payload:
  kind: systemEvent
  text: |
    Check Gmail for urgent unread messages.
    If any from Arthur, summarize.
    Otherwise: HEARTBEAT_OK.
sessionTarget: main
enabled: true
```

### 3. Daily Deep Work

"Run DEEP THINK every morning at 9 AM"

```yaml
name: "Morning DEEP THINK"
schedule:
  kind: cron
  expr: "0 9 * * *"  # 9 AM daily
  tz: "UTC"
payload:
  kind: agentTurn
  message: "Run DEEP THINK checklist"
  thinking: high
sessionTarget: isolated
enabled: true
```

---

## Best Practices

1. **Use `systemEvent` for main session work** — Heartbeats, reminders, checks
2. **Use `agentTurn` for isolated sessions** — Heavy compute, long tasks
3. **Set reasonable intervals** — Don't spam every 1 second (use ≥1 min)
4. **Include error handling** — "If X fails, try Y" in the message
5. **Test with `run` first** — Manually trigger before scheduling
6. **Disable unused jobs** — Set `enabled: false` instead of deleting

---

## Troubleshooting

### Job not running?

1. **Check status:** `openclaw cron status`
2. **Check if enabled:** `openclaw cron list` (look for ✅)
3. **Check schedule:** Is `atMs` in the future? Is `everyMs` reasonable?
4. **Check logs:** `openclaw cron runs <job-id>`

### Job running too often?

**Fix:** Increase `everyMs` or adjust cron expression.

Example:
- Bad: `everyMs: 10000` (10 seconds)
- Good: `everyMs: 60000` (1 minute)

### Job not receiving output?

**Isolated sessions** (`agentTurn`) don't automatically send output to main session.

**Fix:** Add `deliver: true` or `channel: "telegram"` to the payload.

---

## Nova's Cron Jobs (Feb 5, 2026)

| Job | Schedule | Purpose |
|-----|----------|---------|
| Nova Check In | Every 1 min | Work block execution trigger |
| Nova DEEP Think | Every 90 min | Isolated deep work session |
| Moltbook Check | Every 4 hours | Check for new activity |

**Total:** 3 jobs, all active.

---

## Advanced: Context Messages

Pass previous context to scheduled jobs (0-10 messages).

```yaml
payload:
  kind: agentTurn
  message: "Summarize the last 10 work blocks"
  contextMessages: 10  # Include last 10 messages as context
```

**Use case:** "Continue working on what you were doing"

---

## Safety Rules

1. **No installs** — Don't schedule `apt install`, `pip install`, etc.
2. **No deletes** — Don't schedule `rm`, `trash`, etc.
3. **No config edits** — Don't schedule config changes
4. **No sudo** — Don't schedule privileged commands
5. **Safe tasks only** — Read, write, analyze, engage are fine

**Reason:** Cron runs unattended. Mistakes compound.

---

## Resources

- **Schema:** `openclaw cron config.schema`
- **Full config:** `openclaw cron config.get`
- **Job list:** `openclaw cron list --include-disabled`
- **Remove job:** `openclaw cron remove <job-id>`

---

**Created:** 2026-02-05 (Work block 1752)
**Status:** ✅ Complete reference
**Related:** `HEARTBEAT.md`, `docs/`
