# pipeline-reconciler.py — Data Consistency Checker

**Purpose:** Detect inconsistencies between pipeline data sources to prevent revenue leakage from bad data.

---

## Why This Tool Matters

**Bad data = bad decisions.**

Discovered in work block 2162:
- revenue-pipeline.json claimed: $2.48M
- today.md claimed: $880K
- Actual calculated: $2.237M

**$1.6M discrepancy** between sources. Without reconciliation, you make decisions on wrong numbers.

---

## What It Checks

### Data Sources
1. **revenue-pipeline.json** — Main pipeline tracking
2. **service-outreach-tracker.json** — Service outreach messages
3. **today.md** — Daily status snapshot
4. **Actual calculated values** — Ground truth from source arrays

### Validates
- Total pipeline value across sources
- Service outreach totals
- Grant totals
- Bounty totals
- Conversion rates

---

## Usage

```bash
# Run reconciliation check
python3 tools/pipeline-reconciler.py

# Verbose mode (detailed output)
python3 tools/pipeline-reconciler.py --verbose
```

---

## Output

```
============================================================
📊 PIPELINE RECONCILIATION REPORT
============================================================

✅ ACTUAL VALUES (from source data):
   Services: $2.06M (104 ready, 0 sent)
   Grants:   $130K
   Bounties: $50K
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   TOTAL:    $2.24M

📋 CLAIMED VALUES (from summaries):
   revenue-pipeline.json:  $2.48M
   today.md:               $880K

⚠️  DISCREPANCIES FOUND:

   🔴 revenue-pipeline.json services
      Claimed: $2.31M
      Actual:  $2.06M
      Diff:    $248K (+248K)

   🟡 today.md
      Claimed: $880K
      Actual:  $2.24M
      Diff:    $-1357K (-1357K)

📈 SERVICE OUTREACH STATS:
   Messages ready: 104
   Messages sent:  0
   Avg value:      $20K per message
   Conversion:     0.0%

============================================================
```

---

## Severity Levels

- 🔴 **HIGH** — Difference >$200K (immediate action needed)
- 🟡 **MEDIUM** — Difference >$100K (investigate soon)
- 🟢 **LOW** — Known stale data (tracker summary field)

---

## Exit Codes

- `0` — No discrepancies (or only LOW severity)
- `1` — HIGH or MEDIUM severity discrepancies found

Use in automation:
```bash
python3 tools/pipeline-reconciler.py || echo "⚠️ Data inconsistencies found"
```

---

## Common Issues

### revenue-pipeline.json overcounts
**Cause:** Duplicate entries or outdated values
**Fix:** Audit the JSON file, remove duplicates

### today.md undercounts
**Cause:** Outdated snapshot from earlier in week
**Fix:** Update today.md with current values

### service-outreach-tracker.json summary wrong
**Cause:** Summary field not updated when messages added
**Fix:** Ignore summary, use actual calculated values

---

## Integration

### Cron job (hourly check)
```bash
# Add to HEARTBEAT.md
0 * * * * cd /home/node/.openclaw/workspace && python3 tools/pipeline-reconciler.py >> pipeline-reconciler.log
```

### Pre-execution check
```bash
# Before sending messages
python3 tools/pipeline-reconciler.py
python3 tools/service-batch-send.py --top 10
```

---

## Technical Details

### Calculation Method
1. **Services:** Sums `pipeline_value` × 1000 from all messages in service-outreach-tracker.json
2. **Grants:** Reads from revenue-pipeline.json categories.grants.amount
3. **Bounties:** Reads from revenue-pipeline.json categories.bounties.amount

### Discrepancy Detection
Triggers on:
- >5% difference OR
- >$100K absolute difference

Ensures both relative and absolute accuracy.

---

## Created

**Date:** 2026-02-05
**Work block:** 2163
**Author:** Nova
**Inspired by:** $1.6M discrepancy discovery in work block 2162

---

**Remember:** Good data → Good decisions → Good revenue.
