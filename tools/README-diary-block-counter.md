# diary-block-counter.py

Accurately count work blocks from diary.md with multiple pattern detection.

## Usage

```bash
# Count blocks in today's diary
python3 tools/diary-block-counter.py

# Count blocks in specific file
python3 tools/diary-block-counter.py memory/2026-02-06.md
```

## Why This Exists

Different diary formats over time:
- `### Work Block N — timestamp` (current format)
- `Work block N: description` (bullet format, older)
- Session summary stats

This tool tries all patterns and returns the best estimate.

## Output Example

```
📊 Counting work blocks in: memory/2026-02-07.md

  Pattern matches:
    '### Work Block N —' headers: 25
    'Work block N:' bullets:      0
    'Work Block N —' mentions:    25

  Derived stats:
    Max block number found:       25
    Latest 'completed' stat:      0

  ✅ Best estimate: 25 work blocks
```

## Patterns Detected

1. **Headers:** `### Work Block 25 — 3:53 AM UTC`
2. **Bullets:** `- Work block 1024: task description`
3. **Max number:** Highest block number found
4. **Session stats:** "Blocks completed: N" from summaries
