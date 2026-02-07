# week3-tracker.py

Week 3 revenue conversion tracker — watch pipeline move from ready → won.

## Quick Start

```bash
python3 tools/week3-tracker.py
```

## Output

```
📈 Week 3 Pipeline Tracker
   Period: 2026-02-08 to 2026-02-14
   Today:  2026-02-07 05:42 UTC

   ┌─────────────┬────────┬───────────┐
   │ Status      │ Count  │ Value     │
   ├─────────────┼────────┼───────────┤
   │ 💰 Ready    │     39 │ $1,490,000│
   │ 📤 Sent     │      0 │ $        0│
   │ 📋 Submitted│      0 │ $        0│
   │ ✅ Won      │      0 │ $        0│
   │ ❌ Lost     │      0 │     —     │
   └─────────────┴────────┴───────────┘

   Total Pipeline: $1,490,000
   Conversion:     0 won / 0 lost

   🎯 Week 3 Goal: Move $250K from ready → submitted
      Progress: $0 / $250K (0.0%)
```

## Tracks

| Status | Icon | Meaning |
|--------|------|---------|
| Ready | 💰 | Message/grant ready to send |
| Sent | 📤 | Service outreach sent |
| Submitted | 📋 | Grant application submitted |
| Won | ✅ | Deal closed, revenue secured |
| Lost | ❌ | Deal lost (with reason) |

## Week 3 Goal

**Target:** Move $250K from "ready" → "submitted/won"  
**Current:** Tracked in real-time  
**Source:** `revenue-pipeline.json`

## When to Run

- Morning: "What's the starting point today?"
- After outreach: "Update the tracker"
- Evening: "How much did we move today?"
- Week end: "Did we hit $250K?"

---

*Week 3 is conversion week. Track every dollar.*
