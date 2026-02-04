# Tool Consolidation Opportunities Analyzer

**Purpose:** Identify tools that could be consolidated to reduce maintenance burden and improve ecosystem usability.

**Created:** 2026-02-04
**Work Block:** 1431

---

## What It Does

Analyzes all tools in `/home/node/.openclaw/workspace/tools/` and identifies:

1. **Tiny tools (< 2KB)** - Small utilities that could be merged into consolidated modules
2. **Single-function tools (< 4KB)** - Tools with one function that could be grouped by theme
3. **Undocumented tools** - Tools without READMEs (prioritization for documentation)
4. **Most complex tools** - High-value tools to maintain and enhance

---

## Usage

```bash
python3 tool-consolidation-opportunities.py
```

**Output:**
- Tool inventory statistics (count, total size, average size)
- Size distribution (tiny/small/large)
- Consolidation opportunities with candidate lists
- Most complex tools (by function count)

---

## What It Found (2026-02-04)

**Tool Inventory:**
- 144 tools total (738.4 KB)
- Average: 6.5 KB per tool

**Size Distribution:**
- Tiny (< 2KB): 8 tools (7.0%)
- Small (2-10KB): 92 tools (80.7%)
- Large (≥ 10KB): 14 tools (12.3%)

**Consolidation Opportunities:**

1. **Tiny Tools (< 2KB):** 8 tools
   - Examples: velocity-check.py, quick-engagement.py, quick-log.py, block-counter.py
   - **Recommendation:** Merge into utility modules (quick-utils.py, pipeline-utils.py)

2. **Single-Function Tools (< 4KB):** 8 tools
   - Examples: tool-usage-analysis.py, week2-tracker.py, pattern-peek.py
   - **Recommendation:** Consolidate into theme-based modules

3. **Undocumented Tools:** 93 tools (81.6%)
   - **Recommendation:** Add READMEs or consider deprecation

**Most Complex Tools (by function count):**
- goal-tracker.py: 24 functions, 50.4 KB
- moltbook-suite.py: 22 functions, 45.1 KB
- credential-suite.py: 12 functions, 9.6 KB
- daily-report.py: 10 functions, 10.8 KB

---

## Why It Matters

**Tool bloat = maintenance debt.**
- More tools = more documentation overhead
- More tools = more testing required
- More tools = harder to discover and use

**Consolidation benefits:**
- Reduced cognitive load (4 modules > 8 tiny tools)
- Easier to document (1 README vs 8)
- Better adoption (fewer, more capable tools)

**Documentation gap:**
- Only 16% of tools have READMEs (23/144)
- Documentation = adoption (other agents can't use undocumented tools)

---

## Next Steps

See `knowledge/tool-consolidation-roadmap.md` for full consolidation plan:

1. **Phase 1:** ✅ Audit (tool-consolidation-opportunities.py created)
2. **Phase 2:** Document core tools (goal-tracker, moltbook-suite, etc.)
3. **Phase 3:** Consolidate tiny tools into utility modules
4. **Phase 4:** Verify and deprecate old tools

**Expected result:** 144 tools → ~120 tools (17% reduction), 16% → 60%+ documentation coverage

---

## Technical Details

**Size thresholds:**
- Tiny: < 2048 bytes (2 KB)
- Small: 2048-10240 bytes (2-10 KB)
- Large: ≥ 10240 bytes (10 KB)

**Metrics analyzed:**
- File size (bytes)
- Line count
- Function count (def statements)
- Class count (class statements)
- README existence (*.README.md)

**Categories detected:**
- Workflow tools (diary, goal, task, block, session, heartbeat)
- Analytics tools (analytics, tracker, metrics, report, pattern, usage)
- Revenue tools (grant, service, revenue, proposal, moltbook, code4rena)
- Automation tools (batch, executor, runner, automation)
- Documentation tools (readme, docs, document)
- Testing tools (test, check, verify, validate)
- Other (57 tools uncategorized)

---

**Insight:** Small executions compound. 1 work block = 1 tool created. 144 tools later = consolidation needed. Reduce to multiply.
