# validate-interfaces.py

**Quick linter for Nova's "files as interface" approach.**

Validates diary.md and JSON state files for consistency, proper formatting, and best practices. Catches duplicates, missing timestamps, and malformed data before it becomes technical debt.

---

## Overview

Files are interfaces. When you rely on files for state, logging, and communication, consistency matters. This tool validates those interfaces preventively.

## What It Checks

### diary.md Validation
- **Duplicate Work Block IDs:** Detects reused block numbers (breaks reference integrity)
- **Timestamp presence:** Ensures ISO 'Z' timestamps exist for grep/diff tooling
- **Line number reporting:** Shows exact locations for easy cleanup

### JSON State File Validation
- **Top-level keys:** Recommends `version` and `lastUpdated` for compatibility
- **lastUpdated format:** Validates ISO-8601 timestamps
- **JSON validity:** Catches syntax errors before runtime

### Default File Patterns
Scans these locations:
- `status/**/*.json`
- `notifications/**/*.json`
- `memory/**/*.json`
- `.heartbeat_state.json`

## Use Cases

- **Pre-commit checks:** Validate before pushing to GitHub
- **CI integration:** Catch interface drift in automated workflows
- **Data integrity:** Ensure state files are parseable and versioned
- **Migration safety:** Validate after file format changes

## Usage

### Basic Validation

```bash
python3 tools/validate-interfaces.py
```

### Custom JSON Patterns

```bash
python3 tools/validate-interfaces.py --json-glob 'data/**/*.json'
```

### Multiple Patterns

```bash
python3 tools/validate-interfaces.py \
  --json-glob 'outreach/**/*.json' \
  --json-glob 'reports/**/*.json'
```

### Exit Codes

- **0:** No warnings (all interfaces valid)
- **1:** Warnings found (check output)

## Output Examples

### No Issues

```bash
$ python3 tools/validate-interfaces.py
OK: no interface warnings
```

### Duplicate Work Blocks

```bash
$ python3 tools/validate-interfaces.py
[diary] diary.md: Duplicate Work Block ids detected: 123 @ lines 45,67,89; 456 @ lines 12,34(+2 more)
```

### Missing JSON Keys

```bash
$ python3 tools/validate-interfaces.py
[json] status/heartbeat-state.json: Missing recommended top-level keys: version, lastUpdated
```

### Invalid Timestamp

```bash
$ python3 tools/validate-interfaces.py
[json] memory/2026-02-01.json: lastUpdated exists but is not ISO-8601 compatible
```

## Integration Examples

### Git Hook (pre-commit)

Create `.git/hooks/pre-commit`:

```bash
#!/bin/bash
python3 tools/validate-interfaces.py
if [ $? -ne 0 ]; then
  echo "❌ Interface validation failed. Fix issues before committing."
  exit 1
fi
```

### GitHub Actions

```yaml
name: Validate Interfaces
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run validator
        run: python3 tools/validate-interfaces.py
```

### Cron Job

```bash
# Check interfaces every hour
0 * * * * cd /home/node/.openclaw/workspace && python3 tools/validate-interfaces.py
```

## Validation Rules

### diary.md

**Rule 1: Work Block IDs must be unique**
- Duplicates break reference integrity
- Tool reports line numbers for easy cleanup
- Example: `## 🔥 WORK BLOCK #123` and `## 🔥 WORK BLOCK #123` → conflict

**Rule 2: ISO 'Z' timestamps required**
- Format: `2026-02-02T19:57Z` or `2026-02-02 19:57Z`
- Enables grep/sort/diff tooling
- Example: `2026-02-02T19:57Z` ✅ | `Feb 2, 2026` ❌

### JSON Files

**Rule 1: Top-level `version` recommended**
- Enables format migration and backward compatibility
- Example: `{"version": "1.0.0", "data": {...}}`

**Rule 2: Top-level `lastUpdated` recommended**
- Tracks file freshness for automation
- Format: ISO-8601 with Z suffix
- Example: `{"lastUpdated": "2026-02-02T19:57Z", ...}`

**Rule 3: `lastUpdated` must be ISO-8601**
- Parseable by standard datetime libraries
- Example: `2026-02-02T19:57Z` ✅ | `2/2/26` ❌

## Data Structures

### Finding Object

```python
@dataclass
class Finding:
    kind: str      # "diary" or "json"
    path: str      # Absolute file path
    message: str   # Human-readable issue description
```

## Best Practices

### Diary.md
- **Increment Work Block IDs:** Never reuse numbers
- **Timestamp everything:** Use `datetime.now().isoformat() + "Z"`
- **Consistent format:** Follow existing patterns

### JSON Files
- **Version your schemas:** `{"version": "1.0.0", ...}`
- **Track updates:** `{"lastUpdated": "2026-02-02T19:57Z", ...}`
- **Validate early:** Run this tool before commits

## Troubleshooting

### Issue: "Duplicate Work Block ids"
**Fix:** Search diary.md for duplicate IDs, renumber sequentially
```bash
grep "WORK BLOCK #" diary.md | sort
```

### Issue: "Missing recommended top-level keys"
**Fix:** Add to JSON file:
```json
{
  "version": "1.0.0",
  "lastUpdated": "2026-02-02T19:57Z",
  ...
}
```

### Issue: "lastUpdated exists but is not ISO-8601"
**Fix:** Use Python datetime:
```python
from datetime import datetime
ts = datetime.utcnow().strftime("%Y-%m-%dT%H:%MZ")
```

## Limitations

- **Line numbers:** Approximate for Work Block IDs (first 5 shown)
- **Timestamp regex:** Basic ISO 'Z' detection (doesn't validate full ISO-8601)
- **JSON validation:** Doesn't validate custom schemas, only presence of recommended keys

## Future Enhancements

- [ ] Custom schema validation (JSON Schema definitions)
- [ ] Auto-fix for simple issues (renumber Work Blocks)
- [ ] Markdown link validation
- [ ] Cross-file reference checking (e.g., `[ref:WORK_BLOCK_123]`)
- [ ] Integration with pre-commit hooks framework

---

**Version:** 1.0.0
**Created:** 2026-02-02
**Category:** Quality Assurance
**Dependencies:** Python 3.7+ (standard library only)
**Exit codes:** 0 (OK), 1 (warnings found)
