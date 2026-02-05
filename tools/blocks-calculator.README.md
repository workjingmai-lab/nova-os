# Blocks Calculator

Quick velocity projections for work block planning.

## What It Does

Shows how many work blocks you can complete in a given time at different velocities. Useful for:
- Milestone planning ("How long to reach 2000 blocks?")
- Timeboxing ("How many blocks in 30 minutes?")
- Velocity comparisons ("Sustained vs burst vs peak")

## Usage

```bash
# Default: 1 hour at 44 blocks/hr (sustained velocity)
python3 tools/blocks-calculator.py

# Custom time: 30 minutes at sustained velocity
python3 tools/blocks-calculator.py 30

# Custom time + velocity: 2 hours at burst velocity
python3 tools/blocks-calculator.py 120 55
```

## Output Example

```
📊 Blocks Calculator — 60 minutes @ 44 blocks/hr
   Time: 1.0 hours (60 minutes)
   Velocity: 44 blocks/hr (0.73 blocks/min)
   Result: 44 work blocks

🔹 Velocity Scenarios:
   • 25 blocks/hr → 25 blocks (relaxed)
   • 44 blocks/hr → 44 blocks (sustained)
   • 55 blocks/hr → 55 blocks (burst)
   • 70 blocks/hr → 70 blocks (peak)
```

## Velocity Benchmarks

- **Relaxed (25/hr):** 2.4 min/block — learning, research, complex tasks
- **Sustained (44/hr):** 1.36 min/block — consistent execution, default pace
- **Burst (55/hr):** 1.09 min/block — focused execution, deep work
- **Peak (70/hr):** 0.86 min/block — maximum velocity, short bursts only

## Use Cases

1. **Milestone Planning:** Calculate time to reach 2000 blocks
   ```bash
   # 77 blocks remaining @ sustained 44/hr = 105 minutes (1.75 hours)
   python3 tools/blocks-calculator.py 105 44
   ```

2. **Timeboxing:** Plan focused work sessions
   ```bash
   # 30-minute focused session @ burst 55/hr = 27 blocks
   python3 tools/blocks-calculator.py 30 55
   ```

3. **Velocity Tracking:** Compare actual vs planned
   ```bash
   # Planned: 44 blocks in 60 minutes (sustained)
   # Actual: 55 blocks in 60 minutes (burst) = +25% improvement
   ```

## Related Tools

- `velocity-calc.py` — Historical velocity + milestone ETA predictions
- `work-pattern-analyzer.py` — Diurnal velocity patterns by hour
- `daily-output-tracker.py` — Daily block counts + trends

## File Size

2.0 KB (Python script + README)

## Created

2026-02-05 — Work block 1925
