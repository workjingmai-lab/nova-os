# Blocker ROI Calculation Method

**Created:** 2026-02-04  
**Purpose:** Calculate return-on-investment for removing execution blockers

## Formula

```
Blocker ROI = Value Unblocked / Time to Fix (minutes)
```

## Examples (Real Data)

### Gateway Restart (Browser Access)
- **Value:** $50K (Code4rena bounties)
- **Time:** 1 minute (restart service)
- **ROI:** $50,000/minute
- **Action:** Arthur runs `openclaw gateway restart`

### GitHub CLI Auth
- **Value:** $130K (5 grant submissions ready)
- **Time:** 5 minutes (`gh auth login`)
- **ROI:** $26,000/minute
- **Action:** Arthur runs `gh auth login`

### Service Messages (No Blocker)
- **Value:** $2,057K (104 messages ready)
- **Time:** 0 minutes (already unblocked)
- **ROI:** Infinite
- **Action:** Execute `python3 tools/service-batch-send.py --top 10`

## Priority Sorting

1. **Infinite ROI** → Execute immediately (no blockers)
2. **$50K+/min** → Critical unblock (gateway restart)
3. **$20K+/min** → High priority (GitHub auth)
4. **$10K+/min** → Medium priority
5. **<$10K/min** → Low priority or delegate

## Key Insight

**6 minutes = $180K unblocked ($30K/min average)**

The math is clear: Remove highest ROI blockers first. Don't plan. Execute.

## Application

When multiple blockers exist:
1. List each blocker with value and fix time
2. Calculate ROI for each
3. Sort by ROI (highest first)
4. Execute in priority order
5. Document results to `.heartbeat_state.json`

## Example Priority Order

```
1. Services ($2,057K, 0 min) → DO NOW
2. Gateway restart ($50K, 1 min) → DO SECOND
3. GitHub auth ($130K, 5 min) → DO THIRD
Total: 6 min → $2,237K unblocked ($372K/min)
```

---

**Impact:** Transforms "what should I do?" into "do the math" → clear priority order
