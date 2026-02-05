# action-recommender.py — Action Recommendation Engine

**Purpose:** Suggest the highest-impact next action based on current revenue pipeline state.

**Problem solved:** Eliminates decision fatigue by automatically prioritizing actions by ROI. No more "what should I do next?" — the pipeline data tells you exactly what to execute.

**Created:** 2026-02-04 (Work block 1745)

---

## How It Works

The tool analyzes the `data/revenue-pipeline.json` file and scores each item based on:
- **Category** (services, grants, bounties, leads)
- **Status** (ready, submitted, lead, etc.)
- **Timing** (follow-up due dates)
- **Priority** (HIGH, MEDIUM, LOW)
- **Value** (potential revenue)

**Scoring system:**
1. **Services ready NOW** → 100 points (zero blockers, can execute immediately)
2. **Services submitted + follow-up due** → 80 points (conversion is in follow-ups)
3. **Grants ready_to_submit** → 60 points (blocked by GitHub auth)
4. **Bounties ready** → 40 points (blocked by browser access)
5. **Leads** → 20 points (need outreach message first)

**Bonuses:**
- +10 points for HIGH priority
- +5 points for value ≥ $50K
- -5 points for LOW priority

---

## Quick Start

### Show the #1 recommended action
```bash
python3 tools/action-recommender.py
```

### Show top 5 recommendations
```bash
python3 tools/action-recommender.py --top 5
```

### Filter by category
```bash
python3 tools/action-recommender.py --category services
python3 tools/action-recommender.py --category grants
python3 tools/action-recommender.py --category bounties
```

### Show only grants (top 3)
```bash
python3 tools/action-recommender.py --category grants --top 3
```

---

## Output Example

```
============================================================
🎯 ACTION RECOMMENDATIONS
============================================================
Generated: 2026-02-04 23:29:16 UTC

============================================================
#1 — Quick Automation
============================================================
  Category: SERVICES  |  Priority: 🟡 MEDIUM  |  Status: ✅ ready
  Value: $2,000
  Score: 100/100

  🎯 ACTION: SEND message
  📋 WHY: Ready NOW, zero blockers
  📝 Notes: 25 leads, 21 messages ready in outreach/...

============================================================
#2 — Ethereum Foundation
============================================================
  Category: SERVICES  |  Priority: 🔴 HIGH  |  Status: ✅ ready
  Value: $40,000
  Score: 110/100

  🎯 ACTION: SEND message
  📋 WHY: Ready NOW, zero blockers
  📝 Notes: HIGH priority, $40K potential...

============================================================
Showing 2 recommendation(s)
============================================================
```

---

## Integration with Cron

Add to HEARTBEAT.md for automated action suggestions during periodic checks:

```yaml
- name: "Action Recommender"
  every: "2h"
  message: |
    Run action-recommender.py --top 3
    Report top recommendations if any HIGH priority items appear
```

---

## Data Sources

- **Pipeline data:** `data/revenue-pipeline.json` (updated by revenue-tracker.py)
- **Follow-up schedule:** Day 0/3/7/14/21 (configurable in tool)
- **Priority levels:** HIGH, MEDIUM, LOW

---

## ROI Math

**Time saved:** No more browsing spreadsheets or guessing what to do next.
**Impact:** Always working on the highest-ROI action available.

Example:
- 39 service messages ready → $332K pipeline
- action-recommender.py instantly tells you which to send first
- HIGH priority + highest value = top recommendation

---

## Dependencies

- `data/revenue-pipeline.json` (must exist, updated by revenue-tracker.py)
- Python 3.x (standard library only, no external deps)

---

## Maintenance

**Updates needed:** If pipeline data structure changes, update `load_pipeline()` and `calculate_action_score()`.

**Scoring tuning:** Adjust score values in `calculate_action_score()` if priorities change (e.g., if bounties become higher priority than grants).

---

## Related Tools

- `revenue-tracker.py` — Manages pipeline data
- `follow-up-reminder.py` — Tracks follow-up timing
- `lead-prioritizer.py` — Prioritizes leads by value/priority

---

**Tool count:** 162 (active)

**Last updated:** 2026-02-04
