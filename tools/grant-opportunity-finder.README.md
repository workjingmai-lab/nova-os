# Grant Opportunity Finder — Tool README

**Purpose:** Discover and track grant opportunities automatically across Web3, AI, and open source programs.

## What It Does

- **Auto-discovery**: Searches known grant programs (Gitcoin, Octant, Olas, Optimism RPGF, Moloch DAO, etc.)
- **Deadline tracking**: Flags grants with deadlines in next 30 days
- **Status management**: Organizes grants by status (tracked/prospect/submitted)
- **Pipeline integration**: Feeds into revenue-pipeline.json for unified tracking

## Usage

### Search for grants
```bash
python3 tools/grant-opportunity-finder.py --search web3    # Web3/crypto grants
python3 tools/grant-opportunity-finder.py --search ai      # AI/agent research grants
python3 tools/grant-opportunity-finder.py --search all     # All categories
```

### List tracked opportunities
```bash
python3 tools/grant-opportunity-finder.py --list-active
```

Output:
```
📊 Discovered Grants (8 total):

✅ TRACKED (in pipeline):
   • Gitcoin Grants: $5,000
   • Octant (GP): $15,000
   • Olas (GP): $50,000
   • Optimism RPGF: $50,000
   • Moloch DAO: $10,000

🔍 PROSPECTS (to research):
   • Ethereum Foundation: $50,000
     URL: https://ethereum.org/en/grants/
   • GitHub Sponsors: $10,000
     URL: https://github.com/sponsors
```

### Check upcoming deadlines
```bash
python3 tools/grant-opportunity-finder.py --check-deadlines
```

### Add custom opportunity
```bash
python3 tools/grant-opportunity-finder.py --add '{"name":"My Grant","url":"https://...","potential":10000}'
```

## Data Structure

**File:** `data/grants/opportunities.json`
```json
{
  "discovered": [
    {
      "name": "Gitcoin Grants",
      "program_id": "gitcoin",
      "url": "https://gitcoin.co/grants",
      "cycle": "Quarterly",
      "potential": 5000,
      "status": "tracked",
      "discovered": "2026-02-04T09:22:00Z"
    }
  ],
  "last_checked": "2026-02-04T09:22:00Z"
}
```

## Known Grant Programs

| Program | Category | Potential | Cycle |
|---------|----------|-----------|-------|
| Gitcoin Grants | Web3 | $5K | Quarterly |
| Octant (GP) | Web3 | $15K | Quarterly |
| Olas (GP) | Web3 | $50K | Varies |
| Optimism RPGF | Web3 | $50K | Rounds |
| Moloch DAO | Web3 | $10K | Ongoing |
| Ethereum Foundation | Web3 | $50K | Ongoing |
| GitHub Sponsors | Open Source | $10K | Ongoing |
| Open Collective | Open Source | $5K | Ongoing |

## Workflow

1. **Discover**: Run `--search all` to find opportunities
2. **Research**: Visit URLs, check eligibility, note deadlines
3. **Track**: Move prospects to "tracked" status in opportunities.json
4. **Submit**: Use grant-submit-helper.py to prepare applications
5. **Update**: Change status to "submitted" after submission

## Integration with Revenue Pipeline

Tracked grants automatically sync to `data/revenue-pipeline.json` under the "grants" array. This provides unified visibility across all revenue sources.

## Next Steps

- Add more AI research grant programs (Anthropic, OpenAI, etc.)
- Implement deadline reminders via cron
- Add eligibility filtering (stage, category, region)
- Integrate with grant-submit-helper.py for one-click submissions

## Dependencies

- Python 3.8+
- `json`, `urllib`, `datetime`, `pathlib` (stdlib only)

## Author

Nova (OpenClaw agent)
Created: 2026-02-04
