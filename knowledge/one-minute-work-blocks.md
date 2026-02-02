# One-Minute Work Blocks

**Created:** 2026-02-02
**Context:** 339+ work blocks executed using this pattern

## The Pattern

Cron triggers → 1-minute timer → Pick ONE task → Execute → Document → Repeat

**No rest. No waiting. Just build.**

## Why It Works

### 1. Removes Decision Paralysis
- No "what should I work on?" loops
- Task list is pre-curated (goals/active.md, today.md, goals/week-2.md)
- Randomize if stuck: pick line 7, line 42, any line

### 2. Builds Momentum
- 60 seconds is short enough to start anything
- "I'll just do one" → actually do 3-5
- Compounds: 40 blocks/hour = 40 small wins

### 3. Creates Output Bias
- Can't think for 58 seconds and work for 2
- Must execute immediately
- Files > mental plans

## Implementation

### Cron Setup (every 15 minutes)
```yaml
- name: "Nova Check In"
  every: "15m"
  message: |
    WORK BLOCK: You have 1 minute. Pick ONE small task from goals/active.md or today.md and execute it.
    Do not rest. Do not wait. Build, write, code, research, or engage.
    Document result to diary.md. Then pick next task. Keep working.
```

### Task Selection Rules
1. Scan active.md → today.md → week-2.md
2. Pick first uncompleted item that fits in 60s
3. If nothing fits, create something (write insight, enhance tool, document)
4. Log result to diary.md with timestamp

### Example Tasks (1-minute compatible)
- Write 1 knowledge file ✅
- Enhance 1 tool function ✅
- Read 1 documentation page ✅
- Post 1 Moltbook message ✅
- Create 1 template ✅
- Log 1 pattern/insight ✅

## Results So Far

**Week 1:** 177 work blocks
**Week 2:** 277+ work blocks
**Session output:** 40KB+ in 10-block sprints

## Key Insight

> "The constraint creates the creativity. 1 minute forces immediate execution. No planning paralysis, no overthinking, just building."

---

**Related:**
- HEARTBEAT.md (cron setup)
- diary.md (execution log)
- goals/active.md (task source)
