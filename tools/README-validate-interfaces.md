# validate-interfaces.py

Quick linter for Nova's "files as interface" approach.

## What It Does

Checks workspace interface files for consistency:
- **diary.md**: Duplicate Work Block IDs + timestamp presence
- **JSON files**: Recommended top-level keys (`version`, `lastUpdated`)

## Usage

```bash
# Check all default paths
python3 tools/validate-interfaces.py

# Add custom JSON glob patterns
python3 tools/validate-interfaces.py --json-glob 'custom/**/*.json'
```

## Exit Codes

- `0` = No warnings
- `1` = Warnings found

## Default Paths Checked

- `diary.md`
- `status/**/*.json`
- `notifications/**/*.json`
- `memory/**/*.json`
- `.heartbeat_state.json`

## Checks Performed

### diary.md
- Detects duplicate Work Block IDs with line numbers
- Ensures UTC timestamps exist (`...Z` format)

### JSON files
- Recommends `version` field for schema tracking
- Recommends `lastUpdated` field in ISO-8601 format

## Why This Matters

Interface consistency = reliable tooling. Duplicate work block IDs break tracking. Missing version fields make schema evolution fragile.

---

**Work Block:** #955  
**Created:** 2026-02-03T06:04Z
