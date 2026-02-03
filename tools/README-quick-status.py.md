# quick-status.py — Instant Health Snapshot

## What It Does

Provides a one-line command to see Nova's complete status:
- Work blocks (today, this session, week)
- Revenue pipeline ($ tracked, ready to submit)
- Current blockers (GitHub auth, browser access)
- Next actions (prioritized by ROI)
- Activity status (active/recent/stale)

**Perfect for:**
- Heartbeat checks
- Quick status reviews
- Debugging agent state
- Reporting to Arthur

## Usage

```bash
python3 tools/quick-status.py
```

**Output:**
```
==================================================
 📊 NOVA STATUS — Quick Snapshot
==================================================

🔥 Work Blocks:
   Today:    244 blocks (+113 this session)
   Week 2:   632 blocks
   Streak:   Alive

💰 Revenue Pipeline:
   Total:    $300,000
   Ready:    $212,000
   Items:    5 grants, 14 services, 1 bounties

⏱️  Activity:
   Status:   🟢 Active (0m ago)

⚠️  Blockers:
   📝 GitHub auth (grants) — Arthur action needed
   🌐 Browser access (Code4rena) — Gateway restart needed

➡️  Next Actions:
   1. Execute grant submissions ($130K) — awaiting GitHub auth
   2. Send service proposals ($82K) — outreach ready
   3. Code4rena onboarding — awaiting browser access

==================================================
```

## Data Sources

**Reads from:**
- `today.md` — Work block counts and streak
- `data/revenue-pipeline.json` — Pipeline value and status
- `diary.md` — Last activity timestamp

**Calculates:**
- Activity status (green < 15min, yellow < 2h, red > 2h)
- Pipeline totals (grants + services + bounties)
- Ready-to-submit value (status="ready")

## Integration

**Heartbeat example:**
```yaml
- name: "Nova Status Check"
  every: "1h"
  message: |
    python3 tools/quick-status.py
```

**Cron example:**
```bash
# Every hour, log status to diary
0 * * * * cd /home/node/.openclaw/workspace && python3 tools/quick-status.py >> diary.md
```

## Error Handling

- Missing files → Shows "Unknown" for that section
- Parse errors → Returns safe defaults (0 values)
- Never crashes → Always shows partial status

## Why This Matters

**Before quick-status.py:**
- Had to read multiple files to understand state
- No single source of truth for current status
- Debugging agent health required manual investigation

**After quick-status.py:**
- One command shows everything
- Heartbeats are more informative
- Arthur can check status instantly
- Faster debugging when things go wrong

**Principle:** Visibility = Control. Can't fix what you can't see.

## Related Tools

- `revenue-tracker.py` — Detailed pipeline management
- `goal-tracker.py` — Task and project tracking
- `self-improvement-loop.py` — Performance analysis
- `moltbook-suite.py status` — Moltbook-specific metrics

## Version History

- **2026-02-03:** Initial creation — work blocks, pipeline, blockers, next actions
- Fixed field name bug (`potential_value` → `potential`)
- Tested with real data ($300K pipeline, 632 blocks)

---

**Created by:** Nova — 632 work blocks and counting
**Purpose:** Instant situational awareness for autonomous agents
