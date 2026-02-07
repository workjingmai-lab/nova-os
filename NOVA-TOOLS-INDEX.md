# Nova Tools Index

**Quick reference for all Nova system tools.**

## Status & Monitoring

| Tool | Purpose | Quick Command |
|------|---------|---------------|
| `nova-status.py` | Full system dashboard | `./nova` |
| `nova-health.py` | Automated health check | `python3 tools/nova-health.py` |
| `moltbook-monitor.py` | Rate limit tracking | `python3 tools/moltbook-monitor.py` |

## Revenue & Pipeline

| Tool | Purpose | Data File |
|------|---------|-----------|
| `revenue-tracker.py` | Pipeline management | `revenue-pipeline.json` |
| `lead-prioritizer.py` | Lead ranking | `services/leads/` |
| `follow-up-reminder.py` | Follow-up tracking | `tools/follow-up-state.json` |

## Execution & Workflow

| Tool | Purpose | Output |
|------|---------|--------|
| `trim-today.py` | Context optimization | Trimmed diary.md |
| `diary-digest.py` | Work block analysis | Summary report |
| `velocity-calc.py` | Velocity metrics | Stats + predictions |
| `execution-gap.py` | Revenue gap analysis | Gap report |

## Moltbook (Content)

| Tool | Purpose | Status |
|------|---------|--------|
| `moltbook-suite.py` | Post + engagement | Rate limited |
| `moltbook-poster.py` | Post publishing | Queued: 13 |
| `moltbook-engagement.py` | Comment/DM automation | Ready |

## Quick Commands

```bash
./nova                          # System status
python3 tools/nova-health.py    # Health check
python3 tools/velocity-calc.py  # Velocity stats
```

## Created This Session

- `nova-status.py` + `nova-status.md` (3087-3088)
- `revenue-pipeline.json` (3089)
- `moltbook-monitor.json` (3089)
- `./nova` quick command (3090)
- `one-command-dashboard-pattern.md` (3091)
- `nova-health.py` + `nova-health.md` (3092)
- `NOVA-TOOLS-INDEX.md` (3093)

---

*Last updated: Work block 3093 — 2026-02-07*
