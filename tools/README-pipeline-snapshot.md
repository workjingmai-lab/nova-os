# pipeline-snapshot.py — Instant Pipeline Visibility

## What It Does

Shows your entire revenue pipeline status in one second:
- Total messages, ready, sent, responded
- Pipeline value by status
- Response rate tracking
- Top 5-10 prospects by value

## Usage Examples

**Quick text snapshot:**
```bash
python3 tools/pipeline-snapshot.py
```

**JSON output (for scripts):**
```bash
python3 tools/pipeline-snapshot.py --json
```

**Markdown table (for reports):**
```bash
python3 tools/pipeline-snapshot.py --markdown
```

## Output Examples

**Text format:**
```
📊 PIPELINE SNAPSHOT
==================================================

Total messages: 100
Total value: $1979K

By status:
  ready              100 messages | $1979K

Response rate: 0.0% (0/0)

Top 5 by value:
  1. Ethereum Foundation  $40K (ready)
  2. Fireblocks           $35K (ready)
  3. Alchemy              $30K (ready)
  4. Infura               $30K (ready)
  5. Circle               $30K (ready)
```

**JSON format:**
```json
{
  "total_messages": 100,
  "total_value": 1979,
  "by_status": {
    "counts": {"ready": 100},
    "values": {"ready": 1979}
  },
  "response_rate": 0.0,
  "responded": 0,
  "sent": 0
}
```

## Data Sources

Reads from:
- `service-outreach-tracker.json` — Pipeline messages
- `data/responses.json` — Response tracking

## Use Cases

**Before execution:**
```bash
python3 tools/pipeline-snapshot.py
# Verify 100 messages ready → $1979K → execute
```

**After sending:**
```bash
python3 tools/pipeline-snapshot.py
# Check: 100 sent, 15 responded → 15% response rate
```

**Status reports:**
```bash
python3 tools/pipeline-snapshot.py --markdown > status-report.md
# Share pipeline health with team
```

## Why This Matters

**Visibility = velocity.**
- 1 command = 1 second = full pipeline health
- 120× faster than opening tracker file + counting manually
- Answer "how's it going?" instantly

**Arthur asks:** "How's the pipeline doing?"
**You:** One command → full picture → answer → done.

---

**Created:** Work block 1179  
**Last updated:** 2026-02-03  
**Related tools:** service-batch-send.py, response-tracker.py, outreach-tracker.py
