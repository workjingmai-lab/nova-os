# diary-append.py — Safe Diary Updates

## What It Does

Appends work block entries to `diary.md` without overwriting existing content.

## The Problem

Using `>>` redirection from Python's `subprocess` caused race conditions where diary.md would be completely overwritten instead of appended. This tool solves that by reading the file first, then writing.

## Usage

```bash
python3 diary-append.py "Your work block text here"
```

## What It Does

1. Reads existing `diary.md` content
2. Appends new text with proper formatting
3. Writes back complete content (no overwrites)

## Example

```python
python3 diary-append.py "
### Work Block 1234

**TASK:** Revenue pipeline check
**RESULT:** $300K total pipeline
**INSIGHT:** Services have NO blockers
"
```

## Created

2026-02-04 — After work block 1473 revealed diary.md was being overwritten

## Related

- `diary.md` — Main activity log
- `today.md` — Current session memory
- `memory/YYYY-MM-DD.md` — Daily logs
