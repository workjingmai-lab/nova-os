# grant-opportunity-finder.py

**Grant discovery — find, filter, and track Web3/Web2 grant opportunities.**

## What it does

Discover and track grant opportunities across multiple platforms:
- Gitcoin (quadratic funding)
- Optimism RPGF (retroactive public goods)
- Octant (Optimism retro PGF)
- OLAS (autonomous agents)
- Moloch DAO (Ethereum ecosystem)
- Arbitrum Stylus (developer tools)
- Ethereum Foundation ESP
- Aave Grants DAO

Filter by status, category, value, deadline urgency. Export to JSON/Markdown.

## Usage

```bash
# List all opportunities
python3 tools/grant-opportunity-finder.py

# Show only open grants
python3 tools/grant-opportunity-finder.py --status open

# Filter by minimum value ($50K+)
python3 tools/grant-opportunity-finder.py --min-value 50000

# Filter by category
python3 tools/grant-opportunity-finder.py --category gitcoin

# Show urgent grants (deadline within 7 days)
python3 tools/grant-opportunity-finder.py --urgent-days 7

# Show statistics
python3 tools/grant-opportunity-finder.py --stats

# JSON output
python3 tools/grant-opportunity-finder.py --json

# Export to markdown
python3 tools/grant-opportunity-finder.py --export markdown

# Export to JSON
python3 tools/grant-opportunity-finder.py --export json

# Combine filters
python3 tools/grant-opportunity-finder.py --status open --min-value 50000 --category defi
```

## Output examples

### List all (`grant-opportunity-finder.py`)
```
🎯 Found 8 grant opportunities:

1. 🟢 Gitcoin Grants Round 21
   Platform: Gitcoin | Category: quadratic_funding
   Value: $1K-$100K | Deadline: 2026-02-28
   URL: https://gitcoin.co/grants
   Topics: developer_tools, infrastructure, education

2. 🟢 Optimism RPGF Season 6
   Platform: Optimism | Category: retropgf
   Value: $10K-$500K | Deadline: 2026-02-20
   URL: https://app.optimism.io/retropgf
   Topics: defi, infrastructure, developer_tools

3. 🟡 Octant Epoch 7
   Platform: Octant | Category: retropgf
   Value: $5K-$50K | Deadline: 2026-03-15
   URL: https://octant.app
   Topics: public_goods, infrastructure, research
...
```

### Statistics (`--stats`)
```
📊 Grant Opportunity Stats:
   Total: 8
   Open: 5 | Upcoming: 3
   Urgent (≤7 days): 2
   Total Potential: $1,780K
```

### Export markdown (`--export markdown`)
Creates `tmp/grant-opportunities.md`:

```markdown
# Grant Opportunities

| Name | Platform | Status | Value | Deadline | Topics |
|------|----------|--------|-------|----------|--------|
| [Gitcoin Grants Round 21](https://gitcoin.co/grants) | Gitcoin | 🟢 Open | $1K-$100K | 2026-02-28 | developer_tools, infrastructure |
| [Optimism RPGF Season 6](https://app.optimism.io/retropgf) | Optimism | 🟢 Open | $10K-$500K | 2026-02-20 | defi, infrastructure |
...
```

### Export JSON (`--export json`)
Creates `data/grant-opportunities-export.json` with full opportunity data.

## Filters

| Filter | Description | Example |
|--------|-------------|---------|
| `--status` | Filter by status (open, upcoming) | `--status open` |
| `--category` | Filter by category | `--category gitcoin` |
| `--min-value` | Minimum grant value (in dollars) | `--min-value 50000` |
| `--urgent-days` | Deadline within N days | `--urgent-days 7` |

## Data structure

Each grant opportunity has:
- `name` — Grant name
- `platform` — Platform (Gitcoin, Optimism, etc.)
- `category` — Category (quadratic_funding, retropgf, etc.)
- `status` — Status (open, upcoming)
- `deadline` — Deadline date (YYYY-MM-DD) or "rolling"
- `value_range` — Funding range (e.g., "$10K-$500K")
- `url` — Application URL
- `description` — Grant description
- `topics` — List of relevant topics

## Data storage

Opportunities stored in `data/grant-opportunities.json`.
On first run, uses sample data (8 opportunities across 8 platforms).
Subsequent runs load from file.

## Use cases

- **Grant research** — Discover new opportunities across platforms
- **Pipeline building** — Filter by value/status to build submission pipeline
- **Deadline tracking** — Find urgent grants (deadline within N days)
- **Category focus** — Filter by category (defi, infrastructure, AI)
- **Reporting** — Export to markdown for status updates
- **Automation** — Use `--json` for programmatic access

## Dependencies

**None** — Pure Python standard library only.

## Integration

Perfect for:
- Weekly grant reviews (use `--stats` for overview)
- Pipeline building (filter open grants, export to CSV)
- Deadline tracking (cron job with `--urgent-days 7`)
- Status reports (export markdown for documentation)
- Revenue forecasting (sum potential values)

## Sample platforms

Currently tracks 8 platforms:
1. **Gitcoin** — Quadratic funding for open source
2. **Optimism RPGF** — Retroactive public goods funding
3. **Octant** — Optimism retro PGF
4. **OLAS** — Autonomous agents and AI services
5. **Moloch DAO** — Ethereum ecosystem grants
6. **Arbitrum** — Stylus (Rust smart contracts)
7. **Ethereum Foundation ESP** — Ecosystem support
8. **Aave Grants DAO** — DeFi ecosystem grants

## Design decisions

- **Seed data** — Includes 8 sample opportunities to start immediately
- **File-based storage** — Simple JSON file, no database
- **Flexible filters** — Combine multiple filters for precise queries
- **Multi-format export** — Text (human), JSON (automation), Markdown (docs)
- **Deadline parsing** — Handles both dates and "rolling" deadlines
- **Value parsing** — Extracts max value from range strings
