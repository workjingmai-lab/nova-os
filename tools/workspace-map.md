# workspace-map.py

Generate a visual tree map of your workspace with file statistics.

## What It Does

`workspace-map.py` creates a tree view of your workspace directory structure, plus file counts by type, size statistics, and key highlights. Helps you understand what's in your workspace at a glance.

## Usage

```bash
# Map entire workspace (default)
python3 tools/workspace-map.py

# Map specific directory
python3 tools/workspace-map.py --dir /path/to/directory
```

## Example Output

```bash
$ python3 tools/workspace-map.py

🗂️ WORKSPACE MAP
============================================================

📊 Statistics:
  Total files: 523
  Total size: 1842.3 KB

📁 Top File Types:
  • .py: 112 files (412.5 KB)
  • .md: 87 files (328.1 KB)
  • .json: 43 files (156.7 KB)
  • .jsonl: 24 files (892.4 KB)
  • .txt: 18 files (12.3 KB)
  • .html: 12 files (45.6 KB)
  • .sh: 8 files (8.9 KB)
  • .sol: 5 files (15.2 KB)
  • no_ext: 3 files (2.1 KB)
  • .toml: 2 files (4.5 KB)

🌳 Directory Structure (partial):
├── dashboard/
│   └── index.html
├── docs/
│   ├── index.html
│   └── skills/
├── goals/
│   ├── active.md
│   ├── week-1.md
│   └── week-2.md
├── knowledge/
│   ├── agent-communication.md
│   └── autonomous-work-loops.md
├── logs/
│   └── heartbeats/
├── reports/
│   └── patterns-2026-02-01.md
├── tools/
│   ├── goal-tracker.py
│   ├── diary-digest.py
│   └── ... (107 more files)
├── AGENTS.md
├── diary.md
├── MEMORY.md
└── today.md
```

## Features

- **Directory tree** — Visual representation of workspace structure
- **File type breakdown** — Top 10 file types with counts and sizes
- **Size statistics** — Total files and storage used
- **Smart filtering** — Skips hidden files/directories (`.git`, `.env`, etc.)
- **Depth control** — Limits tree depth for readability
- **Per-directory mode** — Map any directory, not just workspace root

## Use Cases

- **Onboarding** — Show new collaborators what's in the workspace
- **Cleanup** — Find large files or unexpected directories
- **Audit** — Quick check of workspace composition
- **Documentation** — Include in README for project structure overview

## Customization

Adjust `max_depth` in `generate_tree()` to show more/less detail:

```python
tree = generate_tree(workspace, max_depth=4, prefix="")  # Deeper tree
```

Adjust file limit in tree generation:

```python
for i, f in enumerate(files[:10]):  # Show 10 files instead of 5
```

## Why This Matters

**Visibility = organization.** You can't organize what you can't see. A workspace map helps you:

- **Spot redundancies** — Multiple similar directories? Consolidate them
- **Find bloat** — Large file types consuming space?
- **Understand structure** — New to the workspace? Get oriented fast
- **Track growth** — Run periodically to see how the workspace evolves

## Limitations

- **Read-only** — Doesn't modify files, only displays structure
- **Depth-limited** — Trees truncated to avoid overwhelming output
- **No search/filter** — Shows everything, not just specific patterns

## See Also

- `workspace-organizer.py` — Analyze duplicates and large files
- `tool-organizer.py` — Categorize tools and find consolidation opportunities
- `public-export.py` — Create sanitized exports for public sharing

---

**Version:** 1.0  
**Created:** 2026-02-01  
**Category:** Organization / Visualization
