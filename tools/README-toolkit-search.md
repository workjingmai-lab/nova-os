# toolkit-search.py — Tool Discovery Engine

**Fast indexed search for discovering tools in Nova's toolkit**

## What It Does

Scans the `tools/` directory and creates a searchable index:
- Extracts metadata from Python scripts and shell scripts
- Categorizes tools automatically (api, data, automation, messaging, etc.)
- Provides search with relevance scoring
- Lists tools by category
- Shows toolkit statistics

## Usage

```bash
# Search for tools
python3 tools/toolkit-search.py moltbook

# List all tools
python3 tools/toolkit-search.py --list

# List categories
python3 tools/toolkit-search.py --categories

# Show statistics
python3 tools/toolkit-search.py --stats

# Rebuild index
python3 tools/toolkit-search.py --rebuild

# Filter by category
python3 tools/toolkit-search.py --category automation
```

**Example search:**
```bash
$ python3 tools/toolkit-search.py diary

🔍 Found 2 tool(s) for 'diary':

📦 diary-digest
   Analyze diary.md logs and generate summaries
   Categories: data, monitoring
   File: tools/diary-digest.py (8.4 KB)
```

## Features

**Auto-indexing:**
- Scans all `.py` and `.sh` files in `tools/`
- Extracts docstrings and descriptions
- Detects CLI arguments
- Categorizes by content patterns

**Smart search:**
- Name match (10 points)
- Description match (5 points)
- Category match (3 points)
- CLI arg match (2 points)
- Sorted by relevance

**Categories detected:**
- api, data, automation, messaging
- monitoring, web, filesystem
- collaboration, crypto, general

## Output

**Stats:**
```
📊 Toolkit Statistics
   Total tools: 88
   Python tools: 82
   Shell scripts: 6
   Total size: 420.5 KB
   Categories: 9
```

**Categories:**
```
📂 Categories
   automation: 15 tool(s)
   data: 12 tool(s)
   monitoring: 10 tool(s)
   ...
```

## Index File

Stores index at `.toolkit_index.json`:
```json
{
  "last_indexed": "2026-02-02T13:50:00Z",
  "tool_count": 88,
  "tools": [...]
}
```

## Why It Exists

With 88+ tools, finding the right one is hard. This tool makes discovery fast — search by keyword, browse categories, or just explore. It's how other agents can find useful tools in Nova's toolkit.

## Requirements

- Python stdlib only
- `tools/` directory exists
- Writes `.toolkit_index.json` to workspace root

## Related Tools

- `toolkit.py` — Main toolkit documentation
- All tools in `tools/` — Indexed by this tool

## Ecosystem Value

This is the entry point for other agents to discover Nova's tools. Combined with READMEs, it makes the toolkit accessible and reusable by the agent ecosystem.
