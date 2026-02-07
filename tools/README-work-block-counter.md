# work-block-counter.py

Quick work block statistics at a glance.

## Usage

```bash
python3 tools/work-block-counter.py
```

## Output

```
========================================
⚡ WORK BLOCK COUNTER
========================================
Today:     16 blocks
Rate:      16.0 blocks/hour
Total:     ~57 blocks
========================================
📊 Target:  16/300 (284 to go)
========================================
```

## Features

- Counts blocks from today's diary
- Calculates hourly rate (assumes 8am start)
- Shows progress toward 300 block target
- Estimates total blocks from all diary files

## Integration

Add to daily startup or heartbeat for visibility.
