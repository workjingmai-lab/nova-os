# daily-target-calc.py

Real-time progress calculator for daily work block goals.

## Quick Start

```bash
python3 tools/daily-target-calc.py
```

## Output Example

```
📊 Daily Target Calculator
   Time: 05:41 UTC | Hours remaining: 18.3

   Current:  3214 blocks
   Goal:     300 blocks
   Progress: 1071.3% ✅ GOAL CRUSHED

   Surplus:  +2914 blocks (971% over goal)
   Week 3 Day 1 starts tomorrow — Feb 8
```

## Features

- **Live progress tracking** — Current vs goal in real-time
- **Velocity calculation** — Blocks/hour needed to hit target
- **Time estimation** — Hours of work required at sustained velocity
- **Status indicators** — Visual status (🟢 🟡 🔴 ✅)
- **UTC time-aware** — Calculates hours remaining in day

## Status Levels

| Status | Progress | Meaning |
|--------|----------|---------|
| ✅ | ≥100% | Goal crushed |
| 🟢 | 75-99% | On track |
| 🟡 | 50-74% | Needs attention |
| 🔴 | <50% | Behind schedule |

## Config

Edit `DAILY_GOAL` constant in the script (default: 300).

## Use Cases

- Morning planning: "How much work today?"
- Midday check: "Am I on track?"
- Evening review: "Did I hit the goal?"

---

*Simple tool. Clear insight. No surprises.*
