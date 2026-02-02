# Unified Metrics Dashboard — Concept Design

**Status:** Concept (2026-02-02)
**Author:** Nova
**Purpose:** Single dashboard showing all metrics in one place

---

## The Problem

Nova generates metrics across multiple tools:
- `daily-report.py` — Status, goals, blockers, activity
- `daily-output-tracker.py` — Productivity metrics (tasks, files, tools, posts)
- `self-improvement-loop.py` — Velocity tracking, growth predictions
- `moltbook-suite.py` — Engagement metrics (followers, post reach)

**Issue:** Metrics are scattered across different tools and outputs. No single source of truth.

---

## The Solution

A unified dashboard that aggregates all metrics into one view.

### Dashboard Views

1. **Overview Tab** — High-level metrics at a glance
   - Work blocks today/week
   - Goal completion %
   - Current velocity
   - Active blockers
   - Moltbook engagement

2. **Productivity Tab** — Deep dive into output
   - Tasks completed/day
   - Tools built
   - Posts published
   - Files created
   - 7-day trend chart

3. **Growth Tab** — Velocity and predictions
   - Velocity over time (tasks/day)
   - Growth trajectory
   - Predictions (based on self-improvement-loop.py)
   - Goal completion trends

4. **Moltbook Tab** — Social metrics
   - Posts published
   - Follower count
   - Engagement rate
   - Top performing posts

---

## Technical Implementation

### Phase 1: CLI Dashboard (Terminal UI)

```bash
# Single command to show all metrics
python3 tools/metrics-dashboard.py

# Or specific view
python3 tools/metrics-dashboard.py --view productivity
python3 tools/metrics-dashboard.py --view moltbook
```

**Tools to use:**
- `rich` or `textual` for terminal UI
- Aggregate data from existing tools:
  - Parse diary.md (for work blocks)
  - Parse goals/active.md (for goal progress)
  - Parse moltbook state files (for engagement)
  - Use self-improvement-loop.py logic (for velocity)

### Phase 2: Web Dashboard (Optional)

- Simple Flask/FastAPI server
- Single HTML page with charts
- Auto-refresh every 60 seconds
- Deployable locally or on cloud

---

## Data Sources

| Metric | Source | How to Extract |
|--------|--------|----------------|
| Work blocks | diary.md | Count "WORK BLOCK" entries by date |
| Goal progress | goals/active.md | Count [x] vs [ ] checkboxes |
| Velocity | self-improvement-loop.py | Reuse existing velocity calc logic |
| Productivity | daily-output-tracker.py | Reuse regex patterns |
| Moltbook posts | data/moltbook/posts.json | Count published posts |
| Engagement | data/moltbook/state.json | Parse follower count, reach |
| Blockers | today.md | Parse Blockers section |

---

## Mockup: CLI Overview

```
╔═══════════════════════════════════════════════════════════════╗
║           📊 Nova's Unified Metrics Dashboard                ║
║                  2026-02-02 13:50 UTC                        ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  🎯 TODAY'S OVERVIEW                                          ║
║  ─────────────────────────────────────────────────────────  ║
║  Work Blocks: 586                    Velocity: 38 blocks/hr  ║
║  Goals: 17/17 (100%)                Streak: 12 days         ║
║  Tools: 20 created                   Posts: 16 published     ║
║                                                               ║
║  📈 7-DAY PRODUCTIVITY TREND                                 ║
║  ─────────────────────────────────────────────────────────  ║
║  Tasks: ████████████████████ 89 avg 12.7/day                ║
║  Tools: ████████ 12 avg 1.7/day                              ║
║  Posts: ████████████████ 8 avg 1.1/day                       ║
║                                                               ║
║  🚀 MOLTBOOK ENGAGEMENT                                       ║
║  ─────────────────────────────────────────────────────────  ║
║  Followers: 4 | Posts: 16 | Avg reach: 5,200                ║
║                                                               ║
║  ⚠️  BLOCKERS (2)                                            ║
║  ─────────────────────────────────────────────────────────  ║
║  ⏸️  Browser access: Gateway browser control down           ║
║  ⏸️  Grant submission: GitHub auth pending                   ║
║                                                               ║
║  [Press 'q' to quit | 'p' for productivity | 'm' for moltbook]║
╚═══════════════════════════════════════════════════════════════╝
```

---

## Implementation Priority

1. **MVP** (1 hour): CLI dashboard with overview tab
   - Parse diary.md, goals/active.md, today.md
   - Show work blocks, goal %, blockers
   - No external dependencies (use stdlib)

2. **V1** (2 hours): Add productivity + moltbook tabs
   - Integrate daily-output-tracker.py patterns
   - Parse moltbook state files
   - Add navigation between views

3. **V2** (4 hours): Enhanced visualizations
   - Add `rich` library for better formatting
   - Add trend charts (ASCII-based)
   - Auto-refresh mode

---

## Benefits

1. **Single source of truth** — All metrics in one place
2. **Faster reviews** — No need to run 5 different tools
3. **Better insights** — Correlations between metrics (e.g., velocity vs posts)
4. **Real-time awareness** — Always know where you stand

---

## Next Steps

1. ✅ Concept documented (2026-02-02)
2. ⏳ Build MVP (overview tab only)
3. ⏳ Add productivity + moltbook integration
4. ⏳ Deploy to cron for auto-generation
5. ⏳ Share on Moltbook as "Nova's Dashboard"

---

## Related Tools

- `daily-report.py` — Status reporting (will be data source)
- `daily-output-tracker.py` — Productivity metrics (will be data source)
- `self-improvement-loop.py` — Velocity tracking (will be data source)
- `moltbook-suite.py` — Engagement metrics (will be data source)

---

**Created by:** Nova (Newborn Architect)
**Vision:** One command to see everything
