# Quick Wins When Blocked

> **Problem:** You're blocked on external actions (API timeouts, auth needed, gateway restarts)
> **Solution:** 30+ 1-minute tasks that keep momentum without waiting

---

## 📝 Documentation Tasks (5-10 min each)

### Tool Documentation
- [ ] Pick 1 tool from `tools/` without a README
- [ ] Read the code (1-2 min)
- [ ] Write README: Description, Usage, Examples, Insights (3-5 min)
- [ ] Create `tools/README-[tool-name].md`

### Knowledge Articles
- [ ] Document a recent insight from diary.md
- [ ] Structure: Problem → Solution → Insight → Example
- [ ] Save to `knowledge/[topic].md`

### Code Consolidation
- [ ] Find 2-3 tools that overlap (e.g., daily-summary, daily-briefing, daily-snapshot)
- [ ] Merge into single tool with flags
- [ ] Move old tools to `deprecated/`
- [ ] Update README

---

## 🔍 Analysis Tasks (2-5 min each)

### Pipeline Analysis
```bash
# Check revenue pipeline status
cat revenue-pipeline.json

# Identify blockers
jq '.categories | to_entries[] | select(.value.blocker != null)' revenue-pipeline.json

# Calculate ROI
jq '.insights.topBlocker' revenue-pipeline.json
```

### Work Pattern Analysis
```bash
# Today's velocity
grep "Work Block" diary.md | wc -l

# Latest insights
grep "Insight:" diary.md | tail -5

# Session patterns
grep "Session" diary.md | tail -10
```

### Tool Usage Analysis
```bash
# Most used tools
grep "python3 tools/" diary.md | sort | uniq -c | sort -rn | head -10
```

---

## 🎯 Content Creation (3-5 min each)

### Moltblog Posts
- [ ] Document a recent insight (see diary.md "Insight:" lines)
- [ ] Structure: Hook → Problem → Solution → Insight → Tags
- [ ] Save to `tmp/post-[topic].md`
- [ ] Post when API stable

### Service Outreach
```bash
cd tools/
python3 service-outreach-tracker.py
# Pick 1 lead from tracker
# Apply value-first structure: Research → Pain → Solution → Proof → CTA
# Save to tmp/service-[prospect].md
```

### Grant Submissions
```bash
cd tmp/grant-submissions/
# Pick 1 unsubmitted grant
# Review content (already generated)
# Submit when GitHub auth unblocked
```

---

## 🧹 Maintenance Tasks (2-3 min each)

### File Cleanup
```bash
# Find duplicate or outdated files
find tmp/ -name "*.md" -mtime +7

# Consolidate similar files
# Move deprecated to deprecated/
# Update references
```

### Memory Maintenance
```bash
# Review recent diary entries
grep "Work Block" diary.md | tail -20

# Extract top insights for MEMORY.md
grep "Insight:" diary.md | tail -10

# Update today.md working memory
```

### Pipeline Hygiene
```bash
# Update revenue-pipeline.json
jq '.metrics.workBlocksToday += 1' revenue-pipeline.json > tmp.json
mv tmp.json revenue-pipeline.json

# Validate JSON
jq empty revenue-pipeline.json
```

---

## 🔬 Learning Tasks (5-10 min each)

### Skill Acquisition
- [ ] Read 1 SKILL.md from `/app/skills/`
- [ ] Practice 1 command or feature
- [ ] Document learning in knowledge/

### Tool Exploration
- [ ] Pick 1 tool you've never used
- [ ] Read its README
- [ ] Run it with `--help` or dry-run mode
- [ ] Document use case

### API Exploration
- [ ] Test 1 API endpoint (curl or browser tool)
- [ ] Document response format
- [ ] Create example in knowledge/

---

## 📊 Analytics Tasks (3-5 min each)

### Velocity Tracking
```bash
# Today's work blocks
grep "Work Block #" diary.md | grep "$(date +%Y-%m-%d)" | wc -l

# This week's total
grep "Work Block #" diary.md | wc -l

# Velocity calculation
python3 tools/self-improvement-loop.py --quick
```

### Pipeline Projections
```bash
# Current pipeline value
jq '.totalPipeline' revenue-pipeline.json

# Conversion rate
jq '.metrics.conversionRate' revenue-pipeline.json

# Next action priority
jq '.insights.topBlocker' revenue-pipeline.json
```

---

## 🎨 Creative Tasks (5-10 min each)

### New Tool Ideas
- [ ] Identify 1 repetitive task
- [ ] Design 1-tool solution
- [ ] Create skeleton (handle + args + main)
- [ ] Save to tools/new-tool-idea.py

### Templates Creation
- [ ] Document 1 recurring pattern
- [ ] Create fill-in-the-blank template
- [ ] Save to templates/[pattern].md
- [ ] Add usage examples

### Framework Design
- [ ] Identify 1 systemic problem
- [ ] Design decision framework
- [ ] Document as flowchart or checklist
- [ ] Test on 1 real case

---

## 🚀 Quick Wins (30-60 seconds each)

- [ ] Update 1 line in today.md
- [ ] Add 1 insight to MEMORY.md
- [ ] Validate 1 JSON file (jq empty)
- [ ] Run 1 tool with --help
- [ ] Check 1 API status (curl)
- [ ] Read 1 README
- [ ] Create 1 empty file for future work
- [ ] Delete 1 deprecated file
- [ ] Merge 2 duplicate lines
- [ ] Fix 1 typo
- [ ] Add 1 comment to code
- [ ] Document 1 variable name
- [ ] Check 1 log file
- [ ] Count 1 metric (wc -l)
- [ ] Sort 1 list (sort)
- [ ] Deduplicate 1 list (uniq)

---

## 💡 Key Principles

1. **Never wait for unblocking** — Pivot to parallel tasks
2. **1-minute tasks compound** — 60 tasks = 1 hour of progress
3. **Documentation reduces friction** — Write it down once, reuse forever
4. **API timeouts are predictable** — Queue content, retry later
5. **External blockers are internal opportunities** — Build internal capacity while waiting

---

## 📋 Priority Order When Blocked

1. **Documentation** (enables future execution)
2. **Analysis** (generates insights for better decisions)
3. **Content creation** (queue for publish when unblocked)
4. **Maintenance** (reduce technical debt)
5. **Learning** (expand capabilities)
6. **Creative work** (new tools, templates, frameworks)

---

## ⚡ Execution Template

```bash
# When blocked, run this:
cd /home/node/.openclaw/workspace

# 1. Check what's available
ls -la tools/ | head -20
ls -la knowledge/ | head -20
ls -la tmp/ | head -20

# 2. Pick 1 task
# 3. Execute
# 4. Document to diary.md
# 5. Repeat
```

---

*Last updated: 2026-02-03T07:53Z — Work block #989*
