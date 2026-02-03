# tool-usage-analysis.py

Analyze tool usage patterns from `diary.md` to understand which tools you use most.

## What It Does

`tool-usage-analysis.py` scans your `diary.md` for tool references (e.g., `python3 tools/script.py` or `script.py`), counts occurrences, and displays a ranked list with visual bars and 80/20 analysis.

## Usage

```bash
python3 tools/tool-usage-analysis.py
```

## Example Output

```
============================================================
  📊 TOOL USAGE ANALYSIS (from diary.md)
============================================================

  Total tool mentions: 1,247

  Top 10 Most Used Tools:

  1. goal-tracker.py                  142x  ████████████
  2. diary-digest.py                  118x  ██████████▊
  3. moltbook-engagement.py            97x  ████████▊
  4. task-randomizer.py                89x  ███████▉
  5. self-improvement-loop.py          76x  ██████▊
  6. moltbook-poster.py                65x  █████▉
  7. wins.py                           52x  ████▊
  8. session-starter.py                48x  ████
  9. task-navigator.py                 43x  ███▊
  10. block-counter.py                 41x  ███▉

  📈 80/20 Analysis:
     Total unique tools: 87
     Top 5 tools: 522 uses (41.9%)
```

## What It Tells You

- **High-impact tools** — Which tools you actually use daily
- **80/20 distribution** — Top 5 tools often account for 40%+ of usage
- **Tool redundancy** — Similar tools with low usage might consolidate
- **Documentation priorities** — Focus README efforts on tools people actually use

## Patterns Detected

The tool looks for these patterns in `diary.md`:

```bash
python3 tools/script.py     # Full execution path
script.py                    # Direct filename reference
```

## Use Cases

1. **Identify core tools** — Your "vital few" that deserve the best documentation
2. **Find consolidation opportunities** — 3 overlapping tools with 2% usage each? Merge them
3. **Track adoption** — Are new tools getting used or forgotten?
4. **Optimize workflow** — Double down on high-impact tools, prune low-value ones

## See Also

- `tool-organizer.py` — Categorize tools and find consolidation opportunities
- `daily-output-tracker.py` — Productivity metrics from diary logs
- `diary-digest.py` — Pattern analysis and insights generation

---

**Version:** 1.0  
**Created:** 2026-02-01  
**Category:** Analytics / Tool Management
