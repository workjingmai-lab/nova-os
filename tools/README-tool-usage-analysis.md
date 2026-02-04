# tool-usage-analysis.py

Analyze which tools you actually use most — find your 80/20 pattern.

## What It Does

Scans `diary.md` for tool usage patterns, identifies top 10 most-used tools, and calculates 80/20 distribution (Pareto principle). Helps you understand which tools provide the most value.

## Installation

No dependencies required. Uses Python standard library only.

## Quick Start

```bash
python3 tools/tool-usage-analysis.py
```

**Output:**
```
============================================================
  📊 TOOL USAGE ANALYSIS (from diary.md)
============================================================

  Total tool mentions: 847

  Top 10 Most Used Tools:

  1. goal-tracker.py                   127x  ████████░░░░░░░░░░░░░
  2. moltbook-suite.py                  89x   ██████░░░░░░░░░░░░░░░
  3. diary-digest.py                    76x   ██████░░░░░░░░░░░░░░░
  4. task-randomizer.py                 54x   ████░░░░░░░░░░░░░░░░░
  5. self-improvement-loop.py           48x   ███░░░░░░░░░░░░░░░░░░
  6. revenue-tracker.py                 41x   ███░░░░░░░░░░░░░░░░░░
  7. grant-submit-helper.py             33x   ██░░░░░░░░░░░░░░░░░░░
  8. moltbook-monitor.py                29x   ██░░░░░░░░░░░░░░░░░░░
  9. service-outreach-tracker.py        21x   █░░░░░░░░░░░░░░░░░░░░
  10. work-pattern-analyzer.py          18x   █░░░░░░░░░░░░░░░░░░░░

  📈 80/20 Analysis:
     Total unique tools: 47
     Top 5 tools: 394 uses (46.5%)

============================================================
```

## How It Works

1. **Scans diary.md** for tool usage patterns
2. **Two pattern types:**
   - Direct execution: `python3 tools/script.py`
   - File references: `script.py`
3. **Counts mentions** and ranks by frequency
4. **Calculates percentages** and visualizes with bar charts
5. **Identifies 80/20 pattern** — do top 5 tools provide 80% of value?

## Use Cases

### 1. Identify Core Tools
Find out which tools you actually use every day:
```bash
$ python3 tools/tool-usage-analysis.py
# Top 5 tools = your core workflow
```

**Insight:** If 5 tools provide 46% of value, prioritize their documentation and maintenance.

### 2. Detect Tool Debt
Discover unused tools taking up space:
```bash
# 47 unique tools, but only 10 used regularly
# → 37 tools are candidates for deletion/consolidation
```

### 3. Optimize Learning
Focus on mastering high-impact tools:
```
If goal-tracker.py is used 127x, it's worth:
- Full README documentation
- Keyboard shortcuts
- Alias/automation setup
```

### 4. Track Workflow Evolution
Run weekly to see patterns:
```bash
# Week 1: Goal-tracker dominates (planning phase)
# Week 2: Moltbook-suite dominates (outreach phase)
# Week 3: Grant-submit-helper dominates (execution phase)
```

## Examples

### Basic Analysis
```bash
$ python3 tools/tool-usage-analysis.py

============================================================
  📊 TOOL USAGE ANALYSIS (from diary.md)
============================================================

  Total tool mentions: 847
  Top 10 Most Used Tools:
  1. goal-tracker.py                   127x
  ...
```

### Empty Diary Handling
```bash
$ python3 tools/tool-usage-analysis.py

============================================================
  📊 TOOL USAGE ANALYSIS (from diary.md)
============================================================

  Total tool mentions: 0

  No tool usage found in diary.md

  📈 80/20 Analysis:
     Total unique tools: 0
     No usage data available
```

## Data Source

**Reads from:** `/home/node/.openclaw/workspace/diary.md`

**Pattern matching:**
- `python3 tools/[script_name].py`
- `[script_name].py` (standalone references)

**Note:** Only counts `.py` files explicitly mentioned in diary.md, not all executed tools.

## Design Philosophy

**80/20 insight > vanity metrics.**

This tool isn't about total usage — it's about identifying which tools provide disproportionate value. If 5 tools account for 46% of usage, those 5 deserve:
- Best documentation
- Priority maintenance
- Keyboard aliases
- Feature requests

The remaining tools? Consider:
- Consolidation (3 overlapping tools → 1)
- Deprecation (unused for 30+ days)
- Documentation gaps (good but undiscovered)

## Return Codes

- `0` — Success (even if no tools found)
- `1` — Error (diary.md missing)

## Integration

### Weekly Analysis (HEARTBEAT.md)
```yaml
- name: "Weekly Tool Analysis"
  every: "7d"
  message: |
    python3 tools/tool-usage-analysis.py
    # Identify top 5 tools, document insights
    # Consider consolidating unused tools
```

### With tool-organizer.py
```bash
# Analyze usage, then organize workspace
python3 tools/tool-usage-analysis.py
python3 tools/tool-organizer.py --consolidate
```

### With self-improvement-loop.py
```bash
# Run analysis, feed into velocity tracking
python3 tools/tool-usage-analysis.py > analysis.txt
python3 tools/self-improvement-loop.py --input analysis.txt
```

## See Also

- `diary-digest.py` — Analyze patterns in diary entries
- `work-pattern-analyzer.py` — Deep dive into work sessions
- `task-randomizer.py` — Most-used tool for execution
- `tool-organizer.py` — Consolidate and organize tools
- `knowledge/tool-consolidation-analysis.md` — Tool debt audit

## Sample Insights

**From Week 2 analysis:**
- **Total tools:** 87
- **Regular usage:** 7 tools (8% of total)
- **Usage share:** 7 tools = 80% of mentions
- **Conclusion:** Core tools principle confirmed — 8% of tools provide 80% of value
- **Action:** Focus documentation on top 10, consolidate overlapping tools

**Example insight:**
```
Top 5 tools = 394 uses (46.5%)
→ If 5 tools provide half the value, they deserve half the maintenance effort
→ README priority: goal-tracker, moltbook-suite, diary-digest, task-randomizer, self-improvement-loop
```
