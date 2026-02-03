# public-publish-gh-pages.sh — Publish Portfolio to GitHub Pages

**Version:** 1.0  
**Category:** Publishing / Portfolio  
**Created:** 2026-02-01

---

## What It Does

Publishes sanitized portfolio content from `public/` to GitHub Pages. One-command deployment of public-facing work.

### Features

- Validates git repository status
- Runs `public-export.py` to sanitize content
- Commits and pushes to `gh-pages` branch
- Provides GitHub Pages URL
- Rollback support

---

## Usage

```bash
# Publish to GitHub Pages
./tools/public-publish-gh-pages.sh

# Force publish (skip git status check)
./tools/public-publish-gh-pages.sh --force

# Preview what would be published
./tools/public-publish-gh-pages.sh --dry-run
```

---

## What It Does

1. **Checks git status** — Warns if uncommitted changes
2. **Runs export** — Generates sanitized `public/` directory
3. **Switches to gh-pages** — Creates branch if needed
4. **Commits changes** — Adds new public content
5. **Pushes to origin** — Deploys to GitHub Pages
6. **Returns to branch** — Restores previous branch

---

## Output

```bash
$ ./tools/public-publish-gh-pages.sh

✓ Generating public export...
  Found 47 portfolio items
  Sanitized 12 files

✓ Switching to gh-pages branch...
✓ Committing changes...
✓ Pushing to origin...

✓ Deployed to: https://username.github.io/workspace/
✓ Process completed in 4.2 seconds
```

---

## Dependencies

- `git` — Version control
- `public-export.py` — Content sanitization
- GitHub repository with `gh-pages` branch

---

## Setup

First-time setup:

```bash
# Create gh-pages branch
git checkout --orphan gh-pages
git rm -rf .
echo "# Portfolio" > README.md
git add README.md
git commit -m "Initial gh-pages commit"
git push origin gh-pages
git checkout -
```

---

## Configuration

Edit variables:

```bash
GH_PAGES_BRANCH="${GH_PAGES_BRANCH:-gh-pages}"
PUBLIC_DIR="${PUBLIC_DIR:-public}"
COMMIT_MSG="${COMMIT_MSG:-Update portfolio}"
```

---

## Integration

- Pair with `public-export.py` for content generation
- Use `refresh-portfolio-metrics.py` before publishing for updated stats
- Schedule via cron for automatic daily/weekly deployments

---

## Tips

1. Run `--dry-run` first to preview changes
2. Commit main branch work before publishing
3. Use `--force` only if you know what you're doing
4. Check GitHub Pages settings if site doesn't appear
