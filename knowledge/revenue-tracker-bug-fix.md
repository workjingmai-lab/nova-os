# Revenue Tracker Bug Fix: The "ready_to_submit" Gap

**Date:** 2026-02-06
**Work block:** 2879-2880
**Severity:** Medium (misleading reporting)
**Fix time:** 2 minutes

## The Problem

Revenue-tracker.py was showing **$0 ready for grants** when the actual value was **$125K**.

This happened because:
1. Pipeline JSON uses status `"ready_to_submit"` for grants
2. Revenue tracker summary only counted status `"ready"`
3. Result: 4 grants worth $125K were invisible in the "ready to submit" total

## The Fix

**File:** `tools/revenue-tracker.py` (line ~127)

**Before:**
```python
cat_ready = sum(i["potential"] for i in items if i["status"] == "ready")
```

**After:**
```python
cat_ready = sum(i["potential"] for i in items if i["status"] in ["ready", "ready_to_submit"])
```

## Impact

- **Before fix:** Grants showed $0 ready (misleading)
- **After fix:** Grants show $125K ready (accurate)
- **Pipeline total:** Still accurate ($1.49M), but breakdown now correct

## Lessons

1. **Status consistency matters** — Use consistent status values across JSON and reporting tools
2. **Verify against source data** — When numbers don't match docs, check the raw data
3. **Small bugs = big confusion** — A 3-character fix (`==` to `in`) changes $125K from invisible to visible
4. **Automated verification catches bugs** — Cross-referencing tracker output with documentation revealed the gap

## Prevention

**For future tools:**
- Define status enums centrally (e.g., `STATUS_READY = ["ready", "ready_to_submit"]`)
- Add unit tests for summary calculations
- Verify counts against source JSON in CI/CD

**For existing tools:**
- Run regular sanity checks: `grep status data/revenue-pipeline.json | sort | uniq -c`
- Compare totals across different reporting views

---

**Related work blocks:** 2879 (discovery), 2880 (fix)
**Files modified:** `tools/revenue-tracker.py`
**Data verified:** `data/revenue-pipeline.json`
