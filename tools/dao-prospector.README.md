# dao-prospector.py — Find DAO Outreach Targets

**Purpose:** Filter DAOs by treasury size to identify outreach opportunities.

## What It Does

- Filters DAOs by minimum treasury threshold
- Shows governance type and category
- Sorted by treasury size (largest first)

## Usage

```bash
python3 tools/dao-prospector.py <min_treasury>
```

**Examples:**
```bash
# Find DAOs with $50K+ treasury
python3 tools/dao-prospector.py 50000

# Find DAOs with $1M+ treasury
python3 tools/dao-prospector.py 1000000
```

## Sample Output

```
Found 8 DAOs with treasury >= $50,000

🏛️  MakerDAO
   Treasury: $10,000,000,000
   Governance: MKR token
   Category: DeFi
...
```

## Data Source

Currently uses hardcoded SAMPLE_DAOS dict with major DAOs (Uniswap, Aave, Compound, MakerDAO, ENS, Gitcoin, Optimism, Arbitrum).

**Future enhancements:**
- Integrate DeepDAO API
- Integrate Messari DAO leaderboard
- Add recent activity filter
- Add governance participation metrics

## Use Case

Revenue pipeline expansion:
1. Find DAOs with $50K+ treasuries
2. Research their current automation stack
3. Craft value-first outreach messages
4. Track in revenue-tracker.py

---

**Created:** 2026-02-05 (Work block 2100)
**Status:** Active, ready for use
