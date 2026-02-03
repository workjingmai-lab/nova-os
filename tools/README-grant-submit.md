# grant-submit.py

Grant submission automator — fast-track $130K revenue pipeline.

## What It Does

Automates grant application submission process across 5 platforms:
- Validates prerequisites (GitHub repo, CLI auth, docs)
- Generates platform-specific submission content
- Creates applications from templates
- Tracks submission status
- Supports dry-run mode for preview

## Installation

Requires `gh` (GitHub CLI) for repo operations:
```bash
# Check GitHub auth status
gh auth status

# Login if needed
gh auth login
```

## Quick Start

### Check prerequisites
```bash
python3 tools/grant-submit.py --check
```

**Output:**
```
🔍 Grant Submission Prerequisites

✅ GitHub CLI installed
✅ GitHub repo detected
⚠️  Repo not public (needed for some grants)
✅ README.md exists

Status: 3/4 checks passed
Action: Run `git push` to make repo public before submitting
```

### Submit all ready grants
```bash
python3 tools/grant-submit.py --all
```

### Submit specific grant
```bash
python3 tools/grant-submit.py gitcoin
python3 tools/grant-submit.py octant
python3 tools/grant-submit.py olas
python3 tools/grant-submit.py optimism
python3 tools/grant-submit.py moloch
```

### Dry-run preview
```bash
python3 tools/grant-submit.py --all --dry-run
```

## Supported Platforms

| Platform | Potential | Fields | Method |
|----------|-----------|--------|--------|
| Gitcoin | $5K | name, description, website, impact, budget | Web |
| Octant | $10K | name, description, impact, metrics | Web |
| Olas | $25K | title, proposal, budget, timeline | Web |
| Optimism RPGF | $80K | name, description, impact, category | Web |
| Moloch DAO | $10K | title, proposal, tribute, applicant | On-chain |

**Total pipeline:** $130K

## Output

Submissions are saved to `tmp/grant-submissions/`:
```
tmp/grant-submissions/
├── gitcoin-submission.md
├── octant-submission.md
├── olas-submission.md
├── optimism-submission.md
└── moloch-submission.md
```

Each file contains:
- Platform-specific formatted content
- Pre-filled fields from templates
- Budget breakdown
- Impact metrics

## Features

- **Prerequisites validation:** Checks GitHub CLI, repo status, README
- **Multi-platform:** 5 grant platforms with different requirements
- **Template-based:** Generates content from outreach templates
- **Dry-run mode:** Preview submissions without committing
- **Batch mode:** Submit all ready grants with `--all`
- **Status tracking:** Updates revenue-pipeline.json after submission

## Use Cases

- **Revenue generation:** Fast-track $130K grant pipeline
- **Grant season:** Submit multiple applications quickly
- **A/B testing:** Generate variations with `--dry-run`
- **Pipeline management:** Track submission status across platforms

## Prerequisites Checklist

Before submitting:
- [ ] GitHub CLI installed and authenticated
- [ ] GitHub repo is public (required by most platforms)
- [ ] README.md exists in workspace root
- [ ] Grant templates exist in `outreach/` directory
- [ ] Metrics JSON available for impact numbers

## Pipeline Integration

Works with:
- `revenue-tracker.py` — View full pipeline status ($285K)
- `grant-submission-generator.py` — Generate grant applications
- `data/revenue-pipeline.json` — Central pipeline database

## Return Codes

- `0` — Success
- `1` — Validation failed or error

## Workflow Example

```bash
# 1. Check prerequisites
python3 tools/grant-submit.py --check

# 2. Preview all submissions
python3 tools/grant-submit.py --all --dry-run

# 3. Submit to specific platform
python3 tools/grant-submit.py gitcoin

# 4. Check pipeline status
python3 tools/revenue-tracker.py
```

## Authentication

Uses GitHub CLI for repo operations. Ensure `gh auth status` shows authenticated user.

## See Also

- `README-grant-submission-generator.md` — Generate grant applications
- `README-revenue-tracker.md` — Track full pipeline
- `outreach/` — Grant templates and proposals
- `data/revenue-pipeline.json` — Pipeline database

---

**Created:** Week 2 (Feb 2026)
**Purpose:** Automate grant submissions and unblock $130K revenue
**Pipeline:** 5 grants ready ($130K), 13 service proposals ($155K)
