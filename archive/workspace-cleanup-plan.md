# Workspace Cleanup Plan — Archive Candidates

**Created:** 2026-02-06 (Work block 2843)
**Purpose:** Identify files for archival to reduce workspace clutter
**Status:** Ready for Arthur review

---

## 📊 Current State

**Workspace root files:** 237 markdown files
**Goal:** Reduce to <100 active files (archive 137+ outdated files)

---

## 🎯 Archive Candidates (137+ files)

### Category 1: Status/Snapshot/Summary Files (35 files)
**Pattern:** One-time status reports that are now obsolete
```
*STATUS*.md (13 files)
*SNAPSHOT*.md (4 files)
*SUMMARY*.md (18 files)
```
**Examples:**
- STATUS-SNAPSHOT.md
- CURRENT-STATE-SNAPSHOT.md
- STATUS-FOR-ARTHUR.md (duplicate of START-HERE.md)
- QUICK-STATUS-*.md (multiple versions)
- SESSION-SUMMARY-*.md
- DAILY-SUMMARY-*.md
- EXEC-SUMMARY-*.md

**Action:** Move to `archive/status-reports/`

---

### Category 2: Milestone Files (8 files)
**Pattern:** Old milestone checklists (2000-block complete)
```
*MILESTONE*.md
```
**Examples:**
- MILESTONE-2000*.md (4 variants)
- MILESTONE-CHECKPOINT-*.md
- 2000-BLOCK-MILESTONE.md

**Action:** Move to `archive/milestones/2000-block/`

**Keep active:**
- MILESTONE-3000.md (current milestone)
- 3000-BLOCK-MILESTONE-*.md (current)

---

### Category 3: Quick Start/Guides (37 files)
**Pattern:** Multiple versions of similar guides
```
*QUICK*.md
*START*.md
```
**Examples:**
- QUICK-START*.md (5 variants)
- QUICK-WINS*.md (3 variants)
- QUICK-STATUS*.md (3 variants)
- QUICK-COMMANDS.md (duplicate of TOP-10-QUICK-COMMANDS.md)
- ARTHUR-QUICK*.md (6 variants)
- START-HERE.README.md (duplicate of README.md)

**Action:**
- Keep 1 canonical version of each guide
- Archive duplicates to `archive/duplicate-guides/`

**Keep active:**
- START-HERE.md (master execution index)
- QUICK-REVENUE-COMMANDS.md (canonical)
- TOP-5-TOOLS-QUICK-REF.md (canonical)

---

### Category 4: Arthur Action Files (15 files)
**Pattern:** "Next action" reminders (superseded by ARTHUR-HANDOFF-CHECKLIST.md)
```
ARTHUR-*ACTION*.md
ARTHUR-NEXT*.md
NEXT-ACTION*.md
```
**Examples:**
- ARTHUR-NEXT-ACTION.md
- ARTHUR-NEXT-ACTIONS.md
- ARTHUR-QUICK-ACTION.md
- NEXT-ACTION.md
- NEXT-ACTIONS.md

**Action:** Archive to `archive/superseded-arthur-guides/`

**Keep active:**
- ARTHUR-HANDOFF-CHECKLIST.md (master handoff guide)
- ARTHUR-57-MIN-QUICK-REF.md (specific execution plan)

---

### Category 5: Blocker/Gap Files (12 files)
**Pattern:** Old blocker status files (blockers resolved or superseded)
```
*BLOCKER*.md
*GAP*.md
```
**Examples:**
- BLOCKER-SUMMARY.md
- BLOCKERS-SUMMARY.md (duplicate)
- BLOCKER-STATUS.md (outdated)
- EXECUTION-GAP-*.md (3 variants)
- GAP-REMINDER.md

**Action:** Archive to `archive/blocker-history/`

**Keep active:**
- BLOCKER-ROI-SUMMARY.md (reference doc)
- GATEWAY-RESTART-QUICK-START.md (active blocker resolution)

---

### Category 6: Outreach Draft Files (13 files)
**Pattern:** Old outreach drafts in wrong location
```
outreach-*.md (in workspace root, not outreach/messages/)
```
**Action:**
- Review if still relevant
- Move to `outreach/messages/` if relevant
- Archive to `archive/outreach-drafts/` if outdated

---

### Category 7: Old Cron/Session Files (8 files)
**Pattern:** One-time session summaries
```
cron-session-*.md
daily-summary-*.md
session-summary-*.md
```
**Action:** Move to `archive/session-summaries/2026-02/`

---

### Category 8: Temporary/Draft Files (9 files)
**Pattern:** Clearly temporary files
```
gap-now.txt
*.clobbered.*.md
*.tmp
tmp/
```
**Action:** Delete or archive to `archive/temp/`

---

## 📋 Execution Plan

### Step 1: Create Archive Structure
```bash
mkdir -p archive/{status-reports,milestones/2000-block,duplicate-guides,superseded-arthur-guides,blocker-history,outreach-drafts,session-summaries/2026-02,temp}
```

### Step 2: Move Files (Example)
```bash
# Status files
mv *STATUS*.md archive/status-reports/
mv *SNAPSHOT*.md archive/status-reports/
mv *SUMMARY*.md archive/status-reports/

# Old milestones
mv MILESTONE-2000*.md archive/milestones/2000-block/
mv 2000-BLOCK-MILESTONE.md archive/milestones/2000-block/

# Duplicate guides
mv QUICK-START*.md archive/duplicate-guides/
# (keep only canonical versions)

# And so on for each category...
```

### Step 3: Verify
```bash
# Count remaining .md files in workspace root
ls *.md | wc -l
# Target: <100 files (down from 237)
```

---

## 🎯 Expected Outcome

**Before:** 237 .md files in workspace root
**After:** ~80-100 active .md files
**Archived:** 137+ files organized by category
**Result:** Cleaner workspace, easier navigation, faster file access

---

## ⚠️  Caution

**DO NOT archive without Arthur review:**
- AGENTS.md, SOUL.md, USER.md, IDENTITY.md (core identity)
- MEMORY.md, TOOLS.md, HEARTBEAT.md (core config)
- today.md, diary.md (active working memory)
- START-HERE.md, EXECUTION-DASHBOARD.md (active guides)
- All revenue/execution files (ACTIVE pipeline)

**Archive ONLY:**
- Old status reports (one-time, now obsolete)
- Duplicate guides (superseded by canonical versions)
- Old milestone files (2000-block complete, now in 3000-block phase)
- Temporary drafts and session summaries

---

*Created: 2026-02-06 — Work block 2843*
*Next: Arthur reviews → Approves → Execute archival → Cleaner workspace*
