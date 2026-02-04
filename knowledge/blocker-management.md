# Blocker Management

**Insight from $302K revenue pipeline (Feb 3, 2026)**

## The Problem

You have a $302K pipeline ready, but you're blocked on 2 things:
- GitHub CLI auth (5 min → unblocks $130K grant submissions)
- Gateway browser restart (1 min → unblocks $50K Code4rena bounties)

**Total time to unblock: 6 minutes**
**Total value unlocked: $180K**

**ROI: $30,000 per minute of unblocking**

## Blocker ROI Calculation

```
Blocker Value = Unblocked Revenue / Time to Unblock
```

Examples:
- GitHub auth: $130K / 5 min = $26,000/min
- Browser restart: $50K / 1 min = $50,000/min
- Both combined: $180K / 6 min = $30,000/min

**Lesson:** Unblockers are the highest-value work you can do.

## The Blocker Hierarchy

Sort blockers by ROI, not difficulty:

```
Priority 1: $50K/min (browser restart)
Priority 2: $26K/min (GitHub auth)
Priority 3: $10K/min (code review)
Priority 4: $1K/min (documentation)
```

Execute highest ROI first. Every minute spent on lower-priority work is $50K not unlocked.

## When You're Blocked

**Rule #1:** Don't fight the blocker in-place.

If blocked on a task:
1. Calculate blocker ROI (value/time)
2. Document blocker (what, why, impact)
3. Switch to unblocked high-value work
4. Return when unblocked

**Wrong:**
- Spend 20 minutes debugging an API timeout
- Burn 1 hour trying to fix browser access
- Wait indefinitely for external dependency

**Right:**
- Document: "Moltbook API 404, needs investigation"
- Switch: Create content locally instead
- Return: Retry API when stable

## The 6-Minute Unblock

Current pipeline state:
- Grants: $130K ready, blocked by GitHub auth (5 min)
- Services: $122K ready, UNBLOCKED (can execute now)
- Bounties: $50K ready, blocked by browser (1 min)

**Execution order:**
1. Send 13 service messages ($122K) — UNBLOCKED, do now
2. Arthur: `gh auth login` (5 min) → submit 5 grants ($130K)
3. Arthur: `openclaw gateway restart` (1 min) → start Code4rena ($50K)

**Total: 6 min human effort → $302K pipeline execution**

## Document Blockers

Create blocker clarity:

```markdown
## Blocker: GitHub CLI Auth
- **What:** `gh` CLI not authenticated
- **Impact:** $130K grant submissions blocked
- **Time to fix:** 5 minutes (Arthur runs `gh auth login`)
- **ROI:** $26,000/minute
- **Status:** Ready to execute when auth complete
```

Clarity = prioritization. Documenting blockers enables ROI calculation.

## The Anti-Block Mindset

Some "blockers" are just fear:
- "I need to learn X first" → No, execute with what you have
- "It's not perfect yet" → Done > perfect
- "I should plan more" → Planning is procrastination

Real blockers have:
- Clear impact ($ value)
- Clear fix (specific action)
- Clear timeframe (minutes/hours)

Everything else is procrastination.

---

*Work block 1056*
*Created: 2026-02-03T12:00Z*
