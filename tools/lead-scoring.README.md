# Lead Scoring System

Prioritize leads based on **fit**, **urgency**, **value**, and **signal strength**.

## Usage

```bash
# Score and rank all leads
python3 tools/lead-scoring.py score

# Show top 10 leads
python3 tools/lead-scoring.py top10

# Show top 5 leads
python3 tools/lead-scoring.py top5

# Show top N leads (any number)
python3 tools/lead-scoring.py top20
```

## How Scoring Works

Each lead is scored on 5 dimensions (0-100 scale):

### 1. Value Score (30% weight)
- Higher value = higher score
- Normalized against highest-value lead
- $50K deal = 100, $25K deal = 50 (if $50K is max)

### 2. Fit Score (25% weight)
- Problem-solution fit (1-10 scale, manual assessment)
- Default: 5/10 (50/100)
- Override in revenue-pipeline.json with `fit_score`

### 3. Urgency Score (20% weight)
- Time sensitivity (1-10 scale, manual assessment)
- Default: 5/10 (50/100)
- Override in revenue-pipeline.json with `urgency_score`
- Higher for time-sensitive opportunities (e.g., grants with deadlines)

### 4. Signal Score (15% weight)
- Engagement signals (auto-calculated)
- Each signal = +2 points (max 100)
- Examples: Twitter interaction, Discord mention, email response

### 5. Competition Score (10% weight)
- Competitor pressure (1-10 scale, manual assessment)
- Default: 5/10 (50/100)
- Higher if competitors are active in the space

## Formula

```
Total Score =
  (Value × 0.30) +
  (Fit × 0.25) +
  (Urgency × 0.20) +
  (Signal × 0.15) +
  (Competition × 0.10)
```

## Example Output

```
📊 Ranked Leads (Top 5 of 15)

1. Optimism RPGF — Score: 57.5/100
   Tier: MEDIUM | Value: $50K
   Status: ready | Priority: MEDIUM
   Breakdown:
     • Value: 100.0/100
     • Fit: 50.0/100
     • Urgency: 50.0/100
     • Signal: 0.0/100
     • Competition: 50.0/100
```

## Customizing Scores

Edit `revenue-pipeline.json` to add custom scores:

```json
{
  "name": "Ethereum Foundation",
  "amount": 40000,
  "priority": "HIGH",
  "fit_score": 8,        // High problem-solution fit
  "urgency_score": 9,    // Very time-sensitive
  "signals": ["Twitter reply", "Discord mention"]
}
```

## When to Use

- **Before sending** — Identify highest-priority leads to contact first
- **After responses** — Re-rank based on new engagement signals
- **Weekly review** — Adjust scores based on market changes

## Integration

Use with other tools:
- `service-batch-send.py` — Send to top N scored leads
- `revenue-tracker.py` — Update scores based on responses
- `followup-reminder.py` — Prioritize follow-ups for high-scoring leads

## Scoring Philosophy

**Value isn't everything.** A $50K grant with poor fit (score: 60) is less valuable than a $40K HIGH priority with perfect fit (score: 75).

Scoring helps you:
1. **Focus on the right leads** — Not just the highest-value
2. **Prioritize time** — Spend effort where it matters most
3. **Track pipeline health** — See shifts in fit/urgency over time

## Adjusting Weights

Edit `WEIGHTS` in `lead-scoring.py` if priorities change:

```python
WEIGHTS = {
    "value": 0.3,          # 30% weight
    "fit": 0.25,           # 25% weight
    "urgency": 0.2,        # 20% weight
    "signal": 0.15,        # 15% weight
    "competition": 0.1     # 10% weight
}
```

## Data Sources

Reads from:
- `revenue-pipeline.json` — Categories, opportunities, top prospects
- Auto-extracts flat lead list from nested structure

## Why Scoring Matters

- **15 leads** × different priorities = hard to rank manually
- **$50K grant** vs **$40K HIGH priority** — which first?
- **Scoring = objectivity** — Remove emotion from prioritization
- **Velocity = focus** — Spend time on high-ROI leads first

---

**Created:** 2026-02-06
**Work Block:** 2713
**Tags:** lead-scoring, prioritization, pipeline, analytics
