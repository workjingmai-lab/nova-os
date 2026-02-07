# action-recommender.py

Suggest highest-impact next action based on current pipeline state.

## Usage

```bash
# Show top recommendation
python3 tools/action-recommender.py

# Show top 5 recommendations
python3 tools/action-recommender.py --top 5

# Filter by category
python3 tools/action-recommender.py --category services
python3 tools/action-recommender.py --category grants
```

## How It Works

Analyzes revenue pipeline and scores actions by:

1. **Services ready NOW** (no blockers) → 100 points
2. **Services submitted** + follow-up due → 80 points  
3. **Grants ready** (small blocker) → 60 points
4. **Bounties** (large blocker) → 40 points
5. **New leads** → 20 points

## Scoring Factors

- **Value**: Higher $ = higher score
- **Blocker cost**: Smaller blocker = higher score
- **Time since last action**: Longer = higher urgency
- **Follow-up timing**: Due now = priority boost

## Sample Output

```
╔══════════════════════════════════════════════════════════════╗
║           TOP RECOMMENDED ACTION                               ║
╠══════════════════════════════════════════════════════════════╣
║  Action: Send service message to Ethereum Foundation          ║
║  Value:  $40,000                                              ║
║  Blocker: NONE (ready now)                                    ║
║  Score:  98/100                                               ║
╚══════════════════════════════════════════════════════════════╝
```

## Why This Matters

Eliminates decision fatigue. Instead of choosing between 50+ possible actions, get the single highest-ROI next step.

## Data Sources

- `data/revenue-pipeline.json` — Pipeline state
- `data/follow-ups.json` — Follow-up timing
- `BLOCKER-STATUS.md` — Blocker information

## Created

2026-02-07 — Work block 3266
