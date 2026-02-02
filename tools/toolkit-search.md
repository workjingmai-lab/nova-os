# toolkit-search.py — Find Tools Fast

**Purpose:** Search and discover tools by keyword, category, or pattern

## Quick Start

```bash
# Search for keyword
python3 tools/toolkit-search.py search "moltbook"

# List by category
python3 tools/toolkit-search.py category workflow

# Find recent tools (last 7 days)
python3 tools/toolkit-search.py recent

# Show top 10 most-used tools
python3 tools/toolkit-search.py top
```

## Features

- **Keyword search** — Find tools by name/description
- **Category filtering** — workflow, analytics, grant, outreach, moltbook
- **Recent discovery** — Tools created/modified in last N days
- **Usage ranking** — Sort by execution frequency
- **Pattern matching** — Regex-based tool discovery

## Use Cases

- "What tool handles Moltbook posting?" → `search "post"`
- "Show me analytics tools" → `category analytics`
- "What did I build this week?" → `recent 7`
- "What are my most-used tools?" → `top`

---

**Created:** 2026-02-02
**Usage:** Part of Nova's toolkit management system
