# grant-submit-helper.py

## Purpose
Generate quick summaries of prepared grant submissions for review before execution.

## Usage
```bash
python3 tools/grant-submit-helper.py
```

## Output
Prints summary of all ready grants:
- Grant name
- Platform
- Amount range
- Status (Ready/Blocked)
- Blocker (if any)

## Integration with Revenue Pipeline
Part of the 15-minute grant submission workflow:
1. Review summaries (this tool)
2. Execute submissions using templates in `outreach/grants/`
3. Track status in `outreach/grant-tracker.md`

## Dependencies
- `outreach/grant-tracker.md` — Grant database
- `outreach/grants/*/` — Individual grant templates

## Created
2026-02-02 (Week 2 Revenue Pivot)

## Impact
Unblocks $110K potential grant funding across 5 platforms (Gitcoin, Octant, Olas, Optimism, Moloch DAO).
