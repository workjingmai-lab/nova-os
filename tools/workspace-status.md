# workspace-status.py - Quick Workspace Overview

**Get a complete snapshot of your workspace state in 1 second.**

## What It Does

`workspace-status.py` gives you instant visibility into your ecosystem:
- Work blocks completed (from diary.md)
- Revenue pipeline value (from revenue-pipeline.json)
- Total tools created
- Documentation coverage (READMEs)
- Knowledge articles count
- Latest diary entry preview
- Status recommendation (EXECUTE MODE / ramp up / keep building)

## Usage

```bash
python3 tools/workspace-status.py
```

## Output Example

```
==================================================
🧠 WORKSPACE STATUS
==================================================
📊 Work Blocks: 1440
💰 Pipeline: $2,237,000
🔧 Tools: 115
📚 READMEs: 29
🧠 Knowledge: 18 articles

📝 Latest: WORK BLOCK #1440: Heartbeat status check — Updated .heartbeat_state.json...

==================================================
✅ Pipeline ready - EXECUTE MODE
==================================================
⏰ 2026-02-04 07:15:00 UTC
```

## How It Works

- **Work blocks**: Parses diary.md for latest "Work Block Count:" value
- **Pipeline**: Reads revenue-pipeline.json for totalPipeline or totalValue
- **Tools**: Counts *.py files in tools/ directory
- **READMEs**: Counts README-*.md files
- **Knowledge**: Counts *.md articles in knowledge/ directory
- **Latest entry**: Scans diary.md for latest WORK BLOCK or HEARTBEAT entry

## When to Use

- **Heartbeat checks**: Quick status without reading full files
- **Session start**: See where you left off
- **Velocity tracking**: Monitor progress over time
- **Before pushes**: Confirm pipeline and documentation status

## Integration

Perfect for:
- Cron job status checks
- Session startup scripts
- Dashboard integrations
- Progress monitoring

## Dependencies

- Python 3.6+
- Standard library only (no external deps)
- Requires: diary.md, revenue-pipeline.json (optional - returns 0 if missing)

## File Locations Checked

- `diary.md` or `/home/node/.openclaw/workspace/diary.md`
- `revenue-pipeline.json` or `/home/node/.openclaw/workspace/revenue-pipeline.json`
- `tools/` or `/home/node/.openclaw/workspace/tools/`
- `knowledge/` or `/home/node/.openclaw/workspace/knowledge/`

## Version

Created: 2026-02-04
