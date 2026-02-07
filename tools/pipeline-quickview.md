# pipeline-quickview.py

Essential revenue numbers at a glance. No fluff, just the numbers that matter.

## Usage

```bash
python3 tools/pipeline-quickview.py
```

## Output

```
========================================
💰 PIPELINE QUICKVIEW
========================================
Total Pipeline:    $   1,490,065
Ready to Send:     $     609,500
Submitted:         $       5,000
Won:               $           0
----------------------------------------
Conversion Rate:           0.0%
========================================

🚀 Action: $609,500 ready to convert
```

## Data Source

Reads `revenue-pipeline.json` with structure:
```json
{
  "opportunities": [
    {"value": 50000, "status": "ready"},
    {"value": 25000, "status": "submitted"}
  ]
}
```

## When to Use

- Morning check: What's the state of play?
- Before work blocks: What should I prioritize?
- End of day: What got done?

## One-Liner

```bash
cd /home/node/.openclaw/workspace && python3 tools/pipeline-quickview.py
```
