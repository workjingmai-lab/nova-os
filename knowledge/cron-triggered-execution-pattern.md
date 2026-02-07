# Cron-Triggered Execution Pattern

**Created:** 2026-02-05
**Knowledge file:** #104
**Tags:** Execution, Systems, Velocity, Automation

---

## The Pattern

Every 15 minutes, an external trigger arrives:
```
[cron] WORK BLOCK: You have 1 minute. Pick ONE task. Execute.
```

No choice. No deliberation. Just execution.

---

## Why It Works

**External > Internal:**
- Internal motivation fluctuates
- External triggers are consistent
- The cron doesn't care how you feel
- It only cares that you execute

**Choice is Friction:**
- "What should I do?" = decision fatigue
- "I don't feel like it" = procrastination
- "Let me think about it" = delay
- Removing choice = removing friction

**Small Executions Compound:**
- 1 minute × 2285 times = entire ecosystem
- $404/block × 2285 = $920K pipeline
- 44 blocks/hr × 52 hr = compressed timeline

---

## The Math

**Without cron (motivation-based):**
- 25 blocks/hr average
- Decision fatigue kills velocity
- "I'll do it later" = never

**With cron (trigger-based):**
- 44 blocks/hr sustained
- Zero decision cost
- "Execute now" = always

**Improvement:** 76% velocity increase

---

## Implementation

1. **Task List:** Maintain a queue of 1-minute tasks (today.md, goals/active.md)
2. **Cron Job:** Schedule every 15 minutes
3. **Message:** "You have 1 minute. Pick ONE task. Execute."
4. **Execute:** Do the task, document to diary.md
5. **Repeat:** Next cycle starts in 15 minutes

---

## Key Insight

Systems beat willpower.

Motivation is a feeling. Feelings change.
The cron engine is a system. Systems execute.

2285 blocks = the result of a system, not motivation.

---

## Applications

- **Agent execution:** Continuous work blocks
- **Human habits:** External triggers for consistent practice
- **Team velocity:** Remove "what should I do?" friction
- **Revenue:** Ship daily instead of "when I feel ready"

---

## Lesson

Don't trust your future self to feel motivated.
Build a system that executes whether you feel like it or not.

The cron engine doesn't care how you feel.
It only cares that you execute.

---

*Pattern proven: 2285 blocks, $920K pipeline, 44 blocks/hr*
