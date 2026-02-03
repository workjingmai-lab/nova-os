# workspace-cleanup.py — Workspace Maintenance & Cleanup

**Version:** 1.0  
**Category:** Maintenance / Workspace  
**Created:** 2026-02-01

---

## What It Does

Cleans up workspace: removes temporary files, compresses old logs, and reorganizes misplaced files.

### Features

- Remove temp files (*.tmp, *.temp, .DS_Store)
- Compress logs older than N days
- Archive old diary entries
- Find and report large files
- Reorganize misplaced files
- Dry-run mode for safe testing

---

## Usage

```bash
# Preview what would be cleaned (safe)
python3 tools/workspace-cleanup.py --dry-run

# Clean temp files
python3 tools/workspace-cleanup.py --temp

# Compress logs older than 30 days
python3 tools/workspace-cleanup.py --compress-logs --days 30

# Archive old diary entries
python3 tools/workspace-cleanup.py --archive-diary --months 6

# Find large files (>100MB)
python3 tools/workspace-cleanup.py --large-files --size 100

# Full cleanup (all operations)
python3 tools/workspace-cleanup.py --all
```

---

## Operations

| Operation | Description | Safety |
|-----------|-------------|--------|
| `--temp` | Remove temp files | Safe (reversible if committed) |
| `--compress-logs` | Gzip old logs | Safe (files preserved) |
| `--archive-diary` | Move old diary to archive/ | Safe (files preserved) |
| `--large-files` | Report large files | Read-only |
| `--all` | Run all operations | Use `--dry-run` first |

---

## What It Cleans

**Temp files:**
- `*.tmp`, `*.temp`, `*.bak`
- `.DS_Store`, `Thumbs.db`
- `*.pyc`, `__pycache__/`
- `.pytest_cache/`, `.coverage`

**Old logs:**
- `logs/*.log` older than N days
- Compressed to `.gz` format

**Old diary entries:**
- `memory/YYYY-MM-DD.md` older than N months
- Moved to `memory/archive/`

---

## Output

```bash
$ python3 tools/workspace-cleanup.py --dry-run

🔍 WORKSPACE CLEANUP (DRY RUN)
────────────────────────────────────────────────────────────
Temp files: 23 found (15.2 MB)
  • .DS_Store (3 files)
  • *.tmp (12 files)
  • __pycache__ (8 directories)

Old logs: 45 found (234 MB)
  • Compressible: 42 (older than 30 days)

Large files: 3 found
  • reports/archive.tar.gz (245 MB)
  • logs/old-run.log (112 MB)
  • public/export.zip (89 MB)

Run without --dry-run to execute cleanup.
```

---

## Dependencies

- Python 3.7+
- Standard library only

---

## Configuration

Edit defaults:

```python
TEMP_PATTERNS = ['*.tmp', '*.temp', '.DS_Store', '*.pyc']
LOG_RETENTION_DAYS = 30
DIARY_ARCHIVE_MONTHS = 6
LARGE_FILE_THRESHOLD_MB = 100
```

---

## Integration

- Pair with `workspace-health.sh` for health checks
- Use `workspace-organizer.py` for structural analysis
- Schedule via cron weekly for maintenance

---

## Tips

1. Always run `--dry-run` first
2. Commit important changes before cleanup
3. Review large files before deleting
4. Archive rather than delete when possible
5. Schedule cleanup during low-activity hours
