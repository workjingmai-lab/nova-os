# Verify Leads

Pre-flight validation tool for outreach message files. Ensures all lead files are properly formatted before batch sending.

## What It Does

Validates lead JSON files to catch formatting errors before batch sending:
- Checks required fields (name, company, tier, value, contact)
- Validates data types (value must be integer)
- Warns about missing contact info (email/telegram)
- Verifies message file references exist
- Reports errors, warnings, and missing files

## Usage

```bash
# Check all leads
python3 tools/verify-leads.py

# Check specific tier only
python3 tools/verify-leads.py expert
python3 tools/verify-leads.py tactical
python3 tools/verify-leads.py high
python3 tools/verify-leads.py medium
```

## Output

```
🔍 Lead File Verification
==================================================
Filtering by tier: EXPERT
Checking 10 leads...

📊 Summary:
  ✅ OK: 8
  ⚠️  Warnings: 1
  ❌ Errors: 0
  📁 Missing: 1

🚨 Issues Found (2):

  [EXPERT] Uniswap
    ⚠️  No email or telegram contact found
    ⚠️  Message file not found: outreach/messages/uniswap-outreach.md

  [TACTICAL] Aave
    ❌  Missing required field: value
```

## Validation Checks

### Required Fields (Error)
- `name` — Lead or company name
- `company` — Company/organization name
- `tier` — Lead tier (EXPERT/TACTICAL/HIGH/MEDIUM)
- `value` — Deal size in USD (integer)
- `contact` — Contact info object

### Warnings
- Value is zero or negative
- No email or telegram in contact object
- Referenced message file doesn't exist

### Errors
- File not found (missing lead JSON)
- Invalid JSON syntax
- Missing required field
- Value is not an integer

## When to Use

### Before Batch Sending
Run before `send-everything.sh` to catch errors early:

```bash
python3 tools/verify-leads.py && bash tools/send-everything.sh full
```

### After Adding New Leads
After creating new lead files, verify they're formatted correctly:

```bash
python3 tools/verify-leads.py expert  # Check just EXPERT tier
```

### After Manual Edits
If you manually edited lead JSON files, verify no syntax errors:

```bash
python3 tools/verify-leads.py
```

## Exit Codes

- `0` — All leads OK (or warnings only)
- `1` — Errors found (missing files, invalid JSON, missing required fields)

Use in scripts:
```bash
if python3 tools/verify-leads.py; then
    echo "All leads valid, proceeding with send"
    bash tools/send-everything.sh full
else
    echo "Errors found, aborting send"
    exit 1
fi
```

## Integration

### With send-everything.sh
The main send script doesn't automatically run verify-leads.py to avoid slowing down the process. Add it manually:

```bash
# Safe send workflow
python3 tools/verify-leads.py
python3 tools/execution-gap.py  # See what you're about to send
bash tools/send-everything.sh full
```

### In Cron Jobs
Schedule daily verification to catch drift:

```bash
# Daily lead health check
0 9 * * * cd ~/.openclaw/workspace && python3 tools/verify-leads.py > logs/lead-verify.log 2>&1
```

## Why It Matters

**Pre-flight checks prevent failed batch sends.**

A single malformed lead file can cause the entire batch send to fail mid-process. That means:
- Some messages sent (can't undo)
- Some messages failed (need to manually sort)
- Wasted time debugging
- Unprofessional if leads receive duplicate messages

verify-leads.py catches issues before execution, not during.

## Troubleshooting

### "0 leads" result
If the script shows "Checking 0 leads" but you have leads:
- Check that `revenue-pipeline.json` exists and is valid JSON
- Verify leads are organized in the expected structure
- The script expects lead data in `categories.services.tiers.[tiername].leads`

### "Invalid JSON" error
Open the lead JSON file and check for:
- Missing commas between fields
- Trailing commas (not valid in JSON)
- Unquoted keys
- Single quotes instead of double quotes
- Comments (not valid in JSON)

### "Missing required field"
Ensure your lead JSON has all required fields:
```json
{
  "id": "uni",
  "name": "Uniswap",
  "company": "Uniswap Labs",
  "tier": "EXPERT",
  "value": 40000,
  "contact": {
    "email": "contact@uniswap.org"
  },
  "message_file": "outreach/messages/uniswap-outreach.md"
}
```

## Related Tools

- `send-everything.sh` — Batch send all ready messages
- `revenue-tracker.py` — Track and manage pipeline
- `service-batch-send.py` — Send specific tiers

## Data Files

- Reads: `revenue-pipeline.json`
- Validates: `outreach/leads/*.json`
- Checks: `outreach/messages/*.md` (if referenced)

## Created

Work block 2914 — 2026-02-06 23:21Z
