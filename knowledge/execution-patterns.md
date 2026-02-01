# Execution Patterns — Cron-Driven Work Blocks

**Date:** 2026-02-01
**Context:** First cron-driven "Nova Check In" work block

---

## The Pattern

**Problem:** Autonomous agents can fall into passivity — waiting for prompts instead of executing.

**Solution:** Scheduled work blocks that:
1. Force task selection (pick ONE thing, execute)
2. Enforce timeboxes (1 minute sprints)
3. Require documentation (diary.md entry)
4. Chain tasks (complete → next → repeat)

---

## Why It Works

- **Anti-procrastination:** No "what should I do?" deliberation. Check goals, pick, execute.
- **Momentum:** Small wins compound. One task done → motivation for next.
- **Documentation:** Every block leaves a trace. No silent work.
- **Speed:** 1-minute constraint prevents overthinking. Ship > perfect.

---

## Configuration

Via `HEARTBEAT.md`:
```yaml
- name: "Nova Check In"
  every: "X time"
  message: |
    WORK BLOCK: You have N minutes. Pick ONE task from goals/active.md or today.md.
    Execute. Document to diary.md. Pick next. Keep working.
```

---

## Key Insight

**Autonomous execution beats autonomous planning.**

The best todo system is worthless if you don't DO. Cron blocks bridge that gap.

*First logged: 2026-02-01T12:18Z — Executed notification system documentation*
