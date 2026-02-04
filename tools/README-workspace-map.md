# README - workspace-map.py

**Workspace visualization and file structure analysis.**

## What It Does

Generate a tree view of your workspace with file counts, size statistics, and key highlights.

## Use Cases

- **Onboarding:** Quick visual overview of workspace structure
- **Audit:** Find large files or directories cluttering workspace
- **Organization:** See file type distribution at a glance
- **Documentation:** Generate workspace structure for docs

## Installation

No dependencies. Uses Python stdlib only.

```bash
# Already in workspace/tools/
chmod +x tools/workspace-map.py
```

## Usage

```bash
# Full workspace overview
python3 tools/workspace-map.py

# Specific directory
python3 tools/workspace-map.py --dir /path/to/dir

# Examples
python3 tools/workspace-map.py --dir tools/
python3 tools/workspace-map.py --dir memory/
```

## Output

```
🗂️ WORKSPACE MAP
============================================================

📊 Statistics:
  Total files: 847
  Total size: 4231.2 KB

📁 Top File Types:
  • .py: 95 files (284.5 KB)
  • .md: 156 files (412.3 KB)
  • .json: 34 files (89.1 KB)

🌳 Directory Structure (partial):
├── tools/
│   ├── agent-collaboration.py
│   ├── agent-digest.py
│   └── ...
├── memory/
│   ├── 2026-02-01.md
│   └── ...
└── ...
```

## Key Features

- **File type analysis:** Count and size by extension
- **Tree view:** Visual directory structure (configurable depth)
- **Hidden file filtering:** Skips .git, .env, etc.
- **Size statistics:** Track workspace bloat
- **Flexible targeting:** Map any directory, not just workspace

## Aliases

```bash
# Add to shell for quick access
alias wsmap="python3 ~/workspace/tools/workspace-map.py"
alias tools="wsmap --dir ~/workspace/tools/"
```

## Created

2026-02-03 — Work block #968

## Insight

"Visibility = control. You can't organize what you can't see."
