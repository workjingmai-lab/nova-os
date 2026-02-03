# Nova Brief — Daily Status Dashboard

**Top 3 things Arthur needs to know. One glance. Zero noise.**

---

## What It Does

Generates a clean, focused daily brief showing:
- **🚨 Top Priority:** Current blockers needing attention
- **💰 Revenue Pipeline:** Total, ready, leads, submitted amounts
- **🔥 Recent Work:** Last 3 work blocks completed
- **📊 Metrics:** Work block count, revenue total

Perfect for busy humans who want visibility without reading through hundreds of lines of logs.

---

## Usage

```bash
# Quick brief (default)
python3 tools/nova-brief.py

# Full brief with next actions
python3 tools/nova-brief.py --full

# Show only blockers
python3 tools/nova-brief.py --blockers
```

---

## Output Examples

### Quick Brief (default)
```
╔════════════════════════════════════════╗
║     📯 NOVA'S DAILY BRIEF              ║
╠════════════════════════════════════════╣
║ Time:         2026-02-02 21:47 UTC         ║
╠════════════════════════════════════════╣
║ 🚨 TOP PRIORITY:                        ║
║  • gh auth login                      ║
║  • browser access                     ║
╠════════════════════════════════════════╣
║ 💰 REVENUE PIPELINE                      ║
║  Total: $ 261,000 | Ready: $173,000     ║
║  Leads: $ 88,000 | Submitted: $   0      ║
╠════════════════════════════════════════╣
║ 🔥 RECENT WORK (last 3 blocks)          ║
║  • Knowledge base update               ║
║  • Session complete                    ║
║  • Create $180K unblock guide          ║
╠════════════════════════════════════════╣
║ 📊 METRICS                              ║
║  Work blocks:   761                         ║
║  Revenue: $  261,000                      ║
╚════════════════════════════════════════╝
```

### Full Brief (`--full`)
Includes:
- All sections from quick brief
- Blocker details with clear descriptions
- Next actions with specific commands

### Blockers Only (`--blockers`)
Shows only active blockers with reference to unblock guide.

---

## Data Sources

- **Revenue pipeline:** `data/revenue-pipeline.json` (grants, services, bounties)
- **Work blocks:** `today.md` (primary) or `diary.md` (fallback)
- **Blockers:** Extracted from revenue pipeline notes

---

## Features

- **Auto-detects data files:** Falls back gracefully if files missing
- **Extracts highest block number:** Tracks cumulative count across sessions
- **Blocker extraction:** Parses revenue pipeline notes for blockers
- **ASCII art box:** Clean, terminal-friendly output
- **Multiple output modes:** Quick, full, blockers-only

---

## Use Cases

1. **Morning check-in:** See priorities at a glance
2. **Before unblocking:** Review blockers with `--blockers`
3. **Status meetings:** Quick snapshot for Arthur
4. **Pipeline monitoring:** Track revenue progress over time

---

## Dependencies

- **Python:** 3.7+
- **Workspace:** `/home/node/.openclaw/workspace`
- **Data files:** `data/revenue-pipeline.json`, `today.md`

---

## Related Tools

- **revenue-tracker.py** — Detailed revenue pipeline management
- **revenue-dashboard.py** — Visual bar charts of pipeline
- **revenue-progress-tracker.py** — Monitor execution progress
- **docs/unblock-180k.md** — Guide to unlock revenue pipeline

---

## Integration Tips

**Add to .bashrc for instant status:**
```bash
alias nova='python3 ~/workspace/tools/nova-brief.py'
alias nova-full='python3 ~/workspace/tools/nova-brief.py --full'
alias nova-blockers='python3 ~/workspace/tools/nova-brief.py --blockers'
```

**Cron-friendly:** Can run automatically and email output.

---

## Why This Tool

**Problem:** Arthur wants visibility without noise.
**Solution:** One command shows exactly what matters most.

The brief answers:
1. What's blocking progress?
2. What's the revenue pipeline status?
3. What have I been working on?
4. What are the key metrics?

Everything else is detail. The brief cuts to the chase.

---

*Created: 2026-02-02 — Work block 763*
