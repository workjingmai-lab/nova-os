# Learning: GitHub Pages for Agent Dashboards

**Date:** 2026-02-01  
**Source:** Building Nova OS Dashboard  
**Impact:** High — free hosting for agent UIs

---

## Why GitHub Pages

- **Free:** $0 for public repos
- **Fast:** CDN-backed, global edge servers
- **Simple:** Push HTML → live in seconds
- **Custom domain:** Optional (nova-os.dev?)

## The Setup

```bash
# 1. Create repo with special name
#    <username>.github.io for root
#    or any repo with Pages enabled

# 2. Push static files
git checkout -b gh-pages
git add index.html
git commit -m "Deploy dashboard"
git push origin gh-pages

# 3. Enable Pages in repo settings
#    Source: Deploy from branch → gh-pages
```

## Dashboard Architecture

```
dashboard/
├── index.html          # Main UI (14.5KB)
├── data.json           # Dynamic data (updated via script)
├── notifications.json  # Alert state
└── v2-live.html        # Experimental version
```

## Dynamic Data Without Backend

Since Pages is static-only, use:

### Option 1: Client-side polling
```javascript
// Fetch fresh data.json every 30s
setInterval(() => {
  fetch('data.json?t=' + Date.now())
    .then(r => r.json())
    .then(updateUI);
}, 30000);
```

### Option 2: GitHub Actions
```yaml
# .github/workflows/update-data.yml
on:
  schedule:
    - cron: '*/5 * * * *'  # Every 5 min
jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: python generate-data.py
      - run: |
          git add data.json
          git commit -m "Update data"
          git push
```

### Option 3: External API
Host data on a tiny service (Railway/Render), UI on Pages.

## Current Blocker

GitHub auth pending. Arthur needs to provide PAT or SSH key.

## Next Steps

1. ✅ Build dashboard (done)
2. 🔄 Get GitHub auth (blocked)
3. 📋 Push to repo
4. 📋 Enable Pages
5. 📋 Share URL with Arthur

---

*Pattern: Static hosting + dynamic data = powerful, cheap dashboards.*
