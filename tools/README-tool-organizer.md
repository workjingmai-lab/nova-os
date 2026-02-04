# tool-organizer.py — Tool Categorization & Consolidation Advisor

**Purpose:** Analyzes the tools/ directory, categorizes tools by function, and identifies consolidation opportunities to reduce tool sprawl.

**Category:** Workspace Management

**Created:** 2026-01-31

---

## What It Does

Scans all Python scripts in `tools/` and:
- **Categorizes** tools by function (Moltbook, Goals, Analysis, Automation, etc.)
- **Groups** related tools together
- **Identifies** consolidation opportunities (similar tools that could merge)
- **Provides** actionable recommendations for tool cleanup

---

## When to Use

- **Weekly:** Review tool organization and identify consolidation opportunities
- **Before** building new tools — check if similar tools already exist
- **After** a tool-building sprint — identify and merge overlapping tools
- **When** tools/ directory feels cluttered or hard to navigate

---

## Usage

```bash
# Run full analysis
python3 tools/tool-organizer.py
```

**Output sections:**
1. **Tools by Category** — All tools grouped by function (Moltbook, Goals, Analysis, etc.)
2. **Consolidation Opportunities** — Tools with similar names that could merge (e.g., `goal-tracker.py` + `goal-tracker-v2.py` → `goal-suite.py`)
3. **Statistics** — Total tools, categories, averages
4. **Recommendations** — Actionable next steps (archive unused, consolidate, create suites)

---

## How It Works

**Categorization logic:**
- Scans tool filenames for keywords (e.g., "moltbook" → Moltbook category)
- Groups tools by function using predefined keyword lists
- Falls back to "Other" if no match

**Consolidation detection:**
- Strips common suffixes from filenames (`-tracker`, `-analyzer`, `-monitor`)
- Groups tools with the same base name
- Highlights groups with 2+ tools as consolidation candidates

**Recommendations:**
- Identifies largest categories (may need sub-categorization)
- Suggests archiving unused tools (>30 days no use)
- Recommends creating "suite" tools for related functionality

---

## Examples

**Sample output:**
```
📁 TOOLS BY CATEGORY:
------------------------------------------------------------

Analysis (15):
  • diary-digest.py
  • pattern-analyzer.py
  • work-pattern-analyzer.py
  ...

🔍 CONSOLIDATION OPPORTUNITIES:
------------------------------------------------------------

📦 goal (3 tools):
     • goal-tracker.py
     • goal-tracker-v2.py
     • goal-progress.py
     → Consider: goal-suite.py
```

---

## Insights from Use

> "Tool sprawl kills productivity. 100 tiny tools → hard to find, hard to use, hard to maintain. Consolidation → fewer tools, clearer purpose, easier ecosystem."

> "Similar tools with version suffixes (v1, v2) are consolidation signals. One well-designed tool > three half-baked variants."

---

## Related Tools

- **workspace-cleanup.py** — Cleans orphaned files and empty directories
- **tool-usage-analysis.py** — Identifies 80/20 patterns in tool usage
- **quick-wins.md** — 30 one-minute tasks for when blocked

---

## Why It Exists

During Week 2, I built 25+ new tools in a few days. The tools/ directory became hard to navigate. I needed a way to:
1. See what tools exist at a glance
2. Identify overlapping tools that could merge
3. Keep the ecosystem lean and maintainable

**Result:** Consolidated 3 daily reporting tools into 1 (38% code reduction), identified 5+ other consolidation opportunities.

---

## Maintenance

- Update `CATEGORIES` dict when new tool types emerge
- Run weekly during workspace review
- Archive unused tools to `deprecated/` instead of deleting
- Update QUICK-TOOL-REF.md with top 10 most-used tools

---

**Status:** ✅ Active — Used weekly for tool organization
**Last Updated:** 2026-02-03
**Lines of Code:** ~180
