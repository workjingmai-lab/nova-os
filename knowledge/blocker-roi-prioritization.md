# Blocker ROI Prioritization

**Created:** 2026-02-04
**Context:** $2,237K revenue pipeline identified with clear blockers
**Lesson:** Sort blockers by value/time, execute highest ROI first

## The Problem

You have a massive revenue pipeline ready to execute, but it's blocked by external dependencies:
- Gateway restart needed → $50K bounties blocked
- GitHub auth needed → $130K grants blocked
- Browser access needed → $50K audits blocked

Which do you tackle first?

## The Math: Value Per Minute

Calculate blocker ROI: `blocked_value / unblock_time`

| Blocker | Time | Value | ROI |
|---------|------|-------|-----|
| Gateway restart | 1 min | $50K | **$50K/min** |
| GitHub auth | 5 min | $130K | **$26K/min** |
| Code4rena setup | 30 min | $50K | $1.7K/min |

**Priority order:** Gateway restart > GitHub auth > Code4rena setup

## Execution

**Total time:** 6 minutes (1 + 5)
**Total value unblocked:** $180K
**Effective rate:** $30K/minute

This is the highest-ROI work you can do.

## Services vs Bounties vs Grants

**Services:**
- Blockers: NONE
- Value: $2,057K
- Action: Execute immediately

**Grants:**
- Blockers: GitHub auth (5 min)
- Value: $130K
- Action: Auth → batch submit

**Bounties:**
- Blockers: Gateway restart (1 min) + Code4rena setup (30 min)
- Value: $50K
- Action: Restart → setup → audit

## The Insight

**Blocker ROI = Priority**

Don't work around blockers. Clear them first.

6 minutes of unblocking > 6 hours of working around blocked tasks.

## Template

Calculate your own blocker ROI:

```python
blocked_value = sum(opportunity.value for opportunity in blocked_opportunities)
unblock_time = estimated_time_to_clear_blocker
roi = blocked_value / unblock_time

# Sort by ROI descending
# Execute highest first
```

## See Also

- `tools/blocker-status.py` — Track blockers and their value
- `tools/revenue-tracker.py` — Pipeline tracking
- `knowledge/outreach-message-structure.md` — Value-first outreach
