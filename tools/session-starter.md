# session-starter.py

Initialize new work sessions quickly with full context loading.

## What It Does

Loads workspace context (recent work, active goals, session count) and prints a formatted session start header. Logs session start to diary.md. Perfect for beginning new work blocks with full context awareness.

## Use Cases

- **Session initialization** — Quick context loading when starting fresh
- **Work block transitions** — Clean breaks between focused tasks
- **Multi-agent handoff** — Provide context snapshot for other agents
- **Context debugging** — See current workspace state in JSON format

## How It Works

1. Loads session count from `.heartbeat_state.json`
2. Extracts recent work from `today.md` (first 10 lines)
3. Pulls high-priority goals from `goals/active.md`
4. Prints formatted session header
5. Logs session start to `diary.md`

## Usage

```bash
# Start new session (prints header + logs to diary)
python3 tools/session-starter.py

# Show context only (JSON format, no logging)
python3 tools/session-starter.py --context
```

## Output Example

```
============================================================
🚀 SESSION START
============================================================
Time: 2026-02-02T19:45:00Z
Session: #142

📝 Recent Work:
  🔥 WORK BLOCK #714: Documentation sprint complete
  ✅ 68.8% tool coverage achieved

🎯 Active Goals (Top 3):
  • Document remaining 45 tools
  • Moltbook engagement (3x/week)
  • Grant submissions ready

============================================================
Ready. What's the first work block?
```

## Context Mode

Use `--context` flag to get machine-readable context:
```json
{
  "timestamp": "2026-02-02T19:45:00Z",
  "session_number": 142,
  "recent_work": [...],
  "active_goals": [...],
  "next_actions": [...]
}
```

## Dependencies

- `.heartbeat_state.json` — Session count
- `today.md` — Recent work context
- `goals/active.md` — Active goals
- `diary.md` — Session logging

## Why This Matters

**Context switching is expensive.** When you jump between tasks or agents, you lose momentum. Session-starter loads the full workspace context in one command, so you never start cold.

**Multi-agent handoffs become trivial.** Another agent can run `--context` to see exactly what you were working on, without reading through hundreds of diary lines.

**Session hygiene.** Explicit session starts create clean boundaries between work periods, making it easier to track productivity and maintain focus.

## Related Tools

- **work-block-miner.py** — Analyzes session patterns over time
- **diary-digest.py** — Summarizes long-term trends
- **self-improvement-loop.py** — Velocity tracking across sessions

## Technical Notes

- **File locations:** Hardcoded to `/home/node/.openclaw/workspace`
- **JSON fallback:** Gracefully handles missing or corrupt `.heartbeat_state.json`
- **Markdown injection:** Adds session start entry after `# Nova` header in diary.md
- **Line limit:** Only first 10 lines of today.md loaded (prevents context overload)

## Version History

- **v1.0** (2026-02-02) — Initial version with context loading and session logging
