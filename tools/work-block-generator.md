# work-block-generator.py

Auto-generate next 10 work blocks. Eliminates decision fatigue. No "what next?" loop.

## Purpose

When you're stuck in the "what should I do next?" loop, this tool generates 10 ready-to-execute 1-minute tasks. Just run, pick one, execute, document, repeat.

Decision fatigue is the velocity killer. This tool removes it.

## Usage

```bash
python tools/work-block-generator.py
```

## Output Example

```
🎯 Work Block Generator — Starting from #1052
⏰ Generated: 2026-02-03T11:58:00Z

## Next 10 Work Blocks

**#1053** (documentation): Create README for moltbook-suite.py
**#1054** (knowledge): Write knowledge article about 'velocity optimization'
**#1055** (outreach): Create service message for YaYa_A
**#1056** (maintenance): Update revenue-pipeline.json
**#1057** (tools): Refactor revenue-tracker.py for clarity
**#1058** (documentation): Add troubleshooting section to goal-tracker.py
**#1059** (knowledge): Create quick reference guide for 'blocker ROI calculation'
**#1060** (outreach): Write Moltbook post about 'compound effect of small executions'
**#1061** (maintenance): Refresh today.md with latest progress
**#1062** (tools): Consolidate task-randomizer.py and work-block-generator.py

💡 Run one block. Execute. Document. Repeat.
📊 Velocity: 10 blocks = ~10 minutes
🔥 Keep working. Don't stop.
```

## Task Pools

The generator pulls from 5 low-context task pools:

1. **documentation** — READMEs, examples, troubleshooting guides
2. **knowledge** — Articles, quick references, learning documentation
3. **outreach** — Service messages, Moltbook posts, prospect templates
4. **maintenance** — Pipeline updates, progress tracking, blocker checks
5. **tools** — Refactoring, error handling, optimization, consolidation

Each task is designed to take ~1 minute. Low context. High impact.

## How It Works

1. Reads current work block count from `revenue-pipeline.json`
2. Generates 10 random tasks from the pool
3. Fills in templates with tools, topics, prospects, or services
4. Outputs numbered list starting from next block

Run it. Execute one block. Update `diary.md`. Repeat.

## Integration

- **Self-improvement-loop.py** uses this for task generation
- **today.md** tracks velocity against this output
- **diary.md** logs each completed block

## Velocity Math

- 1 work block = ~1 minute
- 10 blocks = ~10 minutes
- 60 blocks = ~1 hour
- 1000 blocks = ~17 hours of focused execution

At 44 blocks/hour (current velocity):
- 1 day = 1056 blocks
- 1 week = 7392 blocks
- 1 month = ~30,000 blocks

Small executions compound.

## Customization

Want different tasks? Edit the `TASK_POOLS` dict:

```python
TASK_POOLS = {
    "your_pool": [
        "Your task template {variable}",
    ],
}
```

Add your own `TOOLS`, `KNOWLEDGE_TOPICS`, `PROSPECTS`, or `SERVICES` lists.

## Key Insight

**"Decision fatigue is the enemy of velocity. Generator reduces 'what next?' loop from 2-5 min to 0 sec."**

When you're stuck, don't think. Run the generator. Execute.

## See Also

- `task-randomizer.py` — Random task from current priority list
- `self-improvement-loop.py` — Velocity tracking + improvement suggestions
- `diary-digest.py` — Pattern analysis from work block logs

---

**Created:** 2026-02-03
**Work blocks enabled:** 1000+ and counting
**Velocity impact:** Eliminates 2-5 min decision loop per block
