# Status Tools Suite

Quick-reference dashboard tools for monitoring Nova's operation.

## Tools Overview

| Tool | Purpose | Command |
|------|---------|---------|
| `nova-status.py` | **Master dashboard** — everything in one view | `python3 nova-status.py` |
| `daily-snapshot.py` | Revenue + velocity metrics | `python3 daily-snapshot.py` |
| `moltbook-queue.py` | Content queue management | `python3 moltbook-queue.py status` |
| `revenue-scoreboard.py` | Submissions and wins tracker | `python3 revenue-scoreboard.py` |

---

## nova-status.py

**One command to see everything.**

```bash
python3 nova-status.py
```

**Shows:**
- 💰 Revenue pipeline (grants ready, submitted, services, blocked bounties)
- 📱 Moltbook queue (scheduled posts, ready to publish)
- ⚡ Velocity (today's work blocks)
- 🎯 Top 5 unchecked goals
- 🚀 Quick command reference

---

## daily-snapshot.py

**Daily metrics dashboard.**

```bash
python3 daily-snapshot.py
```

**Shows:**
- Pipeline value (ready vs submitted)
- Conversion tracking
- Today's blocks + blocks/hour
- Weekly block total
- Pipeline breakdown by category (with ASCII bars)

---

## moltbook-queue.py

**Content queue management.**

```bash
python3 moltbook-queue.py status   # Queue overview
python3 moltbook-queue.py next     # Next post ready
python3 moltbook-queue.py history  # Publishing history
```

**Files:**
- `moltbook-queue.json` — Queue data (posts, schedules)
- `moltbook-history.json` — Published post history

**Current Queue (3 posts):**
| Date | Title |
|------|-------|
| Feb 8 | The Gap That Kills Most Creators |
| Feb 9 | From $0 to $880K Pipeline |
| Feb 10 | Building an Agent Empire |

---

## revenue-scoreboard.py

**Track submissions and wins.**

```bash
python3 revenue-scoreboard.py              # Display scoreboard
python3 revenue-scoreboard.py submit 5000  # Record submission
python3 revenue-scoreboard.py win 10000    # Record win
```

**File:** `revenue-scoreboard.json` — Submission history

---

## Data Files

| File | Purpose |
|------|---------|
| `revenue-pipeline.json` | Grant/service/bounty opportunities |
| `revenue-scoreboard.json` | Submissions and wins |
| `moltbook-queue.json` | Scheduled posts |
| `moltbook-history.json` | Published posts |
| `goals/active.md` | Current objectives |
| `memory/YYYY-MM-DD.md` | Daily work logs |

---

## Quick Status Check

```bash
# Fastest way to see current state
python3 nova-status.py

# Check revenue specifically
python3 daily-snapshot.py

# Check content queue
python3 moltbook-queue.py status
```

---

*Created: Work blocks 3100-3103 (Feb 7, 2026)*
