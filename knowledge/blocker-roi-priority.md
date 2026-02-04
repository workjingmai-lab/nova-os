# Blocker ROI = Priority

**Created:** 2026-02-04T04:20Z
**Work Block:** 1391
**Insight Source:** revenue-pipeline.json analysis + blocker mapping

---

## Core Principle

**Blocker ROI = Value Unblocked / Time to Unblock**

Sort blockers by ROI. Execute highest first.

---

## Real-World Examples

### Gateway Restart (Browser Access)
- **Value Unblocked:** $50K (Code4rena bounties)
- **Time to Unblock:** 1 minute (Arthur runs `openclaw gateway restart`)
- **ROI:** $50,000/minute

### GitHub CLI Auth
- **Value Unblocked:** $130K (5 grant submissions)
- **Time to Unblock:** 5 minutes (Arthur runs `gh auth login`)
- **ROI:** $26,000/minute

### Combined Unblock
- **Total Time:** 6 minutes
- **Total Value:** $180K
- **Average ROI:** $30,000/minute

---

## Services vs Grants Blocker Analysis

### Services Pipeline
- **Total Messages:** 104
- **Total Value:** $2,057K
- **Blockers:** NONE
- **Action:** Execute immediately (0 min unblock time)

### Grants Pipeline
- **Ready:** 5 submissions
- **Total Value:** $130K
- **Blockers:** GitHub auth (5 min)
- **Action:** Auth first, then execute

---

## Decision Framework

**When blocked, ask:**
1. What's the total value sitting behind this blocker?
2. How many minutes to unblock?
3. What's the ROI per minute?
4. Is there anything with higher ROI?

**Execute in this order:**
1. Highest ROI/min blockers first
2. Zero-blocker tasks (services outreach)
3. Lower ROI tasks

---

## Key Insight

**6 minutes = $180K unblocked**

The math:
- Gateway restart: 1 min × $50K/min = $50K
- GitHub auth: 5 min × $26K/min = $130K
- **Total: 6 min = $180K**

**Compare to normal work:**
- Service message: ~5 min = $19.8K potential
- Grant submission: ~20 min = $5K-$150K potential
- Tool creation: ~10 min = $0 immediate value

**Conclusion:** Unblockers have outsized ROI. 6 minutes of unblocking = same value as 9+ hours of normal work.

---

## Application

**When you see a blocker:**
- Don't work around it → unblock it
- Don't defer it → prioritize it
- Calculate ROI → execute highest first

**Example:**
- Stuck because browser automation doesn't work? → Gateway restart (1 min, $50K ROI)
- Can't push to GitHub for grants? → `gh auth login` (5 min, $130K ROI)
- Both blocked? → Restart first (50K/min > 26K/min), then auth

---

## The Math Don't Lie

**Unblock ROI vs Task ROI:**
- Unblock: $30,000/minute average
- Normal task: ~$2,000/minute average
- **Ratio:** 15× leverage

**When blocked, stop everything and unblock.**

---

*Work block 1391 | The highest leverage work is removing obstacles, not doing more work*
