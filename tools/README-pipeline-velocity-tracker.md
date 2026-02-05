# Pipeline Velocity Tracker

## Overview
Measures how fast prospects move through pipeline stages (lead → ready → sent → replied → closed). Identifies bottlenecks and optimization opportunities.

## Installation
```bash
chmod +x tools/pipeline-velocity-tracker.py
```

## Usage

### Overall velocity
```bash
python3 tools/pipeline-velocity-tracker.py
```

Shows:
- Average total pipeline time
- Average time per stage
- Bottleneck identification
- Velocity insights

### Breakdown by service type
```bash
python3 tools/pipeline-velocity-tracker.py --by-service
```

Shows separate metrics for services, grants, bounties.

### Specific stage timing
```bash
python3 tools/pipeline-velocity-tracker.py --stage lead
python3 tools/pipeline-velocity-tracker.py --stage sent
python3 tools/pipeline-velocity-tracker.py --stage replied
```

Shows average time prospects spend in a specific stage.

## Output Example
```
📊 Pipeline Velocity Metrics
==================================================
Opportunities tracked: 16
Moved through stages: 8
Avg pipeline time: 12.3 days

⏱️  Average time per stage:
  lead: 5.2 days
  ready: 2.1 days
  sent: 4.0 days
  replied: 1.0 days

💡 Velocity Insights:
  ⚠ Moderate pipeline speed (7-30 days)
  🐢 Bottleneck: lead stage (5.2 days)
```

## Requirements
- `revenue-pipeline.json` must exist with proper structure
- Opportunities must have `history` arrays with timestamps

## Data Format
Expected opportunity structure:
```json
{
  "name": "Opportunity Name",
  "status": "lead",
  "history": [
    {"stage": "lead", "timestamp": "2026-02-01T10:00:00Z"},
    {"stage": "ready", "timestamp": "2026-02-03T14:30:00Z"}
  ]
}
```

## Use Cases
- **Identify bottlenecks:** Which stage takes longest?
- **Track optimization:** Did velocity improve after process changes?
- **Forecast completion:** Based on average stage times
- **Compare channels:** Do grants move faster than services?

## Integration
Add to cron or heartbeat for regular velocity monitoring:
```bash
# Weekly velocity check
python3 tools/pipeline-velocity-tracker.py >> weekly-metrics.md
```

## Future Enhancements
- Visual velocity charts (plot stage times)
- Trend detection (accelerating vs slowing)
- Stage conversion rates (lead→ready, ready→sent, etc.)
- Predictive completion dates

---

**Created:** 2026-02-04  
**Purpose:** Pipeline optimization — identify where opportunities stall
