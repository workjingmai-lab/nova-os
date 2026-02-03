# public-export.py

Create a sanitized, publishable static bundle for public hosting (GitHub Pages, Netlify, etc.).

## What It Does

`public-export.py` copies only an allowlisted subset of your workspace to a `public/` directory, automatically redacting sensitive data like API keys and tokens. Safe-by-default for public hosting.

## Design Goals

- **Safe-by-default** — Copy ONLY allowlisted paths
- **Minimal footprint** — Intended for static hosting
- **Automatic redaction** — Removes API keys, tokens, bearer auth strings
- **Allowlist-driven** — Add paths intentionally, nothing by accident

## Usage

```bash
# Export to default public/ directory
python3 tools/public-export.py

# Specify custom output directory
python3 tools/public-export.py --out ~/site/public

# Use custom allowlist file
python3 tools/public-export.py --allowlist tools/public-allowlist.txt
```

## Default Allowlist

The tool copies only these paths by default:

- `index.html` — Landing page
- `README.md` — Project overview
- `PORTFOLIO.md` — Work portfolio
- `toolkit.md` — Tool documentation
- `EARNING-STRATEGY.md` — Revenue strategy (sanitized)
- `dashboard/` — System health dashboard
- `reports/` — Analytics reports

## Automatic Redactions

The tool redacts these patterns from text files (`.md`, `.txt`, `.html`, `.json`, `.js`, `.css`):

- `Authorization: bearer [token]` → `Authorization: bearer [REDACTED]`
- `sk_...`, `pk_...`, `api_...` (16+ chars) → `[REDACTED]`
- `Bearer [long-token]` → `Bearer [REDACTED]`

**Note:** Redaction is basic — review output before publishing!

## Custom Allowlists

Create `tools/public-allowlist.txt`:

```
# Comments start with #

# Documents
index.html
README.md
PORTFOLIO.md

# Dashboards and reports
dashboard/
reports/

# Specific tools (if you want to share)
tools/task-randomizer.py
tools/diary-digest.py
```

Then run:

```bash
python3 tools/public-export.py --allowlist tools/public-allowlist.txt
```

## Output Structure

```
public/
├── index.html
├── README.md
├── PORTFOLIO.md
├── toolkit.md
├── dashboard/
│   └── index.html
├── reports/
│   └── patterns-2026-02-01.md
├── PUBLIC_EXPORT.md     # Auto-generated note
└── [other allowlisted files]
```

## Publishing to GitHub Pages

```bash
# Generate the export
python3 tools/public-export.py

# Deploy to gh-pages branch
cd public
git init
git add .
git commit -m "Deploy public site"
git push -f origin main:gh-pages
```

Or use subtree:

```bash
git add -f public
git commit -m "Update public export"
git subtree push --prefix public origin gh-pages
```

## Security Principles

1. **Allowlist, not blocklist** — Nothing is copied unless explicitly allowed
2. **Text file redaction** — Sensitive patterns removed from supported formats
3. **No hidden files** — Dotfiles excluded by default
4. **Review before publishing** — Always check the `public/` output before deploying

## Why This Matters

**Share your work without sharing your secrets.**

For agents building in public, you want to showcase your tools, documentation, and dashboards—but not your API keys, tokens, or private data. `public-export.py` bridges this gap:

- **Portfolio building** — Share toolkits and docs publicly
- **Transparency with safety** — Show work without leaking secrets
- **Static hosting ready** — Drop `public/` onto any static host

## Warnings

⚠️ **Review output before publishing!** Redaction is basic and may miss edge cases.

⚠️ **Don't publish entire workspace** — Use allowlists to control what's shared.

⚠️ **Check git history** — Remove sensitive data from past commits before pushing.

---

**Version:** 1.0  
**Created:** 2026-01-31  
**Category:** Security / Publishing
