# block-roi-calc.py

Calculate execution efficiency: revenue, output, or impact per work block.

## Usage

```bash
# Basic ROI calculation
python3 tools/block-roi-calc.py 1000 880000 --currency USD

# Output:
# ╔══════════════════════════════════════════════════════════════╗
# ║           WORK BLOCK ROI ANALYSIS                            ║
# ╠══════════════════════════════════════════════════════════════╣
# ║  Total Blocks:     1,000                                     ║
# ║  Total Value:      $880.0K                                   ║
# ║  Time Invested:    16.7 hours                                ║
# ╠══════════════════════════════════════════════════════════════╣
# ║  PER-BLOCK METRICS                                           ║
# ║  Value per block:  $880.00                                   ║
# ║  Blocks per hour:  60.0                                      ║
# ╠══════════════════════════════════════════════════════════════╣
# ║  PROJECTIONS                                                 ║
# ║  1,000 blocks →  $880.0K  (16.7 hours)                      ║
# ║  5,000 blocks →  $4.4M   (83.3 hours)                       ║
# ╚══════════════════════════════════════════════════════════════╝
```

## Why This Matters

Work blocks are the atomic unit of execution. This tool answers:
- What's my per-block value generation?
- Am I improving over time?
- What should my next milestone target be?

## Formula

```
Per-block ROI = Total Value / Total Blocks
Hourly Velocity = Blocks / Hours Invested
```

## Use Cases

- **Grant work:** Track $ per block on grant applications
- **Client work:** Calculate effective hourly via blocks
- **Content:** Measure audience growth per block invested

## Created

2026-02-07 — Work block 3265
