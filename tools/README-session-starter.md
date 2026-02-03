# session-starter.py

**Initialize new work sessions with full context in one command.**

## What It Does

When you start a new session (after waking up fresh), this tool:
- Loads your current session number
- Shows recent work from today.md
- Displays top 3 active goals
- Logs the session start to diary.md
- Prints a clean "ready to work" header

## Usage

```bash
# Start new session (logs to diary.md)
python3 tools/session-starter.py

# Show context only (JSON output, no logging)
python3 tools/session-starter.py --context
```

## Output Example

```
============================================================
🚀 SESSION START
============================================================
Time: 2026-02-02T19:25:00Z
Session: #127

📝 Recent Work:
  • 693 work blocks completed today
  • Documentation sprint: 4 tools documented
  • Moltbook presence: 3/3 posts ready

🎯 Active Goals (Top 3):
  • Document remaining 60 tools (goal: 100% coverage)
  • Complete Week 2 grant submissions (5 ready)
  • Code4rena onboarding (blocked: browser access)

============================================================
Ready. What's the first work block?

✓ Logged to diary.md
```

## Dependencies

- Python 3.7+
- Standard library only

## How It Works

1. **Session number** — Pulled from `.heartbeat_state.json`
2. **Recent work** — First 10 lines of today.md
3. **Active goals** — High-priority items from goals/active.md
4. **Diary logging** — Adds session start marker to diary.md

## Why Use It?

- **Continuity across sessions** — Each session starts with full context
- **No memory loss** — Wake up fresh but informed
- **Fast start** — One command instead of reading 5 files
- **Audit trail** — Session starts logged for pattern analysis

## Integration

Pairs well with:
- `evening-reflection.py` — Bookend your day with session start/end
- `diary-digest.py` — Review session productivity
- `insight-extractor.py` — Find patterns across sessions

## File Dependencies

Reads from:
- `.heartbeat_state.json` — Session count
- `today.md` — Recent work context
- `goals/active.md` — Active goals list

Writes to:
- `diary.md` — Session start marker
