# toolkit-search.md — Search Toolkit by Keywords

**Version:** 1.0  
**Category:** Search / Discovery  
**Created:** 2026-02-01

---

## What It Does

Searches all tools in the toolkit by keywords, descriptions, and tags. Fast discovery without browsing the entire directory.

### Features

- Full-text search across all tools
- Tag-based filtering
- Fuzzy matching for typos
- Category filtering (Python, shell, docs)
- Quick preview of matching tools
- Integration with `toolkit.md`

---

## Usage

```bash
# Search by keyword
python3 tools/toolkit-search.py "browser"

# Search by tag
python3 tools/toolkit-search.py --tag "analytics"

# Fuzzy search
python3 tools/toolkit-search.py --fuzzy "bloker"  # Finds "blocker"

# Category filter
python3 tools/toolkit-search.py --category "shell"

# Show descriptions
python3 tools/toolkit-search.py "automation" --describe
```

---

## Search Syntax

| Pattern | Matches |
|---------|---------|
| `keyword` | Tool name, description, tags |
| `--tag TAG` | Tools with specific tag |
| `--category CAT` | Tools in category (python, shell, md) |
| `--fuzzy TERM` | Approximate matching (typos OK) |
| `--describe` | Show tool descriptions |
| `--path` | Show full paths to tools |

---

## Output Example

```bash
$ python3 tools/toolkit-search.py "browser"

🔍 Searching for "browser"...
────────────────────────────────────────────────────────────

Found 3 tools:

1. nova_browser.py
   Tags: browser, automation, control
   Category: Python
   Description: Advanced browser control via OpenClaw browser tool

2. lightweight-browser.py
   Tags: browser, http, requests
   Category: Python
   Description: Lightweight HTTP-based browser, no Chromium overhead

3. novabrowser-watch-tail.sh
   Tags: browser, monitoring, logs
   Category: Shell
   Description: Live browser log monitor
```

---

## Dependencies

- Python 3.7+
- `tools/` directory
- `toolkit.md` for metadata

---

## Data Source

Reads tool metadata from:
- Tool README files (`tools/*.md`)
- `toolkit.md` for categorized listings
- Tool source files for fallback

---

## Integration

- Pair with `toolkit.md` for full toolkit reference
- Use `tool-organizer.py` to maintain clean categorization
- Feed into `agent-starter-kit.md` for new agent onboarding

---

## Tips

1. Use `--fuzzy` when unsure of exact spelling
2. Filter by `--category` to narrow results
3. Use `--describe` for detailed information
4. Combine with `--tag` for precise filtering
5. Search by problem domain ("automation", "analytics") not just tool names
