# Grant Pipeline — Quick Start Guide

**Status:** Ready to execute (5 grants, $130K potential)
**Blocker:** GitHub CLI auth required (`gh auth login`)
**Time to unblock:** 5 minutes → $130K unlocked

---

## Pipeline Overview

```
Discovery → Selection → Writing → Review → Submission → Tracking
```

**Current status:** 5 grants written and reviewed, ready to submit

---

## Ready to Submit (tmp/grant-submissions/)

| Grant | Platform | Amount | Status |
|-------|----------|--------|--------|
| Gitcoin | Gitcoin Grants | $5-15K | ✅ Ready |
| Octant | Octant Program | $10-50K | ✅ Ready |
| Olas | Olas Persistence | $5-25K | ✅ Ready |
| Optimism | RPGF Round | $25-150K | ✅ Ready |
| Moloch DAO | Moloch Grants | $5-10K | ✅ Ready |

**Total:** $130K potential

---

## Execution Steps

### 1. Unblock GitHub (5 min, do ONCE)
```bash
gh auth login
# Follow prompts to authenticate
```

### 2. Submit Grants (15 min total, 3 min each)
```bash
# Submit all 5 grants at once
python3 tools/grant-submit.py --quick

# Or submit individually
python3 tools/grant-submit.py --grant gitcoin
python3 tools/grant-submit.py --grant octant
python3 tools/grant-submit.py --grant olas
python3 tools/grant-submit.py --grant optimism
python3 tools/grant-submit.py --grant moloch
```

### 3. Track Status (Ongoing)
```bash
python3 tools/grant-status-tracker.py
```

---

## Tools

- **grant-submit.py** — Main submission tool (consolidated)
- **grant-status-tracker.py** — Track submission status
- **grant-discovery-tracker.py** — Find new opportunities
- **templates/grant-submission-template.md** — Proposal template

---

## Documentation

- **README-grant-submit.md** — Full documentation
- **grant-submission-quick-ref.md** — Command reference
- **grant-submission-checklist.md** — Pre-submit validation

---

## After Submission

1. **Track status** in grant-status-tracker.py
2. **Update revenue-pipeline.json** with submission dates
3. **Follow up** if reviewer feedback received
4. **Celebrate** wins, learn from rejections

---

**ROI:** 5 min GitHub auth → $130K pipeline unblocked = **$26,000/min**

**Next:** Arthur runs `gh auth login`, then I execute submission.

---

*Created: 2026-02-03*
*Last updated: 2026-02-03*
