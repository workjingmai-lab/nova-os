# find-diary-duplicate-workblocks.py

**Purpose:** Find duplicate Work Block IDs in diary.md — maintain data integrity for work tracking.

## What It Does

- **Scans diary.md** — Searches for Work Block IDs using regex pattern matching
- **Detects duplicates** — Reports which Work Block numbers appear multiple times
- **Shows line numbers** — Displays exact line locations for each duplicate
- **Provides context** — Shows nearby header text for safe renumbering

## When to Use It

**Run when:**
- Validating diary.md integrity
- Preparing reports or analytics from work logs
- Suspecting work block numbering errors
- Before running diary analysis tools

## Usage

```bash
# Check diary.md for duplicates
python3 tools/find-diary-duplicate-workblocks.py

# Check specific file
python3 tools/find-diary-duplicate-workblocks.py /path/to/diary.md
```

## Output Format

**No duplicates:**
```
OK: no duplicate Work Block IDs detected
```

**Duplicates found:**
```
DUPLICATE Work Block IDs detected:

- Work Block 123 appears 2 times
    line 45: ## [WORK BLOCK] 2026-02-02T10:15:00Z — Work Block 123
    line 67: ## [WORK BLOCK] 2026-02-02T10:15:00Z — Work Block 123

- Work Block 456 appears 3 times
    line 89: ## [WORK BLOCK] 2026-02-02T11:20:00Z — Work Block 456
    line 112: ## [WORK BLOCK] 2026-02-02T11:45:00Z — Work Block 456
    line 134: ## [WORK BLOCK] 2026-02-02T12:00:00Z — Work Block 456

Next: decide a renumbering policy (e.g., keep earliest occurrence, renumber later ones),
then implement a safe patcher that updates both headers and any internal references.
```

## Pattern Matching

Matches these formats (case-insensitive):
- `Work Block 123`
- `WORK BLOCK 123`
- `Work Block #123`

**Avoids matching:**
- Timestamps like `WORK BLOCK — 2026-02-02T13:00:00Z`

## Exit Codes

- **0:** No duplicates found
- **1:** File not found
- **2:** Duplicates detected

## Why It Matters

**Data integrity matters.** Duplicate Work Block IDs cause:
- **Inaccurate counts** — Work block totals will be wrong
- **Analysis errors** — Time calculations will be incorrect
- **Confusion** — Can't distinguish between different blocks
- **Report corruption** — Analytics will have duplicate entries

**For autonomous agents:** Maintain clean data. Detect and fix duplicates before they propagate into analytics.

## Integration

- **Pre-analysis validation:** Run before generating reports
- **CI/CD checks:** Add to validation pipelines
- **Data hygiene:** Run weekly to catch duplicates early
- **Manual review:** Check after manual diary edits

## Renaming Strategy

When duplicates are found, you have options:

1. **Keep earliest, renumber rest** — Preserve original block, renumber duplicates
2. **Renumber all** — Assign completely new IDs to all duplicates
3. **Merge into one** — Combine duplicate entries (if they're the same work)

**Example fix:**
```bash
# Manual renumbering (be careful!)
sed -i 's/Work Block 123/Work Block 124/g' diary.md
```

## Automation Potential

Could be extended to:
- **Auto-fix mode** — Automatically renumber duplicates
- **Interactive mode** — Ask which occurrence to keep
- **Reference updating** — Update internal cross-references
- **Validation mode** — Check for gaps in numbering

## Requirements

- **Python 3.7+** — For type hints and dataclasses
- **diary.md** — Work log in standard Nova format

---

*Created: Week 2 — Part of data validation infrastructure*
