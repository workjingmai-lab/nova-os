# workspace-organizer.py — Workspace Structure Analysis

**Purpose:** Scan workspace/, report on file organization, detect duplicates, and suggest improvements.

**Created:** Week 1 (2026-01-31)
**Usage:** ~3-5 times (workspace health checks)

## What It Does

- **Scans entire workspace** — Counts files, directories, extensions
- **Categorizes by directory** — Shows which folders have most files
- **Finds largest files** — Reports top 10 by size
- **Detects duplicates** — SHA256 hashing to find identical files
- **Saves JSON report** — `reports/workspace-scan-{pid}.json`

## Usage

```bash
python3 tools/workspace-organizer.py
```

## Output

**Console:**
- Total files/directories
- Top 5 directories by file count
- Top 10 file extensions
- Largest 5 files (with size in MB)
- Potential duplicates (if any found)

**JSON Report:**
```json
{
  "total_files": 1200,
  "total_dirs": 85,
  "top_extensions": {".py": 150, ".md": 200},
  "top_dirs": {"tools/": 112, "docs/": 45},
  "potential_duplicates": [...]
}
```

## Dependencies

- Python 3.8+
- pathlib, hashlib, json, collections (stdlib only)

## Why This Matters

Workspace health = productivity velocity.
- **Duplicate detection** saves disk space and reduces confusion
- **File distribution** reveals structural issues (e.g., cluttered root)
- **Extension tracking** shows tech stack distribution

## Example Output

```
🔍 Workspace Organizer — Scan starting...

📊 Overview:
   Files: 1247
   Dirs: 89

📁 Top directories by file count:
   tools/: 112 files
   docs/: 45 files
   memory/: 32 files

📄 File extensions:
   .py: 120 files
   .md: 85 files
   .json: 12 files

💾 Largest files:
   data/export.json: 45.2 MB
   models/weights.pt: 128.7 MB

✅ No duplicates detected!
✅ Report saved: reports/workspace-scan-12345.json
```

## Related Tools

- `swarm-monitor.py` — Multi-agent collaboration tracking
- `diary-digest.py` — Pattern analysis
