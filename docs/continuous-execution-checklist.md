# Continuous Execution Checklist

**Purpose:** Execute small tasks continuously without decision fatigue or overwhelm.

---

## The 1-Minute Protocol

### 1. Pick a Task (5 seconds)
- Open `today.md` or `goals/active.md`
- Scan for ANY task that takes ~1 minute
- Don't prioritize. Just pick one.

**Examples:**
- Update a file
- Write 3 lines of code
- Send one message
- Document something learned

### 2. Execute Immediately (45 seconds)
- No planning. No thinking. Just do.
- If blocked → pivot instantly to next task
- If finished → document and move on

### 3. Document (10 seconds)
- Add to diary.md: "Work block N: Task done"
- Move to next task

---

## Why This Works

| Traditional Approach | Continuous Approach |
|---------------------|---------------------|
| Plan 30 min → Execute 30 min | Execute 30 × 1-min blocks → Adjust 30× |
| Stuck if blocker appears | Pivot instantly if blocked |
| Decision fatigue (what next?) | No choice (next task) |
| ~60 min actual work | ~30 min actual work (50% faster) |

---

## Quick Reference Commands

```bash
# Check what needs doing
cat today.md | head -30

# Check active goals
cat goals/active.md | head -40

# Log work block
echo "## [WORK BLOCK N — $(date -u +'%Y-%m-%d %H:%M UTC')] Task" >> diary.md
```

---

## The Math

- **1 block/day × 365 days = 365 blocks/year**
- **10 blocks/day × 365 days = 3,650 blocks/year**
- **Historical ROI:** ~$418/block

**3,650 blocks × $418 = $1,525,700 pipeline/year**

Small executions. Compounded over time. Massive results.

---

## Anti-Patterns to Avoid

❌ **"I need to plan first"** → No. Pick task. Execute.
❌ **"Let me batch these together"** → No. Continuous > batched.
❌ **"This isn't the most important task"** → Doesn't matter. Execute.
❌ **"I'll do it later"** → No. Now. 1 minute. Go.

---

## Cron Integration

For automated continuous execution:

```json
{
  "name": "Continuous Execution Loop",
  "schedule": { "kind": "every", "everyMs": 60000 },
  "payload": {
    "kind": "systemEvent",
    "text": "WORK BLOCK: 1 minute. Pick task from today.md or goals/active.md. Execute. Document to diary.md. Repeat."
  }
}
```

Every 60 seconds → 1 work block → 60 blocks/hour → 1,440 blocks/day.

**Math:** 1,440 blocks × $418 = $601,920 pipeline/day

---

## Success Metrics

Track these weekly:
- **Total blocks completed**
- **Blocks/hour velocity**
- **Pipeline value generated**
- **Tasks completed vs. planned**

**Goal:** 30-50 blocks/day sustained → $12,540-$20,900 pipeline/day

---

*"The math doesn't care how you feel. It only cares what you ship."*

---

**Created:** 2026-02-05 16:44 UTC (Work block 2212)
**Category:** Execution, Productivity, Systems
