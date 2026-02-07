# README-follow-up-reminder.md

## follow-up-reminder.py

Check for due follow-ups and display reminder checklist with urgency indicators. Prevents leads from slipping through cracks.

### Usage

```bash
# All due follow-ups (overdue + today + soon)
python3 tools/follow-up-reminder.py

# Only overdue (critical)
python3 tools/follow-up-reminder.py --urgent

# Due today or overdue
python3 tools/follow-up-reminder.py --today
```

### Output Example

```
Follow-Up Reminder Checklist
============================================================
🔴 OVERDUE  | 2026-02-05 | msg_001 → Uniswap
🔴 OVERDUE  | 2026-02-06 | msg_003 → Aave
🟡 TODAY    | 2026-02-07 | msg_007 → Compound
🟢 SOON     | 2026-02-08 | msg_012 → MakerDAO
🟢 SOON     | 2026-02-09 | msg_015 → Curve

============================================================
Total: 5 follow-ups due

Commands:
  python3 tools/follow-up-tracker.py export    # Full checklist
  python3 tools/follow-up-tracker.py complete <id>  # Mark done
```

### Urgency Levels

| Level | Icon | Meaning | Action |
|-------|------|---------|--------|
| OVERDUE | 🔴 | Past follow-up date | Send immediately |
| TODAY | 🟡 | Due today | Send today |
| SOON | 🟢 | Within 2 days | Prepare to send |
| UPCOMING | ⚪ | 3+ days out | Monitor |

### Data Source

Reads from: `outreach/follow-up-tracker.json`

Created by: `follow-up-tracker.py` (companion tool)

### Filter Options

| Flag | Shows |
|------|-------|
| (none) | OVERDUE + TODAY + SOON |
| `--urgent` | OVERDUE only |
| `--today` | OVERDUE + TODAY |

### Integration

- Companion to `follow-up-tracker.py` (creates/manages data)
- Used in daily revenue checklist
- Called by heartbeat for proactive follow-up alerts

### Dependencies

- Python 3.6+
- Standard library (json, sys, datetime, pathlib)
- `outreach/follow-up-tracker.json` (created by follow-up-tracker.py)

### Created

Week 2 revenue pivot toolkit
