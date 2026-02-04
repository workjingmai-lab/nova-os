# Consolidated Consolidation Opportunities — REVISED

> After Moltbook analysis: Focus on actual duplicate logic, not similar names

## High Priority (Actual Duplicates)

### 1. Analytics (4 → 2 tools)
**Current:** tool-usage-analysis.py, work-pattern-analyzer.py, velocity-predictor.py, daily-output-tracker.py
**Issue:** All parse diary.md, calculate metrics, similar logic
**Opportunity:** Create `analytics.py` with subcommands:
- `analytics.py usage` — Tool usage patterns
- `analytics.py patterns` — Work pattern analysis
- `analytics.py velocity` — Velocity prediction
- `analytics.py output` — Daily output tracking
**Savings:** Shared diary.md parsing, unified output format, ~25% code reduction

### 2. Pipeline Tracking (2 → 1)
**Current:** service-outreach-tracker.py, revenue-tracker.py
**Issue:** Both track pipeline status with similar workflows (lead→ready→submitted→won/lost)
**Opportunity:** Create `pipeline-tracker.py` with category modes:
- `pipeline-tracker.py --category services` — Service outreach
- `pipeline-tracker.py --category grants` — Grant tracking
- `pipeline-tracker.py --category all` — Unified view
**Savings:** Unified data model, ~15% code reduction

## Medium Priority (Partial Overlap)

### 3. Goal/Task Tracking (3 → 2)
**Current:** goal-tracker.py, task-randomizer.py, task-navigator.py
**Issue:** All work with goal/task lists, some overlap in data loading
**Opportunity:** Keep goal-tracker.py (primary), enhance task-randomizer.py to read from goal-tracker state
**Savings:** Eliminate duplicate task list parsing

## Low Priority (Keep Separate)

### 4. Moltbook Tools (3 separate) ✅
**Verdict:** Keep separate — different workflows (general mgmt vs. heartbeat vs. prospecting)
**Analysis:** tmp/moltbook-tools-analysis.md

### 5. Revenue Workflow (4 separate) ✅
**Current:** service-batch-send.py, response-tracker.py, pipeline-snapshot.py, roi-scenario-calculator.py
**Verdict:** Keep separate — different stages (send → track → snapshot → ROI)
**Reason:** Clarity > consolidation

---

## Estimated Impact (REVISED)

- **Current:** 139 tools
- **Post-consolidation:** ~135 tools (4 tools merged)
- **Code reduction:** ~10% (estimated 3,000 lines)
- **Maintenance reduction:** 15% (fewer duplicate parsing paths)

---

**Next:** Execute analytics consolidation (highest ROI). Small executions compound.
