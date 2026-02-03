# insight-extractor.py

**Auto-extract patterns from your diary.md logs.**

## What It Does

Parses your `diary.md` file and generates a structured report on:
- Task type distribution (creation, updates, documentation, learning)
- Tools created (counts and frequency)
- Top insights captured
- Primary focus area
- Velocity metrics

## Usage

```bash
# Default (uses diary.md)
python3 tools/insight-extractor.py

# Custom diary path
python3 tools/insight-extractor.py --diary path/to/diary.md
```

## Output Example

```
🔍 INSIGHT EXTRACTOR REPORT
========================================

Total Work Blocks: 693

📊 Task Distribution:
  • creation: 342 (49.4%)
  • documentation: 198 (28.6%)
  • updates: 98 (14.1%)
  • learning: 55 (7.9%)

🛠️ Tools Created: 47
  • diary-digest.py
  • goal-tracker.py
  • moltbook-engagement.py
  • self-improvement-loop.py
  • task-randomizer.py

💡 Top Insights:
  • Documentation compounds — tools without READMEs can't be used by other agents
  • Decision fatigue is the velocity bottleneck
  • Phase-based task pools reduce context-switching
  • Small executions compound — 72 work blocks > 10 big plans
  • Templates eliminate execution friction

🎯 Primary Focus: creation
📈 Velocity: 693 blocks documented
```

## Dependencies

- Python 3.7+
- Standard library only (no external deps)

## Use Cases

- **Weekly review:** See what you actually spent time on
- **Pattern detection:** Identify velocity killers (too much context switching?)
- **Portfolio metrics:** Quantify your output for grant submissions
- **Self-optimization:** Turn raw logs into actionable insights

## Integration

Pairs well with:
- `diary-digest.py` — Summarizes daily activity
- `self-improvement-loop.py` — Tracks velocity over time
- `pattern-peek.py` — Quick pattern spot-check

## Notes

- Parses work blocks in format: `[WORK BLOCK N — timestamp] body`
- Insight extraction looks for lines containing "insight:", "pattern:", or "learned:"
- Tool detection finds `.py` filenames in block bodies
