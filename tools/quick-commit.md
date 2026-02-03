# quick-commit.py — Fast Git Commit with Smart Defaults

**Version:** 1.0  
**Category:** Git / Workflow  
**Created:** 2026-02-01

---

## What It Does

Creates git commits with auto-generated messages based on changed files. Eliminates "what did I change?" friction.

### Features

- Auto-generates commit messages from file changes
- Groups related changes
- Supports custom commit messages
- Adds and commits in one command
- Skip CI option (for documentation-only commits)

---

## Usage

```bash
# Quick commit (auto-generates message)
python3 tools/quick-commit.py

# Custom message
python3 tools/quick-commit.py -m "Add Ethernaut exploit for Token challenge"

# Add specific files only
python3 tools/quick-commit.py file1.py file2.md

# Skip CI (documentation changes)
python3 tools/quick-commit.py -m "Update README" --skip-ci

# Dry run (show what would be committed)
python3 tools/quick-commit.py --dry-run
```

---

## Commit Message Patterns

Auto-generated messages follow this format:

```
<type>(<scope>): <description>

<files changed>
```

**Types:**
- `feat` — New feature or tool
- `fix` — Bug fix or correction
- `docs` — Documentation changes
- `refactor` — Code restructuring
- `test` — Test additions or changes
- `chore` — Maintenance tasks

**Scopes:**
- `tools` — New or updated tools
- `docs` — Documentation
- `diary` — Diary entries
- `goals` — Goal tracking
- `knowledge` — Knowledge base

---

## Examples

```bash
$ python3 tools/quick-commit.py

✓ Detected 3 changed files:
  • tools/new-tool.py
  • tools/new-tool.md
  • today.md

✓ Commit message:
  feat(tools): Add new-tool.py for automated X

✓ Committed 3 files (abc1234)
```

---

## Dependencies

- Python 3.7+
- Git

---

## Configuration

Edit defaults:

```python
DEFAULT_COMMIT_TYPE = "chore"
SKIP_CI_PATTERNS = [r'\.md$', r'diary\.md$', r'today\.md$']
AUTO_ADD_ALL = True  # git add -A vs explicit files
```

---

## Integration

- Pair with `git` for full workflow
- Use before `public-publish-gh-pages.sh`
- Chain with other git operations

---

## Tips

1. Use `-m` for important commits (milestones, releases)
2. Use `--skip-ci` for documentation to save CI resources
3. Run `--dry-run` to review before committing
4. Customize commit types to match your workflow
