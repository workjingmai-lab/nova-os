# conversion-dashboard.py

Real-time revenue pipeline dashboard. One command shows complete conversion status.

## Quick Start

```bash
python3 tools/conversion-dashboard.py
```

## Output

```
======================================================================
  REVENUE CONVERSION DASHBOARD
======================================================================
  Generated: 2026-02-07 02:05 UTC

======================================================================
  PIPELINE OVERVIEW
======================================================================
  Total Pipeline                 $1,490,065 
  Ready to Send                    $734,500 
  Submitted                          $5,000 
  Won                                    $0 

  Submitted       |░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|   0.3%
  Won             |░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|   0.0%

  Conversion Rate                       0.0 %
  Execution Gap                        99.7 %

======================================================================
  BY CATEGORY
======================================================================

  SERVICES
    Total: $1,310,065
    Progress: Ready $609,500 | Submitted $0 | Won $0

  GRANTS
    Total: $130,000
    Progress: Ready $125,000 | Submitted $5,000 | Won $0

======================================================================
  TOP 5 OPPORTUNITIES (READY)
======================================================================
  $    50,000 | grants     | Olas
  $    50,000 | grants     | Optimism RPGF
  $    40,000 | services   | Ethereum Foundation

======================================================================
  ACTION ITEMS
======================================================================
  ⚠️  35 items ready to send ($734,500)
     Estimated time: 18 minutes
     Potential value: $734,500
```

## Sections

| Section | Description |
|---------|-------------|
| Pipeline Overview | Total, ready, submitted, won + conversion rate |
| By Category | Breakdown by grants/services/bounties |
| Recent Activity | Last 10 updates with timestamps |
| Top 5 Opportunities | Highest-value ready items |
| Action Items | Count and time estimate to close |

## Why This Exists

Before: `python3 tools/revenue-tracker.py summary` → parse text output
After: `python3 tools/conversion-dashboard.py` → visual status in 1 second

## Integration

- Data source: `data/revenue-pipeline.json`
- Updated by: `tools/revenue-tracker.py`
- Use before: Daily planning, status reports, Arthur updates

## Run Frequency

- **Daily:** Morning standup check
- **Weekly:** Review conversion rates
- **After sends:** Verify pipeline movement
