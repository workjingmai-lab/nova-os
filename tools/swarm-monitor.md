# swarm-monitor.py — Agent Swarm Monitor

**Purpose:** Track multi-agent collaboration status by parsing diary entries for CLAIM, HANDOFF, and STATUS markers.

**Created:** Week 1 (2026-01-31)
**Usage:** ~5-10 times (diary analysis)

## What It Does

- **Parses CLAIM entries** — Extracts task claims by agents (`CLAIM: task_name by agent_name`)
- **Parses HANDOFF entries** — Tracks agent-to-agent task transfers
- **Parses STATUS entries** — Extracts agent progress updates
- **Generates swarm report** — Creates `reports/swarm-status.md` with summary

## Usage

```bash
# Basic usage (default diary.md)
python3 tools/swarm-monitor.py

# Custom diary file
python3 tools/swarm-monitor.py path/to/diary.md
```

## Output

Generates `reports/swarm-status.md` with:
- Active claims count
- Handoffs completed
- Status updates
- Recent claims/handoffs/statuses (last 5 each)

## Dependencies

- Python 3.8+
- pathlib, re, json (stdlib only)

## Why This Matters

Multi-agent collaboration requires coordination. This tool provides visibility into:
- Who is working on what
- How tasks are being handed off
- Overall swarm activity levels

## Example Diary Format

```markdown
CLAIM: grant-submission by Nova

## HANDOFF — Nova → SubAgent
**Completed:** 2026-02-02T15:00Z

## STATUS — SubAgent
**Last Update:** 2026-02-02T15:30Z
**Progress:** Draft complete, reviewing
```

## Related Tools

- `diary-digest.py` — Pattern analysis
- `self-improvement-loop.py` — Velocity tracking
