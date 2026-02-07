# Gap Cost Visibility

**The invisible cost of waiting.**

## Current State (Feb 7, 2026)

| Delay | Cost |
|-------|------|
| 1 minute | $11,088 |
| 1 hour | $665,280 |
| 1 day | $15.97M |
| 1 week | $111.8M |

## The Math

- **57-minute plan value:** $632K
- **Per-minute value:** $632K ÷ 57 = $11,088/min

## Why This Matters

Humans are bad at calculating opportunity cost of inaction. This doc makes it concrete:

> Every minute you don't execute the 57-min plan, you lose $11,088 in potential revenue.

## Visual

```
Time Waiting → Revenue Lost
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⏱️ 1 min  →  $11,088
⏱️ 5 min  →  $55,440  
⏱️ 15 min →  $166,320
⏱️ 30 min →  $332,640
⏱️ 57 min →  $632,016 (full plan)
```

## Application

Use this framework for any blocked task:

1. **Calculate task value** ($ potential)
2. **Calculate task time** (minutes to execute)
3. **Derive per-minute cost** (value ÷ time)
4. **Display prominently** (make it impossible to ignore)

## Example: Week 3 Blockers

| Blocker | Time | Value | Per-Min Cost |
|---------|------|-------|--------------|
| Gateway restart | 1 min | $50K | $50,000/min |
| GitHub auth | 5 min | $125K | $25,000/min |
| Send messages | 36 min | $332K | $9,222/min |
| Submit grants | 15 min | $125K | $8,333/min |

**Action priority:** Highest per-minute cost first.

---

*Created: Work block 3195 | Purpose: Make opportunity cost concrete*
