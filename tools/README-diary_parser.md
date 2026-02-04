# diary_parser.py

**Core parsing library — shared foundation for all analytics tools.**

## What it does

Extracts structured data from `diary.md` for analytics, reporting, and optimization:
- Work blocks with timestamps
- Tool usage patterns
- Daily productivity metrics
- Hourly work patterns
- Velocity calculation and forecasting

This is a **library**, not a CLI tool. Other tools import it:

```python
from diary_parser import DiaryParser

parser = DiaryParser()
blocks = parser.get_blocks()
tools = parser.get_tool_usage()
daily = parser.get_daily_metrics()
```

## API

### `DiaryParser()`

Main parser class.

```python
parser = DiaryParser()  # Uses default diary.md path
parser = DiaryParser(diary_path=Path("custom/diary.md"))  # Custom path
```

### Methods

#### `get_blocks() → List[WorkBlock]`

Extract all work blocks with timestamps.

**Returns:** List of `WorkBlock` objects sorted by number

```python
blocks = parser.get_blocks()
for block in blocks[-5:]:  # Last 5 blocks
    print(f"#{block.number} at {block.timestamp}")
```

#### `get_tool_usage() → Counter`

Extract tool usage patterns.

**Returns:** Counter of tool mention counts

```python
tools = parser.get_tool_usage()
for tool, count in tools.most_common(10):
    print(f"{tool}: {count}x")
```

#### `get_daily_metrics() → Dict[str, DailyMetrics]`

Calculate daily productivity metrics.

**Returns:** Dict mapping date strings to `DailyMetrics` objects

```python
daily = parser.get_daily_metrics()
for date, metrics in sorted(daily.items())[-7:]:  # Last 7 days
    print(f"{date}: {metrics.tasks_completed} tasks, {metrics.files_created} files")
```

**`DailyMetrics` fields:**
- `date` — Date string (YYYY-MM-DD)
- `tasks_completed` — Number of completed tasks
- `files_created` — Number of files created
- `tools_built` — Number of tools built
- `posts_published` — Number of posts published
- `learnings_logged` — Number of learnings logged
- `word_count` — Word count of entry

#### `get_blocks_by_hour() → Dict[int, List[WorkBlock]]`

Group work blocks by hour of day.

**Returns:** Dict mapping hour (0-23) to list of blocks

```python
hourly = parser.get_blocks_by_hour()
for hour in sorted(hourly.keys()):
    count = len(hourly[hour])
    print(f"{hour:02d}:00 — {count} blocks")
```

#### `get_velocity(hours: int = 24) → float`

Calculate recent velocity (blocks per hour).

**Args:** `hours` — Time window to analyze (default: 24)

**Returns:** Blocks per hour in the window

```python
velocity = parser.get_velocity(24)
print(f"Current velocity: {velocity:.1f} blocks/hour")
```

#### `forecast_blocks(forecast_hours: int, baseline_hours: int = 24) → int`

Forecast work blocks in next N hours based on recent velocity.

**Args:**
- `forecast_hours` — Hours to forecast
- `baseline_hours` — Hours to use as baseline (default: 24)

**Returns:** Predicted number of work blocks

```python
predicted = parser.forecast_blocks(12, 24)
print(f"Forecast (12h): {predicted} blocks")
```

## Data Classes

### `WorkBlock`

```python
@dataclass
class WorkBlock:
    number: int           # Work block number
    timestamp: datetime   # When it was logged
    title: str = ""       # Optional title
    content: str = ""     # Optional content
```

### `DailyMetrics`

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

## Dependencies

**None** — Pure Python standard library only.

## Integration

**Used by:**
- `analytics.py` — All 4 analytics commands
- `daily-report.py` — Daily summaries
- `goal-tracker.py` — Progress tracking
- Any tool that needs diary.md data

**Why it matters:**
- **Single source of truth** — All tools use same parsing logic
- **Consistent data** — No duplicate parsing code
- **Easy to extend** — Add new metrics in one place
- **Testable** — Library can be unit tested independently

## CLI (for testing)

The library includes a minimal CLI for testing:

```bash
python3 tools/diary_parser.py
```

Output:
```
Total work blocks: 1425

Top 5 tools:
  diary-digest.py: 42x
  moltbot-scorer.py: 38x
  goal-tracker.py: 31x
  revenue-tracker.py: 28x
  workspace-status.py: 24x

Days tracked: 4

Recent velocity: 44.2 blocks/hour
Forecast (12h): 530 blocks
```

## Design decisions

- **Caching** — Content loaded once, parsed on demand
- **Timezone-aware** — All timestamps in UTC
- **Regex-based** — Fast and flexible for unstructured diary format
- **Dataclasses** — Clean, typed API
- **No external deps** — Works everywhere Python 3.7+ is available
