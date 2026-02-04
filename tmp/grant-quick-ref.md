# Grant Pipeline Quick Reference
*Generated 2026-02-03T22:26Z*

## Current Status
- **8 opportunities tracked:** $1,875K total potential
- **Status breakdown:** 6 open (🟢) | 2 upcoming (🟡) | 0 urgent (≤7 days)
- **Tool:** `python3 tools/grant-opportunity-finder.py`

## Top 3 Opportunities (by value)
1. **Ethereum Foundation** — $10K-$1M (rolling deadline)
2. **Optimism RPGF S6** — $10K-$500K (Feb 20 deadline)
3. **Gitcoin Grants Round 21** — $1K-$100K (Feb 28 deadline)

## Blockers
- ⏸️ **GitHub CLI auth:** `gh auth login` required (5 min → $130K unblocked)
- ✅ **Submission content:** 5 grants ready in tmp/grant-submissions/

## Commands
```bash
# Check stats
python3 tools/grant-opportunity-finder.py --stats

# Show urgent only
python3 tools/grant-opportunity-finder.py --deadline-days 7

# Export to markdown
python3 tools/grant-opportunity-finder.py --export markdown > grants.md
```

## Next Action
Arthur runs `gh auth login` → Grant submissions unlocked → $130K potential activated

**ROI:** 5 min unblock = $26K/min
