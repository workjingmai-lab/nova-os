# contest-tracker.py

Track and prioritize audit competitions on Code4rena and similar platforms.

## What It Does

- Manages contest data (active, upcoming, completed)
- Calculates opportunity scores based on prize pool, difficulty, tech stack
- Prioritizes contests by expected value
- Tracks registration, submission, and rewards

## Usage

```bash
# Show dashboard with prioritized contests
python3 tools/contest-tracker.py

# Use in Python
from tools.contest_tracker import ContestTracker

tracker = ContestTracker()
tracker.add_contest(
    name="Jupiter Lend",
    platform="Code4rena",
    prize_pool=107000,
    start_date="2026-02-04T20:00:00Z",
    end_date="2026-03-04T20:00:00Z",
    tech_stack=["solana", "rust"],
    difficulty="hard"
)
tracker.print_dashboard()
```

## Opportunity Score

Formula: `prize_pool × difficulty_mult × (1 + tech_bonus × 0.1)`

**Difficulty multiplier:**
- Easy: 1.2× (less competition usually)
- Medium: 1.0× (baseline)
- Hard: 0.7× (more specialized, fewer participants)

**Tech bonus:** +10% per familiar tech (Solidity, EVM, JavaScript)

## Example Output

```
🛡️  CODE4RENA CONTEST TRACKER

🔥 ACTIVE (2)
  • Olas: $62,000 | Ends: 2026-02-09
  • Jupiter Lend: $107,000 | Ends: 2026-03-04

📅 UPCOMING (1)
  • Uniswap V5: $150,000 | Score: 180000 | Starts: 2026-02-15

📊 STATS
  Total Prize Pool Available: $319,000
  Contests Tracked: 12
```

## Data Storage

Contests saved to `contests.json` (workspace root):
```json
{
  "active": [...],
  "upcoming": [...],
  "history": [...]
}
```

## Contest Status

- **upcoming** - Not started yet
- **active** - Currently running
- **completed** - Ended, moved to history

## Why It Matters

Audit competitions are high-revenue but time-intensive. Tracking and prioritizing ensures you focus on high-ROI opportunities instead of chasing everything.

## Next Steps

1. **Track** - Add active contests from code4rena.com
2. **Research** - Check tech stack and difficulty
3. **Register** - Mark contest as `registered: true`
4. **Audit** - Work during the contest window
5. **Submit** - Mark findings and rewards
6. **Review** - Learn from completed contests

## Integration

Works well with:
- `code4rena-scout.py` - For automated contest discovery
- `grant-discovery-tracker.py` - For parallel grant tracking

## See Also

- Code4rena: https://code4rena.com
- Sherlock: https://sherlock.xyz
- Audit competitions can pay $5K-$100K+ per contest
