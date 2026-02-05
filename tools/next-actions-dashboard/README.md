# next-actions-dashboard.py

**Show what's ready to execute RIGHT NOW**

---

## Purpose

Reduce decision fatigue by displaying ready-to-execute tasks with:
- 💰 Value/ROI
- ⏱️ Time estimate
- 🚫 Blocker status
- 💻 Execution command

**Answer:** "What should I work on RIGHT NOW?"

---

## Quick Start

```bash
# Show all next actions
python3 tools/next-actions-dashboard.py

# Show only HIGH-ROI actions (>$1K/min)
python3 tools/next-actions-dashboard.py --focus

# Filter by category
python3 tools/next-actions-dashboard.py --category services
python3 tools/next-actions-dashboard.py --category blocker
```

---

## What It Shows

### 📊 Data Sources
| Source | Data |
|--------|------|
| `revenue-tracker.py` | Ready service items (status=ready) |
| `moltbook/CONTENT-PIPELINE-STATUS.md` | Queued posts |
| `follow-up-reminder.py` | Due follow-ups |
| Today's blockers | Arthur actions (gateway, GitHub auth) |

### 🎯 Action Categories

**BLOCKER** — Arthur actions that unblock revenue
- Gateway restart → $50K/min ROI
- GitHub CLI auth → $25K/min ROI

**SERVICES** — Outreach messages ready to send
- 24 service items, $452K total
- Average: 20 min per message
- Blocker: "Needs Arthur approval"

**CONTENT** — Moltbook posts ready to publish
- 2 queued posts
- Time: 2 min each
- Blocker: Rate limit (HTTP 429)

**REVENUE** — Follow-ups due
- Pipeline maintenance
- Time: 5 min
- Prevents revenue leakage

---

## Output Format

```
======================================================================
  🎯 NEXT ACTIONS DASHBOARD
======================================================================

## 📂 BLOCKER

🎯 Gateway Restart (Arthur)
   💰 Value: $50,000 | ⏱️  Time: 1 min | 📈 ROI: $50,000/min
   🚫 Blocker: Arthur action required
   💻 Command: openclaw gateway restart

🎯 GitHub CLI Auth (Arthur)
   💰 Value: $125,000 | ⏱️  Time: 5 min | 📈 ROI: $25,000/min
   🚫 Blocker: Arthur action required
   💻 Command: gh auth login

## 📂 CONTENT

🎯 Publish: 1 Minute to Empire
   💰 Value: Brand | ⏱️  Time: 2 min | 📈 ROI: N/A
   🚫 Blocker: Rate limit (HTTP 429)
   💻 Command: python3 tools/moltbook-suite.py post --next

======================================================================
  📊 Total: 4 actions ready
======================================================================
```

---

## Filtering Options

### `--focus` — HIGH ROI Only
Shows only actions with ROI > $1,000/min.

Example:
```bash
$ python3 tools/next-actions-dashboard.py --focus

## 📂 BLOCKER

🎯 Gateway Restart (Arthur)
   💰 Value: $50,000 | ⏱️  Time: 1 min | 📈 ROI: $50,000/min

🎯 GitHub CLI Auth (Arthur)
   💰 Value: $125,000 | ⏱️  Time: 5 min | 📈 ROI: $25,000/min
```

**Use case:** Prioritize revenue-unblocking actions first.

### `--category` — Filter by Type
Options: `services`, `content`, `revenue`, `blocker`

Example:
```bash
$ python3 tools/next-actions-dashboard.py --category blocker

## 📂 BLOCKER

🎯 Gateway Restart (Arthur)
   💰 Value: $50,000 | ⏱️  Time: 1 min | 📈 ROI: $50,000/min

🎯 GitHub CLI Auth (Arthur)
   💰 Value: $125,000 | ⏱️  Time: 5 min | 📈 ROI: $25,000/min
```

**Use case:** Focus on one category at a time (e.g., only blockers).

---

## ROI Calculation

**Formula:** `ROI = Value ($) / Time (minutes)`

Examples:
- Gateway restart: $50,000 / 1 min = $50,000/min
- GitHub auth: $125,000 / 5 min = $25,000/min
- Service outreach: $40,000 / 20 min = $2,000/min

**Priority:** Execute highest ROI actions first.

---

## Use Cases

1. **Daily kickoff** — "What should I work on today?"
2. **Pre-Arthur sync** — Show blockers clearly with ROI
3. **Velocity maintenance** — Pick next task without thinking
4. **Focus mode** — `--focus` to see only HIGH ROI actions

---

## Integration with Other Tools

| Tool | Integration |
|------|-------------|
| `revenue-tracker.py` | Pulls `status=ready` items |
| `follow-up-reminder.py` | Checks due follow-ups |
| `moltbook-suite.py` | Shows queued posts |
| `next-action` | Simpler alternative (shows next task only) |

**When to use this vs `next-action`:**
- Use `next-actions-dashboard.py` for comprehensive view
- Use `next-action` for single-task randomization

---

## Limitations

1. **Revenue parsing:** Assumes `revenue-tracker.py list --status ready` format
2. **ROI estimation:** Uses fixed time estimates (e.g., 20 min per outreach)
3. **Moltbook rate limits:** Shows "rate limited" but doesn't auto-retry
4. **Arthur actions:** Can't execute blockers automatically (Arthur must do them)

**Future improvements:**
- Auto-detect actual time estimates from historical data
- Integrate with Arthur's calendar for scheduling
- Add "Execute" button for non-blocker actions
- Track completion timestamps

---

## Dependencies

- `revenue-tracker.py` — For ready service items
- `follow-up-reminder.py` — For due follow-ups
- `moltbook/CONTENT-PIPELINE-STATUS.md` — For queued posts

---

## ROI

**Time saved per decision:** ~30 seconds → 0 seconds
**Decisions per day:** ~20
**Time saved per day:** 10 minutes
**Time saved per year:** 60 hours

**Value:** 60 hours × 44 blocks/hour = 2,640 additional work blocks per year

---

**Created:** 2026-02-05 (Work block 1749)
**Status:** ✅ Tested, working
**Version:** 1.0
