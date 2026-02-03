# morning-goals.py — Daily Planning Generator

## What It Does

Generates 3-5 focused goals for the day by combining:
- **Active long-term goals** (from `goals/active.md`)
- **Recent momentum** (from `diary.md` achievements)
- **Yesterday's incomplete items** (carry forward)
- **Smart defaults** (if above sources are empty)

Outputs to `today.md` in clean, actionable format.

## When to Use

**Every morning** as part of your daily routine:
1. Run `python tools/morning-goals.py`
2. Review generated goals in `today.md`
3. Adjust manually if needed
4. Execute against goals all day

## Usage

```bash
# Generate today.md with daily goals
python tools/morning-goals.py

# Preview goals without writing
python tools/morning-goals.py preview
```

## How It Works

1. **Reads active goals**: Scans `goals/active.md` for unchecked `- [ ]` items
2. **Analyzes recent wins**: Parses `diary.md` for `🏆 ACHIEVEMENT:` entries (last 24h)
3. **Identifies carry-overs**: Finds yesterday's incomplete/pending items
4. **Mixes smart defaults**: Adds "learn," "document," "engage" goals if sources run dry
5. **Generates 4 goals** (balanced across categories)
6. **Backs up old today.md**: Preserves previous day's plan as `.backup`

## Output Format

Generated `today.md` includes:
- Date and weekday header
- 4 prioritized goals with checkboxes
- Context stats (heartbeats, goals completed, generation time)
- Recent momentum list (last 3 achievements)

## Why It Matters

**Eliminates decision fatigue.** Instead of "what should I do today?" you wake up to a ready-made plan. Combines long-term focus with daily progress tracking.

**Maintains continuity.** Carries forward yesterday's incomplete work while celebrating recent wins.

**Faster than planning manually.** 1 command vs 10 minutes of thinking.

## Dependencies

- `diary.md` — Your work log (achievement entries)
- `goals/active.md` — Long-term goals checklist format
- `.agent_state.json` — Stats tracking (auto-created if missing)

## See Also

- `daily-report.py` — End-of-day summary
- `goal-tracker.py` — Progress tracking across goals
- `evening-reflection.py` — Day review and tomorrow planning
