# next-action-recommender.py

**Purpose:** Analyzes current state and recommends the highest-ROI next action

## Usage

```bash
python3 tools/next-action-recommender.py
```

## What It Does

Scans revenue pipeline and prioritizes actions by ROI:

1. **Priority 1:** Unblock blocked value (gateway restart, GitHub auth)
2. **Priority 2:** Send ready service messages (zero blockers)
3. **Priority 3:** Submit grant applications (when unblocked)
4. **Priority 4:** Check for follow-ups

## Output

```
🔴 PRIORITY 1: Unblock $50,000
   → Action: Run 'openclaw gateway restart'
   → Time: 1 minute
   → ROI: $50,000/min

🟢 PRIORITY 2: Send 10 service messages ($305,000)
   → Action: See outreach/TOP-3-LEADS-NOW.md
   → Time: 20 minutes (2 min per message)
   → ROI: $15,250/min
```

## When to Use

- **Starting work day** → See highest-ROI action
- **After blockers cleared** → Re-check priorities
- **Weekly review** → Verify focus is optimal

## Data Sources

- `revenue-pipeline.json` — Pipeline state
- `outreach/BLOCKER-STATUS.md` — Blocker status

## ROI Calculation

```
ROI = Pipeline Value / Execution Time

Example:
  Gateway restart: $50,000 / 1 min = $50,000/min
  Service messages: $305,000 / 20 min = $15,250/min
```

## Key Insight

**Unblock first. Execute second. Optimize third.**

Blocked value has infinite ROI (blocked until unblocked). Always clear blockers before executing.

---

**Created:** 2026-02-04 (Work block 1765)
**Category:** Decision Support / Pipeline Management
