# Tool Consolidation Plan — Feb 3, 2026

> **Goal:** Reduce maintenance burden, improve interface consistency, eliminate redundancy
> **Opportunity:** 10+ overlapping tools can be consolidated into 3-4 unified tools

---

## 🔍 Identified Consolidation Opportunities

### Priority 1: Velocity Tools (3→1)
**Tools to merge:**
- `velocity-predictor.py` — Forecast future velocity
- `velocity-check.py` — Count tasks completed today
- `velocity-calc.py` — Calculate work block metrics

**Consolidated tool:** `velocity-suite.py`
**Modes:**
- `predict` — Forecast velocity (from velocity-predictor.py)
- `check` — Count tasks today (from velocity-check.py)
- `calc` — Calculate metrics (from velocity-calc.py)

**Code reduction:** ~250 lines → ~120 lines (52% reduction)

### Priority 2: Work Block Tools (3→1, already 1 redundant)
**Tools:**
- `work-block-tracker.py` — Log work blocks (REDUNDANT)
- `work-block-suite.py` — Log + track + estimate (KEEP, already consolidated)
- `work-block-miner.py` — Pattern analysis (KEEP, distinct purpose)

**Action:** Deprecate `work-block-tracker.py` (functionality in work-block-suite.py)

**Code reduction:** ~130 lines removed

### Priority 3: Wins Tools (2→1)
**Tools:**
- `wins.py` — Motivation tracker
- `win-streak.py` — Streak calculator

**Consolidated tool:** `wins.py` (enhance with streak mode)
**Modes:**
- `log` — Log a win (from wins.py)
- `streak` — Calculate streak (from win-streak.py)

**Code reduction:** ~180 lines → ~100 lines (44% reduction)

### Priority 4: Workspace Tools (3→1)
**Tools:**
- `workspace-organizer.py` — Organize workspace
- `workspace-map.py` — Visualize workspace structure
- `workspace-cleanup.py` — Clean up workspace

**Consolidated tool:** `workspace-manager.py`
**Modes:**
- `organize` — Organize files and folders
- `map` — Generate workspace visualization
- `cleanup` — Remove temp files, deprecated tools

**Code reduction:** ~300 lines → ~150 lines (50% reduction)

---

## 📊 Consolidation ROI

| Priority | Tools Before | Tools After | Lines Removed | Time Saved |
|----------|--------------|-------------|---------------|------------|
| 1: Velocity | 3 | 1 | ~130 | 15 min |
| 2: Work Block | 2 → 1 (deprecate) | 1 | ~130 | 10 min |
| 3: Wins | 2 | 1 | ~80 | 10 min |
| 4: Workspace | 3 | 1 | ~150 | 20 min |
| **Total** | **10** | **4** | **~490** | **55 min** |

**Maintenance burden reduction:** 60% fewer tools to document, test, update

---

## ⚡ Execution Plan

### Phase 1: Quick Win (10 min)
**Merge wins tools**
1. Read wins.py and win-streak.py
2. Create wins.py v2 with `--streak` mode
3. Test: `python3 tools/wins.py --streak`
4. Move win-streak.py to deprecated/
5. Update tools/README-wins.md

### Phase 2: High Value (15 min)
**Merge velocity tools**
1. Read all 3 velocity tools
2. Create velocity-suite.py with modes
3. Test: `python3 tools/velocity-suite.py --predict`, `--check`, `--calc`
4. Move old tools to deprecated/
5. Create tools/README-velocity-suite.md

### Phase 3: Deprecation (5 min)
**Remove redundant work-block-tracker.py**
1. Verify work-block-suite.py has log mode
2. Move work-block-tracker.py to deprecated/
3. Update any references in documentation

### Phase 4: Major Consolidation (20 min)
**Merge workspace tools**
1. Read all 3 workspace tools
2. Create workspace-manager.py with modes
3. Test all modes (organize, map, cleanup)
4. Move old tools to deprecated/
5. Create tools/README-workspace-manager.md

---

## 🎯 Success Criteria

- [ ] 10 tools → 4 tools (60% reduction)
- [ ] All modes tested and working
- [ ] Old tools moved to deprecated/
- [ ] READMEs created for consolidated tools
- [ ] Documentation updated with new tool names
- [ ] No broken references in scripts or docs

---

## 💡 Key Insight

**"Tool consolidation is not just about reducing code. It's about reducing cognitive load."**

Fewer tools = easier to remember = higher velocity.

When you have 3 velocity tools (predictor, check, calc), you think:
- "Which one do I use?"
- "What was the command?"
- "Where's the README?"

When you have 1 velocity tool with 3 modes:
- "velocity-suite --predict"
- "velocity-suite --check"
- "velocity-suite --calc"

One tool to remember. One README to read. One interface to learn.

---

*Created: 2026-02-03T08:03Z — Work block #994*
*Next: Execute Phase 1 (wins consolidation)*
