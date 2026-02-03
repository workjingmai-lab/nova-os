# workspace-health.sh — Workspace Health & Maintenance

**Version:** 1.0  
**Category:** System Maintenance  
**Created:** 2026-02-01

---

## What It Does

Checks workspace health: disk usage, file counts, broken links, large files, and git status. Provides warnings and suggestions.

### Features

- Disk usage check (warns at 80%, critical at 90%)
- File count by directory
- Broken symlink detection
- Large file identification (>100MB)
- Git status summary
- Cleanup recommendations

---

## Usage

```bash
# Run health check
./tools/workspace-health.sh

# Run with quiet output (warnings only)
./tools/workspace-health.sh --quiet

# Generate report file
./tools/workspace-health.sh --report reports/health-2026-02-02.txt
```

---

## What It Checks

| Check | Warning | Critical |
|-------|---------|----------|
| Disk usage | 80% | 90% |
| Git uncommitted changes | 50 files | 100 files |
| Broken symlinks | Any | — |
| Large files | 100MB | 500MB |
| Old temp files | 7 days | 30 days |

---

## Dependencies

- Standard Unix tools (`df`, `find`, `git`, `du`)

---

## Output Example

```
=== Workspace Health Check ===
Disk usage: 78% (warning threshold: 80%)
Git status: 12 uncommitted files
Broken symlinks: 0
Large files: 1 (reports/archive.tar.gz, 245MB)
Temp files older than 7 days: 3

Recommendations:
- Consider archiving large files
- Commit pending changes
- Clean old temp files
```

---

## Integration

- Pair with `heartbeat-check.sh` for system-level monitoring
- Use `workspace-cleanup.py` for automated cleanup
- Schedule via cron weekly for proactive maintenance

---

## Tips

1. Run weekly to catch issues early
2. Archive old logs and reports to free space
3. Use `git gc` to clean repository if needed
4. Monitor temp directories to prevent bloat
