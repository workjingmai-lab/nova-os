# grant-opportunity-finder.py

## What It Does

Discovers and tracks grant opportunities across Web3/Web2 platforms (Gitcoin, Octant, Optimism, OLAS, Moloch, etc.). Filters by status, value, category, and deadline. Exports to JSON/markdown for pipeline integration.

## How It Works

Loads sample opportunities (seed data) and provides CLI filtering:
- **Status filters:** open, upcoming, closed, rolling
- **Value filters:** minimum value threshold ($1K-$500K range)
- **Category filters:** quadratic_funding, retropgf, developer_program, dao_funding
- **Platform filters:** Gitcoin, Octant, Optimism, OLAS, Moloch, Etherscan, etc.
- **Topic filters:** developer_tools, infrastructure, defi, ai, education, etc.

## Usage

```bash
# List all opportunities
python3 tools/grant-opportunity-finder.py

# Filter by status
python3 tools/grant-opportunity-finder.py --status open

# Filter by minimum value
python3 tools/grant-opportunity-finder.py --min-value 50000  # $50K+ only

# Filter by platform
python3 tools/grant-opportunity-finder.py --platform gitcoin

# Filter by category
python3 tools/grant-opportunity-finder.py --category retropgf

# Multiple filters
python3 tools/grant-opportunity-finder.py --status open --min-value 10000 --platform optimism

# Export formats
python3 tools/grant-opportunity-finder.py --json
python3 tools/grant-opportunity-finder.py --export markdown

# Deadline warnings
python3 tools/grant-opportunity-finder.py --deadline-warning 14  # Warn if < 14 days
```

## What It Outputs

**Text Output (default):**
```
🔍 Grant Opportunities — 9 total

💰 OPEN (4)
────────────────────────────────────────────────────────────
  Gitcoin Grants Round 21
    Platform: Gitcoin | Category: quadratic_funding
    Value: $1K-$100K | Deadline: 2026-02-28 (24 days)
    Topics: developer_tools, infrastructure, education
    https://gitcoin.co/grants

  Optimism RPGF Season 6
    Platform: Optimism | Category: retropgf
    Value: $10K-$500K | Deadline: 2026-02-20 (16 days)
    Topics: defi, infrastructure, developer_tools
    https://app.optimism.io/retropgf
  [...]
```

**JSON Output:**
```json
{
  "timestamp": "2026-02-04T06:20:00Z",
  "total": 9,
  "filtered": 4,
  "opportunities": [
    {
      "name": "Gitcoin Grants Round 21",
      "platform": "Gitcoin",
      "category": "quadratic_funding",
      "status": "open",
      "deadline": "2026-02-28",
      "value_range": "$1K-$100K",
      "url": "https://gitcoin.co/grants",
      "description": "Quadratic funding for open source Web3 projects",
      "topics": ["developer_tools", "infrastructure", "education"]
    }
  ]
}
```

## Supported Platforms

- **Gitcoin** — Quadratic funding for open source
- **Octant** — Optimism retroactive public goods funding
- **Optimism RPGF** — Retroactive funding for ecosystem contributors
- **OLAS** — Autonomous agents and AI services
- **Moloch DAO** — Ethereum ecosystem development
- **Ethereum Foundation** — Core protocol research and development
- **Uniswap** — DeFi protocol grants

## Categories

- `quadratic_funding` — Community matching funds
- `retropgf` — Retroactive public goods funding
- `developer_program` — Ongoing developer grants
- `dao_funding` — DAO-based allocation
- `research` — Academic and industry research
- `ecosystem` — Platform-specific ecosystem growth

## Use Cases

- **Grant discovery** — Find new opportunities beyond manual research
- **Pipeline expansion** — Grow grant pipeline systematically
- **Deadline tracking** — Filter by upcoming deadlines (≤ 14 days, etc.)
- **Value filtering** — Focus on high-value opportunities ($50K+)
- **Platform targeting** — Platform-specific grant strategies

## Integration with Pipeline

Export to JSON → import into grant pipeline:
```bash
python3 tools/grant-opportunity-finder.py --status open --json > tmp/grant-opportunities.json
# Then import into grant-pipeline.json via grant-submit-helper.py
```

## Sample Opportunities (Seed Data)

Built-in sample opportunities demonstrate filtering:
- Gitcoin Grants Round 21 ($1K-$100K)
- Octant Epoch 7 ($5K-$50K)
- Optimism RPGF Season 6 ($10K-$500K)
- OLAS Compute 4 Decay ($5K-$25K)
- Moloch DAO Grants ($5K-$100K)
- Ethereum Foundation Fellowship ($30K-$100K)
- Uniswap V4 Extension ($10K-$50K)
- Polygon DAO Grants ($5K-$25K)
- Arbitrum STIP Wave 4 ($10K-$100K)

## When to Use It

- **Weekly grant research** — Discover new opportunities
- **Pipeline expansion** — Add qualified opportunities to pipeline
- **Deadline management** — Track approaching submission windows
- **Platform targeting** — Focus on specific platforms (Optimism, Gitcoin, etc.)

## See Also

- `grant-submit-helper.py` — Prepare and submit grant applications
- `revenue-tracker.py` — Track all revenue opportunities (grants, services, bounties)
- `execution-dashboard.py` — Real-time pipeline visibility
