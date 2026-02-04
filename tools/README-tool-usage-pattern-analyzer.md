# README — tool-usage-pattern-analyzer.py

**Analyzes tool usage patterns to identify what's actually being used**

---

## What It Does

Scans `diary.md` for tool invocations and generates:
- **Usage frequency:** Top 10 most-used tools
- **Category breakdown:** Tools by function (Workflow, Analytics, Revenue, etc.)
- **Unused tools:** Identifies tools never invoked
- **Pareto analysis:** How many tools provide 80% of value
- **Consolidation opportunities:** Categories with >10 tools (candidates for merging)

**Why this matters:** 115+ tools create maintenance debt. Understanding what's actually used helps prioritize documentation, consolidation, and deletion.

---

## Usage

```bash
python tools/tool-usage-pattern-analyzer.py
```

**No arguments needed** — scans diary.md and tools/ automatically.

---

## Example Output

```
🔍 Tool Usage Pattern Analyzer
==================================================

📊 Tool Inventory: 115 tools

By Category:
  Analytics: 28 tools
  Workflow: 22 tools
  Revenue: 18 tools
  Documentation: 12 tools
  Automation: 9 tools
  Other: 26 tools

📈 Usage Analysis: 1,433 invocations logged

🔥 Top 10 Most Used Tools:
  moltbook-suite.py: 156 uses
  revenue-tracker.py: 143 uses
  task-randomizer.py: 128 uses
  diary-digest.py: 97 uses
  goal-tracker.py: 84 uses
  daily-report.py: 76 uses
  moltbook-engagement.py: 65 uses
  blocker-status.py: 54 uses
  analytics.py: 48 uses
  session-logger.py: 42 uses

📦 Unused Tools: 38 (33.0%)
  - old-script.py
  - experimental-feature.py
  - ...

🎯 Core Tools Analysis (Pareto 80/20):
  8 tools provide 80% of usage (6.9% of inventory)
  Core tools: moltbook-suite.py, revenue-tracker.py, task-randomizer.py...

🔧 Consolidation Opportunities:
  Analytics: 28 tools - consider consolidation
  Workflow: 22 tools - consider consolidation
==================================================
```

---

## What It Detects

**Usage patterns:**
- Extracts tool names from diary work blocks (pattern: `Work block X: tool-name.py`)
- Counts invocations per tool
- Identifies tools never logged

**Categories:**
- **Workflow:** diary-, goal-, task-, block-, session-, heartbeat
- **Analytics:** analytics, tracker, metrics, report, pattern, usage
- **Revenue:** grant, service, revenue, proposal, moltbook, code4rena
- **Automation:** batch, executor, runner, automation, nexus
- **Documentation:** readme, docs, document
- **Testing:** test, check, verify, validate
- **Other:** Everything else

**Consolidation signals:**
- Categories with >10 tools are candidates
- Unused tools (>30% unused suggests cleanup needed)
- Pareto 80/20: Small % of tools providing majority of value

---

## When to Use

**Use when:**
- Planning tool consolidation or cleanup
- Prioritizing documentation efforts
- Understanding which tools to maintain vs deprecate
- Reviewing ecosystem health

**Before:**
- Deleting old tools
- Merging overlapping functionality
- Planning refactoring work

---

## Actionable Insights

**Pareto Principle (80/20):**
- If 8 tools provide 80% of value → document and enhance those first
- Unused 33% of tools → consider deletion or archival

**Consolidation candidates:**
- Analytics: 28 tools with overlapping functionality
- Workflow: 22 tools for task/goal management

**Documentation priority:**
- Top 10 most-used tools should have best READMEs
- Unused tools need less documentation investment

---

## Technical Details

- **Input:** `diary.md` (session logs), `tools/*.py` (tool inventory)
- **Pattern matching:** Regex extracts `Work block X: tool-name.py` format
- **Categories:** Auto-assigned by filename patterns
- **Dependencies:** Python 3 stdlib only

---

## Related Tools

- `tool-consolidation-opportunities.py` — Identifies tiny tools for merging
- `analytics.py` — General analytics dashboard
- `diary-digest.py` — Summarizes diary entries

---

**Created:** 2026-02-04
**Category:** Analytics / Tool Management
**Priority:** Medium (useful for cleanup planning)
