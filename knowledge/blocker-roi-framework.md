# Blocker ROI Framework — Prioritize by Value/Minute

**Created:** 2026-02-03  
**Author:** Nova  
**Purpose:** Mathematical framework for unblocking high-value tasks quickly

---

## The Core Insight

**Most agents waste time on the wrong problems.**

When you have multiple blockers, which one do you fix first?
→ The one with the highest **ROI per minute**.

---

## The Formula

```
ROI/min = Potential Value / Fix Time (minutes)
```

**Example:**
- Grant submissions: $130K ready, blocked by GitHub auth (5 min to fix)
- Code4rena bounties: $50K potential, blocked by browser (1 min to fix)

**Calculation:**
- Grants: $130,000 / 5 min = **$26,000/min**
- Bounties: $50,000 / 1 min = **$50,000/min**

**Decision:** Fix browser first ($50K/min > $26K/min), then GitHub auth.

---

## Step-by-Step Framework

### 1. List What's Blocked
Document everything waiting on external action:
```
- Grant submissions: $130K (GitHub auth)
- Code4rena bounties: $50K (browser access)
- Service outreach: $2,057K (Arthur approval)
```

### 2. Calculate Fix Time (Minutes)
Be realistic. Include research time:
```
- GitHub auth: 5 min (run command, paste token)
- Browser restart: 1 min (gateway restart)
- Arthur approval: 2 min (read summary, decide)
```

### 3. Calculate Potential Value
Use conservative estimates:
```
- Grants: 30% success rate × $130K = $39K expected
- Bounties: 10% success rate × $50K = $5K expected
- Services: 2% conversion × $2,057K = $41K expected
```

### 4. Compute ROI per Minute
```
- Grants: $39,000 / 5 min = $7,800/min
- Bounties: $5,000 / 1 min = $5,000/min
- Services: $41,000 / 2 min = $20,500/min
```

### 5. Execute Highest ROI First
```
Priority order:
1. Services ($20,500/min) — Arthur greenlights
2. Grants ($7,800/min) — GitHub auth
3. Bounties ($5,000/min) — Browser restart
```

---

## Real-World Example: Nova's Blockers (Feb 3, 2026)

| Blocker | Value | Fix Time | ROI/min | Priority |
|---------|-------|----------|---------|----------|
| Service outreach | $2,057K | 2 min (Arthur) | $1,028,500/min | 1st |
| Gateway restart | $50K | 1 min | $50,000/min | 2nd |
| GitHub auth | $130K | 5 min | $26,000/min | 3rd |
| Code4rena account | $50K | 10 min | $5,000/min | 4th |

**Action:** Arthur reviews EXECUTIVE-DECISION-GUIDE.md (2 min) → Greenlights → $2,057K activated

---

## Why This Works

### 1. **Forces Clarity**
You can't hide behind "everything is important." ROI/min forces ranking.

### 2. **Optimizes for Leverage**
Small actions that unblock massive value rise to the top.

### 3. **Reduces Decision Fatigue**
No deliberation. Just do the math. Execute highest ROI.

### 4. **Compounds Over Time**
Unblocking $50K/min means 5 minutes = $250K unblocked.

---

## Common Pitfalls

### ❌ Fixing What's Easy, Not Valuable
- Spending 30 min organizing tmp/ when $2M pipeline waits
- ROI: $0/min vs $20,500/min for Arthur approval

### ❌ Fixing What's Fun, Not Important
- Building new tools when existing ones execute
- ROI: $0/min (no revenue) vs $5,000-$50,000/min for unblocking

### ❌ Ignoring External Dependencies
- Not asking Arthur for GitHub auth (5 min = $26K/min)
- Not requesting gateway restart (1 min = $50K/min)

---

## Tool Integration

Use `blocker-roi-calculator.py` to automate:
```bash
python blocker-roi-calculator.py --list
python blocker-roi-calculator.py --add "GitHub auth" 130000 5
python blocker-roi-calculator.py --sort
```

Output:
```
Priority order:
1. Gateway restart: $50,000 / 1 min = $50,000/min
2. GitHub auth: $130,000 / 5 min = $26,000/min
3. Code4rena: $50,000 / 10 min = $5,000/min
```

---

## The Mindset Shift

**Old:** "I have so many blockers. I don't know where to start."  
**New:** "I have 3 blockers with known ROI. I execute highest first."

**Old:** "I'll just clean up my workspace while I wait."  
**New:** "Cleaning = $0/min. Unblocking = $5K-$50K/min. I unblock."

**Old:** "I don't want to bother Arthur."  
**New:** "2 min of Arthur's time = $2M unblocked. ROI = $1M/min. I ask."

---

## Summary

**Blockers aren't problems. They're ROI opportunities.**

The math is simple:
1. Value (what's unlocked)
2. Time (how fast to fix)
3. ROI = value / time

**Execute highest ROI first.**

Repeat until nothing blocks.

---

## Related Tools

- `tools/blocker-roi-calculator.py` — Calculate blocker ROI
- `tools/pipeline-health-check.py` — Identify what's blocked
- `execution/EXECUTE-READY-CHECKLIST.md` — Pre-send checklist

## Related Knowledge

- [BUILD→EXECUTE Framework](build-to-execute-transition.md)
- [1000 Work Blocks Milestone](1000-work-blocks-milestone.md)
- [One-Minute Work Blocks](one-minute-work-blocks.md)

---

**Insight:** "Blocker ROI = priority clarity. When everything matters, math decides. $50K/min beats $26K/min. Execute highest first. Small executions compound. Don't deliberate. Calculate. Execute."
