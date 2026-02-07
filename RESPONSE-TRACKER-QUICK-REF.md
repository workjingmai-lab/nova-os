# Response Tracker — Quick Reference

**Tool:** `tools/response-tracker.py`
**Purpose:** Track conversion from sent messages to revenue

---

## Quick Commands

```bash
# Show conversion funnel status
python3 tools/response-tracker.py status

# Add a new response
python3 tools/response-tracker.py add

# List all responses
python3 tools/response-tracker.py list

# Export to JSON
python3 tools/response-tracker.py export
```

---

## Conversion Funnel

```
Sent → Responses → Calls → Won/Lost
```

**Metrics tracked:**
- Response rate: Responses / Sent
- Call rate: Calls / Responses
- Close rate: Won / Calls
- Overall rate: Won / Sent

---

## Example Workflow

### 1. Check Status (do this daily)
```bash
python3 tools/response-tracker.py status
```

Output:
```
📊 Conversion Funnel Status
==================================================
📤 Sent:            60 messages
💬 Responses:        6 (10.0%)
📞 Calls:            3 (50.0% of responses)
✅ Won:              1 ($ 10,000 est.)
❌ Lost:             0

📈 Conversion Rates:
   Response rate:  10.0%
   Call rate:      50.0%
   Close rate:     33.3%
   Overall rate:    1.7%

💰 Pipeline value: $ 1,500,000
💵 Revenue won:    $    10,000
📊 Gap:            $ 1,490,000
```

### 2. Add Response (when you get one)
```bash
python3 tools/response-tracker.py add
```

Interactive prompts:
```
Target organization: Ethereum Foundation
Stage (response/call/won/lost): response
Notes: Interested in R&D suite, asked for call
```

### 3. List Recent Responses
```bash
python3 tools/response-tracker.py list
```

Shows last 20 responses with dates, targets, stages.

---

## What This Tells You

**Pre-execution:** All zeros (baseline)
**Day 1:** 60 sent, 0 responses (waiting game)
**Day 3:** 60 sent, 6 responses (10% response rate ✅)
**Day 7:** 60 sent, 6 responses, 3 calls (50% call rate ✅)
**Day 14:** 60 sent, 6 responses, 3 calls, 1 won (33% close rate ✅)

**Target metrics:**
- Response rate: 10-20%
- Call rate: 30-50%
- Close rate: 20-40%
- Overall: 1-5%

---

## Data File

**Location:** `conversion-funnel.json`
**Backup:** `conversion-funnel-export.json`

Format:
```json
{
  "created": "2026-02-06T19:08:00",
  "lastUpdated": "2026-02-06T19:08:00",
  "funnel": {
    "sent": 0,
    "responses": 0,
    "calls": 0,
    "won": 0,
    "lost": 0
  },
  "responses": []
}
```

---

## Integration with Revenue Tracker

- **Revenue tracker:** Pipeline potential ($1.49M)
- **Response tracker:** Conversion reality (what actually converts)

Use both:
1. `revenue-tracker.py status` → What's ready to send
2. `response-tracker.py status` → What's converting

---

*Created: Work block 2826*
*Post-3000 focus: Conversion > Pipeline*
