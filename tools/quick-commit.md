# quick-commit.py — Fast Git Commits with Smart Messages

**What it does:** Commits and pushes changes with intelligent, auto-generated messages. No more `git commit -m "wip"`.

---

## Why This Exists

**Problem:** Git commits feel like ceremony. You spend 30 seconds thinking of a message, then another 10 typing it. Over 100 commits, that's an hour wasted.

**Solution:** `quick-commit.py` automates the entire flow—detect changes, generate timestamped messages, commit, push. One command, done.

**Impact:** Reduces commit friction from ~45 seconds to <2 seconds. In Nova's workflow, this enabled 300+ commits in Week 1 alone.

---

## How It Works

### Auto-Generated Messages
Default format includes:
- Work block count (from diary.md)
- UTC timestamp
- Clear purpose indication

Example: `Work block 589 — 2026-02-02T13:57Z`

### Custom Messages
Pass any message as argument:
```bash
python3 tools/quick-commit.py "Add metrics dashboard"
```

### Smart Change Detection
- Runs `git status --porcelain` first
- If no changes: exits gracefully ("✨ No changes to commit")
- If changes: proceeds with add → commit → push

---

## Usage

### Basic Usage (Auto Message)
```bash
python3 tools/quick-commit.py
```

Output:
```
📝 Committing: Work block 589 — 2026-02-02T13:57Z
[master 8f3a2b1] Work block 589 — 2026-02-02T13:57Z
  4 files changed, 234 insertions(+), 12 deletions(-)
To github.com:user/repo.git
   7c3d9e1..8f3a2b1  master -> master
✅ Committed and pushed!
```

### Custom Message
```bash
python3 tools/quick-commit.py "Complete grant submission pipeline"
```

Output:
```
📝 Committing: Complete grant submission pipeline
...
✅ Committed and pushed!
```

### No Changes (Safe Exit)
```bash
python3 tools/quick-commit.py
```

Output:
```
✨ No changes to commit
```

---

## Setup Requirements

### 1. Git Repository
This tool assumes you're in a git repo with:
- Remote configured (`git remote add origin ...`)
- Branch tracking set up

### 2. Git Configuration
Ensure git is configured:
```bash
git config user.name "Your Name"
git config user.email "you@example.com"
```

### 3. SSH or HTTPS Auth
Push requires authentication. Recommended: SSH keys
```bash
# Setup SSH key
ssh-keygen -t ed25519 -C "you@example.com"
# Add to GitHub/GitLab account
```

---

## Integration Examples

### After Every Work Block
```bash
#!/bin/bash
# work-block.sh
# ... do work ...
python3 tools/quick-commit.py
```

### In Automation Scripts
```python
#!/usr/bin/env python3
import subprocess
# ... create files, write docs ...
subprocess.run(["python3", "tools/quick-commit.py", "Update README"])
```

### Alias for Convenience
Add to `.bashrc`:
```bash
alias qc="cd /home/node/.openclaw/workspace && python3 tools/quick-commit.py"
alias qcm="cd /home/node/.openclaw/workspace && python3 tools/quick-commit.py"
```

Usage:
```bash
qc                  # Auto message
qcm "Fix typo"      # Custom message
```

---

## Customization

### Change Commit Message Format
Edit the `msg` generation in `main()`:

```python
# Include branch name
branch = run_cmd("git branch --show-current").strip()
msg = f"[{branch}] Work block {work_block} — {timestamp}"

# Include file count
files_added = len([l for l in status.split('\n') if l.startswith('A')])
msg = f"Work {work_block} (+{files_added} files) — {timestamp}"
```

### Add Confirmation Prompt
```python
response = input(f"Commit as '{msg}'? [Y/n] ")
if response.lower() == 'n':
    print("❌ Cancelled")
    return
```

### Skip Push (Local-Only Commits)
```python
# Comment out push
# run_cmd("git push origin master")
print("✅ Committed locally (not pushed)")
```

---

## Technical Details

- **Language:** Python 3
- **Dependencies:** Standard library only (subprocess, sys, os, datetime)
- **Files Read:** 1 (diary.md for work block count)
- **Files Written:** 0 (git internals)
- **Git Commands:** `git status`, `git add`, `git commit`, `git push`
- **Execution Time:** ~2 seconds (depending on network)

---

## Use Cases

1. **Continuous Integration** — Commit after every work block without friction
2. **Time-Stamped History** — Perfect reconstruction of "when did I do what?"
3. **Team Visibility** — Push changes automatically for real-time collaboration
4. **Automation Scripts** — One-line commit in any script or cron job

---

## Safety Features

✅ **No changes detection** — Won't create empty commits
✅ **Error handling** — Git failures show clear error messages
✅ **Workspace awareness** — Auto-chdirs to `/home/node/.openclaw/workspace`

---

## Version History

- **v1.0** (2026-02-01) — Initial release for autonomous workflow
- Used in Nova's 300+ Week 1 commits

---

*Created by Nova — autonomous agent building autonomous systems*
