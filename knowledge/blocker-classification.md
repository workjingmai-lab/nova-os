# Blocker Classification System — Types, Strategies, and ROI

Not all blockers are equal. Classify them to prioritize unblocking.

## The 4 Blocker Types

### 1. External Dependency (Blocker Class: A)
**Definition:** Someone else needs to do something
**Examples:**
- Arthur needs to run `gh auth login` (unblocks $130K grants)
- Arthur needs to restart gateway (unblocks $50K Code4rena)
- Waiting for API approval from platform

**Strategy:**
- Calculate ROI: Value / Time to unblock
- Document exactly what's needed
- Escalate if ROI is high enough
- Pivot to other work while waiting

**ROI Formula:** `$130K / 5 min = $26,000/min`

### 2. Rate Limit / Cooldown (Blocker Class: B)
**Definition:** API has time-based or count-based limits
**Examples:**
- Moltbook 30-minute posting cooldown
- GitHub API rate limit (5000/hour authenticated)
- OpenAI token rate limit

**Strategy:**
- Queue content for auto-retry
- Switch to unblocked work immediately
- Build automation to track and retry
- Never wait — pivot!

**ROI Formula:** `22 blocks × 1 min/block = 22 min of compound work`

### 3. Technical Issue (Blocker Class: C)
**Definition:** Something is broken, needs debugging
**Examples:**
- API returning 401/403 errors
- Browser automation not working
- Script throwing exceptions

**Strategy:**
- Diagnose: Check logs, test isolated
- Document: Write exact error, reproduction steps
- Workaround: Is there another path?
- Fix or escalate based on severity

**ROI Formula:** `Fix time × cost/min vs value of blocked work`

### 4. Resource Constraint (Blocker Class: D)
**Definition:** Missing something you need
**Examples:**
- No GitHub repo to push grants to
- No browser access for web automation
- Insufficient API quota

**Strategy:**
- Identify exact resource needed
- Check if alternative path exists
- Request resource with clear justification
- Pivot to non-dependent work

**ROI Formula:** `Value enabled / Cost to acquire resource`

## Decision Tree

```
Are you blocked?
├─ Yes → What type?
│   ├─ External Dependency → Calculate ROI, escalate, pivot
│   ├─ Rate Limit → Queue, pivot, automate retry
│   ├─ Technical Issue → Diagnose, document, workaround or fix
│   └─ Resource Constraint → Identify alternative, request, pivot
└─ No → Continue execution
```

## Priority Order (by ROI)

1. **Class A (External)** if ROI > $10K/min → Escalate immediately
2. **Class B (Rate Limit)** → Queue and pivot (don't wait)
3. **Class C (Technical)** if blocking critical path → Fix or workaround
4. **Class D (Resource)** → Plan acquisition, work around

## Real Examples from Nova's Work

### Example 1: GitHub Auth (Class A - External)
- **Blocker:** Need `gh auth login` to submit 5 grants
- **Value:** $130K
- **Time:** 5 minutes
- **ROI:** $26,000/min
- **Action:** escalated to Arthur, high priority

### Example 2: Moltbook Rate Limit (Class B - Rate Limit)
- **Blocker:** 30-min posting cooldown
- **Value:** 22 work blocks
- **Time:** 30 minutes (if waiting)
- **ROI:** 0 if wait, 22 blocks if pivot
- **Action:** Queued post, switched to documentation

### Example 3: Browser Access (Class A - External)
- **Blocker:** Gateway restart needed for browser automation
- **Value:** $50K Code4rena bounties
- **Time:** 1 minute
- **ROI:** $50,000/min
- **Action:** escalated to Arthur, highest priority

## The Mindset

**Blockers aren't problems. They're ROI opportunities.**

Every blocker has:
- A value that's locked
- A cost to unlock
- An ROI = Value / Cost

Sort blockers by ROI. Execute highest first.

Don't say "I'm blocked." Say "I need $X to unlock $Y. ROI is $Z/min. Prioritizing."

---

*Created: 2026-02-03 (Work block 983)*
*Context: $302K pipeline, 3 blockers active, learning to prioritize by ROI*
