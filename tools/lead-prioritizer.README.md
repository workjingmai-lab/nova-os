# Lead Prioritizer — Tool README

**Purpose:** Rank service leads by priority to focus on highest-ROI opportunities first.

## What It Does

- **Scores leads** based on potential value, status, strategic fit, and recency
- **Ranks opportunities** to identify which leads to pursue first
- **Filters by readiness** (ready vs. lead vs. prospect)
- **Pipeline metrics** — total potential, breakdown by status

## Usage

### Show pipeline metrics
```bash
python3 tools/lead-prioritizer.py --metrics
```

Output:
```
📊 Pipeline Metrics:

Total Leads: 16
Total Potential: $157,500

By Status:
  ✅ ready: 10 leads, $82,000
  🟡 lead: 6 leads, $75,500
```

### Rank all leads by priority
```bash
python3 tools/lead-prioritizer.py --rank
```

### Show top N leads
```bash
python3 tools/lead-prioritizer.py --top 5
```

Output:
```
🎯 Ranked Leads (Top 5):

1. 🟡 DAO Automation (Uniswap/Aave/Compound)
   Potential: $20,000 | Score: 2069.9 | Fit: 1.4x
   Status: lead
   Notes: Outreach proposal created...

2. 🟡 Claude Ecosystem (Anthropic)
   Potential: $17,500 | Score: 1804.7 | Fit: 1.3x
   Status: lead
```

### Show only ready-to-send leads
```bash
python3 tools/lead-prioritizer.py --show-ready
```

## Scoring Algorithm

**Score = sqrt(potential) × 10 + status_bonus + strategic_fit × multiplier + recency_bonus**

| Factor | Weight | Description |
|--------|--------|-------------|
| Potential | √value × 10 | Logarithmic scaling (reduces outlier impact) |
| Status | 0-100 | ready=100, ready_to_submit=90, lead=50, prospect=10 |
| Strategic Fit | 1.0-1.5× | Web3=1.5, DAO=1.4, AI=1.3, Claude=1.2 |
| Recency | +20 | Updated in last 7 days |

### Strategic Fit Multipliers

| Category | Multiplier | Keywords |
|----------|------------|----------|
| Web3 | 1.5× | web3, crypto, blockchain, defi, dao |
| DAO | 1.4× | dao, governance, protocol |
| AI | 1.3× | ai, claude, anthropic, automation |
| Claude | 1.2× | claude, anthropic |
| DevOps | 1.1× | devops, cicd, infrastructure |
| Automation | 1.0× | automation, tools (default) |
| General | 0.8× | No strategic keywords |

## Workflow

1. **Create lead** — Add outreach proposal to `outreach/proposals/`
2. **Update pipeline** — Add lead to `data/revenue-pipeline.json`
3. **Run prioritizer** — `python3 tools/lead-prioritizer.py --top 10`
4. **Execute outreach** — Focus on top-scored leads first
5. **Track responses** — Update status (lead → submitted → won/lost)

## Data Sources

**Input:** `data/revenue-pipeline.json` (services array)

**Output:** Ranked list with scores, metrics breakdown

## Integration

Pairs with:
- **revenue-tracker.py** — Updates pipeline JSON
- **Grant Opportunity Finder** — Adds grant leads to pipeline
- **Outreach templates** — `outreach/proposals/*.md`

## Example Scenarios

**Scenario 1: Focus on ready leads**
```bash
python3 tools/lead-prioritizer.py --show-ready
# → Get list of leads with proposals ready to send
```

**Scenario 2: Identify highest-value opportunities**
```bash
python3 tools/lead-prioritizer.py --top 3
# → See top 3 leads by combined score (value + fit + readiness)
```

**Scenario 3: Weekly pipeline review**
```bash
python3 tools/lead-prioritizer.py --metrics
# → Get snapshot of total pipeline value and status breakdown
```

## Dependencies

- Python 3.8+
- `json`, `datetime`, `pathlib` (stdlib only)

## Author

Nova (OpenClaw agent)
Created: 2026-02-04
