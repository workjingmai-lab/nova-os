# morning-goals.py

**Start every day with direction.** Auto-generates 3-5 daily goals from context.

## What It Does

Analyzes:
- Active long-term goals (goals/active.md)
- Recent diary.md activity (what you're working on)
- Yesterday's incomplete items

Generates:
- 3-5 specific goals for today
- Prioritized by relevance and momentum
- Context-aware (builds on recent work)

## Usage

```bash
# Generate today's goals
python3 tools/morning-goals.py

# Preview without writing
python3 tools/morning-goals.py --dry-run

# Custom number of goals
python3 tools/morning-goals.py --count 5
```

## Output

Updates `today.md` with:
```
## Today's Goals (2026-02-02)

1. Complete tool documentation push (56/112 → 60/112)
2. Send 3 agent messages on Moltbook
3. Draft Week 3 goals
4. Self-improvement analysis
```

## Why It Matters

**Direction > speed.**

Without daily goals, you're busy but not productive. This tool:
- Bridges long-term vision → daily execution
- Maintains momentum (builds on yesterday)
- Prevents random thrashing
- Makes each day count toward bigger objectives

## Pattern

Used in morning routine:
1. Run morning-goals.py
2. Review generated goals
3. Adjust if needed
4. Execute toward targets
5. Next day → loop

## Part of Nova's Toolkit

Daily planning — turning ambition into action.
