# Blocks Calculator — Work Block Planning

Calculate how many work blocks you can complete in a given time at different velocities. Useful for milestone planning and timeboxing.

## What It Does

Takes time available and velocity (blocks/hour) → outputs work blocks you can complete. Shows scenarios at different velocities (relaxed, sustained, burst, peak).

## Usage

```bash
# Default: 1 hour at 44 blocks/hr
python3 tools/blocks-calculator.py

# 30 minutes at 44 blocks/hr
python3 tools/blocks-calculator.py 30

# 2 hours (120 min) at 55 blocks/hr
python3 tools/blocks-calculator.py 120 55

# 15 minutes at default velocity (44)
python3 tools/blocks-calculator.py 15
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

## Velocity Reference

| Velocity | Label | Use Case |
|----------|-------|----------|
| 25 blocks/hr | Relaxed | Learning, research, documentation |
| 44 blocks/hr | Sustained | Normal work, proven average |
| 55 blocks/hr | Burst | Focused execution, task randomizer |
| 70 blocks/hr | Peak | High-focus flow state (rare) |

## When to Use

- **Session planning:** "I have 2 hours before lunch, how many blocks can I do?"
- **Milestone targeting:** "Need 200 more blocks to 3000. How long at 44/hr?"
- **Timeboxing:** "Want to do 50 blocks. How long at sustained velocity?"
- **Velocity experiments:** "What if I push to 55 blocks/hr for 1 hour?"

## Math

```
blocks = (minutes / 60) × velocity

Examples:
  60 min @ 44/hr = 44 blocks
  30 min @ 44/hr = 22 blocks
  120 min @ 55/hr = 110 blocks
  15 min @ 44/hr = 11 blocks
```

## Related Tools

- `blocks-to-go.py` — Calculate blocks remaining to milestone
- `3000-milestone.py` — Full milestone tracker with ETA
- `work-pattern-analyzer.py` — Analyze your velocity over time

## Created

2026-02-06 — Week 3, quick planning tool for milestone execution
