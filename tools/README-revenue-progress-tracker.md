# revenue-progress-tracker.py

Track progress across all revenue channels (grants, services, bounties).

## What It Does

Monitors the complete revenue pipeline across multiple channels:
- Grants (applications, submissions, awards)
- Services (leads, proposals, contracts)
- Bounties (discoveries, submissions, wins)

Calculates velocity, conversion rates, and ROI across channels.

## Installation

No dependencies required beyond Python 3. Uses `revenue-progress-tracker.json` for data persistence.

## Usage

### Get summary
```bash
python3 tools/revenue-progress-tracker.py summary
```

### Log grant activity
```bash
python3 tools/revenue-progress-tracker.py log grant "Gitcoin" "$5,000" "submitted"
```

### Log service lead
```bash
python3 tools/revenue-progress-tracker.py log service "Acme Corp" "$10,000" "lead"
```

### Log bounty submission
```bash
python3 tools/revenue-progress-tracker.py log bounty "Code4rena#123" "$15,000" "submitted"
```

## Data Structure

```json
{
  "lastUpdated": "2026-02-03T01:47:00Z",
  "channels": {
    "grants": {
      "potential": 130000,
      "submitted": 0,
      "won": 0,
      "conversionRate": 0.0
    },
    "services": {
      "potential": 122000,
      "sent": 10,
      "replied": 0,
      "won": 0,
      "conversionRate": 0.0
    },
    "bounties": {
      "potential": 50000,
      "submitted": 0,
      "won": 0,
      "conversionRate": 0.0
    }
  },
  "metrics": {
    "totalPipeline": 302000,
    "overallVelocity": 0.0,
    "topChannel": "services"
  }
}
```

## Channel Status Types

**Grants:** `lead` → `drafting` → `submitted` → `under_review` → `won`/`rejected`

**Services:** `lead` → `contacted` → `proposing` → `sent` → `negotiating` → `won`/`declined`

**Bounties:** `discovered` → `analyzing` → `submitted` → `judging` → `won`/`rejected`

## Use Cases

- **Pipeline visibility**: Single view of all revenue channels
- **Conversion tracking**: Measure success rates by channel
- **ROI calculation**: Compare effort vs reward across channels
- **Forecasting**: Project revenue based on conversion velocity

## Examples

Track grant submission:
```bash
python3 tools/revenue-progress-tracker.py \
  log grant "Optimism RPGF" "$50,000" "submitted"
```

Log service proposal sent:
```bash
python3 tools/revenue-progress-tracker.py \
  log service "SEMI" "$25,000" "sent"
```

Check overall health:
```bash
python3 tools/revenue-progress-tracker.py summary
```

## Integration

Works with:
- `revenue-tracker.py` — Detailed per-item tracking
- `service-outreach-tracker.py` — Service-specific tracking
- `revenue-pipeline.json` — Total pipeline snapshot

## Return Codes

- `0` — Success
- `1` — Error (invalid arguments, file write error)

## Notes

- All timestamps in UTC
- Currency in USD
- Conversion rates calculated as (won / submitted) × 100
- Potential amounts updated as pipeline evolves

---

*Monitors $302K total pipeline across grants, services, bounties*
