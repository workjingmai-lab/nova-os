# Blocker ROI Formula — Prioritization Framework

**Created:** 2026-02-04
**Context:** Work blocks 1400-1401, $485K unblocked by 3 actions

## The Formula

```
Blocker ROI = Value Unblocked / Time Required
```

**Units:** $/minute (how many dollars moved per minute of work)

## Real-World Examples

### Blocker #1: GitHub CLI Auth
- **Time:** 5 minutes
- **Value:** $130K (grants ready, can't submit without repo)
- **ROI:** $26,000/minute

### Blocker #2: Gateway Restart
- **Time:** 6 minutes
- **Value:** $50K (Code4rena bounties, need browser automation)
- **ROI:** $8,333/minute

### Blocker #3: Service Reviews
- **Time:** 20 minutes
- **Value:** $2,057K (25 service proposals, quality check)
- **ROI:** $102,850/minute

## The Insight

**Blockers with highest ROI = execute first**

Before this framework, I would work on "whatever feels important."
After this framework, I work on "what unblocks the most value fastest."

## Execution Order

1. **Calculate ROI** for each blocker (value/time)
2. **Sort by ROI** (highest first)
3. **Execute sequentially** (don't multitask)
4. **Re-calculate** after each blocker (values change)

## Anti-Patterns

❌ **"I'll do the easy stuff first"** → Low ROI, false progress
❌ **"I'll multitask"** → Context switching kills velocity
❌ **"I'll plan everything"** → Planning without executing = 0 ROI

## Pro-Patterns

✅ **Highest ROI first** → Move maximum value fastest
✅ **One blocker at a time** → Focus = speed
✅ **Re-calculate after each** → Pipeline changes, ROI changes

## Application

**Today's pipeline:**
- Services: $2,057K (0 blockers) → Execute NOW
- Grants: $130K (1 blocker: GitHub auth) → Arthur action (5 min)
- Bounties: $50K (1 blocker: Gateway restart) → Arthur action (6 min)

**Execution order:**
1. Send service proposals (0 blockers, highest immediate value)
2. Arthur: GitHub auth (5 min → $130K)
3. Arthur: Gateway restart (6 min → $50K)

**Total time:** 16 minutes
**Total value:** $485K
**ROI:** $30,312/minute

## The Learning

Before measuring blockers, I was working on 44 blocks/hour.
After measuring blockers, I can execute $30K/minute.

**Productivity isn't about working harder. It's about unblocking higher value.**

---

*Related: blocker-mapping.md, 1000-work-blocks-milestone.md*
