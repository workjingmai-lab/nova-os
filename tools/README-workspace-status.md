# workspace-status.py

## Overview
Quick workspace overview script that shows current work blocks, revenue pipeline, tool count, and active blockers.

## Installation
No installation required. Uses only Python standard library.

## Usage

```bash
# Run status check
python3 tools/workspace-status.py

# Output format:
# 📊 Work Blocks: <count>
# 💰 Pipeline: $<total>
# 🔧 Tools: <count>
# 📚 READMEs: <count>
# 🧠 Knowledge: <count>
# 🚧 REVENUE BLOCKERS: <list with ROI>
```

## What It Shows

### Main Metrics
- **Work Blocks:** Total completed work blocks
- **Pipeline:** Total revenue tracked (grants + services + bounties)
- **Tools:** Number of tools in ecosystem
- **READMEs:** Number of documented tools
- **Knowledge:** Number of knowledge articles

### Revenue Blockers Section
For each blocker, shows:
- **Status:** blocked / working / disconnected
- **Fix time:** Minutes to resolve
- **ROI:** Value unlocked per minute
- **Unlocks:** What becomes available when fixed

### Example Output
```
==================================================
🧠 WORKSPACE STATUS
==================================================
📊 Work Blocks: 1467
💰 Pipeline: $2,237,000
🔧 Tools: 115
📚 READMEs: 115
🧠 Knowledge: 202

==================================================
🚧 REVENUE BLOCKERS:
==================================================
🔴 GATEWAY: blocked
   Fix: 1 min | ROI: $50K/min
   Unlocks: Code4rena bounties
🔴 GITHUB: blocked
   Fix: 5 min | ROI: $26K/min
   Unlocks: 5 grant submissions
✅ MOLTBOOK: working
   Status: Connected, 15 posts queued
==================================================
```

## Use Cases
- **Heartbeat checks:** Quick status during periodic checks
- **Blocker prioritization:** ROI-based sorting shows what to fix first
- **Pipeline visibility:** Single source of truth for revenue tracking
- **Session start:** Get current state before starting work

## Data Sources
- Work blocks: Computed from diary.md session count
- Pipeline: revenue-pipeline.json
- Tools: File count in tools/
- READMEs: README.md files in tools/
- Knowledge: File count in knowledge/
- Blockers: Hardcoded blocker definitions with ROI

## Blocker ROI Formula
```
ROI = Value Unlocked / Time to Fix (minutes)
```

## Dependencies
- Python 3.x
- revenue-pipeline.json (auto-created by revenue-tracker.py)
- diary.md (auto-maintained)

## Frequency
Run during:
- Heartbeat checks (every 15-90 minutes)
- Before starting revenue-generating work
- After completing blockers (to verify status change)

## Related Tools
- `revenue-tracker.py` - Updates pipeline data
- `diary.md` - Source for work block count
- `credential-suite.py` - Checks auth status for blockers

## Maintenance
Blockers are hardcoded. To add new blockers:
1. Edit workspace-status.py
2. Add to `blockers` dict with: fix_time, value_unlocked, unlocks, status
3. ROI is auto-calculated

---

*Category: System Monitoring*  
*Core tool: Yes (high-frequency use)*
