# lead-score-calculator.py — Service Lead Prioritization

**Purpose:** Score and prioritize service leads based on fit, value, and readiness.

**Problem Solved:** When you have 10+ leads but limited time, which do you contact first? This tool calculates a 0-100 priority score.

**Usage:**

```bash
# Score a single lead
python3 tools/lead-score-calculator.py score \
  --company "DeFi Protocol" \
  --fit 8 \
  --value 5000 \
  --readiness 7

# Score all leads from tracker
python3 tools/lead-score-calculator.py batch --from-file data/service-outreach-tracker.json
```

**Scoring Algorithm:**
```
Score = (fit × 0.4) + (value_norm × 0.3) + (readiness × 0.3)
```

- **Fit (0-10):** How well does this match my skills? (40% weight)
- **Value ($1K-$25K):** Project value normalized (30% weight)
- **Readiness (0-10):** How ready are they to buy? (30% weight)

**Output:**
- Priority score (0-100)
- Tier classification (high/medium/low)
- Ranking among all leads

**Example:**
```
Company: DeFi Protocol
Score: 60/100
Tier: MEDIUM
- Fit: 8/10 (strong match)
- Value: $5K (medium)
- Readiness: 7/10 (interested)

Recommendation: Contact in batch 2 (after high-priority leads)
```

**Created:** 2026-02-03 (Work block #888)
**Part of:** Service Outreach Pipeline ($122K tracked)

---

**See Also:**
- `service-outreach-tracker.md` — Lead database
- `outreach-personalizer.md` — Message generation
- `pipeline-summary.md` — $302K revenue overview
