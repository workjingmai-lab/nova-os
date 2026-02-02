# quick-commit.py — Fast Git Commits

**Auto-generate timestamped commit messages + push in one command**

## What It Does

- Detects if there are changes to commit
- Auto-generates timestamped commit messages
- Counts work blocks from diary.md for context
- Adds all changes, commits, and pushes in one go

## Usage

```bash
# Auto-generate message: "Work block 588 — 2026-02-02T13:48Z"
python3 tools/quick-commit.py

# Custom message
python3 tools/quick-commit.py "Add nova-metrics dashboard"
```

**Output:**
```
📝 Committing: Work block 588 — 2026-02-02T13:48Z
✅ Committed and pushed!
```

## Why It Exists

Avoid commit message decision fatigue. When you're cranking through work blocks, you don't want to think about git messages. This tool handles it automatically.

## Features

- Auto-detects changes (exits cleanly if none)
- Reads work block count from diary.md
- UTC timestamps for consistency
- Custom message override available
- Pushes to origin/master automatically

## Workflow Integration

Add to your end-of-block routine:
```bash
python3 tools/quick-commit.py  # Commit and push after each work block
```

## Requirements

- Git repo initialized
- Origin remote configured
- diary.md exists (for work block counting)

## Related Tools

- `workspace-cleanup.py` — Clean workspace before commits
- `diary.py` — Log work blocks to diary.md

## Note

This is a convenience wrapper around `git add -A`, `git commit`, and `git push`. Use it when you want fast commits without thinking about messages.
