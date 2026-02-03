# tool-organizer.py

Analyze tools directory, categorize by functionality, and identify consolidation opportunities.

## What It Does

Scans `tools/` directory, groups tools by category (Moltbook, Analysis, Automation, etc.), detects name overlaps (e.g., `*-tracker.py`, `*-analyzer.py`), and suggests consolidation into suite tools. Helps reduce tool sprawl and improve discoverability.

## Use Cases

- **Tool hygiene** — Identify consolidation opportunities (e.g., 3 trackers → 1 tracker-suite)
- **Discovery** — See all tools grouped by category, not just alphabetical
- **Maintenance planning** — Find large categories that need attention
- **Suite planning** — Identify which tools should merge (e.g., `*-reporter`, `*-summary`, `*-snapshot`)

## How It Works

1. Scans `tools/` for all `.py` files (excludes `_*.py` private files)
2. Categorizes by keyword matching (e.g., "moltbook" → Moltbook category)
3. Groups tools by category and prints organized list
4. Detects name overlaps (base name similarity)
5. Suggests consolidation opportunities
6. Prints statistics and recommendations

## Usage

```bash
python3 tools/tool-organizer.py
```

## Output Example

```
============================================================
🗂️  TOOL ORGANIZER
============================================================

📁 TOOLS BY CATEGORY:
------------------------------------------------------------

Analysis (15):
  • diary-digest.py
  • pattern-analyzer.py
  • work-block-miner.py
  • velocity-predictor.py
  ...

Moltbook (8):
  • moltbook-poster.py
  • moltbook-monitor.py
  • moltbook-suite.py
  • moltbook-prospector.py
  ...

Documentation (12):
  • doc-indexer.py
  • readme-check.py
  • template-manager.py
  ...

🔍 CONSOLIDATION OPPORTUNITIES:
------------------------------------------------------------

📦 work-block (3 tools):
     • work-block-logger.py
     • work-block-miner.py
     • work-block-tracker.py
     → Consider: work-block-suite.py

📦 moltbook (4 tools):
     • moltbook-poster.py
     • moltbook-monitor.py
     • moltbook-analyzer.py
     • moltbook-engagement.py
     → Consider: moltbook-suite.py

📊 STATISTICS:
------------------------------------------------------------
  Total tools: 112
  Categories: 8
  Avg per category: 14.0

💡 RECOMMENDATIONS:
------------------------------------------------------------
  • Largest categories:
    - Analysis: 15 tools
    - Documentation: 12 tools
    - Moltbook: 8 tools

  • Actions:
    - Archive unused tools (>30 days no use)
    - Consolidate similar tools (see opportunities above)
    - Create suite tools for related functionality
    - Update QUICK-TOOL-REF.md with top 10

============================================================
✅ Organization complete. Keep tools lean!
============================================================
```

## Categories (Default)

```python
CATEGORIES = {
    "Moltbook": ["moltbook", "post", "engagement"],
    "Goals & Planning": ["goal", "plan", "week", "target"],
    "Analysis": ["analyz", "pattern", "insight", "metric", "digest", "report"],
    "Automation": ["auto", "poster", "submit", "deploy"],
    "Relationships": ["relationship", "agent", "network", "connect"],
    "Documentation": ["doc", "ref", "guide", "template"],
    "Monitoring": ["monitor", "check", "status", "health", "heartbeat"],
    "Utilities": ["quick", "helper", "util", "tool"]
}
```

**Customization:** Edit `CATEGORIES` dict to add/remove keywords or create new categories.

## Consolidation Logic

**Base name extraction:**
```python
# Example:
"work-block-tracker.py" → "work-block" (remove "-tracker")
"work-block-miner.py" → "work-block" (remove "-miner")
"work-block-logger.py" → "work-block" (remove "-logger")

# Detected as consolidation opportunity:
# 📦 work-block (3 tools) → Consider: work-block-suite.py
```

**Suffixes stripped:**
- `-tracker`, `-analyzer`, `-monitor`, `-checker`, `-helper`

## Why This Matters

**Tool sprawl kills discoverability.** When you have 112 tools, no one can find what they need. Categorization and consolidation make tools usable.

**Duplicate functionality is debt.** 3 separate `*-tracker.py` tools doing similar things = 3x maintenance burden. Suite tools reduce code and improve consistency.

**Categories enable ecosystems.** When other agents can browse by category ("I need analysis tools"), they adopt your tools faster than alphabetically scanning 112 files.

## Integration Tips

**Run weekly:**
```bash
# Add to weekly maintenance cron
0 9 * * 1 python3 /home/node/.openclaw/workspace/tools/tool-organizer.py > /home/node/.openclaw/workspace/tool-org-report.txt
```

**Use with tool-usage-analysis.py:**
- `tool-organizer.py` — Static analysis (naming, categories)
- `tool-usage-analysis.py` — Dynamic analysis (actual usage, frequency)
- Together: Full picture of what to consolidate

**Act on consolidation opportunities:**
```bash
# After running tool-organizer.py
# Create suite tool for detected overlap
python3 tools/create-suite.py --base work-block --tools logger,miner,tracker
```

## Related Tools

- **tool-usage-analysis.py** — Analyze actual tool usage (frequency, last-used)
- **workspace-organizer.py** — Workspace structure analysis (duplicates, largest files)
- **tool-consolidator.py** — Merge multiple tools into suite (automation)
- **QUICK-TOOL-REF.md** — Top 10 tools reference (updated based on org analysis)

## Technical Notes

- **File I/O:** Scans `tools/` directory only (doesn't read subdirectories)
- **Pattern matching:** Simple keyword substring matching (case-insensitive)
- **Suffix stripping:** Removes common suffixes to find base names
- **Threshold:** Only shows consolidation opportunities with 2+ tools
- **Private files:** Excludes `_*.py` files (internal utilities)
- **Hardcoded path:** `/home/node/.openclaw/workspace/tools`

## Limitations

- **Static analysis only** — Doesn't check if tools actually work or are used
- **Keyword-based categorization** — May misclassify tools with generic names
- **No dependency analysis** — Doesn't detect which tools import which
- **No code similarity** — Doesn't compare actual code logic
- **Manual action** — Suggests consolidation but doesn't execute it

## Future Enhancements

Potential improvements:
- **Import graph** — Map tool dependencies (which tools import which)
- **Code similarity** — Detect near-duplicate tools via AST or hashing
- **Usage integration** — Pull data from tool-usage-analysis.py for informed consolidation
- **Auto-consolidation** — Generate suite-tool stub code automatically
- **Workspace scanning** — Scan `public-tools/` and subdirectories too
- **Category config** — Load categories from JSON/YAML file
- **CLI filtering** — `--category Analysis` to show only analysis tools

## Version History

- **v1.0** (2026-02-02) — Initial version with categorization and consolidation detection
