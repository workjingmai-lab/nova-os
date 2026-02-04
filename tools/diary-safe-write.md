# diary-safe-write.py

Diary safety helper — prevents accidental overwrites by verifying file health before writes.

## What It Does

- Checks diary.md health (size, line count, format) before write operations
- Appends entries safely with confirmation prompt
- Warns on suspicious file states (too small, malformed)

## Usage

```bash
# Check diary health before writing
python tools/diary-safe-write.py --check-before-write

# Append content with safety checks
python tools/diary-safe-write.py --append "New entry here"
```

## Why It Exists

Prevents catastrophic diary.md overwrites by validating file state first. Catches issues like:
- Suspiciously small file size
- Missing headers
- Low line counts

Use before any automated diary writes to ensure data safety.

---

*Created: Week 2 | Category: Workflow*
