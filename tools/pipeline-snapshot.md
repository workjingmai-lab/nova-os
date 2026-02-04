# pipeline-snapshot.py — Pipeline Status at a Glance

**Purpose:** Instant pipeline status view — total messages, value by status, response rate, top prospects. Core component of orchestration ecosystem.

**When to use:** Quick check on pipeline health, status sync, or before making execution decisions.

---

## What It Does

1. **Loads pipeline** — Reads `service-outreach-tracker.json`
2. **Counts by status** — ready, sent, responded, won, lost
3. **Calculates value** — Pipeline value by status ($2M+ tracked)
4. **Response rate** — % responded vs sent
5. **Top prospects** — Top 5 by value

---

## Usage

### Text Output (Default)

```bash
python3 tools/pipeline-snapshot.py
```

**Example output:**
```
📊 PIPELINE SNAPSHOT
==================================================

Total messages: 25
Total value: $2237K

By status:
  ready            13 messages | $2057K
  sent              8 messages | $ 130K
  responded         3 messages | $  40K
  won               1 messages | $  10K

Response rate: 37.5% (3/8)

Top 5 by value:
  1. Enterprise Co        $25K (ready)
  2. Tech Startup Inc     $10K (ready)
  3. Midsize Corp         $7K (sent)
  4. Small Business LLC   $5K (responded)
  5. Another Corp         $3K (won)
```

### JSON Export

```bash
python3 tools/pipeline-snapshot.py --json
```

**Output:**
```json
{
  "total_messages": 25,
  "total_value": 2237,
  "by_status": {
    "counts": {
      "ready": 13,
      "sent": 8,
      "responded": 3,
      "won": 1
    },
    "values": {
      "ready": 2057,
      "sent": 130,
      "responded": 40,
      "won": 10
    }
  },
  "response_rate": 37.5,
  "responded": 3,
  "sent": 8
}
```

### Markdown Export

```bash
python3 tools/pipeline-snapshot.py --markdown
```

**Output:**
```markdown
## Pipeline Snapshot

**Total Messages:** 25
**Total Pipeline Value:** $2237K

| Status | Count | Value |
|--------|-------|-------|
| ready | 13 | $2057K |
| sent | 8 | $130K |
| responded | 3 | $40K |
| won | 1 | $10K |

**Response Rate:** 37.5% (3/8)
```

---

## Status Breakdown

**Typical pipeline flow:**

```
ready → sent → responded → won/lost
```

**Status meanings:**
- **ready** — Generated, not yet sent
- **sent** — Message sent, awaiting response
- **responded** — Prospect replied
- **won** — Converted to customer
- **lost** — Not interested

---

## Metrics

**Key metrics tracked:**

| Metric | Formula | What It Means |
|--------|---------|---------------|
| **Total value** | Sum of all pipeline values | Potential revenue |
| **Ready value** | Sum of "ready" status | Can execute now |
| **Response rate** | responded / sent × 100% | Message quality |

**Example interpretation:**
- $2057K ready → Can execute immediately (Arthur approval needed)
- $130K sent → Waiting for responses
- 37.5% response rate → Above average (good message quality)

---

## Integration

**Used by:**

1. **pipeline-health-check.py** — Shows pipeline status in unified view
2. **revenue-tracker.py** — Detailed revenue breakdown
3. **Manual checks** — Quick pipeline overview

**Data flow:**
```
service-outreach-tracker.json
         ↓
pipeline-snapshot.py
         ↓
pipeline-health-check.py (unified view)
```

---

## Files

**Input:** `service-outreach-tracker.json`

```json
{
  "messages": [
    {
      "id": 1,
      "prospect": "Enterprise Co",
      "amountRange": "$25K",
      "pipeline_value": 25,
      "status": "ready",
      "file": "path/to/message.md"
    }
  ]
}
```

**Optional input:** `data/responses.json` (for response rate calculation)

---

## Dependencies

- Python 3.6+
- Standard library only (`json`, `sys`, `pathlib`, `typing`)
- **Required:** `service-outreach-tracker.json`

---

## Use Cases

**Before work:**
```bash
# Check pipeline value
python3 tools/pipeline-snapshot.py
# Output: $2057K ready → "Execute services!"
```

**Status sync:**
```bash
# Export markdown for report
python3 tools/pipeline-snapshot.py --markdown > report.md
```

**Automation:**
```bash
# Export JSON for dashboards
python3 tools/pipeline-snapshot.py --json > dashboard/pipeline.json
```

---

## Created

2026-02-03 — Work block ~1100 (pipeline visibility)
