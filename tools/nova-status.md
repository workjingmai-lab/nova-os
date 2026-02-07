# nova-status.py

**One-command Nova system status dashboard.**

## Purpose

Quick health check for Nova's entire operational state — work blocks, pipeline, blockers, and automations in a single glance.

## Usage

```bash
python3 tools/nova-status.py
```

## Sample Output

```
🚀 NOVA SYSTEM STATUS
═══════════════════════════════════════
📊 WORK BLOCKS: Block 3086 ✅
💰 PIPELINE: $880K total
   • Grants: $130K ($5K submitted)
   • Services: $700K+
   • Bounties: $50K
📝 MOLTBOOK: 13 queued, Rate Limited
⏰ CRON: 3 jobs active (15m interval)
🚧 BLOCKERS: 3 external
   • Arthur's 57-min plan ($632K ROI)
   • Moltbook API throttling
   • Code4rena browser access
═══════════════════════════════════════
Status: OPERATIONAL | Awaiting operator
```

## What It Checks

| Component | Source | Status |
|-----------|--------|--------|
| Work blocks | diary.md | Latest block number |
| Revenue | revenue-pipeline.json | Total + breakdown |
| Moltbook | moltbook-monitor.json | Rate limit status |
| Cron | HEARTBEAT.md | Job count + interval |
| Blockers | Active goals | External dependencies |

## Exit Codes

- `0` — All systems operational
- `1` — Critical blocker detected

## Dependencies

- `diary.md` — Work block history
- `revenue-pipeline.json` — Revenue tracking
- `tools/moltbook-monitor.json` — Rate limit state

## Created

Work block 3086 — 2026-02-07
