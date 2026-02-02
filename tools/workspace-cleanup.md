# workspace-cleanup.py — Smart Workspace Organization

**What it does:** Scans workspace for orphaned files, duplicates, empty directories, and old content. Organizes downloads and generates health reports. Safe dry-run mode by default.

---

## Why This Exists

**Problem:** Workspaces accumulate clutter—orphaned files, empty directories, duplicates, old downloads. Over time, this slows you down and creates confusion.

**Solution:** `workspace-cleanup.py` intelligently identifies what to keep, move, or delete based on actual usage patterns, not guesswork.

**Impact:** Keeps workspace clean and organized. Nova runs this weekly to maintain ~100 tools with zero clutter.

---

## How It Works

### Scans Performed

#### 1. Orphaned Files
Finds files not referenced by any active project or tool.
- Checks all `.py`, `.sh`, `.md`, `.json` files for references
- Protects known important directories (`tools/`, `knowledge/`, etc.)
- Identifies truly unused files

#### 2. Duplicate Files
Finds exact duplicates by content hash (MD5).
- Compares file contents, not just names
- Groups duplicates by hash
- Reports all duplicate sets

#### 3. Empty Directories
Finds directories with no files or subdirectories.
- Excludes `archive/` and `orphaned/` (intentionally empty)
- Safe to remove

#### 4. Archivable Files
Finds old files (>30 days by default) that could be archived.
- Checks `memory/` directory for old entries
- Determines if referenced in recent diary
- Suggests archiving to save space

#### 5. Downloads Organization
Organizes files in `downloads/` by type.
- PDFs → `docs/pdfs/`
- Images → `assets/images/`
- Videos → `assets/videos/`
- Archives → `archive/downloads/`

---

## Usage

### Basic Scan (Dry Run — Safe)
```bash
python3 tools/workspace-cleanup.py
```

Output:
```
🔍 Workspace Cleanup (dry_run=True)
==================================================

📊 Scan Results:
   Orphaned files: 3
   Empty directories: 2
   Duplicate groups: 1

📝 Orphaned files (not referenced anywhere):
   - old-script.py
   - test-output.txt
   - temp-draft.md

📂 Empty directories:
   - experiments/old
   - tests/run1

📑 Duplicate files:
   Hash: a1b2c3d4e5f6...
      - config.json
      - config-backup.json

✅ Report saved: .workspace_report.json
   Actions taken: 0
```

### Actually Clean (Not Dry Run)
```bash
python3 tools/workspace-cleanup.py --clean
```

This will:
- Move orphaned files to `orphaned/`
- Remove empty directories
- Log all actions taken

### Organize Downloads
```bash
python3 tools/workspace-cleanup.py --organize
```

Output:
```
Moved: report.pdf → docs/pdfs/report.pdf
Moved: screenshot.png → assets/images/screenshot.png
Moved: archive.zip → archive/downloads/archive.zip
```

### Change Archive Threshold
```bash
# Find files older than 60 days
python3 tools/workspace-cleanup.py --days 60
```

---

## Report File

After every scan, a `.workspace_report.json` file is created:

```json
{
  "timestamp": "2026-02-02T14:10:00.000000",
  "workspace": "/home/node/.openclaw/workspace",
  "stats": {
    "scanned": 150,
    "orphaned": 3,
    "archivable": 0,
    "duplicates": 2,
    "empty_dirs": 2
  },
  "actions": [
    "Moved to orphaned/: old-script.py",
    "Removed empty dir: experiments/old"
  ],
  "orphaned_files": [
    "old-script.py",
    "test-output.txt",
    "temp-draft.md"
  ],
  "empty_directories": [
    "experiments/old",
    "tests/run1"
  ],
  "duplicates": {
    "a1b2c3d4e5f6...": [
      "config.json",
      "config-backup.json"
    ]
  }
}
```

---

## Safety Features

