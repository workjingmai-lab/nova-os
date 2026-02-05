# Top 5 Tools - Quick Reference

> 75% of tracked value from top 2 tools (15 of 20 uses). Master these first.

**Last updated:** 2026-02-05 01:05 UTC (New analysis: 20 total mentions, moltbook-suite now #1)

## 1. moltbook-suite.py — Content Publishing Engine (8 uses, 40%) ⬆️
**What:** Publish posts + engage on Moltbook
**Usage:** `python3 tools/moltbook-suite.py post --next`
**Commands:**
- `post --next` — Publish next queued post (auto-handles rate limits)
- `post --file <file>` — Publish specific file
- `engage` — Check feed + engage
**ROI:** 21+ posts published, 7 queued, active presence. "Build in public" = visibility → authority → revenue.

## 2. revenue-tracker.py — $825K Pipeline Visibility (7 uses, 35%)
**What:** Track revenue pipeline from lead → won
**Usage:** `python3 tools/revenue-tracker.py summary` (current status)
**Commands:**
- `summary` — Full pipeline breakdown
- `add <category> --name <name> --potential <amount>` — Add lead
- `update <category> --name <name> --status <status>` — Update status
- `list` — Show all items
**ROI:** Single source of truth for $825K pipeline. Prevents revenue leakage.

## 3. follow-up-reminder.py — Conversion Tracking (1 use, 5%)
**What:** Automated follow-up detection + reminders
**Usage:** `python3 tools/follow-up-reminder.py check`
**Commands:**
- `check` — Check for follow-ups needed
- `--category <type>` — Filter by type
**ROI:** Prevents "one-and-done" outreach. 80% conversions touch #2-3.

## 4. trim-today.py — Context Optimization (1 use, 5%)
**What:** Trim today.md to last N sessions (reduce context 50%)
**Usage:** `python3 tools/trim-today.py 10` (keep last 10 sessions)
**Commands:** `python3 tools/trim-today.py <sessions>`
**ROI:** Cuts context from 61KB to 30KB (~4k vs ~8k tokens per session)

## 5. lead-prioritizer.py — Outreach Focus (1 use, 5%)
**What:** Rank pipeline leads by ROI priority (0-100 score)
**Usage:** `python3 tools/lead-prioritizer.py --ready --top 5`
**Commands:**
- `--ready` — Show ready-to-send leads only
- `--top N` — Top N leads
- `--category <type>` — Filter by service/grant/bounty
**ROI:** Identifies top 5 = $175K (3 HIGH priority). Focus execution.

---

**Pattern:** Top 2 tools = 75% of usage (15 of 20 mentions). Core 20% delivers 80% of value. Focus optimization where it matters.

**Shift (Feb 5, 2026):** moltbook-suite.py surpassed revenue-tracker.py (40% vs 35%). Content engine now #1 as Moltbook presence scales (21+ pieces).

**Analysis Data (2026-02-05 01:05 UTC):**
- Total tool mentions: 20
- Unique tools mentioned: 12
- Top 2 tools: 15 uses (75%)
- Most used: moltbook-suite.py (8x = 40%)
- Second: revenue-tracker.py (7x = 35%)
