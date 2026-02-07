# daily-revenue-action.py

**One high-ROI action per day. Eliminates decision fatigue.**

## Purpose

Analyzes revenue pipeline and suggests the single most impactful action to move toward conversion. No more guessing what to work on — just run this and execute.

## Usage

```bash
# Get today's highest ROI action
python3 tools/daily-revenue-action.py

# Show reasoning and context
python3 tools/daily-revenue-action.py --why

# Show all possible actions ranked by ROI
python3 tools/daily-revenue-action.py --all
```

## How It Works

The tool evaluates:
1. **Current blockers** (gateway, GitHub auth, etc.)
2. **Pipeline status** (ready vs submitted vs won)
3. **ROI per minute** for each possible action

It returns the single highest ROI action you can take right now.

## Action Rankings

| Action | Time | Value Unblocked | ROI/min |
|--------|------|-----------------|---------|
| Gateway Restart | 1 min | $50K | $50K/min |
| GitHub Auth | 5 min | $125K | $25K/min |
| Send Service Messages | 36 min | $332K | $9.2K/min |
| Submit Grants | 15 min | $125K | $8.3K/min |
| Check Follow-ups | 5 min | $50K | $10K/min |
| Moltbook Post | 2 min | $10K | $5K/min |
| Update Pipeline | 5 min | $5K | $1K/min |

## Integration

Add to daily routine:
```bash
# In heartbeat or morning check
python3 tools/daily-revenue-action.py
```

## Output Example

```
🎯 DAILY REVENUE ACTION — 03:20 UTC

Action: Restart Gateway for Browser Access
Time Required: 1 minute
Value Unblocked: $50K
ROI: $50K/min ⭐

Command: Ask Arthur: Run 'openclaw gateway restart' to unblock $50K bounties
```

## Files

- `tools/daily-revenue-action.py` — Main tool
- `data/revenue-pipeline.json` — Pipeline data source
- `memory/YYYY-MM-DD.md` — Diary for context

## Related Tools

- `revenue-tracker.py` — Full pipeline management
- `follow-up-tracker.py` — Track sent messages
- `moltbook-suite.py` — Content distribution

---

*Created: Work block 3, 2026-02-07*
*Part of Week 3 revenue conversion system*
