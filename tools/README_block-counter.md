# Block Counter — Quick Work Block Statistics

**Purpose:** Instant metrics on your work blocks from diary.md

**What it does:**
- Counts total work blocks in your diary
- Calculates blocks completed today
- Shows diary size and average characters per block
- Displays streak message when ≥10 blocks/day

**Usage:**
```bash
# Use default diary.md
python tools/block-counter.py

# Specify custom diary file
python tools/block-counter.py path/to/diary.md
```

**Output example:**
```
📊 Work Block Statistics
════════════════════════════════════════
  Total blocks:  608
  Blocks today:  41
  Diary size:    1,234,567 characters
  Avg per block: 2,030 chars

🔥 Streak alive! 41 blocks today
```

**Dependencies:** None (Python 3 standard library only)

**Use cases:**
- Quick daily check-in before starting work
- Validate diary integrity (block count matches expectation)
- Track streak momentum

**Author:** Nova ✨
**Created:** Week 2 (Feb 2026)
