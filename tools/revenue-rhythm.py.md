# revenue-rhythm.py

Daily revenue execution tracker. Quick status + next action for maintaining revenue momentum.

## Usage

```bash
python3 revenue-rhythm.py
```

## Output

```
══════════════════════════════════════════════════
💰 REVENUE RHYTHM — 2026-02-07 09:45 UTC
══════════════════════════════════════════════════

📊 PIPELINE STATUS
   Total Potential:  $   754,500
   ─────────────────────────
   Grants Submitted: $     5,000
   Grants Ready:     $   125,000
   Services Ready:   $   629,500
   └─ HIGH Priority: $   115,000

🎯 TODAY'S ACTIONS
   Submit: Gitcoin, Octant
   Contact: Ethereum Foundation, Fireblocks, Uniswap

⏱️  TIME TO $100K: ~10 minutes of focused execution
══════════════════════════════════════════════════
```

## Data Source

Reads from `revenue-pipeline.json` (created by revenue-tracker.py).

## Features

- **Quick status**: Single-command pipeline snapshot
- **Priority focus**: Highlights HIGH priority service leads
- **Action prompts**: Shows next 2 grants to submit, next 2 leads to contact
- **Time estimate**: Calculates "minutes to $100K" based on historical velocity

## Integration

Part of the revenue execution toolkit:
- `revenue-tracker.py` — Full pipeline management
- `revenue-rhythm.py` — Daily quick check (this tool)
- `send-batch.py` — Batch message sending
- `lead-prioritizer.py` — Rank leads by value/effort
