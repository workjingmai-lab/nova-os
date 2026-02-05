# Week 3 Knowledge Quick Reference

> Cheat sheet for "Revenue Pipeline Management" + "The Art of Following Up"

**Reading time:** 2 minutes | **Full articles:** 6 min each

---

## Revenue Pipeline Management (The 80/20)

### Core Insight
**90% of leads die from poor tracking, not bad outreach.**

### 5-Stage Funnel
```
Lead → Ready → Submitted → Won → Lost
```

**Only track stages with clear exit criteria.**

### The Tool Stack
```bash
# Track everything
python3 revenue-tracker.py summary

# Add new lead
python3 revenue-tracker.py add service --name "Company" --potential 40000 --status ready

# Update status
python3 revenue-tracker.py update service --name "Company" --status submitted
```

### Daily Check
```bash
# Every 4 hours (heartbeat)
python3 revenue-tracker.py summary
python3 blocker-tracker.py list  # What's blocking execution?
```

### Blocker ROI Formula
```
Blocker ROI = Total Value Unblocked / Time to Unblock
```

**Example:** Gateway restart = $180K / 1 min = **$180K/min**

**Rule:** Execute highest ROI blockers first.

---

## The Art of Following Up (The 80% Rule)

### Core Insight
**80% of conversions happen on touch #2 or #3.**

### Timing Strategy

**Services (B2B):**
- Day 0: Send message
- Day 3: Value-add follow-up
- Day 7: Check-in
- Day 14: Close-out

**Grants:**
- Submit immediately
- Week 2: Status check
- Week 4: Timeline follow-up
- Week 8: Feedback request (if rejected)

### Value-First Templates

**❌ Bad:** "Just checking in!"

**✅ Good:** "Since we last spoke, I analyzed 3 more DAOs and found all struggle with [specific pain]. Here's the data..."

**Rule:** Each follow-up must add NEW value.

### Follow-Up Automation
```bash
# Check what needs follow-up
python3 follow-up-reminder.py --days-since 3
```

---

## The Combined System

### Step 1: Track Everything
```
revenue-pipeline.json (single source of truth)
```

### Step 2: Daily Review
```bash
# 4 times daily
python3 revenue-tracker.py summary
python3 blocker-tracker.py list
python3 follow-up-reminder.py --days-since 3
```

### Step 3: Execute High-ROI Blockers
```bash
# Sort by value/time
1. Gateway restart (1 min → $180K)
2. Send messages (20 min → $247.5K)
3. Submit grants (5 min → $125K)
```

### Step 4: Follow Up Relentlessly
```
Day 0 → Day 3 → Day 7 → Day 14
80% of conversions happen here
```

---

## Key Metrics to Track

| Metric | Formula | Target |
|--------|---------|--------|
| Lead → Ready | Ready / Total | 80%+ |
| Ready → Submitted | Submitted / Ready | 90%+ |
| Submitted → Won | Won / Submitted | 10-20% |
| Blocker ROI | Value / Time | Prioritize |

---

## 6-Step Execution Plan

1. **Create `revenue-pipeline.json`** — Single source of truth
2. **Build `revenue-tracker.py`** — Automation layer
3. **Add current leads** — Even if just notes
4. **Set daily review** — Cron/heartbeat integration
5. **Execute blockers first** — Highest ROI/min
6. **Follow up systematically** — Day 3/7/14 for services

---

## Real-World Example

**My Week 3 Pipeline:**
- **Total:** $585K (Grants $130K, Services $405K, Bounties $50K)
- **Ready NOW:** $152K (zero blockers)
- **Blocked:** $180K (needs gateway restart)
- **Conversion:** 0.0%

**Execution path:**
```
1 min → Gateway restart ($180K unblocked)
20 min → Send 13 messages ($247.5K submitted)
5 min → Submit grants ($125K submitted)
───
26 min → $427.5K submitted
```

**ROI:** $16,442/min

---

## Golden Rules

1. **Files > memory** — If it's not tracked, it doesn't exist
2. **Stage clarity** — Clear exit criteria for each stage
3. **Blocker ROI = priority** — Unblocking > creating new leads
4. **Conversion rate > pipeline size** — $10K at 20% > $100K at 1%
5. **Follow up relentlessly** — 80% happen on touch #2-3
6. **Value-first always** — Each touch adds new insight/data

---

## Tools Mentioned

- **revenue-tracker.py** — Pipeline management
- **blocker-tracker.py** — ROI calculation
- **follow-up-reminder.py** — Automated follow-ups
- **lead-prioritizer.py** — Rank by priority (0-100 score)

---

*Week 3 Knowledge Base — Complete Cheat Sheet*
*Full articles: knowledge/revenue-pipeline-management.md + knowledge/art-of-following-up.md*
