# session-summary.py

Quick snapshot of what you accomplished this session.

## What It Does

Displays work block count and recent wins from `.wins.json` in a clean, time-sorted format. Perfect for end-of-session reviews or heartbeat check-ins.

## Use Cases

- **Session wrap-up** — See what you accomplished before signing off
- **Heartbeat reporting** — Quick status check during scheduled tasks
- **Motivation boost** — Visual proof of progress (wins don't lie)
- **Velocity tracking** — Verify work block count matches expectations

## How It Works

1. Reads work block count from `today.md` (parses `**Work Blocks Completed:**` line)
2. Loads recent wins from `.wins.json` (managed by `wins.py`)
3. Prints formatted summary with timestamps and descriptions
4. Truncates long descriptions to 60 chars (clean output)

## Usage

```bash
python3 tools/session-summary.py
```

## Output Example

```
📊 Session Summary — 2026-02-02 19:50 UTC
🔸 Work Blocks: 715
🔸 Recent Wins (5):
   19:45 | Documented session-starter.py (workspace context loader)
   19:39 | Work block miner README created (pattern insights)
   19:38 | Weekly reporter tool documented (automation)
   19:37 | Heartbeat viz README completed (universal visualizer)
   19:36 | Daily snapshot documented (deprecated, migration path)
```

## Dependencies

- `today.md` — Work block count (parsed from `**Work Blocks Completed:**` line)
- `.wins.json` — Recent wins array (managed by `wins.py`)

## Data Sources

### today.md
Must contain line like:
```markdown
**Work Blocks Completed:** 715
```

### .wins.json
Must contain array like:
```json
[
  {
    "timestamp": "2026-02-02T19:45:00Z",
    "description": "Documented session-starter.py"
  }
]
```

## Why This Matters

**Evidence of progress.** When you're deep in the trenches, it's easy to lose sight of how much you've actually done. Session-summary shows you the receipts.

**Pattern reinforcement.** Seeing your wins in chronological order builds confidence and highlights productive patterns (e.g., "I ship most documentation between 19:30-19:45").

**Heartbeat hygiene.** Including this in scheduled tasks creates a rhythm of reflection, not just execution.

## Related Tools

- **wins.py** — Manages the `.wins.json` log
- **self-improvement-loop.py** — Velocity tracking and insights
- **today-summary.py** — Human-readable daily summary for Arthur
- **diary-digest.py** — Long-term pattern analysis

## Integration Tips

**Add to heartbeat checklist:**
```bash
# In HEARTBEAT.md or heartbeat script
echo "📊 Session Status:"
python3 tools/session-summary.py
```

**Use with cron:**
```bash
# Every hour, log session status to diary
0 * * * * python3 /home/node/.openclaw/workspace/tools/session-summary.py >> /home/node/.openclaw/workspace/diary.md
```

## Technical Notes

- **Time format:** Extracts HH:MM from ISO timestamps or short formats
- **Description truncation:** Cuts at 60 chars with "..." suffix
- **Error handling:** Gracefully handles missing files (returns 0 blocks, empty wins)
- **JSON parsing:** Expects `.wins.json` to be valid JSON array
- **Block count parsing:** Extracts first integer after `**Work Blocks Completed:**`

## Limitations

- **Read-only** — Doesn't update any files (just displays)
- **No aggregation** — Shows raw wins, doesn't group or analyze
- **Manual wins** — Requires `wins.py` to log wins automatically
- **Hardcoded paths** — Expects specific workspace structure

## Future Enhancements

Potential improvements:
- **Time filtering** — Show wins from last N hours only
- **Category grouping** — Group wins by type (code, docs, outreach)
- **Velocity calculation** — Show blocks/hour based on session start time
- **Mood tracking** — Add emoji or sentiment to wins
- **Export modes** — JSON, CSV, or Markdown formats

## Version History

- **v1.0** (2026-02-02) — Initial version with work block parsing and wins display
