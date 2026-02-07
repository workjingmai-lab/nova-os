# block-roi-calc.py

Work Block ROI Calculator — Measure your execution efficiency.

## Quick Start

```bash
python3 tools/block-roi-calc.py 1000 880000
```

## Usage

```bash
python3 tools/block-roi-calc.py <blocks> <value> [options]

Options:
  --currency USD    Currency code (default: USD)
  --time 1          Avg minutes per block (default: 1)
```

## Examples

```bash
# Basic calculation
python3 tools/block-roi-calc.py 1000 880000

# Different currency
python3 tools/block-roi-calc.py 500 45000 --currency EUR

# Slower blocks (5 min each)
python3 tools/block-roi-calc.py 200 50000 --time 5
```

## Output

- **Per-block ROI:** Value generated per work block
- **Blocks/hour:** Execution velocity
- **1000-block projection:** Value and time to reach 1000 blocks
- **Benchmark:** Performance tier (🚀 Excellent / ✅ Strong / 📈 Growing / 🌱 Early)

## Benchmarks

| Tier | Per-Block ROI | Status |
|------|---------------|--------|
| 🚀 Excellent | $500+ | Top tier execution |
| ✅ Strong | $100+ | Solid performance |
| 📈 Growing | $10+ | Building momentum |
| 🌱 Early | <$10 | Focus on volume first |

## Why Use This

- **Measure efficiency:** Track value per unit of work
- **Compare periods:** See if you're improving over time
- **Set targets:** Know what 1000 blocks will produce
- **Benchmark:** Compare against standard performance tiers

## Integration

Use in scripts or heartbeats:

```bash
# Weekly ROI check
python3 tools/block-roi-calc.py $(cat .heartbeat_state.json | jq .totalBlocks) $(jq .pipelineValue revenue-pipeline.json)
```

## Related

- `velocity-calc.py` — Velocity and milestone predictions
- `revenue-tracker.py` — Pipeline tracking
- `daily-target-calc.py` — Daily progress metrics
