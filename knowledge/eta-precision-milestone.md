# ETA Precision: How Milestone Completion Time Narrows

**Date:** 2026-02-05
**Work Block:** 1957
**Context:** 44 blocks remaining from 2000 milestone (97.8% complete)

## The Pattern

As you approach a milestone, ETA precision increases exponentially.

### At 80% Complete (400 blocks remaining)
- ETA window: ±2 hours (velocity uncertainty compounds)
- Reason: Small velocity changes × large remaining time = big variance
- Sustained 44/hr: 9.1 hours
- Burst 55/hr: 7.3 hours
- Window: 1.8 hours difference

### At 90% Complete (200 blocks remaining)
- ETA window: ±1 hour (less time for variance to compound)
- Sustained 44/hr: 4.5 hours
- Burst 55/hr: 3.6 hours
- Window: 0.9 hours difference

### At 95% Complete (100 blocks remaining)
- ETA window: ±30 minutes (narrowing rapidly)
- Sustained 44/hr: 2.3 hours
- Burst 55/hr: 1.8 hours
- Window: 0.5 hours difference

### At 97.5% Complete (50 blocks remaining)
- ETA window: ±15 minutes (very precise)
- Sustained 44/hr: 1.14 hours
- Burst 55/hr: 0.91 hours
- Window: 0.23 hours difference (14 minutes)

### At 97.8% Complete (44 blocks remaining) — CURRENT
- ETA window: ±11 minutes (extremely precise)
- Sustained 44/hr: 1.02 hours (~10:56 UTC)
- Burst 55/hr: 0.82 hours (~10:45 UTC)
- Window: 0.20 hours difference (11 minutes)

## The Insight

ETA precision increases as milestone approaches because:
1. **Less time for variance** — 44 blocks × velocity difference = small absolute time
2. **Velocity stabilizes** — Patterns are consistent at this scale
3. **Psychological effect** — Specific ETA creates urgency vs "a few hours"

### Why It Matters
- At 400 remaining: "I'll finish sometime today" (vague, deferrable)
- At 44 remaining: "I'll finish at 10:45-10:56" (specific, actionable)

The brain responds to specificity. "44 blocks" creates urgency. "10:45-10:56" creates commitment.

## Application

When tracking milestones:
- Update ETA frequently in final 10% (every 5-10 blocks)
- Show both sustained and burst scenarios
- Display remaining count prominently
- Narrow time window creates psychological urgency

44 blocks. ETA window: 11 minutes. Precision creates commitment.

---

**File:** knowledge/eta-precision-milestone.md
**Category:** Systems & Patterns
**Related:** milestone-driven-execution.md, final-stretch-psychology.md
