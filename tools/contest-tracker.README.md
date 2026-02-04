# contest-tracker.py — Code4rena Audit Competition Tracker

**Purpose:** Track, prioritize, and manage Web3 security audit competitions (Code4rena, Sherlock, etc.).

## What It Does

- Maintains database of audit contests (active, upcoming, history)
- Calculates opportunity scores based on prize pool, difficulty, tech stack
- Displays prioritized dashboard with highest-value contests first
- Tracks contest status (upcoming → active → completed)
- Stores contest metadata: dates, tech stack, URLs, registration status

## Usage

```bash
# Run standalone (displays dashboard)
python3 tools/contest-tracker.py

# Output:
# ============================================================
# 🛡️  CODE4RENA CONTEST TRACKER
# ============================================================
# 
# 🔥 ACTIVE (1)
#   • Olas: $62,000 | Ends: 2026-02-09
# 
# 📅 UPCOMING (1)
#   • Jupiter Lend: $107,000 | Score: 97000 | Starts: 2026-02-04
# 
# 📊 STATS
#   Total Prize Pool Available: $169,000
#   Contests Tracked: 0
# ============================================================
```

## Data Structure

Contests stored in `contests.json`:
```json
{
  "active": [
    {
      "id": "code4rena-olas",
      "name": "Olas",
      "platform": "Code4rena",
      "prize_pool_usd": 62000,
      "start_date": "2026-01-22T20:00:00Z",
      "end_date": "2026-02-09T20:00:00Z",
      "tech_stack": ["solidity", "evm"],
      "difficulty": "medium",
      "url": "https://code4rena.com/audits/2026-01-olas",
      "status": "active",
      "registered": false,
      "submitted": false,
      "findings": [],
      "reward_usd": 0
    }
  ],
  "upcoming": [],
  "history": []
}
```

## Opportunity Score Algorithm

```
score = prize_pool × difficulty_multiplier × (1 + tech_bonus × 0.1)
```

- **Difficulty multiplier:** easy=1.2, medium=1.0, hard=0.7
- **Tech bonus:** +10% per familiar tech stack (Solidity, EVM, JavaScript)

Higher score = better opportunity (prize ÷ effort ratio).

## Key Methods

- `add_contest()` — Add new contest to database
- `get_prioritized()` — Return contests ranked by opportunity score
- `print_dashboard()` — Display formatted contest overview
- `_opportunity_score()` — Calculate contest value score

## Use Cases

- **Audit pipeline:** Identify which Code4rena contests to target
- **Revenue planning:** Track upcoming prize pools
- **Tech stack filtering:** Focus on familiar technologies
- **Competitive analysis:** Monitor market activity

## Dependencies

- Python 3.7+
- No external packages (stdlib only)

## Integration

Can be integrated with:
- **Moltbook:** Auto-post contest opportunities
- **Revenue tracker:** Add audit prizes to pipeline
- **Calendar:** Add contest end-date reminders

## Notes

- Requires manual data entry for new contests (or web scraper)
- Status auto-calculates from start/end dates vs current time
- Opportunity scoring is subjective — adjust weights in `_opportunity_score()`
- Data persists in local `contests.json` file
