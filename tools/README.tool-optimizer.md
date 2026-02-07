# tool-optimizer.py

Analyze tool usage patterns and suggest optimization actions (archive, consolidate, prioritize). Maintains healthy ecosystem as tool count grows.

## What It Does

- **Scans diary.md:** Counts tool mentions (usage frequency)
- **Analyzes tools:** Age, size, documentation status
- **Identifies patterns:**
  - Unused tools (archival candidates)
  - Duplicate tools (consolidation candidates)
  - Popular tools (high-priority maintenance)
- **Suggests actions:** Concrete recommendations based on data

## Usage

```bash
# Show archival candidates (unused tools)
python3 tools/tool-optimizer.py --unused

# Show consolidation candidates (duplicate tools)
python3 tools/tool-optimizer.py --duplicates

# Show high-priority tools (most used)
python3 tools/tool-optimizer.py --popular

# Full optimization report
python3 tools/tool-optimizer.py --report
```

## Metrics Tracked

- **Mention count:** How often tool appears in diary.md
- **Age:** Days since last file modification
- **Size:** Lines of code (larger = higher maintenance cost)
- **Documentation:** README exists or not

## Categories

### Unused Tools
- Never mentioned in diary.md
- Large files are archival priority (high cost, zero benefit)
- Archive to `tools/archived/` to preserve without maintaining

### Duplicate Tools
- Similar names suggest overlapping functionality
- Consolidate into single, more complete tool
- Add migration note to README

### Popular Tools
- High mention count = high impact
- Prioritize testing and optimization
- Breakage affects many workflows

## Example Output

```
🛠️ TOOL OPTIMIZATION REPORT
======================================================================
📊 OVERVIEW
----------------------------------------------------------------------
  Total tools:        193
  Total mentions:     2847
  Tools with usage:   127
  Tools unused:       66
  Avg mentions/tool:  14.7

📚 DOCUMENTATION
----------------------------------------------------------------------
  With README:        193 (100.0%)
  Without README:     0

💡 RECOMMENDATIONS
----------------------------------------------------------------------
  • Archive 66 unused tools (>10%)
     → Reduces maintenance burden
  • revenue-tracker.py has 312 mentions (high impact)
     → Add tests, optimize, document thoroughly
```

## When to Use

1. **Weekly maintenance** — Check `--report` for ecosystem health
2. **Before adding new tools** — Run `--duplicates` to avoid overlap
3. **Monthly cleanup** — Archive unused tools (`--unused`)
4. **Prioritizing work** — Focus on `--popular` tools for maximum impact

## Optimization Strategy

**Archival:**
- Tools with 0 mentions for >30 days
- Large files (high maintenance cost)
- Move to `tools/archived/` with README note

**Consolidation:**
- Merge tools with similar names/purposes
- Keep larger/more complete version
- Update references in diary.md

**Prioritization:**
- Top 10 tools by mentions get priority
- Add tests for stability
- Optimize for performance
- Document thoroughly

## Files Used

- **Reads:** `diary.md` (for usage data), `tools/*.py` (metadata)
- **Creates:** None (read-only analysis)

## Integration with Other Tools

- **tool-usage-analysis.py** — More detailed usage breakdown
- **tool-consolidation-*.md** — Consolidation methodology
- **diary.md** — Source of usage data

## Why This Matters

With 193 tools and growing:
- **Maintenance burden** scales with tool count
- **Unused tools** waste cognitive overhead
- **Duplicates** create confusion (which one to use?)
- **Popular tools** need extra attention (breakage = high impact)

**Optimization keeps ecosystem healthy:**
- Archive dead weight → faster navigation
- Consolidate duplicates → clearer purpose
- Prioritize popular → maximize impact

---

**Tool created:** 2026-02-05 (Work block 2251)
**Purpose:** Maintain healthy tool ecosystem as count scales
**Status:** Ready for weekly maintenance use
