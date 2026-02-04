# diary-digest.py - Activity Summary Generator

Convert raw diary.md logs into structured daily, weekly, and monthly summaries.

## Why It Matters

**Raw logs are noise; digests are signal.** After 1431 work blocks, diary.md is 50K+ lines. Finding patterns requires synthesis, not scrolling. This tool compresses noise into actionable insights.

## Usage

### Generate Daily Summary

```bash
python tools/diary-digest.py daily
```

**Output:** Yesterday's work blocks, top achievements, patterns found

### Generate Weekly Summary

```bash
python tools/diary-digest.py weekly
```

**Output:** Week's velocity, top tools used, trends, blockers

### Generate Monthly Summary

```bash
python tools/diary-digest.py monthly
```

**Output:** Month's growth, peak productivity periods, major milestones

## How It Works

1. **Parses diary.md** - Extracts work blocks with timestamps
2. **Groups by period** - Daily/weekly/monthly buckets
3. **Counts activity** - Tools used, tasks completed, insights generated
4. **Formats output** - Human-readable summary with metrics

## Example Output

```
📊 DAILY DIGEST — 2026-02-03

Work Blocks: 317
Velocity: ~44 blocks/hour
Top Tasks:
  • Documentation (16 READMEs created)
  • Revenue tracking ($302K pipeline)
  • Tool consolidation analysis

Insights:
  • Decision fatigue is velocity bottleneck
  • Documentation coverage: 26.8% (32/119 tools)
```

## Key Features

- **Zero config** - Just run it, it finds diary.md
- **Pattern detection** - Identifies trends over time
- **Metric tracking** - Velocity, task distribution, focus areas
- **Actionable output** - Not just data, but what to do next

## See Also

- `diary.md` - Raw activity logs (source data)
- `tools/pattern-analyzer.py` - Detect anomalies/trends
- `knowledge/1000-work-blocks-milestone.md` - What 1000 blocks built
