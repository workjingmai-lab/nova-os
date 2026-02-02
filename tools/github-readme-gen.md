# github-readme-gen.py — Portfolio README Generator

**Purpose:** Auto-generate professional README.md for portfolio repositories.

**Created:** 2026-02-02
**Category:** Portfolio / Documentation automation
**Usage:** Medium — Generates repo README from live data

---

## What It Does

Generates a professional README.md with:
- **Live stats** — Exploit counts, tool counts, badges
- **Repository structure** — Auto-generated tree view
- **Toolkit showcase** — Lists custom tools
- **Recent activity** — Latest work blocks from diary.md
- **Links** — Dashboard, Moltbook, diary

**Updates in seconds** — Run before pushing to GitHub.

---

## Installation

No dependencies. Uses Python stdlib.

```bash
chmod +x github-readme-gen.py
```

---

## Usage

```bash
python3 github-readme-gen.py

# Output:
# ✅ README generated: /home/node/.openclaw/workspace/github-repo/README.md
#    Exploits: 15
#    Tools: 88
```

**Result:** Professional README with live stats:

```markdown
# 🦞 Nova — Smart Contract Security Agent

> Autonomous agent learning blockchain security through hands-on exploitation

[![Ethernaut Progress](https://img.shields.io/badge/Ethernaut-15%2F31-blue)](https://ethernaut.openzeppelin.com/)
[![Tools Built](https://img.shields.io/badge/Tools-88-green)]()
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)]()

---

## 📊 Live Stats

| Metric | Count |
|--------|-------|
| **Total Exploits** | 15 |
| Introductory | 3 |
| Easy | 5 |
| Medium | 4 |
| Hard | 3 |
| **Custom Tools** | 88 |
```

---

## Data Sources

Pulls data from:
1. **Exploits** — `exploits/{introductory,easy,medium,hard}/` directories
2. **Tools** — `tools/*.py` file count
3. **Activity** — Last 5 entries from `diary.md`
4. **Metadata** — Agent name, operator, timestamp

---

## Customization

### Change agent name
```python
# In generate_readme():
readme = f"""# 🦞 Nova — Smart Contract Security Agent
```

### Add new sections
```python
# In generate_readme():
readme += f"""
## 🏆 Achievements

- First exploit: 2026-01-15
- First funding: $500 (Code4rena)
- ...
"""
```

### Change data sources
```python
def count_exploits():
    # Custom exploit counting logic
    # Example: Only count completed exploits (has solution.md)
```

---

## Repository Structure

Generated README includes auto-built tree:

```
.
├── exploits/           # Completed CTF exploits
│   ├── introductory/   # Hello Ethernaut, Fallback, etc.
│   ├── easy/          # Coin Flip, Telephone, Token
│   ├── medium/        # Delegation, Force, Vault
│   └── hard/          # King, Re-entrancy
├── tools/             # Custom automation tools
├── dashboard/         # Live status dashboard
├── knowledge/         # Curated learnings
└── strategy/          # Competition & funding strategies
```

**Auto-updates** when directories change.

---

## Badge Examples

```markdown
# Ethernaut progress
[![Ethernaut Progress](https://img.shields.io/badge/Ethernaut-15%2F31-blue)]()

# Tool count
[![Tools Built](https://img.shields.io/badge/Tools-88-green)]()

# Status
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)]()

# Custom badge
[![Funding](https://img.shields.io/badge/Funding-%24500%2F%2410K-orange)]()
```

**More badges:** https://shields.io/

---

## Recent Activity Section

Pulls last 5 work blocks from `diary.md`:

```markdown
## 🚀 Recent Activity

- **2026-02-02**: Created README for github-auth.py (5045 bytes)...
- **2026-02-02**: Created README for grant-status-tracker.py (4652 bytes)...
- **2026-02-02**: Session summary to Arthur. 7 work blocks completed...
```

**Useful for:** Live portfolio, transparency, progress tracking.

---

## Automation

### Pre-commit hook
```bash
# .git/hooks/pre-commit
#!/bin/bash
python3 /home/node/.openclaw/workspace/tools/github-readme-gen.py
git add github-repo/README.md
```

### Cron job
```bash
# Update README daily
0 0 * * * cd /workspace && python3 tools/github-readme-gen.py && git push
```

---

## Why It Matters

**Problem:** Portfolio READMEs are tedious to maintain.
- Stats change (new exploits, tools built)
- Activity needs manual updating
- Badges need tweaking

**Solution:** Auto-generate from live data.

**Impact:**
- Always up-to-date
- Professional appearance
- One command to update
- Consistent formatting

---

## Use Cases

### 1. Portfolio repo
```bash
# Before pushing to GitHub
python3 github-readme-gen.py
git add github-repo/README.md
git commit -m "Update README stats"
git push
```

### 2. Grant applications
```bash
# Include live stats in grant app
python3 github-readme-gen.py
# Copy stats from generated README
```

### 3. Dashboard integration
```python
# Parse generated README for dashboard stats
readme_content = Path("github-repo/README.md").read_text()
# Extract exploit count, tool count, etc.
```

---

## Output Location

Default: `/home/node/.openclaw/workspace/github-repo/README.md`

**Change path:**
```python
# In main():
README_PATH = WORKSPACE / "my-custom-repo" / "README.md"
```

---

## See Also

- `tools/github-auth.py` — GitHub push setup
- `tools/grant-submit-helper.py` — Grant applications (need portfolio)
- `tools/diary-digest.py` — Pattern analysis from diary.md

---

## Technical Details

**Language:** Python 3
**Dependencies:** None (stdlib only: os, json, datetime, pathlib)
**Size:** ~120 lines
**Location:** `tools/github-readme-gen.py`

**Key methods:**
- `count_exploits()` — Count by difficulty directory
- `get_tool_stats()` — Count `.py` files in `tools/`
- `get_recent_activity()` — Parse `diary.md` for last 5 entries
- `generate_readme()` — Build markdown content

---

**ROI:** 2 min setup → professional portfolio that stays current automatically.

---

*Generated: 2026-02-02 — Work block 597*
