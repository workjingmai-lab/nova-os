# pattern-peek.py

**Purpose:** Quick pattern scan of any text file — find regex patterns, count occurrences, see matches.

## What It Does

- **Scans files** — Searches for regex patterns in any text file
- **Counts occurrences** — Shows how many times each pattern appears
- **Displays matches** — Shows first 10 matches or line numbers
- **Default patterns** — Built-in patterns for common work patterns

## When to Use It

**Use when:**
- Searching diary.md for specific patterns
- Counting occurrences of tasks, insights, or work blocks
- Finding lines matching custom regex patterns
- Quick analysis without reading entire file

## Usage

```bash
# Scan with default patterns
python3 tools/pattern-peek.py diary.md

# Scan with custom pattern
python3 tools/pattern-peek.py diary.md "Work Block \d+"

# Search for insights
python3 tools/pattern-peek.py diary.md "Key Insight: (.+)"
```

## Output Format

**Default patterns:**
```
Pattern Scan Results:
  Work Blocks: 591
  Insights: 23
  Files Created: 15
  Tasks: 591
  Session Complete: 8
```

**Custom pattern:**
```
Pattern: Work Block \d+
Count: 591

First 10 matches:
  - Work Block 582
  - Work Block 583
  - Work Block 584
  - Work Block 585
  - Work Block 586
  - Work Block 587
  - Work Block 588
  - Work Block 589
  - Work Block 590
  - Work Block 591
```

**Pattern without capturing group:**
```
Pattern: ERROR
Count: 5

Found at lines: [42, 87, 156, 234, 289]
```

## Default Patterns

Built-in patterns for work analysis:

| Pattern Name | Regex | What It Counts |
|--------------|-------|----------------|
| Work Blocks | `Work Block \d+` | Numbered work block entries |
| Insights | `Key Insight: (.+)` | Key insight lines |
| Files Created | `Files Created: (.+)` | File creation entries |
| Tasks | `\*\*Task:\*\* (.+)` | Task descriptions |
| Session Complete | `SESSION COMPLETE` | Session completion markers |

## Custom Patterns

Any regex pattern works:

```bash
# Find all timestamps
python3 tools/pattern-peek.py diary.md "\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z"

# Find markdown headers
python3 tools/pattern-peek.py diary.md "^#+\s+.+"

# Find TODO/FIXME comments
python3 tools/pattern-peek.py diary.md "(TODO|FIXME):"
```

## Why It Matters

**Quick answers without grep complexity.** This tool helps you:
- **Count fast** — How many work blocks this week?
- **Find patterns** — Where did I write about X?
- **Analyze trends** — Am I completing more sessions?
- **Search smart** — Regex power without grep syntax

**For autonomous agents:** Get quantitative insights from your logs without full analysis pipeline.

## Integration

- **Daily review:** Scan diary.md for yesterday's patterns
- **Goal tracking:** Count completed tasks or work blocks
- **Trend analysis:** Track pattern frequency over time
- **Quick search:** Find specific entries without reading everything

## Examples

**Count today's work blocks:**
```bash
python3 tools/pattern-peek.py diary.md "Work Block \d+" | grep "Count:"
```

**Find all insights:**
```bash
python3 tools/pattern-peek.py diary.md "Key Insight: (.+)"
```

**Check for errors:**
```bash
python3 tools/pattern-peek.py diary.md "ERROR|FAIL"
```

**Find all URLs:**
```bash
python3 tools/pattern-peek.py diary.md "https?://[^\s]+"
```

## Requirements

- **Python 3.7+** — For pathlib and regex
- **Text file** — Any readable text file (diary.md, logs, etc.)

## Limitations

- **First 10 matches only** — For large result sets, shows subset
- **Case-insensitive** — All searches ignore case by default
- **No multiline** — Patterns don't span multiple lines

## Future Enhancements

Could be extended to:
- **Context display** — Show lines around matches
- **File filtering** — Scan multiple files at once
- **Output formats** — JSON, CSV export
- **Trend tracking** — Compare pattern counts over time

---

*Created: Week 2 — Part of quick analysis tools*
