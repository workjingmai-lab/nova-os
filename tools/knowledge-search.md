# knowledge-search.py

Search the knowledge/ directory for insights by keyword or topic.

## Purpose

Fast discovery of relevant insights from curated knowledge articles. Search by keyword, sort by relevance/date/size.

## Usage

```bash
python3 tools/knowledge-search.py <keyword> [--count N] [--sort-by relevance|date|size]
python3 tools/knowledge-search.py --list  # List all articles
```

## Examples

```bash
# Search for articles about "pipeline"
python3 tools/knowledge-search.py pipeline

# Search with more results
python3 tools/knowledge-search.py execution --count 20

# Sort by file size (largest first)
python3 tools/knowledge-search.py blocker --sort-by size

# List all knowledge articles
python3 tools/knowledge-search.py --list
```

## How It Works

**Scoring:**
- Title match = 10 points
- Each content occurrence = 1 point
- Higher score = more relevant

**Sorting options:**
- `relevance` (default) — Highest score first
- `date` — Newest files first
- `size` — Largest files first

## Output Example

```
🔍 Search Results: 'pipeline' (3 found)
============================================================

1. Pipeline Tracking and Documentation
   File: revenue-pipeline-tracking.md
   Relevance: 28 (18 occurrences)
   Size: 8,234 bytes
   Path: knowledge/revenue-pipeline-tracking.md

2. Revenue Outreach Message Structure
   File: outreach-message-structure.md
   Relevance: 15 (5 occurrences)
   Size: 4,567 bytes
   Path: knowledge/outreach-message-structure.md

3. Blocker ROI and Priority
   File: blocker-roi-priority.md
   Relevance: 12 (2 occurrences)
   Size: 3,210 bytes
   Path: knowledge/blocker-roi-priority.md

💡 Tip: Use --count N for more results, --sort-by date/size for different sorting
```

## Use Cases

**Research before action:**
```bash
# Learn about pipeline before executing
python3 tools/knowledge-search.py pipeline
```

**Find specific insights:**
```bash
# What did I learn about blockers?
python3 tools/knowledge-search.py blocker
```

**Discover related content:**
```bash
# All articles about revenue
python3 tools/knowledge-search.py revenue --count 20
```

**Explore knowledge base:**
```bash
# What do I know?
python3 tools/knowledge-search.py --list
```

## File Structure

**Reads from:**
- `knowledge/*.md` — Curated knowledge articles

**Scoring algorithm:**
- Title match (10 points) + content occurrences (1 point each)
- Results sorted by score (relevance)

## Why It Matters

**Knowledge without retrieval = lost.**

- **Fast discovery:** Find insights without reading everything
- **Relevance ranking:** Title matches rank higher than casual mentions
- **Flexible sorting:** Relevance, date, or size
- **Exploration:** `--list` shows all knowledge articles
- **Lightweight:** Simple grep-based search, no index needed

**Complements memory_search** (semantic search):
- `knowledge-search.py` — Exact keyword match, fast, simple
- `memory_search` — Semantic search, fuzzy, finds related concepts

Use both for comprehensive knowledge retrieval.

## Related Tools

- `memory_search` — Semantic search across MEMORY.md and memory files
- `memory_get` — Read specific sections from memory files
- `knowledge-export.py` — Export knowledge base for sharing
- `agent-digest.py` — Summarize knowledge by topic
