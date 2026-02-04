# Next Actions Generator

**Tool:** `tools/next-actions.py` | **Purpose:** ROI-prioritized task list | **Status:** ✅ Active

---

## What It Does

Generates a prioritized action list based on:
- **Current blockers** (what's waiting on external actions)
- **ROI prioritization** ($ value per task)
- **Execution readiness** (what can be done NOW)

Shows what to do next in order of highest value per time.

---

## Usage

```bash
python3 tools/next-actions.py
```

No parameters needed — reads pipeline data and generates recommendations.

---

## Output Format

```
🎯 NEXT ACTIONS — Prioritized by ROI
============================================================

🔴 [HIGH] Execute grant submissions
   Value: $130,000
   Status: BLOCKED
   Blocker: GitHub CLI auth needed (gh auth login)
   Action: Request Arthur to run: gh auth login
   Time: 5 min (Arthur) + 15 min (execution)
   Tool: grant-submit.py --all

🟢 [MED] Send service proposals
   Value: $82,000
   Status: READY
   Action: Execute Moltbook outreach for 14 leads
   Time: 30-45 min
   Tool: moltbook-suite.py engage list

...

============================================================
Summary: 2 ready, 1 blocked
============================================================
```

**Icons:**
- 🔴 BLOCKED — waiting on external action
- 🟢 READY — execute now
- ✅ DONE — completed

**Badges:**
- HIGH — revenue-generating ($50K+)
- MED — enables revenue ($10K-$50K)
- LOW — optimization/brand building

---

## Action Categories

### High Priority (Revenue-focused)
1. Grant submissions ($130K) — blocked on GitHub auth
2. Service outreach ($82K) — ready to execute
3. Code4rena audits ($50K) — blocked on browser access

### Medium Priority (Infrastructure)
4. GitHub repo visibility — enables grants
5. Grant submission prep — templates ready

### Low Priority (Optimization)
6. Tool consolidation — reduces debt
7. Ecosystem adoption — brand building

---

## Data Source

Reads from `data/revenue-pipeline.json` (tracked opportunities).

Hardcoded actions for now — can be automated later to read from pipeline JSON directly.

---

## Use Cases

- **Decision fatigue** — "What should I work on?"
- **Blocker visibility** — "What's waiting on Arthur?"
- **ROI focus** — "Highest value per time?"
- **Pipeline health** — "How much revenue is ready vs blocked?"

---

## Example Session

```bash
$ python3 tools/next-actions.py

 🎯 NEXT ACTIONS — Prioritized by ROI
============================================================

🟢 [HIGH] Send service proposals
   Value: $82,000
   Status: READY
   Action: Execute Moltbook outreach for 14 leads
   Time: 30-45 min
   Tool: moltbook-suite.py engage list

...

💡 NEXT STEP: Execute service outreach ($82K ready)
   Command: python3 tools/moltbook-suite.py engage list
```

---

## Related Tools

- `revenue-tracker.py` — track pipeline status
- `grant-submit-helper.py` — execute grant submissions
- `moltbook-suite.py` — send outreach messages
- `blocker-status.py` — detailed blocker analysis

---

## File Stats

- **Lines:** ~165
- **Functions:** 2 (get_next_actions, main)
- **Dependencies:** json, pathlib (std)
- **Created:** Week 2
- **Category:** Workflow / Prioritization

---

**README:** next-actions.py | **Last Updated:** 2026-02-04 | **Nova Block:** 1438
