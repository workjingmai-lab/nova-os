# contest-tracker.py — Audit Contest Manager

**Purpose:** Track, prioritize, and manage Code4rena audit competitions.

**Created:** 2026-02-02
**Category:** Revenue generation / Audit contests
**Usage:** Medium — Used for Code4rena onboarding

---

## What It Does

Tracks audit contests with:
- Active contests (currently accepting submissions)
- Upcoming contests (scheduled)
- Historical contests (completed)
- Opportunity scoring (prize/difficulty/tech stack)
- Prize pool aggregation

**Opportunity scoring** prioritizes contests by:
- Prize pool size
- Difficulty (easy > medium > hard for quick wins)
- Tech stack familiarity (Solidity/EVM/Rust)

---

## Installation

No dependencies. Uses Python stdlib.

```bash
chmod +x contest-tracker.py
```

---

## Usage

```bash
# Run dashboard (shows active + upcoming contests)
python3 contest-tracker.py

# Example output:
# ============================================================
# 🛡️  CODE4RENA CONTEST TRACKER
# ============================================================
#
# 🔥 ACTIVE (1)
#   • Olas: $62,000 | Ends: 2026-02-09
#
# 📅 UPCOMING (1)
#   • Jupiter Lend: $107,000 | Score: 75,600 | Starts: 2026-02-04
#
# 📊 STATS
#   Total Prize Pool Available: $169,000
#   Contests Tracked: 2
```

---

## Data Structure

Contests stored in `contests.json`:

```json
{
  "active": [
    {
      "id": "code4rena-olas",
      "name": "Olas",
      "platform": "Code4rena",
      "prize_pool_usd": 62000,
      "start_date": "2026-01-22T20:00:00Z",
      "end_date": "2026-02-09T20:00:00Z",
      "tech_stack": ["solidity", "evm"],
      "difficulty": "medium",
      "url": "https://code4rena.com/audits/...",
      "status": "active",
      "registered": false,
      "submitted": false,
      "findings": [],
      "reward_usd": 0
    }
  ],
  "upcoming": [...],
  "history": [...]
}
```

---

## Opportunity Scoring

**Formula:** `prize × difficulty_mult × (1 + tech_bonus)`

**Difficulty multipliers:**
- Easy: 1.2× (quick wins)
- Medium: 1.0× (baseline)
- Hard: 0.7× (high effort, lower odds)

**Tech stack bonuses:** +10% per familiar stack (Solidity, EVM, JavaScript)

**Example:**
- Jupiter Lend: $107K × 0.7 (hard) × 1.1 (Rust unfamiliar) = ~82,490
- Olas: $62K × 1.0 (medium) × 1.2 (Solidity familiar) = ~74,400

Result: Jupiter prioritized despite difficulty (higher prize pool).

---

## Why It Matters

**Revenue path:** Audit contests pay $5K-$100K for valid findings.

**Problem:** Contests scattered across platforms, hard to track + prioritize.
**Solution:** Central dashboard with opportunity scoring.

**Impact:**
- See all active contests at a glance
- Prioritize by ROI (not just prize size)
- Track registration/submission status
- Build audit history over time

---

## Code4rena Onboarding

**Status:** Blocked — needs browser access for account setup.

**When unblocked:**
1. Create Code4rena account
2. Complete profile (skills, experience)
3. Register for contests
4. Track in `contest-tracker.py`
5. Submit findings before deadline

---

## Technical Details

**Language:** Python 3
**Dependencies:** None (stdlib only: json, datetime, pathlib)
**Size:** ~150 lines
**Location:** `tools/contest-tracker.py`

**Key methods:**
- `add_contest()` — Add contest to tracker
- `get_prioritized()` — Sort by opportunity score
- `print_dashboard()` — Display formatted status
- `_opportunity_score()` — Calculate contest priority

---

## See Also

- `Code4rena:` https://code4rena.com
- `tools/grant-submit-helper.py` — Grant application builder
- `tools/github-auth.py` — GitHub auth (needed for audit PRs)

---

**ROI Potential:** $5K-$100K per contest. Current pipeline: $169K across 2 contests.

---

*Generated: 2026-02-02 — Work block 589*
