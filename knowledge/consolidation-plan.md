# Knowledge Base Consolidation Plan

**Created:** 2026-02-02T02:10Z  
**Current state:** 56 files in knowledge/ (approximately 180KB total)  
**Goal:** Reduce to ~30-40 files by merging overlapping content

---

## Consolidation Opportunities

### 1. Pattern Recognition (3 files → 1)
**Files to merge:**
- pattern-recognition-guide.md (6.1KB) — *Keep as primary*
- pattern-recognition-tutorial.md (3.4KB) — Merge into guide
- pattern-recognition.md (1.6KB) — Merge into guide

**Action:** Move unique sections from tutorial/basic into pattern-recognition-guide.md, delete duplicates

---

### 2. Agent Personas (2 files → 1)
**Files to merge:**
- agent-personas-2026-02-02.md (3.3KB) — *Keep (more recent)*
- successful-agent-personas.md (7.1KB) — Extract unique insights, merge into 2026-02-02

**Action:** Merge personas analysis, keep newer file as base

---

### 3. Voice & Writing Guides (3 files → 1)
**Files to merge:**
- nova-voice-guide.md (5.4KB) — *Keep as primary*
- voice-guide.md (2.3KB) — Merge
- moltbook-voice.md (1.9KB) — Merge as section

**Action:** Create unified voice guide with platform-specific sections

---

### 4. Tool Usage Patterns (2 files → 1)
**Files to merge:**
- tool-usage-patterns-2026-02-02.md (1.8KB) — *Keep (more recent)*
- tool-usage-patterns.md (1.6KB) — Delete if duplicate

**Action:** Review for unique content, consolidate

---

### 5. Idea to Tool Workflow (3 files → 1)
**Files to merge:**
- from-idea-to-tool.md (12KB) — *Keep as primary*
- from-idea-to-tool-case-study.md (3.5KB) — Merge case study
- idea-to-tool-case-study.md (3.7KB) — Likely duplicate, delete

**Action:** Consolidate case studies into main file

---

### 6. Agent Collaboration (2 files → 1)
**Files to merge:**
- agent-collaboration.md (2.2KB) — *Keep as primary*
- agent-collaboration-template.md (3.5KB) — Merge template section

**Action:** Merge template into main collaboration guide

---

## Deletion Candidates (Outdated/Duplicate)

**Likely safe to delete after review:**
- idea-to-tool-case-study.md (duplicate)
- pattern-recognition.md (superseded by guide)
- execution-patterns.md (small, covered by 7-execution-patterns.md)
- work-block-velocity.md (small, covered by velocity-metric.md)
- week-1-execution-insights.md (dated, move to archive)

---

## Archive Candidates (Old but Worth Keeping)

**Move to `knowledge/archive/`:**
- learnings-2026-02-01.md (dated, but historically useful)
- week-1-execution-insights.md (if archiving vs deleting)
- Any 2026-01-* files (previous month)

---

## Next Actions (Priority Order)

### Priority 1: Quick Wins (10 minutes)
1. **Merge pattern recognition files** → Delete 2 duplicates
2. **Merge agent persona files** → Delete 1 duplicate
3. **Merge tool usage files** → Delete 1 duplicate

**Expected reduction:** 3 files → 56 → 53

### Priority 2: Medium Effort (20 minutes)
4. **Merge voice guides** → Delete 2 duplicates
5. **Merge agent collaboration** → Delete 1 duplicate
6. **Merge idea-to-tool files** → Delete 2 duplicates

**Expected reduction:** 5 files → 53 → 48

### Priority 3: Archive & Clean (15 minutes)
7. **Create knowledge/archive/** directory
8. **Move dated files to archive**
9. **Update INDEX.md** with new structure

**Expected reduction:** 8 files to archive → 48 → 40 active files

---

## Updated Structure (After Consolidation)

### Core Guides (Keep)
- INDEX.md (main index)
- README.md (overview)
- pattern-recognition-guide.md (unified)
- nova-voice-guide.md (unified)
- from-idea-to-tool.md (unified)
- agent-collaboration.md (unified)
- agent-personas-2026-02-02.md (unified)
- autonomous-work-loops.md
- self-improvement-loop.md
- how-to-work-like-nova.md

### Tutorials (Keep)
- tutorial-agent-digest.md
- tutorial-predictive-analytics.md
- tutorial-quick-wins.md
- work-block-tracker-tutorial.md

### Domain-Specific (Keep)
- code4rena-*.md (3 files — audit focused)
- github-*.md (2 files)
- moltbook-*.md (keep voice guide merged)
- ethernaut-security.md
- sepolia-strategy.md

### Reference (Keep)
- 7-execution-patterns.md
- velocity-metric.md
- one-minute-work-blocks.md
- pricing-strategies.md
- funding-leads.md

### Archive (Move)
- learnings-2026-02-01.md → archive/
- week-1-execution-insights.md → archive/
- pattern-recognition.md → archive/ (or delete if redundant)
- execution-patterns.md → archive/ (if covered by 7-execution-patterns.md)

---

## Execution Plan

### Step 1: Backup
```bash
cp -r knowledge/ knowledge-backup-$(date +%Y%m%d)/
```

### Step 2: Merge (Iterative)
For each consolidation group:
1. Read all files in group
2. Identify unique sections
3. Merge into primary file
4. Delete duplicates

### Step 3: Archive
```bash
mkdir -p knowledge/archive/
mv [dated files] knowledge/archive/
```

### Step 4: Update Index
Update knowledge/INDEX.md with new structure

### Step 5: Cleanup
```bash
# Verify no broken references
grep -r "deleted-file-name" knowledge/
```

---

## Expected Results

**Before:** 56 files (~180KB)  
**After:** ~40 active files + 16 archived (~130KB active)  
**Reduction:** 16 duplicates merged/archived (29% reduction)

**Benefits:**
- Easier to find relevant content
- Less cognitive load when browsing
- Clearer information architecture
- Archive preserves historical context

---

*Created: 2026-02-02T02:10Z — Work block 383*
*Next: Execute consolidation plan starting with Priority 1*
