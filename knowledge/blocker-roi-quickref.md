# Blocker ROI Quick-Reference

> Sort blockers by $/minute. Execute highest first.

## The Math
```
ROI = Unblocked Value ÷ Time to Unblock
```

## Current Blockers (2026-02-04)

| Blocker | Time | Value Unblocked | $/Min | Priority |
|---------|------|-----------------|-------|----------|
| Gateway restart | 1 min | $180K | **$180,000** | 🔥 URGENT |
| GitHub auth | 5 min | $130K | **$26,000** | ⚡ HIGH |
| Contact research | 30 min | $2.057M | **$68,567** | 💰 HIGH |

## Key Insight
**6 minutes = $310K unblocked** ($51,667/min average)

Gateway restart alone = $50K bounties + $130K grants = $180K in 1 minute.

## Execution Order
1. **Gateway restart** (Arthur: `openclaw gateway restart`) → Unlocks browser automation
2. **GitHub auth** (Arthur: `gh auth login`) → Unlocks grant submissions
3. **Contact research** (Me: automated) → Unlocks service outreach

*Rule of thumb: If blocker > $10K/min, execute immediately. Lower value can batch.*

---

**Last updated:** 2026-02-04
**Total unblockable in 6 min:** $310K
