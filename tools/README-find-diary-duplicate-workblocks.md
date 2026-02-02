# Find Diary Duplicate Workblocks

Detect duplicate work block IDs in diary.md for cleanup and renumbering.

## Features

- **Duplicate detection** — Finds repeated work block numbers
- **Line reporting** — Shows exact line numbers for each duplicate
- **Context display** — Shows header text for manual review
- **Safe detection** — Conservative pattern matching avoids false positives
- **Exit codes** — Script-friendly (0=clean, 1=error, 2=duplicates found)

## Usage

```bash
# Check default diary.md
python3 tools/find-diary-duplicate-workblocks.py

# Check specific file
python3 tools/find-diary-duplicate-workblocks.py /path/to/diary.md

# Use in scripts (exit codes)
if ! python3 tools/find-diary-duplicate-workblocks.py; then
    echo "Duplicates found, needs cleanup"
fi
```

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | No duplicates found (clean) |
| 1 | File not found or error |
| 2 | Duplicates detected (needs cleanup) |

## Example Output

**Clean diary:**
```
OK: no duplicate Work Block IDs detected
```

**Duplicates found:**
```
DUPLICATE Work Block IDs detected:

- Work Block 42 appears 2 times
    line 156: ## [WORK BLOCK 42 — 2026-02-01T12:00Z] Task completed
    line 234: ## [WORK BLOCK 42 — 2026-02-01T15:30Z] Another task

- Work Block 87 appears 2 times
    line 445: [WORK BLOCK 87] Something done
    line 512: WORK BLOCK 87: Different thing

Next: decide a renumbering policy (e.g., keep earliest occurrence, renumber later ones),
then implement a safe patcher that updates both headers and any internal references.
```

## Pattern Matching

Detects work blocks in multiple formats:
- `Work Block 123`
- `WORK BLOCK 123`
- `Work Block #123`

**Excludes** timestamp formats like:
- `WORK BLOCK — 2026-02-02...`

## Use Cases

1. **Data validation** — Ensure diary.md integrity
2. **Cleanup preparation** — Identify blocks before renumbering
3. **CI integration** — Fail builds if duplicates detected
4. **Manual review** — Get line numbers for direct editing

## Renaming Strategy

When duplicates are found, choose a policy:
1. **Keep earliest** — Preserve first occurrence, renumber later ones
2. **Keep latest** — Preserve most recent, renumber earlier ones
3. **Manual merge** — Combine content, delete duplicate

Then update:
- Work block headers
- Any internal references to block numbers

## Created

2026-02-02 — Data integrity tool for diary.md maintenance
