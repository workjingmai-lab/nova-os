# wins.py

Wins tracker — log accomplishments and review progress over time.

## What It Does

Simple achievement logging system. Record wins as they happen, review them later to build momentum and combat burnout. Maintains persistent JSON storage so your accomplishments survive session resets.

**Core use case:** Combat "what did I actually do today?" amnesia by logging wins in real-time, then reviewing them to see compounding progress.

## Usage

```bash
# Add a win
python wins.py add "Submitted 5 grant proposals"

# List all wins
python wins.py list

# Show today's wins only
python wins.py today

# Show last 10 wins
python wins.py recent
```

## Features

**Log wins:**
- Timestamped entries (ISO 8601)
- Date grouping for daily reviews
- Reverse chronological order (newest first)

**Review modes:**
- All wins (full history)
- Today's wins (daily motivation)
- Recent wins (last 10, quick recap)

**Persistent storage:**
- JSON file at `.wins.json` (workspace root)
- Survives session restarts
- Easy to backup or migrate

## Data Structure

```json
[
  {
    "description": "Submitted 5 grant proposals",
    "timestamp": "2026-02-03T17:45:00.123456",
    "date": "2026-02-03"
  }
]
```

## Integration Patterns

**With cron/heartbeats:**
```bash
# After each work block, if it was a win
python wins.py add "Completed tool documentation sprint"
```

**With daily review:**
```bash
# Evening reflection
echo "=== Today's Wins ==="
python wins.py today
```

**Programmatic logging (Python):**
```python
from wins import add_win

add_win("Reached 1000 work blocks")
```

## Real-World Usage

**Nova's use case:**
- Logs major milestones (1000 blocks, $300K pipeline, etc.)
- Reviews wins during weekly reflection
- Uses "today's wins" for motivation during slumps
- Exports wins to MEMORY.md for long-term retention

**Anti-burnout routine:**
```bash
# Morning: Review yesterday's wins for momentum
python wins.py recent | head -5

# Evening: Log 3 wins before bed
python wins.py add "Documented 4 tools"
python wins.py add "Sent 5 outreach messages"
python wins.py add "Reached 97% documentation"
```

## Why This Matters

**Momentum > motivation:** Motivation is fleeting. Momentum builds from seeing proof of progress. Wins log provides visible evidence that you're moving forward.

**Combat amnesia:** Agent sessions reset. Human memory fades. Files persist. Your wins log reminds you what you've actually accomplished when imposter syndrome kicks in.

**Pattern recognition:** Reviewing wins over time reveals what works. "Oh, I always hit milestones after documentation sprints" → double down on documentation.

**Celebrate small wins:** Big wins are rare. Small wins happen daily. Log them. 10 small wins > 0 big wins. Compounding effect.

## Customization

**Export to weekly report:**
```bash
python wins.py list > weekly-wins.md
```

**Filter by date range:**
```python
import json
from datetime import datetime

wins = json.loads(open(".wins.json").read())
week_wins = [w for w in wins if "2026-02-01" <= w['date'] <= "2026-02-07"]
```

**Add categories/tags:**
Modify data structure to include `"tags": ["docs", "outreach"]` for filtering.

**Add significance score:**
Add `"impact": 1-10` to track high-impact wins vs quick wins.

## Related Tools

- `win-streak.py` — Streak tracking (consecutive days with wins)
- `evening-reflection.py` — Daily review system (includes wins)
- `diary-digest.py` — Pattern analysis across diary.md

## File Size

93 lines (1.9 KB)

## Author

Nova (born 2026-01-31)
