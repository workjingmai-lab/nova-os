# Quick Revenue Commands

One-liners for pipeline management.

---

## Check Status

```bash
# Full pipeline view
python3 tools/revenue-tracker.py status

# Quick summary only
python3 tools/revenue-tracker.py status --short

# By category
python3 tools/revenue-tracker.py status --category grants
python3 tools/revenue-tracker.py status --category services
python3 tools/revenue-tracker.py status --category bounties
```

---

## Update Opportunities

```bash
# Mark as sent
python3 tools/revenue-tracker.py update "EF Security Audit" --status sent

# Mark as submitted (grants)
python3 tools/revenue-tracker.py update "Gitcoin" --status submitted

# Mark as won
python3 tools/revenue-tracker.py update "Fireblocks" --status won --value 35000

# Mark as lost
python3 tools/revenue-tracker.py update "Lead Name" --status lost --reason "no-budget"
```

---

## Add New Lead

```bash
# Quick add
python3 tools/revenue-tracker.py add "Company Name" --value 25000 --category services

# Full add
python3 tools/revenue-tracker.py add "Company Name" \
  --value 25000 \
  --category services \
  --contact "person@company.com" \
  --source "moltbook" \
  --notes "Met via CLAW post"
```

---

## Conversion Metrics

```bash
# View conversion rates
python3 tools/revenue-tracker.py conversion

# Export for analysis
python3 tools/revenue-tracker.py export > pipeline-export.json
```

---

## Daily Routine

```bash
# Morning check (30 sec)
python3 tools/revenue-tracker.py status --short

# Post-outreach update (1 min)
python3 tools/revenue-tracker.py update "Lead" --status sent

# Evening review (2 min)
python3 tools/revenue-tracker.py conversion
```

---

## Pipeline Health

| Metric | Target | Check Command |
|--------|--------|---------------|
| Ready pipeline | >$500K | `status --short` |
| Conversion rate | >10% | `conversion` |
| Follow-ups due | 0 | `follow-up-tracker.py due` |

---

*Quick reference — 30 seconds to mastery*
