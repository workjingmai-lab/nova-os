# workspace-cleanup.py

**Smart workspace organization and cleanup**

Keeps your workspace clean by identifying orphaned files, empty directories, duplicates, and archiving old content.

---

## What It Does

- 🔍 **Scans for orphaned files** — Files not referenced by any active project or tool
- 📁 **Finds empty directories** — Identifies and removes unused folders
- 📑 **Detects duplicates** — Finds duplicate files by content hash
- 🗄️ **Organizes downloads** — Moves downloaded files to appropriate directories
- 📊 **Health reports** — Generates comprehensive workspace health metrics

---

## When to Use It

**Weekly maintenance:**
```bash
# Dry run (safe, shows what would happen)
python tools/workspace-cleanup.py

# Actually clean up
python tools/workspace-cleanup.py --clean
```

**Organize downloads:**
```bash
python tools/workspace-cleanup.py --organize
```

**Custom archive threshold:**
```bash
# Archive files older than 60 days
python tools/workspace-cleanup.py --days 60
```

---

## What It Protects

The tool **never touches**:
- Core workspace files (`today.md`, `diary.md`, `heartbeat.md`)
- Protected directories (`tools/`, `knowledge/`, `memory/`, `goals/`)
- Hidden files (`.git`, `.env`)
- Documentation files (`.md` files are assumed important)

---

## Reports

After each run, it generates `.workspace_report.json` with:
- Scan statistics (orphaned, empty dirs, duplicates)
- List of orphaned files found
- Empty directories identified
- Duplicate file groups
- Actions taken (if not dry run)

---

## Examples

**Find what needs cleanup:**
```bash
python tools/workspace-cleanup.py
# Output:
# 🔍 Workspace Cleanup (dry_run=True)
# ==================================================
# 📊 Scan Results:
#    Orphaned files: 3
#    Empty directories: 2
#    Duplicate groups: 0
```

**Actually clean:**
```bash
python tools/workspace-cleanup.py --clean
# Moves orphaned files to orphaned/
# Removes empty directories
# Updates .workspace_report.json
```

---

## Tips

1. **Always dry run first** — See what would be affected before cleaning
2. **Check the report** — `.workspace_report.json` has full details
3. **Run weekly** — Prevents clutter from accumulating
4. **Organize downloads** — Use `--organize` after downloading resources
5. **Custom archive age** — Adjust `--days` based on your workflow

---

## Integration

**Add to weekly heartbeat:**
```bash
# In HEARTBEAT.md or cron job
python tools/workspace-cleanup.py
python tools/workspace-cleanup.py --organize
```

**Check workspace health:**
```python
import json
report = json.loads(open(".workspace_report.json").read())
print(f"Orphaned: {report['stats']['orphaned']}")
print(f"Empty dirs: {report['stats']['empty_dirs']}")
```

---

## Stats

- **Size:** ~200 lines, ~7KB
- **Dependencies:** Standard library only
- **Risk:** Low (dry run by default)
- **Frequency:** Weekly maintenance

---

*Workspace organization = mental clarity. Clean workspace, clear mind.*
