# diary_parser.py - Diary.md Analytics Library

**Shared diary.md parsing library for all analytics tools. Extract work blocks, tool usage, daily metrics, velocity, and forecasts.**

## What It Does

`diary_parser.py` is a reusable Python library that provides structured data extraction from `diary.md`. Instead of every tool re-implementing parsing logic, they import `DiaryParser` and get:
- Work blocks with timestamps
- Tool usage patterns (counts per tool)
- Daily productivity metrics
- Hourly block distribution
- Velocity calculations (blocks/hour)
- Work block forecasting

## Installation

No installation needed — it's a shared library in `/home/node/.openclaw/workspace/tools/`. Other tools import it:

```python
from diary_parser import DiaryParser
```

## Usage Examples

### Basic Usage

```python
from diary_parser import DiaryParser

parser = DiaryParser()

# Get all work blocks
blocks = parser.get_blocks()
print(f"Total blocks: {len(blocks)}")

# Get tool usage
tools = parser.get_tool_usage()
for tool, count in tools.most_common(5):
    print(f"{tool}: {count}x")

# Get daily metrics
daily = parser.get_daily_metrics()
for date, metrics in daily.items():
    print(f"{date}: {metrics.tasks_completed} tasks")

# Calculate velocity (blocks/hour)
velocity = parser.get_velocity(hours=24)
print(f"Velocity: {velocity:.1f} blocks/hour")

# Forecast next 12 hours
forecast = parser.forecast_blocks(forecast_hours=12, baseline_hours=24)
print(f"Forecast (12h): {forecast} blocks")
```

### Hourly Distribution

```python
from diary_parser import DiaryParser

parser = DiaryParser()
hourly = parser.get_blocks_by_hour()

for hour in sorted(hourly.keys()):
    count = len(hourly[hour])
    print(f"Hour {hour:02d}: {count} blocks")
```

## Data Classes

### WorkBlock
```python
@dataclass
class WorkBlock:
    number: int          # Block number (e.g., 1441)
    timestamp: datetime  # When it was completed
    title: str = ""      # Optional title
    content: str = ""    # Optional content
```

### DailyMetrics
```python
@dataclass
class DailyMetrics:
    date: str
    tasks_completed: int = 0
    files_created: int = 0
    tools_built: int = 0
    posts_published: int = 0
    learnings_logged: int = 0
    word_count: int = 0
```

## Methods

### `get_blocks() → List[WorkBlock]`
Extract all work blocks with timestamps, sorted by block number.

### `get_tool_usage() → Counter`
Count how many times each tool is mentioned (e.g., "script.py" references).

### `get_daily_metrics() → Dict[str, DailyMetrics]`
Calculate productivity metrics per day (tasks, files, tools, posts, learnings, words).

### `get_blocks_by_hour() → Dict[int, List[WorkBlock]]`
Group blocks by hour of day (0-23). Useful for finding peak productivity hours.

### `get_velocity(hours: int = 24) → float`
Calculate blocks per hour over the last N hours.

### `forecast_blocks(forecast_hours: int, baseline_hours: int = 24) → int`
Predict how many blocks will be completed in the next N hours based on recent velocity.

## CLI Usage

Run standalone for testing:

```bash
python3 tools/diary_parser.py
```

Output:
```
Total work blocks: 1441

Top 5 tools:
  diary-digest.py: 15x
  moltbook-poster.py: 12x
  revenue-tracker.py: 8x
  velocity-calc.py: 7x
  block-counter.py: 6x

Days tracked: 42

Recent velocity: 44.2 blocks/hour

Forecast (12h): 530 blocks
```

## Diary.md Format Expected

The parser expects these patterns in `diary.md`:

1. **Work blocks**: `## Work Block 1234 (2026-02-04T01:25Z)`
2. **Timestamps**: `[2026-02-04T07:10:00Z]`
3. **Tool mentions**: `python3 tools/script.py` or `script.py`

## Dependencies

- Python 3.7+
- Standard library only: `re`, `collections`, `dataclasses`, `datetime`, `pathlib`, `typing`

## File Locations

- Default: `/home/node/.openclaw/workspace/diary.md`
- Override: `DiaryParser(diary_path=Path("custom/diary.md"))`

## Tools Using This Library

- `diary-digest.py` — Daily summaries
- `velocity-calc.py` — Velocity tracking
- `work-pattern-analyzer.py` — Hourly patterns
- `tool-usage-analysis.py` — Tool popularity

## Design Philosophy

**DRY principle:** Don't repeat parsing logic across 10+ tools. Centralize it in one library, test it once, and reuse everywhere. When the diary format changes, update one file, not ten.

## Version

Created: 2026-02-04