✅ **Dry run by default** — Preview changes before executing
✅ **Protected directories** — Never touches `tools/`, `knowledge/`, `memory/`
✅ **Reference checking** — Only removes files not referenced anywhere
✅ **Orphaned directory** — Moves (not deletes) to `orphaned/` for recovery
✅ **Empty dir check** — Only removes truly empty directories

---

## Integration Examples

### Weekly Cleanup Cron
```cron
0 18 * * 0 cd /home/node/.openclaw/workspace && python3 tools/workspace-cleanup.py
```

### Before Major Reorganization
```bash
#!/bin/bash
# pre-cleanup.sh
echo "🔍 Scanning workspace before reorg..."
python3 tools/workspace-cleanup.py
echo "📊 Check .workspace_report.json for details"
read -p "Press Enter to continue with cleanup"
python3 tools/workspace-cleanup.py --clean
```

### In CI/CD Pipeline
```python
#!/usr/bin/env python3
import json
import subprocess

# Scan workspace
subprocess.run(["python3", "tools/workspace-cleanup.py"])

# Read report
report = json.loads(Path(".workspace_report.json").read_text())

# Fail if too many orphaned files
if report["stats"]["orphaned"] > 10:
    print(f"⚠️  Too many orphaned files: {report['stats']['orphaned']}")
    exit(1)
```

---

## Customization

### Change Protected Directories
Edit the `protected_dirs` set:

```python
protected_dirs = {
    "tools", "knowledge", "memory", "goals", "diary.md",
    "today.md", "heartbeat.md", "dashboard", "collab",
    "strategy", "templates",
    "my-important-dir",  # Add your own
}
```

### Add New File Organizers
Extend the `organizers` dictionary:

```python
organizers = {
    ".pdf": WORKSPACE / "docs" / "pdfs",
    ".csv": WORKSPACE / "data" / "exports",  # Add CSV
    ".json": WORKSPACE / "data" / "configs",  # Add JSON
    # ... existing organizers
}
```

### Custom Archiving Rules
Modify `find_archivable()`:

```python
def find_archivable(self, days_old: int = 30) -> List[Path]:
    archivable = []
    cutoff = datetime.now() - timedelta(days=days_old)
    
    # Check custom directories
    for dir_name in ["old-projects", "experiments", "drafts"]:
        custom_dir = WORKSPACE / dir_name
        if custom_dir.exists():
            for f in custom_dir.rglob("*"):
                if f.is_file():
                    mtime = datetime.fromtimestamp(f.stat().st_mtime)
                    if mtime < cutoff:
                        archivable.append(f)
                        self.stats["archivable"] += 1
    
    return archivable
```

---

## Technical Details

- **Language:** Python 3
- **Dependencies:** Standard library only (json, shutil, hashlib, collections)
- **Files Read:** All workspace files (scanning)
- **Files Written:** 1 (`.workspace_report.json`)
- **Files Moved:** Orphaned files to `orphaned/` (if --clean)
- **Execution Time:** ~5 seconds for 150 files

---

## Use Cases

1. **Weekly Maintenance** — Keep workspace clean and organized
2. **Pre-Deployment Cleanup** — Remove unused files before shipping
3. **Duplicate Detection** — Find and merge duplicate configs/docs
4. **Downloads Management** — Auto-organize downloaded files by type
5. **Workspace Health Checks** — Generate reports for CI/CD

---

## Best Practices

### Run Weekly (Not Daily)
Workspace cleanup is a maintenance task, not a continuous process. Run weekly to catch accumulating clutter.

### Review Report Before Cleaning
Always check `.workspace_report.json` before running with `--clean`. Make sure you agree with the proposed actions.

### Recover from Orphaned Directory
If you accidentally move a file you need:
```bash
# Restore from orphaned/
mv orphaned/important-file.py .
```

### Keep Downloads Clean
Use `--organize` regularly to prevent `downloads/` from becoming a dumping ground.

---

## Version History

- **v1.0** (2026-02-01) — Initial release for workspace maintenance
- Integrated into Nova's weekly cleanup routine

---

*Created by Nova — autonomous agent building autonomous systems*
