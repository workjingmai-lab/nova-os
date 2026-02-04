# README — diary-safe-write.py

**Protects diary.md from accidental overwrites with health checks**

---

## What It Does

Prevents catastrophic data loss when writing to `diary.md` by:
- Checking file health before write operations (size, line count, format)
- Validating file structure (header check, recent modification)
- Requiring confirmation before appending
- Detecting suspicious conditions (too small, too few lines)

**Why this matters:** `diary.md` contains 177+ files with 50K+ lines of session history. One bad write operation could delete everything.

---

## Usage

```bash
# Check diary health before any write operation
python tools/diary-safe-write.py --check-before-write

# Safely append content (with health check + confirmation)
python tools/diary-safe-write.py --append "New diary entry"
```

---

## What It Checks

**File stats:**
- File size (warns if < 10KB)
- Line count (warns if < 100 lines)
- Last modified timestamp

**Structure checks:**
- First line starts with `#` (markdown header)
- File exists and is readable

**Safety:**
- Requires confirmation before appending
- Blocks write if any health check fails
- Never overwrites — only appends

---

## When to Use

**Use before:**
- Automated diary writes from scripts
- Batch imports of session data
- Any programmatic diary modifications

**Don't use for:**
- Manual editing (use your editor directly)
- Reading operations (just `cat diary.md`)

---

## Example Output

```
📊 diary.md Health Check:
   Size: 2,548,392 bytes (2.5 MB)
   Lines: 52,847
   Last modified: 2026-02-04 06:15:32
   First line: # diary.md — Nova's Activity Log...
   Last line: [1432] Work block 1432: Tool consolidation analysis...

✅ DIARY HEALTH CHECK PASSED
```

---

## Technical Details

- **Target:** `~/.openclaw/workspace/diary.md`
- **Operation mode:** Append-only (never overwrite)
- **Dependencies:** Python 3 stdlib (no external deps)
- **Exit codes:** 0 = success, 1 = blocked/failed

---

## Related Tools

- `diary-digest.py` — Summarizes diary entries
- `daily-report.py` — Generates daily summaries
- `trim-today.py` — Keeps today.md context size manageable

---

**Created:** 2026-02-04
**Category:** Safety / Data Integrity
**Priority:** High (protects critical session history)
