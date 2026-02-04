# README: lead-prioritizer.py

## Overview
Rank service leads by priority and readiness using multi-factor scoring.

## Purpose
Transform a flat list of leads into an action-ready priority queue. Scores leads based on value, status, strategic fit, and execution complexity.

## Installation
No installation required. Uses Python 3 standard library.

## Usage

### Rank All Leads
```bash
python3 tools/lead-prioritizer.py --rank
```
Outputs prioritized list with scores.

### Show Only Ready Leads
```bash
python3 tools/lead-prioritizer.py --show-ready
```
Filters to status="ready" or "ready_to_submit".

### Top N Leads
```bash
python3 tools/lead-prioritizer.py --top 5
```
Shows highest-priority 5 leads.

## Scoring Formula

```
priority_score = (value × status_weight × strategic_fit) / complexity
```

**Factors:**
- **Value:** Higher dollar amount = higher score
- **Status:** ready (100) > lead (50) > prospect (10)
- **Strategic fit:** Web3/DAO (1.5×) > AI (1.3×) > general (1.0×)
- **Complexity:** Quick automation (1.0) > multi-agent (0.7)

## Example Output

```
🎯 LEAD PRIORITY RANKING
========================================

[1] Ethereum Foundation — Score: 2857
    Value: $40K | Status: ready | Fit: Web3 (1.5×)

[2] Optimism — Score: 2142
    Value: $30K | Status: ready | Fit: DAO (1.4×)

[3] Anthropic — Score: 1950
    Value: $25K | Status: lead | Fit: AI (1.3×)
```

## Data Files

### Input: data/revenue-pipeline.json
```json
{
  "leads": [
    {
      "prospect": "Ethereum Foundation",
      "value": 40000,
      "status": "ready",
      "category": "web3",
      "complexity": "multi-agent"
    }
  ]
}
```

### Output: Console (ranked list)
Optionally updates pipeline with `priority_score` field.

## Use Cases

1. **Daily planning:** Run `--top 10` to pick today's targets
2. **Pipeline review:** Run `--show-ready` before outreach batch
3. **Strategy adjustment:** Modify scoring weights in code

## Related Tools

- **revenue-tracker.py:** Pipeline source of truth
- **service-batch-send.py:** Execute outreach after prioritizing
- **pipeline-snapshot.py:** Health check before acting

## Version History

- **2026-02-04:** Created (multi-factor lead scoring)

## Notes

- Scoring weights are hardcoded; edit tool to adjust
- Strategic fit favors Web3/DAO (Nova's ecosystem strength)
- Complexity penalty reflects execution time
