# send-ready-leads.py

Prepare outreach sends for ready leads with message previews and ROI ranking.

## Usage

```bash
# Show ready leads with previews
python3 tools/send-ready-leads.py

# Generate checklist format
python3 tools/send-ready-leads.py checklist
```

## Output

- Lead ranking by priority and ROI
- Message preview for each lead type
- File reference for detailed message
- Conversion scenarios (5%, 10%, 20%)

## Lead Coverage

| Priority | Lead | Value | Type |
|----------|------|-------|------|
| 1 | Additional Leads | $152K | MIXED |
| 2 | DAO Leads | $127.5K | DAO |
| 3 | Ethereum Foundation | $40K | GRANT |
| 4 | Fireblocks | $35K | SERVICE |
| 5 | Balancer Labs | $20K | SERVICE |
| 6 | Curve Finance | $20K | SERVICE |
| 7 | Yearn Finance | $25K | SERVICE |
| 8 | Lido Finance | $15K | SERVICE |

**Total:** 8 leads, $609.5K value, ~24 min to send

## Integration

Pair with `execution-gap-closer.py` for full pipeline-to-action workflow.
