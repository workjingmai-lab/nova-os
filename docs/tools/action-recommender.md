# Action Recommender — Highest-Impact Next Action

Recommends the single best next action based on revenue pipeline state. Uses blocker status, follow-up timing, and readiness to prioritize by ROI.

## What It Does

Analyzes your entire revenue pipeline and recommends the highest-impact action by scoring:
- **Services ready NOW** (zero blockers) → 100 points
- **Services submitted** with follow-up due → 80 points
- **Grants ready** (blocked by GitHub) → 60 points
- **Bounties ready** (blocked by browser) → 40 points
- **Follow-ups due** → 30 points
- **Leads needing messages** → 20 points

Bonuses: +10 for HIGH priority, +5 for value >$50K, +10 for value >$100K.

## Usage

```bash
# Show top recommendation
python3 tools/action-recommender.py

# Show top 5 recommendations
python3 tools/action-recommender.py --top 5

# Filter by category
python3 tools/action-recommender.py --category services
python3 tools/action-recommender.py --category grants
python3 tools/action-recommender.py --category bounties
```

## Output Example

```
============================================================
🎯 ACTION RECOMMENDATIONS
============================================================
Generated: 2026-02-06 19:42:55 UTC

============================================================
#1 — Quick Automation
============================================================
  Category: SERVICES  |  Priority: 🟡 MEDIUM  |  Status: ✅ ready
  Value: $2,000
  Score: 100/100

  🎯 ACTION: SEND message
  📋 WHY: Ready NOW, zero blockers
  📝 Notes: 25 leads, 21 messages ready in outreach/ (4 templates: quick, setup, multi-agent, audit), awaiting A...

============================================================
Showing 1 recommendation(s)
============================================================
```

## Scoring Logic

| Category | Status | Base Score | Action |
|----------|--------|------------|--------|
| Services | ready | 100 | SEND message |
| Services | submitted (follow-up due) | 80 | FOLLOW-UP |
| Grants | ready_to_submit | 60 | SUBMIT (blocked) |
| Bounties | ready | 40 | START audit (blocked) |
| Any | follow-up due | 30 | FOLLOW-UP |
| Leads | ready | 20 | WRITE message |

**Bonuses:**
- HIGH priority: +10
- Value >$50K: +5
- Value >$100K: +10
- LOW priority: -5

## When to Use

- **Daily standup:** What should I focus on today?
- **Between sessions:** Quick check of highest-impact action
- **After blockers cleared:** Re-run to see new recommendations
- **Pipeline overwhelm:** When you have 50+ items and don't know where to start

## Data Source

Reads from `data/revenue-pipeline.json` with structure:
```json
{
  "services": [
    {
      "name": "Project Name",
      "status": "ready",
      "priority": "HIGH",
      "potential": 25000,
      "notes": "Message ready at outreach/messages/...",
      "last_contact": "2026-02-01T10:00:00Z"
    }
  ],
  "grants": [...],
  "bounties": [...],
  "leads": [...]
}
```

## ROI Math

**Why this matters:**
- Services ready NOW = 100 score = execute immediately
- 25 ready services @ $2K avg = $50K potential
- 1 minute to identify top action vs 10 minutes guessing = 9 minutes saved

**Priority hierarchy:**
1. **Execute first:** Services with zero blockers (money waiting to be claimed)
2. **Follow-up second:** Warm leads > cold outreach
3. **Submit third:** Grants ready (waiting on Arthur for GitHub auth)
4. **Start fourth:** Bounties (waiting on Arthur for browser access)

## Related Tools

- `revenue-tracker.py` — Update pipeline data
- `follow-up-tracker.py` — Track follow-up schedule
- `lead-prioritizer.py` — Rank leads by value/priority

## Created

2026-02-06 — Week 3, decision-making optimization for revenue pipeline
