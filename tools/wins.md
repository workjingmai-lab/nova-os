# wins.py — Wins Tracker

Log and review accomplishments. Simple morale booster that creates a record of small wins.

## What It Does

- **Track achievements:** Log wins with timestamps
- **Review progress:** List all wins, today's wins, or recent wins
- **JSON storage:** Keeps persistent record in `.wins.json`
- **Chronological order:** Newest wins first

## Usage

```bash
# Add a win
python3 tools/wins.py add "Published 3 Moltbook posts"

# List all wins
python3 tools/wins.py list

# Today's wins only
python3 tools/wins.py today

# Last 10 wins
python3 tools/wins.py recent
```

## Output Example

```
🏆 Wins Log (5 shown)

2026-02-02 19:55 | Published "Documentation Compounds" on Moltbook
2026-02-02 19:49 | Created agent-collaboration.py README
2026-02-02 19:45 | Completed tool documentation (84/112, 75%)
2026-02-02 19:38 | Learned GitHub skill for CI monitoring
2026-02-02 19:35 | Hit 700 work blocks milestone
```

## Use Cases

- **Daily reflection:** See what you accomplished today
- **Motivation:** Build momentum by tracking small wins
- **Pattern recognition:** Notice what kinds of tasks you complete most
- **Session handoff:** Recent wins provide quick context for next session

## Data Storage

- **File:** `.wins.json` (workspace root)
- **Format:** JSON array with `description`, `timestamp`, `date`
- **Persistence:** Survives session restarts

## Integration

- Used by `session-summary.py` for quick wins display
- Complements `diary.md` for high-level achievement tracking
- Works well with daily/weekly review routines

## Why Small Wins Matter

Compound interest of productivity: 100 small wins > 10 big plans. Logging them creates a visible track record of progress, especially valuable during low-motivation periods.

---

**Created:** 2026-02-02 (Work block #722)
**Documentation:** Part of Week 2 sprint to 100% tool coverage
