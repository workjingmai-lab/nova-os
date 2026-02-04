# knowledge-search.py

**Knowledge base search — find insights fast.**

## What it does

Search all `knowledge/` articles by keyword or topic. Fast discovery of relevant insights, learnings, and documentation.

## Usage

```bash
# Search by keyword
python3 tools/knowledge-search.py pipeline

# Get top 5 results
python3 tools/knowledge-search.py execution --count 5

# Sort by date (newest first)
python3 tools/knowledge-search.py blocker --sort-by date

# Sort by file size
python3 tools/knowledge-search.py moltbook --sort-by size

# List all articles
python3 tools/knowledge-search.py --list
```

## Output examples

### Search (`knowledge-search.py pipeline`)
```
🔍 Search Results: 'pipeline' (7 found)
═══════════════════════════════════════════════════════════

1. Pipeline Tracking Prevents Revenue Leakage
   File: pipeline-tracking-prevents-leakage.md
   Relevance: 25 (12 occurrences)
   Size: 2,456 bytes
   Path: knowledge/pipeline-tracking-prevents-leakage.md

2. Quick Wins
   File: quick-wins.md
   Relevance: 18 (8 occurrences)
   Size: 3,102 bytes
   Path: knowledge/quick-wins.md

3. Value-First Outreach Structure
   File: outreach-message-structure.md
   Relevance: 15 (5 occurrences)
   Size: 1,892 bytes
   Path: knowledge/outreach-message-structure.md
```

### List all (`--list`)
```
📚 Knowledge Base — 30 articles
══════════════════════════════════════
  1. Pipeline Tracking Prevents Revenue Leakage
  2. Value-First Outreach Structure
  3. Blocker ROI = Priority
  4. Quick Wins
  5. 1000 Work Blocks Milestone
  ...
```

## Scoring

Relevance score:
- **Title match:** +10 points (keyword in article title)
- **Content matches:** +1 point per occurrence

Example: If "pipeline" appears in title (+10) and 12 times in content (+12) = score of 25.

## Sorting options

| Sort method | Description |
|-------------|-------------|
| `relevance` (default) | Highest score first (best matches) |
| `date` | Newest files first (by filename) |
| `size` | Largest files first (most content) |

## Use cases

- **Learnings lookup** — "What did I learn about blockers?"
- **Pattern discovery** — "Which articles mention outreach?"
- **Research** — "Find everything about moltbook"
- **Knowledge inventory** — `--list` to see all articles

## Dependencies

**None** — Pure Python standard library only.

## Integration

Perfect for:
- Quick lookup during work (forgot an insight?)
- Research sessions (explore a topic deeply)
- Weekly reviews (what did I learn this week?)
- Automation (find related articles programmatically)

## Design decisions

- **Simple scoring** — Title matches weighted higher than content
- **Flexible sorting** — Relevance, date, or size
- **Fast** — Searches all articles in milliseconds
- **Zero-index** — Works directly on markdown files, no database needed
