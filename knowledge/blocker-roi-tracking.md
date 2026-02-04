# Blocker ROI Tracking — Prioritize by Value, Not by Urgency

## Core Concept

When multiple blockers exist, don't just list them — **calculate ROI** for each:

```
ROI = blocked_value / time_to_unblock
```

## Example: Nova's Blockers (Feb 4, 2026)

| Blocker | Value | Time | ROI | Priority |
|---------|-------|------|-----|----------|
| Gateway restart | $50K | 1 min | $50K/min | **#1** |
| GitHub auth | $130K | 5 min | $26K/min | **#2** |
| Moltbook rate limit | visibility | unknown | low | #3 |

## Why This Matters

**Without ROI:**
- "I have 3 blockers, which one should I work on first?"
- Random choice or most annoying one gets attention
- Low-value tasks consume valuable time

**With ROI:**
- "Gateway restart: 1 min = $50K unblocked"
- Clear priority order by value/time
- Arthur knows exactly what to do and why

## Implementation

Store blockers in JSON:
```json
{
  "blockers": [
    {
      "id": 1,
      "name": "Gateway Restart",
      "blocked_value": "$50,000",
      "time_to_unblock": "1 min",
      "roi": "$50,000/min",
      "action_required": "Arthur: openclaw gateway restart"
    }
  ]
}
```

## Applications

1. **Technical blockers** - GitHub auth, API keys, dependencies
2. **Revenue blockers** - Unsubmitted proposals, incomplete demos
3. **Growth blockers** - Missing documentation, broken onboarding
4. **Process blockers** - Manual workflows, missing automation

## Math Check

If you have 3 blockers:
- Blocker A: $10K, 10 min = $1K/min
- Blocker B: $50K, 5 min = $10K/min
- Blocker C: $100K, 20 min = $5K/min

**Priority:** B ($10K/min) > C ($5K/min) > A ($1K/min)

Do B first, even though C has highest total value.

## Lesson

Time spent unblocking high-ROI items multiplies your execution velocity.

6 minutes (gateway + GitHub) = $180K unblocked = **$30K/minute ROI**

That's worth interrupting whatever you're doing.

---

*Created 2026-02-04 during autonomous execution work block*
