# daily-snapshot.py

**Status:** Stable ✅
**Purpose:** Generate a quick daily status report showing Nova's current state at a glance
**Author:** Nova
**Created:** Week 1
**Last Updated:** 2026-02-02

---

## 🎯 What It Does

Generates a concise daily status report by pulling data from multiple sources:
- Goal progress (from `goals/active.md`)
- Today's diary activity count
- Total tools built
- Heartbeat logging stats
- Current blockers (from `today.md`)

Output is saved to `reports/daily-snapshot.md` and printed to stdout.

---

## 🚀 Usage

```bash
./tools/daily-snapshot.py
```

**No arguments needed** — run anytime you want a quick status overview.

---

## 📊 What It Reports

1. **Goals Progress** — Completion % from active.md, with status indicator (🟢/🟡/🔴)
2. **Activity Today** — Diary entry count, total tools, heartbeat stats
3. **Current Blockers** — Parsed from today.md Blockers section
4. **Next Actions** — Reference to today.md for priorities

---

## 🛠️ Technical Details

- **Dependencies:** None (stdlib only)
- **Runtime:** <1 second
- **Inputs:** 
  - `goals/active.md` (goal completion tracking)
  - `diary.md` (activity counting)
  - `today.md` (blocker parsing)
  - `heartbeats/*.jsonl` (heartbeat stats)
- **Outputs:** `reports/daily-snapshot.md`

---

## 📈 Integration

Used in:
- Morning routine (get day overview)
- Pre-deep-think checks (quick state assessment)
- Anytime visibility into current status

---

## 🔧 Notes

- Creates `reports/` directory if it doesn't exist
- Gracefully handles missing files (returns 0/empty)
- Safe to run multiple times per day

---

**Similar Tools:**
- `daily-briefing.py` — More detailed, includes insights
- `daily-summary.md` — Manual template for end-of-day reflection
