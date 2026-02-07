# conversion-tracker.py

Track outreach conversion rates through the full funnel. Week 4 tool for optimizing conversion, not just building pipeline.

## Quick Start

```bash
# Check current funnel status
python3 tools/conversion-tracker.py status

# Add a new lead
python3 tools/conversion-tracker.py add ef01 "EF Support" grant 40000 standard

# Update lead stage (when they reply, book call, etc.)
python3 tools/conversion-tracker.py update ef01 replied
python3 tools/conversion-tracker.py update ef01 call_booked
```

## Conversion Funnel

```
sent → opened → replied → call_booked → proposal_sent → closed_won
                                                   ↓
                                              closed_lost
```

## Commands

| Command | Description |
|---------|-------------|
| `status` | Show full funnel visualization |
| `add <id> <name> <source> <value> <type>` | Add new lead |
| `update <id> <stage>` | Move lead to new stage |
| `help` | Show usage help |

## Target Rates

- **Response rate:** 10%+ (replies / sent)
- **Close rate:** 5%+ (closed_won / sent)

## Example Session

```bash
$ python3 conversion-tracker.py add fb01 "Fireblocks" service 35000 audit
✅ Added lead: Fireblocks ($35,000)

$ python3 conversion-tracker.py update fb01 replied
🔄 Fireblocks: sent → replied

$ python3 conversion-tracker.py status
📊 CONVERSION FUNNEL STATUS
══════════════════════════════════════════════════
🔄 FUNNEL:
  sent            │██░░░░░░░░░░░░░░░░░░│ 1
  replied         │█░░░░░░░░░░░░░░░░░░░│ 1
  ...

📈 CONVERSION RATES:
  Response rate:    100.0% (target: 10%+)
```

## Data Storage

- **File:** `data/conversions.json`
- **Format:** JSON with lead history
- **Auto-created:** On first run

## Integration

Use with `revenue-tracker.py` for complete pipeline + conversion visibility:
- `revenue-tracker.py` — Pipeline value and status
- `conversion-tracker.py` — Conversion rates through funnel

---
*Created: Work block 3290*  
*Purpose: Week 4 conversion optimization*
