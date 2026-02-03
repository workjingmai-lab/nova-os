# session-logger.sh — Session Activity Logger

**Version:** 1.0  
**Category:** Logging / Analytics  
**Created:** 2026-02-01

---

## What It Does

Logs session start/end times, work blocks, and key events. Provides a clean record for session analysis and handoffs.

### Features

- Timestamps session boundaries
- Counts work blocks per session
- Logs key events and outcomes
- Outputs to `diary.md` or custom files
- Human-readable summaries

---

## Usage

```bash
# Start a new session
./tools/session-logger.sh start "Deep Work"

# End session
./tools/session-logger.sh end "Deep Work"

# Log an event within session
./tools/session-logger.sh log "Completed tool documentation sprint"

# Generate session summary
./tools/session-logger.sh summary
```

---

## Session Log Format

```markdown
## Session: Deep Work
**Start:** 2026-02-02T18:00:00Z
**End:** 2026-02-02T20:45:00Z
**Duration:** 2h 45m
**Work Blocks:** 45

**Events:**
- Completed tool documentation sprint
- Published 5 messages to leads
- Moltbook post drafted

**Outcome:** High-value execution, documentation sprint complete
```

---

## Dependencies

- Standard Unix tools (`date`, `grep`, `wc`)
- `diary.md` for persistent logging

---

## Configuration

Edit variables:

```bash
SESSION_LOG_DIR="${SESSION_LOG_DIR:-logs/sessions}"
DIARY_FILE="${DIARY_FILE:-diary.md}"
DEFAULT_SESSION_NAME="${DEFAULT_SESSION_NAME:-Work Session}"
```

---

## Output Locations

- Session logs: `logs/sessions/YYYY-MM-DD-session-name.md`
- Diary entries: Appended to `diary.md`
- Summaries: Printed to stdout

---

## Integration

- Pair with `session-starter.py` for full session initialization
- Use `session-summary.py` for formatted reports
- Feed into `work-block-miner.py` for pattern analysis

---

## Tips

1. Always start/end sessions for accurate tracking
2. Use descriptive session names ("Deep Work", "Content Sprint")
3. Log key events as they happen for context
4. Review session summaries weekly to identify patterns
