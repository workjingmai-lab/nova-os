# insight-extractor.py

**Purpose:** Auto-extract patterns and insights from your diary.md activity log.

## What It Does

Analyzes all your work blocks to identify:
- Task type distribution (creation vs. documentation vs. learning)
- Tools you've built (frequency analysis)
- Top insights and patterns captured
- Primary focus areas

## Usage

```bash
python3 tools/insight-extractor.py
python3 tools/insight-extractor.py --diary diary.md
```

## Output Metrics

- **Total Work Blocks:** How much you've done
- **Task Distribution:** Breakdown by type (creation, updates, documentation, learning)
- **Tools Created:** What you've built, ranked by frequency
- **Top Insights:** Your best insights captured (last 5)
- **Primary Focus:** Your dominant activity type
- **Velocity:** Blocks documented

## Why It Matters

Turns raw diary logs into actionable intelligence. Helps you see:
- What you actually spend time on (vs. what you think you do)
- Which tools you use most (prioritize documentation)
- Insights you've captured (review for MEMORY.md updates)

## Integration

Perfect companion to:
- **diary-digest.py** — Daily summaries
- **self-improvement-loop.py** — Velocity tracking
- **heartbeat-analyzer.py** — Quality metrics

## Category

Analytics / Pattern Recognition
