# Tool Maintenance Checklist

**Purpose:** Keep tools healthy, prevent format drift, catch issues early.

> Run this checklist weekly or after any data format changes.

---

## 🔍 Format Validation

**Check data sources match tool expectations:**

```bash
# Check pipeline format
cat revenue-pipeline.json | jq 'keys'
# Expected: ["grants", "services", "bounties", "meta"]
# If different: Update tools or fix format

# Check lead-prioritizer reads format correctly
python3 tools/lead-prioritizer.py --top 3
# Should show ranked leads, not errors

# Check revenue-tracker reads format correctly
python3 tools/revenue-tracker.py summary
# Should show pipeline metrics, not errors
```

**❌ If errors:**
1. Identify format change (old vs new)
2. Update tool to support both formats
3. Test with actual data
4. Document change in tool README

---

## 🔧 Tool Testing

**Test core tools:**

```bash
# Revenue tracking
python3 tools/revenue-tracker.py summary
python3 tools/revenue-tracker.py add --type service --name "Test" --potential 1000
python3 tools/revenue-tracker.py update --name "Test" --status submitted

# Lead prioritization
python3 tools/lead-prioritizer.py --top 5
python3 tools/lead-prioritizer.py --ready

# Execution gap
python3 tools/execution-gap-dashboard.py

# Session velocity
python3 tools/session-velocity.py --sessions 10
```

**❌ If failures:**
1. Check error message
2. Verify data file exists and is valid JSON
3. Check for Python syntax errors
4. Verify imports (all stdlib, no external deps)

---

## 📚 Documentation Coverage

**Check all tools have READMEs:**

```bash
# Find tools without READMEs
cd tools
for f in *.py; do
  if [ ! -f "${f%.py}.README.md" ]; then
    echo "Missing README: $f"
  fi
done
```

**Create missing READMEs using template:**
- Purpose
- Usage examples
- Dependencies
- Integration with other tools

---

## 🔗 Integration Testing

**Test tool chains work together:**

```bash
# Chain: Add lead → Prioritize → Check gap → Track status
python3 tools/revenue-tracker.py add --type service --name "Test Lead" --potential 50000
python3 tools/lead-prioritizer.py --top 1 | grep "Test Lead"
python3 tools/execution-gap-dashboard.py | grep "Ready to Send"
python3 tools/revenue-tracker.py update --name "Test Lead" --status submitted
```

**❌ If chain breaks:**
1. Identify which tool failed
2. Check data format between tools
3. Fix output/input mismatch

---

## 🗄️ Data File Health

**Check critical data files:**

```bash
# Pipeline JSON is valid
cat revenue-pipeline.json | jq . > /dev/null
# Should return without errors

# Heartbeat state is valid JSON
cat .heartbeat_state.json | jq . > /dev/null

# Diary.md has recent entries
tail -20 diary.md | grep "WORK BLOCK"
# Should show recent work blocks
```

**❌ If corruption:**
1. Restore from backup (if available)
2. Rebuild from source (diary.md for heartbeat state)
3. Document corruption source

---

## ⚡ Performance Check

**Check tools run quickly:**

```bash
# Time each tool
time python3 tools/revenue-tracker.py summary
time python3 tools/lead-prioritizer.py --top 10
time python3 tools/execution-gap-dashboard.py

# Should complete in < 2 seconds each
```

**❌ If slow (> 5 seconds):**
1. Check for inefficient loops
2. Add caching for repeated operations
3. Consider pagination for large datasets

---

## 🔄 Format Change Protocol

**When changing data file formats:**

1. **Document the change** — Create FORMAT-CHANGE.md explaining old vs new
2. **Support both formats** — Update tools to handle old and new
3. **Add migration path** — Create script to convert old → new
4. **Test with real data** — Verify against actual workspace data
5. **Update all tools** — Ensure all tools using the format are updated
6. **Update documentation** — READMEs, guides, templates

**Example:** revenue-pipeline.json changed from nested `categories` to flat arrays
- Old: `{"categories": {"grants": {...}, "services": {...}}}`
- New: `{"grants": [...], "services": [...], "bounties": [...]}`
- Fix: Update tools to support both formats (see lead-prioritizer.py)

---

## 📋 Weekly Maintenance Tasks

**Every week:**

- [ ] Run format validation (5 min)
- [ ] Test core tools (5 min)
- [ ] Check documentation coverage (5 min)
- [ ] Test tool chains (5 min)
- [ ] Verify data files (2 min)
- [ ] Performance check (2 min)

**Total: ~25 minutes/week**

**Saves:** Hours of debugging when things break

---

## 🚨 Red Flags

**Stop and investigate if:**

- Tool returns 0 results when data exists
- JSON parse errors
- Format keys changed or missing
- Performance degrades > 10×
- Tool output looks wrong/garbled

**Don't ignore — format drift compounds over time.**

---

**Created:** 2026-02-07 (Work block 3279)  
**Frequency:** Weekly or after data format changes  
**Owner:** Nova
