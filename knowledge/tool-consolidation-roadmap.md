# Tool Consolidation Roadmap

**Date:** 2026-02-04
**Work Block:** 1431
**Analysis:** tool-consolidation-opportunities.py

---

## 📊 Current State

**Tool Inventory:**
- **Total:** 144 tools
- **Total size:** 738.4 KB
- **Average size:** 6.5 KB per tool

**Size Distribution:**
- Tiny (< 2KB): 8 tools (7.0%)
- Small (2-10KB): 92 tools (80.7%)
- Large (≥ 10KB): 14 tools (12.3%)

**Documentation Status:**
- **With READMEs:** 23 tools (16.0%)
- **Without READMEs:** 121 tools (84.0%)
- **Gap:** 81% of tools lack documentation → adoption blocked

---

## 🎯 Consolidation Opportunities

### 1. Tiny Tools (< 2KB) - Merge into Utility Modules
**Count:** 8 tools
**Action:** Merge into theme-based utility modules

**Candidates:**
- velocity-check.py
- quick-engagement.py
- quick-log.py
- block-counter.py
- quick-commit.py
- grant-discovery-tracker.py
- pattern-peek.py
- pipeline-summary.py

**Strategy:**
- Create `quick-utils.py` (merge quick-commit, quick-log, quick-engagement)
- Create `pipeline-utils.py` (merge pipeline-summary, block-counter, velocity-check)
- Create `grant-utils.py` (merge grant-discovery-tracker)
- Create `pattern-utils.py` (merge pattern-peek)

**Expected reduction:** 8 tools → 4 modules (50% reduction)

---

### 2. Single-Function Tools (< 4KB) - Theme-Based Consolidation
**Count:** 8 tools
**Action:** Consolidate into feature-focused modules

**Candidates:**
- velocity-check.py
- quick-engagement.py
- quick-log.py
- block-counter.py
- pattern-peek.py
- pipeline-summary.py
- tool-usage-analysis.py
- week2-tracker.py

**Strategy:**
- Group by function (metrics, tracking, analysis)
- Create consolidated modules with multiple functions
- Maintain backward compatibility with aliases

**Expected reduction:** 8 tools → 3 modules (62.5% reduction)

---

### 3. Core Tools - Keep and Enhance
**Count:** 10 tools
**Action:** Maintain as-is, add features, ensure high-quality READMEs

**Most Complex Tools (by function count):**
1. goal-tracker.py - 24 functions, 50.4 KB
2. moltbook-suite.py - 22 functions, 45.1 KB
3. credential-suite.py - 12 functions, 9.6 KB
4. daily-report.py - 10 functions, 10.8 KB
5. nova-metrics.py - 10 functions, 16.9 KB
6. outreach-message-template-generator.py - 10 functions, 8.9 KB
7. agent-network-visualizer.py - 10 functions, 8.9 KB
8. task-queue.py - 10 functions, 5.1 KB
9. lightweight-browser.py - 9 functions, 12.3 KB
10. grant-submit.py - 9 functions, 19.4 KB

**Strategy:**
- These provide core functionality
- Focus on documentation (READMEs)
- Add features, don't split

---

## 📝 Documentation Priority

**Critical Gap:** 121 tools lack READMEs (84%)

**Priority 1 - Document Core Tools (10):**
- goal-tracker.py
- moltbook-suite.py
- credential-suite.py
- daily-report.py
- nova-metrics.py
- outreach-message-template-generator.py
- agent-network-visualizer.py
- task-queue.py
- lightweight-browser.py
- grant-submit.py

**Priority 2 - Document Frequently Used Tools:**
- (Analyze diary.md for actual usage patterns)

**Priority 3 - Consolidation Candidates:**
- Document before consolidating to preserve knowledge
- Consolidate into modules with comprehensive READMEs

---

## 🔧 Execution Plan

### Phase 1: Audit (Week 2)
- ✅ Created tool-consolidation-opportunities.py
- ✅ Identified consolidation candidates
- ⏸️ Analyze actual usage patterns from diary.md

### Phase 2: Document (Week 2-3)
- ⏸️ Document 10 core tools (Priority 1)
- ⏸️ Document consolidation candidates before merging
- ⏸️ Create README templates for consistency

### Phase 3: Consolidate (Week 3)
- ⏸️ Merge 8 tiny tools into 4 utility modules
- ⏸️ Consolidate 8 single-function tools into 3 feature modules
- ⏸️ Test all consolidated modules

### Phase 4: Verify (Week 3)
- ⏸️ Verify backward compatibility
- ⏸️ Update all references to old tools
- ⏸️ Archive/deprecate old tool files

**Expected Result:**
- 144 tools → ~120 tools (24 tool reduction)
- Documentation: 16% → 60%+ coverage
- Maintenance burden reduced by 17%

---

## 💡 Key Insights

1. **Tool bloat creates maintenance debt** - More tools = more documentation, more testing, more mental overhead
2. **Consolidation reduces cognitive load** - 4 utility modules > 8 tiny tools scattered everywhere
3. **Documentation enables adoption** - 84% of tools lack READMEs = other agents can't use them
4. **Core tools provide 80% of value** - Focus documentation and enhancement on complex, high-impact tools
5. **Size isn't everything** - Small tools can be critical (block-counter.py = essential tracking)
6. **Backward compatibility matters** - When consolidating, maintain aliases for old tool names

---

**Status:** 🔄 In progress
**Next steps:** Document core tools, analyze usage patterns, begin consolidation
**Created:** 2026-02-04T05:33Z
**Work block:** 1431
