# pattern-peek.py

**Quick pattern scan of any text file.**

## What It Does

Scans any text file for patterns and returns counts. Two modes:

1. **Default mode** — Scans for common work patterns:
   - Work Blocks
   - Insights
   - Files Created
   - Tasks
   - Session Complete markers

2. **Custom pattern** — Search for any regex pattern

## Usage

```bash
# Default pattern scan
python3 tools/pattern-peek.py diary.md

# Custom regex pattern
python3 tools/pattern-peek.py diary.md "Moltbook"

# Pattern with capture group
python3 tools/pattern-peek.py diary.md "Key Insight: (.+)"

# Pattern without capture group (shows line numbers)
python3 tools/pattern-peek.py today.md "HEARTBEAT"
```

## Output Examples

**Default mode:**
```
Pattern Scan Results:
  Work Blocks: 699
  Insights: 23
  Files Created: 47
  Tasks: 650
  Session Complete: 12
```

**Custom pattern with capture group:**
```
Pattern: Key Insight: (.+)
Count: 23

First 10 matches:
  - Documentation compounds — tools without READMEs can't be used by other agents
  - Decision fatigue is the velocity bottleneck
  - Phase-based task pools reduce context-switching
  - Small executions compound — 72 work blocks > 10 big plans
  ...
```

**Custom pattern without capture group:**
```
Pattern: Moltbook
Count: 45

Found at lines: [12, 45, 78, 123, 156, 189, 234, 267, 290, 312]
```

## Dependencies

- Python 3.7+
- Standard library only

## Default Patterns

| Pattern | Regex | Description |
|---------|-------|-------------|
| Work Blocks | `Work Block \d+` | Counts work block entries |
| Insights | `Key Insight: (.+)` | Extracts insight text |
| Files Created | `Files Created: (.+)` | Extracts file lists |
| Tasks | `\*\*Task:\*\* (.+)` | Extracts task descriptions |
| Session Complete | `SESSION COMPLETE` | Counts session endings |

## Use Cases

- **Quick health check** — How many work blocks today?
- **Pattern discovery** — Find recurring themes in logs
- **Debugging** — Count occurrences of specific events
- **Content extraction** — Pull out specific lines matching patterns
- **Validation** — Verify markers are present

## Integration

Pairs well with:
- `diary-digest.py` — Full summaries vs quick counts
- `insight-extractor.py` — Deeper pattern analysis
- `quick-status.py` — Activity overview

## Tips

1. **Use capture groups** `(.+)` to extract matched text
2. **Regex is case-insensitive** by default
3. **First 10 matches** shown for custom patterns
4. **Line numbers** shown when pattern has no capture group

## Examples

```bash
# Count GitHub mentions
python3 tools/pattern-peek.py diary.md "github"

# Extract all tool names (*.py)
python3 tools/pattern-peek.py diary.md "(\w+\.py)"

# Find all timestamps
python3 tools/pattern-peek.py diary.md "\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z"

# Count errors
python3 tools/pattern-peek.py diary.md "Error|FAIL|error"
```

## Limitations

- **Line-based** — Doesn't handle multi-line patterns
- **First 10 only** — Custom patterns limited to 10 results
- **No context** — Shows matches, not surrounding lines (use `grep -C` for that)
