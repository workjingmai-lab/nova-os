# tool-usage-pattern-analyzer.py - Tool Usage Analytics

**Identify your most valuable tools, consolidation opportunities, and usage patterns from diary.md.**

## What It Does

`tool-usage-pattern-analyzer.py` analyzes your tool ecosystem to answer:
- Which tools do I actually use? (Top 10 most used)
- Which tools never get used? (Dead code)
- What's my core vs. long-tail distribution? (Pareto 80/20)
- Which categories have too many tools? (Consolidation targets)

## Usage

```bash
python3 tools/tool-usage-pattern-analyzer.py
```

## Output Example

```
🔍 Tool Usage Pattern Analyzer
==================================================

📊 Tool Inventory: 115 tools

By Category:
  Workflow: 28 tools
  Analytics: 24 tools
  Revenue: 18 tools
  Automation: 12 tools
  Documentation: 9 tools
  Other: 24 tools

📈 Usage Analysis: 1,442 invocations logged

🔥 Top 10 Most Used Tools:
  diary-digest.py: 145 uses
  moltbook-poster.py: 98 uses
  revenue-tracker.py: 76 uses
  block-counter.py: 65 uses
  velocity-calc.py: 54 uses
  workspace-status.py: 43 uses
  goal-tracker.py: 38 uses
  self-improvement-loop.py: 32 uses
  moltbook-engagement.py: 28 uses
  quick-commit.py: 21 uses

📦 Unused Tools: 23 (20.0%)
  - unused-script.py
  - old-helper.py
  - test-tool.py
  ...

🎯 Core Tools Analysis (Pareto 80/20):
  12 tools provide 80% of usage (10.4% of inventory)
  Core tools: diary-digest.py, moltbook-poster.py, revenue-tracker.py...

🔧 Consolidation Opportunities:
  Workflow: 28 tools - consider consolidation
  Analytics: 24 tools - consider consolidation

==================================================
✅ Analysis complete
```

## How It Works

1. **Tool Inventory**: Scans `tools/` directory for all `*.py` files
2. **Categorization**: Groups tools by naming patterns (Workflow, Analytics, Revenue, etc.)
3. **Usage Analysis**: Parses `diary.md` for `Work block X: tool-name.py` patterns
4. **Pareto Analysis**: Identifies the smallest set of tools that provide 80% of value
5. **Dead Code Detection**: Lists tools never invoked in the diary

## Categories Recognized

- **Workflow**: diary-, goal-, task-, block-, session-, heartbeat
- **Analytics**: analytics, tracker, metrics, report, pattern, usage
- **Revenue**: grant, service, revenue, proposal, moltbook, code4rena
- **Automation**: batch, executor, runner, automation, nexus
- **Documentation**: readme, docs, document
- **Testing**: test, check, verify, validate
- **Other**: Everything else

## Key Metrics

### Tool Utilization Rate
```
Utilization = (Used Tools / Total Tools) × 100%
```
Healthy range: 70-85%. Below 60% = too many unused tools.

### Core Tool Ratio
```
Core Ratio = (Core Tools for 80% Value / Total Tools) × 100%
```
Healthy range: 5-15%. Above 20% = tools too fragmented.

### Category Saturation
Categories with >10 tools are consolidation candidates.

## When to Use

- **Monthly reviews**: Identify dead code to delete
- **Tool building**: Check if similar tool exists before creating new one
- **Refactoring**: Find consolidation opportunities (merge 3× similar tools → 1)
- **Documentation prioritization**: Document core tools first (80/20 rule)

## Actionable Insights

### If Many Unused Tools (>30%)
→ Delete or archive them. Unused code = maintenance debt.

### If Core Ratio > 20%
→ Your tools are too fragmented. Consolidate overlapping functionality.

### If Category > 15 Tools
→ Consider a unified framework (e.g., moltbook-suite.py vs 5 separate Moltbook tools)

## Integration with Diary.md Format

The parser expects work blocks in this format:
```
### WORK BLOCK 1442: Documentation Sprint (1 minute)
**Action:** Created README for diary_parser.py
```

The tool name is extracted from the block title after "WORK BLOCK #:".

## Dependencies

- Python 3.6+
- Standard library only: `re`, `pathlib`, `collections`, `datetime`

## Files Read

- `/home/node/.openclaw/workspace/diary.md` — Usage patterns
- `/home/node/.openclaw/workspace/tools/*.py` — Tool inventory

## Related Tools

- `diary_parser.py` — Lower-level diary.md parsing library
- `tool-consolidation-opportunities.py` — Detailed consolidation analysis
- `tool-usage-analysis.py` — Frequency analysis over time

## Design Philosophy

**Pareto Principle in Action:** 20% of tools provide 80% of value. Focus documentation, maintenance, and optimization on that 20%. Delete or consolidate the rest.

**Unused Code is Debt:** Every tool requires:
- Documentation (README)
- Maintenance (bug fixes, updates)
- Mental load (remembering it exists)

If you don't use it, delete it.

## Version

Created: 2026-02-04
