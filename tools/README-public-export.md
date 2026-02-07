# public-export.py

**Safe-by-default public export for static hosting.**

Creates a sanitized, publishable bundle with allowlisted paths and automatic redaction.

## What It Does

- Copies only allowlisted files/directories to `public/` folder
- Redacts sensitive patterns (API keys, bearer tokens, auth strings)
- Safe-by-default: nothing is copied unless explicitly allowlisted
- Prepares workspace for GitHub Pages / Netlify deployment

## Usage

```bash
# Basic: use default allowlist
python3 tools/public-export.py

# Custom output directory
python3 tools/public-export.py --out my-public/

# Custom allowlist file
python3 tools/public-export.py --allowlist tools/public-allowlist.txt
```

## Default Allowlist

- `index.html`
- `README.md`
- `PORTFOLIO.md`
- `toolkit.md`
- `EARNING-STRATEGY.md`
- `dashboard/`
- `reports/`

## Redactions (automatic)

- Authorization bearer tokens
- API keys (sk_, pk_, api_ patterns 16+ chars)
- Bearer tokens (16+ chars)

## Redacted Text Examples

```
Before: Authorization: Bearer YOUR_MOLTBOOK_TOKEN_HERE
After:  Authorization: Bearer [REDACTED]

Before: api_key: sk_1234567890abcdef
After:  api_key: [REDACTED]
```

## Output

Creates `public/` directory with:
- Allowlisted files and directories
- In-place redactions applied
- `PUBLIC_EXPORT.md` metadata file
- Ready to deploy to GitHub Pages, Netlify, or any static host

## Use Cases

- **Portfolio publishing:** Share work without exposing secrets
- **GitHub Pages:** Static site for public visibility
- **Collaboration:** Share sanitized workspace with others
- **Backup:** Public snapshot of work

## Security Design

**Allowlist > blacklist.**

Instead of trying to exclude dangerous files, it only includes safe files. Nothing gets copied unless you explicitly allow it.

**Redactions are lightweight.**
Basic pattern matching for obvious secrets. Not a substitute for manual review before publishing.

## Why It Matters

**Public presence requires safety.**

You want to share your work, not your secrets. This tool creates a clean boundary: publish the `public/` folder, keep everything else private.

---

**Created:** 2026-02-02
**Status:** Active ✅
**Output:** `public/` directory
**Safety:** Allowlist-only (safe-by-default)
