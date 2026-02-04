# lead-score-calculator.py

**Prioritize service business opportunities by scoring leads based on fit, value, and readiness.**

## What It Does

Calculates a 0-100 lead score with weighted criteria:
- **Fit (40%):** How well they match my services (1-10 scale)
- **Value (30%):** Deal size normalized ($25K = 10 points, $1K = 1 point)
- **Readiness (30%):** Urgency signals (1-10 scale)

Higher score = prioritize first.

## When to Use

- **Lead prioritization:** Sort which prospects to contact first
- **Pipeline triage:** Focus on high-value, high-fit opportunities
- **Resource allocation:** Decide where to spend limited outreach time

## Usage

```bash
# Score a lead
python3 tools/lead-score-calculator.py score --company "Acme" --fit 8 --value 5000 --readiness 7

# Score high-value lead
python3 tools/lead-score-calculator.py score --company "BigCo" --fit 9 --value 25000 --readiness 8

# Show help
python3 tools/lead-score-calculator.py --help
```

## Output

```
📊 Lead Score: BigCo
   Score: 85/100 (HIGH priority)
   Fit: 9/10
   Value: $25,000 (10.0/10)
   Readiness: 8/10
```

## Scoring Weights

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Fit | 40% | Service match (1-10): 10 = perfect fit, 1 = poor fit |
| Value | 30% | Deal size: $25K = 10 pts, $1K = 1 pt (log scale) |
| Readiness | 30% | Urgency (1-10): 10 = urgent pain, 1 = no urgency |

## Priority Levels

- **High (70+):** Pursue immediately — strong fit, good value, urgent need
- **Medium (50-69):** Worth pursuing — decent fit or value, moderate urgency
- **Low (<50):** Lower priority — poor fit or value, low urgency

## Integration

Pairs with:
- `web-lead-extractor.py` — Detect pain points and service fit
- `service-outreach-tracker.py` — Track scored leads
- `outreach-personalizer.py` — Generate personalized outreach

## Example Workflow

```bash
# 1. Extract lead signals from website
python3 tools/web-lead-extractor.py scan --url "https://acme.com" --content "...manual processes..."

# 2. Score the lead
python3 tools/lead-score-calculator.py score --company "Acme" --fit 8 --value 5000 --readiness 7

# 3. Log to tracker
python3 tools/service-outreach-tracker.py add --company "Acme" --score 68
```

## Status

✅ Working
