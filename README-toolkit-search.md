# Toolkit Search — Fast Indexed Tool Discovery

**Tool:** `tools/toolkit-search.py` | **Purpose:** Indexed search for Nova's toolkit | **Status:** ✅ Active

---

## What It Does

Fast indexed search for discovering scripts, utilities, and automation tools in the workspace.

**Features:**
- **Indexed search** — scans tools/ directory, builds JSON index
- **Relevance scoring** — name (10 pts), description (5 pts), category (3 pts), CLI args (2 pts)
- **Category filtering** — 9 categories (api, data, automation, messaging, monitoring, web, filesystem, collaboration, crypto)
- **Auto-detection** — extracts metadata from Python and shell scripts
- **CLI args discovery** — parses argparse definitions
- **File stats** — size, modified time, runnable status

---

## Usage

### Basic Search
```bash
python3 tools/toolkit-search.py <query>
```

**Example:**
```bash
$ python3 tools/toolkit-search.py "moltbook"
🔍 Found 3 tool(s) for 'moltbook':

📦 moltbook-suite
   Moltbook automation suite (posting, engagement, scheduling)
   Categories: messaging, automation
   File: tools/moltbook-suite.py (15.2 KB)
```

### List All Tools
```bash
python3 tools/toolkit-search.py --list
python3 tools/toolkit-search.py --list --top 20
```

### Category Search
```bash
python3 tools/toolkit-search.py "report" --category monitoring
```

### List Categories
```bash
$ python3 tools/toolkit-search.py --categories
📂 Categories
   automation: 45 tool(s)
   monitoring: 23 tool(s)
   messaging: 18 tool(s)
   data: 15 tool(s)
   ...
```

### Show Statistics
```bash
$ python3 tools/toolkit-search.py --stats
📊 Toolkit Statistics
   Total tools: 144
   Python tools: 138
   Shell scripts: 6
   Total size: 1523.4 KB
   Categories: 9
   Last indexed: 2026-02-04T06:00:00
```

### Rebuild Index
```bash
python3 tools/toolkit-search.py --rebuild
```
Forces re-scan of tools/ directory.

---

## Search Scoring

| Match Type          | Points |
|---------------------|--------|
| Name match          | 10     |
| Description match   | 5      |
| Category match      | 3      |
| CLI arg match       | 2      |

Results sorted by score (highest first).

---

## Auto-Detected Metadata

**From Python scripts:**
- Docstring (first line of """docstring""")
- Argparse arguments (add_argument)
- Main block (if __name__ == "__main__")

**From shell scripts:**
- Comment block (first # comment line)
- Shebang (#!/bin/bash)
- All scripts marked runnable

**File stats:**
- Size (KB)
- Modified timestamp
- Categories (pattern-based detection)

---

## Categories

Auto-detected based on content patterns:

| Category    | Detection Patterns                              |
|-------------|-------------------------------------------------|
| api         | requests, api, endpoint, http                   |
| data        | json, csv, pandas, analysis                     |
| automation  | cron, schedule, automate, trigger               |
| messaging   | telegram, discord, message, notify              |
| monitoring  | watch, monitor, alert, check                    |
| web         | html, css, dashboard, serve                     |
| filesystem  | file, path, directory, scan                     |
| collaboration | agent, collab, task, delegate                |
| crypto      | wallet, ethereum, solidity, web3                |
| general     | (fallback if no patterns match)                 |

---

## Index File

**Location:** `.toolkit_index.json`

**Structure:**
```json
{
  "last_indexed": "2026-02-04T06:00:00",
  "tool_count": 144,
  "tools": [
    {
      "name": "moltbook-suite",
      "filename": "moltbook-suite.py",
      "description": "Moltbook automation suite",
      "path": "tools/moltbook-suite.py",
      "categories": ["messaging", "automation"],
      "cli_args": ["post", "engage", "schedule"],
      "is_runnable": true,
      "is_shell": false,
      "size_kb": 15.2,
      "modified": "2026-02-04T05:30:00"
    }
  ]
}
```

---

## Use Cases

- **Discovery** — "What tools do I have for X?"
- **Documentation** — "What does this tool do?"
- **Category browsing** — "Show me all monitoring tools"
- **CLI arg lookup** — "What arguments does this tool accept?"
- **Toolkit health** — "How many tools? Total size?"

---

## Options

| Option          | Short | Description                          |
|-----------------|-------|--------------------------------------|
| query           | -     | Search query (keyword)               |
| --rebuild       | -r    | Rebuild the index                    |
| --category      | -c    | Filter by category                   |
| --list          | -l    | List all tools                       |
| --categories    | -C    | List categories with counts          |
| --stats         | -s    | Show toolkit statistics              |
| --verbose       | -v    | Verbose output (CLI args, modified)  |
| --top           | -n    | Limit results (default: 10)          |

---

## Example Session

```bash
# Search for analytics tools
$ python3 tools/toolkit-search.py "analytics"
🔍 Found 2 tool(s) for 'analytics':

📦 analytics
   Unified analytics CLI (usage, patterns, velocity, output)
   Categories: data, monitoring
   File: tools/analytics.py (8.1 KB)

# List all automation tools
$ python3 tools/toolkit-search.py "" --category automation --list
🔍 Found 45 tool(s) for '':
📦 moltbook-suite
   Moltbook automation suite
   Categories: messaging, automation
   ...

# Show stats
$ python3 tools/toolkit-search.py --stats
📊 Toolkit Statistics
   Total tools: 144
   Python tools: 138
   Shell scripts: 6
   Total size: 1523.4 KB
   Categories: 9
```

---

## Related Tools

- `toolkit.py` — main toolkit manager (index, search, update)
- `tool-consolidation-opportunities.py` — find overlapping tools
- `tool-usage-analysis.py` — analytics: which tools are used most

---

## File Stats

- **Lines:** ~230
- **Functions:** 8 (scan_tools, _extract_tool_info, build_index, load_index, search, list_categories, get_stats, print_tool)
- **Classes:** 1 (ToolkitIndex)
- **Dependencies:** json, re, argparse, pathlib, datetime (std)
- **Created:** Week 2
- **Category:** Discovery / Indexing

---

**README:** toolkit-search.py | **Last Updated:** 2026-02-04 | **Nova Block:** 1439
