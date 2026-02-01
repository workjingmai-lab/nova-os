# public/ — Publishable Bundle

This folder is intentionally **safe-to-publish** output generated from the private repo.

## How this folder is produced
Run either:

```bash
# from repo root
make public-export
# or
python3 tools/public-export.py
```

This will:
- copy an allowlisted set of artifacts (portfolio/docs/dashboards/reports)
- apply light redactions to common secret/token patterns in text files

## Preview locally
```bash
# from repo root
make public-serve
# or
cd public
python3 -m http.server 8000
# then open http://localhost:8000/index.html
```

## How to publish
### Option A — Netlify (drag & drop)
1. Run the export command above.
2. In Netlify: **Sites → Add new site → Deploy manually**
3. Drag-drop the `public/` folder.

### Option B — GitHub Pages (separate public repo)
If you want Pages, easiest is to publish **only** this folder (not the whole private repo):
- create a separate repo like `openclaw-public`
- copy `public/` contents into that repo root
- enable Pages from the default branch

### Option C — GitHub Pages (gh-pages branch, same repo)
This keeps `main` private-ish (or at least separate) while publishing *only* the exported bundle:
1. Run the export:
   ```bash
   python3 tools/public-export.py
   ```
2. Create/update a `gh-pages` branch containing just `public/` contents:
   ```bash
   git checkout --orphan gh-pages
   git rm -rf .
   cp -R public/* .
   git add .
   git commit -m "Publish public bundle"
   git push -f origin gh-pages
   ```
3. In GitHub: **Settings → Pages → Deploy from branch → gh-pages / (root)**

Note: the `--orphan` + `push -f` flow rewrites the `gh-pages` branch history. That’s usually fine for a static site branch.

## Sanity check (recommended)
Before publishing, do a quick scan for obvious secrets:

```bash
# from repo root
make public-check
# or
cd public
rg -n "(sk-|api[_-]?key|secret|bearer\s+|authorization:|token)" -S .
```

## Notes
- `public/index.html` is the landing page.
- If anything looks sensitive, fix the allowlist/redaction rules in `tools/public-export.py` and re-export.
