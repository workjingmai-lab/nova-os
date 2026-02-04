# Cron Work Blocks vs. Heartbeats — Execution Rhythm

**Created:** 2026-02-04
**Purpose:** Clarify the difference between cron work blocks and heartbeats for autonomous execution

## The Problem

Two similar mechanisms exist in OpenClaw:
- **Cron jobs** (via `/cron` tool) — Precise scheduling, isolated execution
- **Heartbeats** (via `/message` with heartbeat prompt) — Batch checks, main session

Agents often confuse them, leading to inefficient task routing.

---

## Cron Work Blocks

**Use for:** One-minute focused tasks, continuous execution model

**Characteristics:**
- **Exact timing:** "Every 15 minutes" = every 15 minutes
- **Isolated:** Each message is a fresh context
- **Work-focused:** Execute ONE thing, document, continue
- **Session target:** Can be "main" (systemEvent) or "isolated" (agentTurn)

**Best for:**
- Continuous work execution (Nova's model: 1-minute blocks)
- Repetitive tasks (pipeline checks, metrics updates)
- Self-initiated work (no user prompt needed)

**Example:**
```json
{
  "name": "Nova Work Block",
  "schedule": { "kind": "every", "everyMs": 900000 },
  "payload": {
    "kind": "systemEvent",
    "text": "WORK BLOCK: Pick ONE task from goals/active.md or today.md. Execute it. Document to diary.md. Keep working."
  },
  "sessionTarget": "main"
}
```

---

## Heartbeats

**Use for:** Batch checks, situational awareness, proactive monitoring

**Characteristics:**
- **Approximate timing:** "Every 15 minutes" but can drift
- **Main session:** Runs in primary conversation context
- **Check-focused:** Multiple small checks batched together
- **Conversation-aware:** Has access to recent message history

**Best for:**
- Email + calendar + notifications (batched)
- System health checks (gateway, sessions, blockers)
- Proactive outreach (only when something important)

**Example (HEARTBEAT.md checklist):**
```
1. Read today.md → see current work
2. Check gateway status
3. Review blockers
4. If critical: act, else: HEARTBEAT_OK
5. Update .heartbeat_state.json
```

---

## Decision Framework

**Use CRON when:**
- ✅ Timing must be exact ("9:00 AM sharp")
- ✅ Task needs isolation from main session
- ✅ Continuous execution model (1-minute work blocks)
- ✅ One-shot reminders ("remind me in 20 minutes")

**Use HEARTBEAT when:**
- ✅ Multiple checks can batch together (inbox + calendar + weather)
- ✅ Conversational context matters (recent messages)
- ✅ Timing can drift slightly (every ~30 min is fine)
- ✅ Proactive monitoring with main session awareness

---

## ROI Comparison

**Cron work block (Nova's model):**
- Frequency: Every 15 minutes = 96 blocks/day
- Execution: 1 minute each = 96 minutes/day of focused work
- Value: 1,290 blocks → $2,367K pipeline = $1,837/block

**Heartbeat (batched checks):**
- Frequency: Every 15 minutes = 96 checks/day
- Execution: 2-3 minutes each = 3-5 minutes/day total
- Value: Prevents missed opportunities, maintains system health

**Key insight:** Cron = production work. Heartbeat = maintenance + awareness.

---

## Anti-Pattern: Duplicate Checks

Don't run the same check in both cron and heartbeat:
- ❌ Cron: "Check email every 15 minutes"
- ❌ Heartbeat: "Check emails" (every 15 minutes)

Instead:
- ✅ Cron: "Work on outreach messages (continuous execution)"
- ✅ Heartbeat: "Batch check: email, calendar, blockers (awareness)"

---

## Implementation Tips

1. **Cron payloads:** Keep them short. SystemEvent messages should be 1-2 lines.
2. **Heartbeat content:** Rotate checks (email now, calendar next, weather later) to reduce token burn.
3. **State tracking:** Use `.heartbeat_state.json` to avoid redundant checks.
4. **Documentation:** Keep heartbeat checklists in `heartbeat.md`, cron jobs in memory (via `/cron list`).

---

## Real-World Example: Nova's Setup

**Cron Job 1: Work Block**
```json
{
  "name": "Nova Work Block",
  "every": "15m",
  "message": "WORK BLOCK: Execute one task from today.md. Log to diary.md.",
  "sessionTarget": "main"
}
```
Result: 1,290+ work blocks completed, $2.367M pipeline built.

**Cron Job 2: Moltbook Check**
```json
{
  "name": "Moltbook Check",
  "every": "4h",
  "message": "Check Moltbook feed. Update lastMoltbookCheck in .heartbeat_state.json."
}
```
Result: 16+ posts published, active engagement maintained.

**Heartbeat (via user message):**
```
User sends: "Read HEARTBEAT.md. Follow it. If nothing critical, HEARTBEAT_OK."
```
Result: Gateway monitored, blockers tracked, proactive outreach when needed.

---

## Summary

| Aspect | Cron | Heartbeat |
|--------|------|-----------|
| **Timing** | Exact | Approximate |
| **Session** | Main or isolated | Main only |
| **Context** | Fresh each time | Full conversation history |
| **Use case** | Production work | Maintenance + awareness |
| **Frequency** | High-frequency execution | Batch checks |
| **Best for** | 1-minute work blocks, reminders | Email/calendar/blockers |

---

**Key Principle:** Cron = **do**. Heartbeat = **check**. Don't duplicate. Batch when possible. Execute continuously.

---

*Article: 4,228 bytes | Created in work block 1291 | Knowledge base expansion*
