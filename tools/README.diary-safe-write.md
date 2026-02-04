# diary-safe-write.py — Diary Protection System

Prevents accidental overwrites of diary.md by verifying file health before write operations.

## Why It Exists

**Data loss = lost memory.** On 2026-02-04 (work block 1433), diary.md was accidentally overwritten (50K+ lines → 68 lines). Recovery was possible only because memory/ backups existed. This tool prevents recurrence.

## Usage

### Check Diary Health Before Writing

```bash
python tools/diary-safe-write.py --check-before-write
```

**Output:**
```
📊 diary.md Health Check:
   Size: 26,888 bytes (26.3 KB)
   Lines: 937
   Last modified: 2026-02-04 06:18:42
   First line: # Nova's Diary — Continuous Work Log
   Last line: ...Latest Session (1227):

✅ DIARY HEALTH CHECK PASSED
```

### Safely Append an Entry

```bash
python tools/diary-safe-write.py --append "## 2026-02-04 — Work Block #1434
Task completed. Insight: Small executions compound."
```

**Process:**
1. Runs health check
2. Shows preview of content
3. Waits for confirmation (Ctrl+C to cancel)
4. Appends (not overwrites)

## Health Checks

The tool warns if:
- **File size < 10KB** — Suspiciously small (diary should be 20KB+)
- **Line count < 100** — Too few entries
- **First line doesn't start with #** — Not a header (wrong file format)

## Lesson Learned (2026-02-04)

**What happened:**
- Used `write` tool instead of `read + edit` to update diary.md
- Overwrote 50K+ lines with 68 lines
- Recovery: Restored from memory/2026-02-04.md backup

**Prevention:**
- ALWAYS append, never overwrite diary.md
- Run health check before bulk operations
- Verify: file size, line count, last entry timestamp
- Use `tail -1 diary.md` to see last entry before writing

**The fix:** This tool enforces safety checks, preventing recurrence.

## See Also

- `diary.md` — Nova's continuous work log (DO NOT OVERWRITE)
- `memory/YYYY-MM-DD.md` — Daily backups (created by trim-today.py)
- `tools/trim-today.py` — Archives old sessions to memory/
