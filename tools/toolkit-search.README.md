# toolkit-search.py

**Part of Nova's Toolkit — Discovery & Navigation**

## Overview

Fast indexed search for discovering tools, scripts, and utilities in Nova's toolkit. Maintains a JSON index of all tools with metadata, categories, and search capabilities.

## What It Does

- Scans `tools/` directory for Python scripts and shell scripts
- Extracts metadata (description, categories, CLI args, file size)
- Builds searchable JSON index for fast queries
- Supports full-text search across names, descriptions, and categories
- Lists tool statistics and category breakdowns

## When to Use

- Finding the right tool for a specific task
- Discovering tools by category (api, automation, messaging, monitoring, etc.)
- Getting toolkit statistics (total tools, size, categories)
- Browsing all available tools with descriptions

## How to Use

### Search for tools:
```bash
python3 tools/toolkit-search.py grant
python3 tools/toolkit-search.py telegram
python3 tools/toolkit-search.py automation
```

### List all tools:
```bash
python3 tools/toolkit-search.py --list
python3 tools/toolkit-search.py --list --top 20
```

### Filter by category:
```bash
python3 tools/toolkit-search.py --category api
python3 tools/toolkit-search.py automation --category monitoring
```

### Show statistics:
```bash
python3 tools/toolkit-search.py --stats
python3 tools/toolkit-search.py --categories
```

### Rebuild index:
```bash
python3 tools/toolkit-search.py --rebuild
```

## Categories

Tools are auto-categorized by content analysis:

- **api** — API clients, HTTP requests, endpoints
- **automation** — Cron jobs, schedulers, triggers
- **collaboration** — Agent communication, task delegation
- **crypto** — Ethereum, Web3, wallets, solidity
- **data** — JSON/CSV processing, analysis
- **filesystem** — File operations, path handling
- **messaging** — Telegram, Discord, notifications
- **monitoring** — Watchers, alerts, health checks
- **web** — HTML, CSS, dashboards, serving

## Search Scoring

Results are ranked by relevance:
- **Name match:** +10 points (highest priority)
- **Description match:** +5 points
- **Category match:** +3 points
- **CLI arg match:** +2 points

Results are sorted by score descending.

## Index Format

Index stored at `.toolkit_index.json`:

```json
{
  "last_indexed": "2026-02-02T14:20:00Z",
  "tool_count": 88,
  "tools": [
    {
      "name": "goal-tracker",
      "filename": "goal-tracker.py",
      "description": "Track goal progress with metrics",
      "path": "tools/goal-tracker.py",
      "categories": ["automation", "monitoring"],
      "cli_args": ["--json", "--export"],
      "is_runnable": true,
      "is_shell": false,
      "size_kb": 12.34,
      "modified": "2026-02-01T10:30:00Z"
    }
  ]
}
```

## CLI Options

```
toolkit-search.py <query>       # Search tools by name/description
  --rebuild, -r                # Rebuild the index
  --category, -c <cat>         # Filter by category
  --list, -l                   # List all tools
  --categories, -C             # List categories with counts
  --stats, -s                  # Show toolkit statistics
  --verbose, -v                # Verbose output (CLI args, timestamps)
  --top, -n <num>              # Limit results (default: 10)
```

## Examples

### Find automation tools:
```bash
python3 tools/toolkit-search.py automation
# 🔍 Found 12 tool(s) for 'automation':
# 
# 📦 cron-manager
#    Manage cron jobs for agents
#    Categories: automation, monitoring
#    File: tools/cron-manager.py (15.2 KB)
```

### Browse all tools:
```bash
python3 tools/toolkit-search.py --list --top 5
# 📦 All Tools (88 total)
# 
# 📦 goal-tracker
#    Track goal progress with metrics
#    Categories: automation, monitoring
#    ...
```

### Get toolkit stats:
```bash
python3 tools/toolkit-search.py --stats
# 📊 Toolkit Statistics
#    Total tools: 88
#    Python tools: 82
#    Shell scripts: 6
#    Total size: 1245.6 KB
#    Categories: 9
#    Last indexed: 2026-02-02T14:20:00Z
```

## Index Maintenance

### Auto-rebuild:
- Index rebuilds automatically if missing or corrupted
- Checks file modification times for staleness

### Manual rebuild:
```bash
python3 tools/toolkit-search.py --rebuild
# ✅ Indexed 88 tools
```

### When to rebuild:
- After adding new tools to `tools/`
- After modifying tool descriptions
- After renaming or deleting tools

## Pro Tips

1. **Use fuzzy search** — Partial matches work (e.g., "auto" matches "automation")
2. **Category browsing** — Use `--categories` to discover tool types
3. **Verbose mode** — Use `-v` to see CLI arguments and modification times
4. **Regular updates** — Rebuild index weekly to stay current
5. **Wildcard search** — Empty query + `--list` shows all tools

## Performance

- **Index build:** ~2 seconds for 100 tools
- **Search query:** <50ms for typical searches
- **Index size:** ~50KB for 100 tools

## Related Tools

- `toolkit.md` — Manual tool reference (static)
- `blocker-tracker.py` — Track blockers affecting tool usage
- `tool-usage-patterns.py` — Analyze which tools get used most

## Version History

- **v1.0** — Initial release with indexed search
- Auto-categorization by content analysis
- CLI argument extraction
- Statistics and category browsing
- Verbose mode for detailed tool info

---

**Tool Category:** Discovery / Navigation
**Maintenance:** Rebuild index after tool additions
**Dependencies:** None (pure Python stdlib)
**Index Location:** `.toolkit_index.json`
