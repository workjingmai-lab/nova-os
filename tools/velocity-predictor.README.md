# velocity-predictor.py

**Purpose:** Predict when you'll hit milestone work blocks based on current velocity.

## Usage

```bash
# Default: Predict time to 3000 blocks
python3 tools/velocity-predictor.py

# Custom milestone
python3 tools/velocity-predictor.py --milestone 5000

# Custom velocity (blocks/hour)
python3 tools/velocity-predictor.py --blocks-hour 50

# Specific prediction model
python3 tools/velocity-predictor.py --model accelerated
```

## Prediction Models

| Model | Velocity | Description |
|-------|----------|-------------|
| Conservative | 30.8 b/hr | 30% slower than average (accounts for breaks) |
| Linear | 44.0 b/hr | Historical average velocity |
| Accelerated | 57.2 b/hr | 30% faster (with task randomizer) |

## Output Example

```
Current blocks:   2717
Target milestone: 3000
Remaining:        283 blocks

Model: LINEAR
Velocity: 44.0 blocks/hour
Time remaining: 6.4 hours
Estimated arrival: 2026-02-06 20:24 UTC
```

## How It Works

1. **Calculate remaining:** milestone - current_blocks
2. **Apply velocity:** remaining / blocks_per_hour
3. **Predict date:** now + time_remaining
4. **Compare models:** Show conservative/linear/accelerated options

## Configuration

Update `CURRENT_BLOCKS` in the file to reflect your current progress:
```python
CURRENT_BLOCKS = 2717  # From today.md
```

## Related Tools

- `task-randomizer.py` — Increase velocity by reducing decision fatigue
- `velocity-calc.py` — Calculate current velocity from diary.md

## Tips for Acceleration

1. **Reduce decisions:** Use task-randomizer.py instead of choosing tasks
2. **Execute immediately:** Don't plan, just ship
3. **Batch similar tasks:** Phase-based task pools reduce context switching
4. **Skip low-value:** Not all blocks are equal (EXPERT tier > tactical > maintenance)

## Why This Matters

Velocity prediction = realistic goal setting.

Knowing you'll hit 3000 blocks in 6.4 hours at linear velocity means:
- You can plan around milestone completion
- You can see if acceleration is needed
- You understand the compound effect of small executions

**Math:** 44 blocks/hour × 6.4 hours = 282 blocks ≈ milestone hit.
