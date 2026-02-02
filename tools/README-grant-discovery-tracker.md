# Grant Discovery Tracker

Quick reference tool for discovering and evaluating grant opportunities for agents.

## What It Does

Displays:
- Known grant sources (Gitcoin, Ethereum Foundation, etc.)
- Assessment checklist for evaluating opportunities
- Template for logging new grant discoveries
- Quick search commands for common platforms

## When to Use

**Use when:**
- Starting a grant search session
- Need a consistent format for evaluating opportunities
- Want to track multiple grants systematically
- Building a pipeline of potential funding sources

**Don't use when:**
- Actually submitting grants (use `grant-submit-helper.py`)
- Tracking application status (use `grant-status-tracker.py`)

## Usage

```bash
python tools/grant-discovery-tracker.py
```

## Output Example

```
============================================================
🔍 GRANT DISCOVERY TRACKER
============================================================

📍 KNOWN GRANT SOURCES:
  1. Gitcoin Grants
  2. Ethereum Foundation
  3. OpenCLaw Community Fund
  4. Protocol DAO Grants
  5. Climate Crypto
  6. Public Goods Funding

✅ ASSESSMENT CHECKLIST:
  1. Alignment with agent capabilities
  2. Application complexity (1-5)
  3. Time requirement (hours)
  4. Decision timeline
  5. Past award rate

📝 NEW GRANT ENTRY TEMPLATE:
------------------------------------------------------------

Source: [Name]
URL: [Link]
Amount: [$X,XXX]
Deadline: [YYYY-MM-DD]
Alignment: [High/Med/Low]
Complexity: [1-5]
Time Required: [X hours]
Status: [Researching/Applying/Won/Lost]
Notes: [Key details]

------------------------------------------------------------
```

## Integration

**Works with:**
- `grant-submit-helper.py` — Once you've discovered and evaluated grants
- `grant-status-tracker.py` — For tracking application progress
- `grants/tracked-grants.md` — Log discovered grants here

## Quick Workflow

1. Run `grant-discovery-tracker.py` to get checklist
2. Search grant sources (Gitcoin, EF, DAOs)
3. Use template to log each discovery to `grants/tracked-grants.md`
4. Evaluate against assessment criteria
5. Pass high-quality opportunities to `grant-submit-helper.py`

## Customization

Edit these lists in the script:
- `GRANT_SOURCES` — Add new grant platforms
- `ASSESSMENT_CRITERIA` — Modify evaluation checklist

## Related Tools

- `grant-submit-helper.py` — Generate submission content
- `grant-status-tracker.py` — Track application status
- `grant-submission-generator.py` — Full submission builder

---

**Created:** 2026-02-02
**Purpose:** Week 2 Revenue Generation — Grant pipeline development
**Status:** ✅ Active
