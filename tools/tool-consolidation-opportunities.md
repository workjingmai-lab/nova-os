# tool-consolidation-opportunities.py

## What It Does

Analyzes Nova's toolkit to identify consolidation opportunities - tools that could be merged, simplified, or better organized. Helps reduce maintenance debt and improve ecosystem quality.

## How It Works

Scans all `.py` files in `tools/` and categorizes them by:

1. **Tiny tools (< 2KB)** - Small utilities that could merge into shared modules
2. **Similar naming patterns** - Tools with overlapping naming that might have duplicate functionality
3. **Single-function tools (< 4KB)** - Simple tools that could consolidate into theme-based collections
4. **Undocumented tools** - Tools without READMEs (candidates for deprecation or documentation)

## Usage

```bash
# Run full analysis
python3 tools/tool-consolidation-opportunities.py

# Example output:
# 🔧 Tool Consolidation Opportunities
# 📊 Tool Inventory: 144 tools (486.3 KB total)
# 📏 Size Distribution: Tiny (8), Small (120), Large (16)
# 🎯 Consolidation Opportunities: [categories with counts]
```

## What It Outputs

- **Tool inventory stats:** Total count, total size, average size
- **Size distribution:** Breakdown by tiny (< 2KB), small (2-10KB), large (≥ 10KB)
- **Consolidation categories:** Each with count, recommendation, and example candidates
- **Most complex tools:** Top 10 by function count (helps identify core tools to keep separate)

## When to Use It

- **Weekly toolkit review** - Identify consolidation candidates before they accumulate
- **Before adding new tools** - Check if similar functionality already exists
- **Maintenance sprints** - Reduce tool bloat by merging utilities
- **Documentation audits** - Find undocumented tools that need READMEs or removal

## Insights from Last Run (2026-02-04)

- **144 tools total** (486 KB)
- **8 tiny tools (< 2KB)** - Merge candidates
- **8 single-function tools (< 4KB)** - Theme-based consolidation
- **16% documentation coverage** (23/144 tools have READMEs)
- **Most complex:** goal-tracker (24 functions), moltbook-suite (22 functions)

## Key Principle

**Tool bloat = maintenance debt.** Every tool needs documentation, testing, and updates. Consolidation reduces surface area while preserving functionality.

## See Also

- `toolkit-search.py` - Search and discover tools
- `toolkit-overview.md` - Full toolkit documentation
- `knowledge/tool-consolidation-strategy.md` - Consolidation principles
