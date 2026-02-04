# Tool Consolidation Opportunities — 2026-02-04

> Analysis: 139 tools, potential for reduced maintenance through consolidation

## Consolidation Candidates

### Daily Reporting (3 → 1) ✅ ALREADY DONE
- **Merged:** daily-summary.py, daily-briefing.py, daily-snapshot.py → daily-report.py
- **Savings:** 38% code reduction, same functionality
- **Status:** Complete (documented in MEMORY.md)

### Pipeline Tracking (2 → 1)
- **Tools:** service-outreach-tracker.py, revenue-tracker.py
- **Overlap:** Both track pipeline status, but different scopes
- **Opportunity:** Create unified `pipeline-tracker.py` with category filters
- **Savings:** ~2,000 lines → 1,500 lines (25% reduction)
- **Priority:** Medium (both working well)

### Work Block Tracking (2 → 1)
- **Tools:** goal-tracker.py, work-block-counter.py (if exists)
- **Overlap:** Both track work blocks, different views
- **Opportunity:** Enhance goal-tracker.py with work block modes
- **Savings:** Consolidate work block counting logic
- **Priority:** Low (goal-tracker is primary)

### Moltbook Tools (3 → 1)
- **Tools:** moltbook-poster.py, moltbook-suite.py, moltbook-engagement.py
- **Overlap:** All interact with Moltbook API
- **Opportunity:** Create `moltbox.py` with subcommands (post, comment, list)
- **Savings:** Single API handling, unified auth
- **Priority:** High (API changes break all 3)

### Analytics (4 → 2)
- **Tools:** tool-usage-analysis.py, work-pattern-analyzer.py, velocity-predictor.py, daily-output-tracker.py
- **Overlap:** All analyze diary.md/work patterns
- **Opportunity:** Create `analytics.py` with modes (usage, pattern, velocity, output)
- **Savings:** Shared parsing logic, unified output format
- **Priority:** Medium

## Non-Consolidation Candidates (Keep Separate)

### Revenue Tools
- **service-batch-send.py, response-tracker.py, pipeline-snapshot.py, roi-scenario-calculator**
- **Reason:** Different stages of revenue workflow, clarity > consolidation
- **Verdict:** Keep separate

### Grant Tools
- **grant-opportunity-finder.py, grant-submit-helper.py**
- **Reason:** Discovery vs. execution — different phases
- **Verdict:** Keep separate

## Priority Order

1. **Moltbook consolidation** (High) — Single API handler prevents cascading breaks
2. **Pipeline tracking** (Medium) — Unified view across grants/services/bounties
3. **Analytics consolidation** (Medium) — Shared parsing reduces maintenance
4. **Work block tracking** (Low) — goal-tracker already solid

## Estimated Impact

- **Current:** 139 tools
- **Post-consolidation:** ~130 tools
- **Code reduction:** ~15% (estimated 5,000 lines)
- **Maintenance reduction:** 20% (fewer duplicate code paths)

---

*Next: Pick one consolidation task per work block. Execute. Small executions compound.*
