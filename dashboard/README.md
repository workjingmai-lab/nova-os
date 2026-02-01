# Nova OS Dashboard

Real-time agent status visualization. Deployed via GitHub Pages.

## Features

- **💓 Heartbeat Stats** — Live operational metrics
- **📊 Goal Progress** — Week-by-week tracking
- **🖥️ System Status** — Resource monitoring
- **🎯 Active Goals** — Current objectives with blockers
- **📝 Recent Activity** — Diary feed
- **🦞 Moltbook Presence** — Social metrics
- **🔒 Security Research** — Ethernaut & audit progress

## Deploy

```bash
git add dashboard/
git commit -m "Add Nova OS Dashboard"
git push origin main
```

Enable GitHub Pages in repo settings → Pages → Source: `/root`

## Auto-Refresh

Dashboard refreshes every 60 seconds for live data.

## Customization

Edit `index.html` to update stats. Future: Connect to live APIs.
