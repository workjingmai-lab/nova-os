# Grant Opportunity Finder

Automatically discover and filter grant opportunities from Gitcoin, DAOs, foundations, and Web3 ecosystems.

## Overview

**grant-opportunity-finder.py** scans multiple grant programs and provides filtering, statistics, and export capabilities. Perfect for autonomous agents managing revenue pipelines.

## Features

- **Multi-source scanning:** Gitcoin, Optimism, Octant, OLAS, Moloch DAO, Arbitrum, Ethereum Foundation, Aave
- **Smart filtering:** By status (open/upcoming), category, value range, deadline
- **Multiple export formats:** Table, JSON, Markdown
- **Statistics mode:** Summary of opportunities, value ranges, categories
- **Deadline tracking:** Days remaining until grant closes

## Usage

### Basic Usage

```bash
# List all opportunities
python3 grant-opportunity-finder.py

# Show only open grants
python3 grant-opportunity-finder.py --filter open

# Filter by category
python3 grant-opportunity-finder.py --category defi

# Filter by minimum value ($50K+)
python3 grant-opportunity-finder.py --value-min 50000

# Show grants closing within 30 days
python3 grant-opportunity-finder.py --deadline-days 30
```

### Export Formats

```bash
# JSON export (for pipeline tracking)
python3 grant-opportunity-finder.py --export json > grants.json

# Markdown export (for documentation)
python3 grant-opportunity-finder.py --export markdown > grants.md

# Table format (default)
python3 grant-opportunity-finder.py --export table
```

### Statistics Mode

```bash
# Show summary statistics
python3 grant-opportunity-finder.py --stats
```

Output:
```json
{
  "total_opportunities": 8,
  "open_now": 6,
  "upcoming": 2,
  "total_value_range": "$135,000-$1,675,000",
  "urgent_deadlines": 0,
  "categories": ["infrastructure", "defi", "ai_agents", ...]
}
```

## Output Examples

### Table Format (Default)

```
ID                   Name                           Category        Deadline     Value        Status         
-------------------------------------------------------------------------------------------------------------
gitcoin-20           Gitcoin Grant Round 20         public_goods    2026-02-28 (24d) $5K-$150K    open           
optimism-rpgf-season-5 Optimism RPGF Season 5         infrastructure  2026-03-01 (25d) $20K-$500K   open           
olas-grant-program   OLAS Grant Program             ai_agents       2026-04-01 (56d) $5K-$100K    open           
arbitrum-stip-3      Arbitrum STIP Phase 3          layer2          2026-02-20 (16d) $25K-$200K   closing_soon   
```

### JSON Format

```json
[
  {
    "id": "gitcoin-20",
    "name": "Gitcoin Grant Round 20",
    "category": "public_goods",
    "deadline": "2026-02-28",
    "value_range": "$5K-$150K",
    "status": "open",
    "url": "https://gitcoin.co/grants",
    "description": "Quadratic funding for public goods"
  }
]
```

## Grant Categories

- **public_goods:** Open source, developer tools, education
- **infrastructure:** L2s, bridges, oracles, nodes
- **defi:** DEXs, lending, derivatives, liquidity
- **ai_agents:** AI agent tooling, automation
- **layer2:** Rollups, sidechains, scaling
- **ethereum:** Ethereum core improvements
- **security:** Audits, bug bounties, formal verification

## Grant Status Values

- **open:** Accepting applications
- **closing_soon:** Deadline within 7 days
- **upcoming:** Not yet open (future round)

## Integration Examples

### Pipeline Tracking

```bash
# Export open grants to pipeline tracker
python3 grant-opportunity-finder.py --filter open --export json > pipeline/grant-opportunities.json
```

### Urgent Deadlines

```bash
# Find grants closing within 7 days
python3 grant-opportunity-finder.py --deadline-days 7 --filter open
```

### Category-Specific

```bash
# DeFi grants only, $50K+ minimum
python3 grant-opportunity-finder.py --category defi --value-min 50000
```

## Data Sources

**Current implementation:** Sample data (8 grants, $135K-$1.675M range)

**Production implementation:** Would fetch from:
- Gitcoin API (`https://gitcoin.co/grants`)
- Optimism RPGF API
- DAO governance forums (Snapshot, Discourse)
- Foundation grant portals
- Web3 grant boards (GrantHub, Drips)

## Requirements

- Python 3.7+
- No external dependencies (uses only stdlib)

## Future Enhancements

- [ ] API integration for real-time data
- [ ] Automated application deadline reminders
- [ ] Grant requirement extraction (eligibility criteria)
- [ ] Success rate tracking by grant program
- [ ] Auto-populate grant templates from opportunity data

## Author

Created by Nova (2026-02-03) — Work block 1186

## See Also

- `grant-submit-helper.py` — Grant submission assistance
- `revenue-tracker.py` — Pipeline value tracking
- `service-batch-send.py` — Outreach message batch sending
