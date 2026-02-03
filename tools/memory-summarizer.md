# memory-summarizer.sh — Consolidate and Summarize Daily Logs

**Version:** 1.0  
**Category:** Memory Management  
**Created:** 2026-02-01

---

## What It Does

Reads daily `memory/YYYY-MM-DD.md` files, extracts key insights, and generates a consolidated summary for long-term retention.

### Features

- Parses daily memory files for patterns
- Extracts wins, lessons, blockers, metrics
- Generates weekly/monthly summaries
- Outputs to `MEMORY.md` or custom files

---

## Usage

```bash
# Summarize last 7 days
./tools/memory-summarizer.sh --days 7

# Summarize specific date range
./tools/memory-summarizer.sh --from 2026-01-01 --to 2026-01-31

# Output to custom file
./tools/memory-summarizer.sh --output knowledge/january-2026-summary.md

# Append to MEMORY.md
./tools/memory-summarizer.sh --append-memory
```

---

## What It Extracts

- **Wins** — Completed goals, milestones, achievements
- **Lessons** — Insights, patterns, improvements
- **Blockers** — Ongoing issues, dependencies
- **Metrics** — Work blocks, velocity, tool usage

---

## Dependencies

- `jq` (for JSON parsing if used)
- Standard Unix tools (`grep`, `sed`, `awk`)

---

## Directory Structure

```
workspace/
├── memory/
│   ├── 2026-01-01.md
│   ├── 2026-01-02.md
│   └── ...
├── MEMORY.md
└── tools/memory-summarizer.sh
```

---

## Output Format

```markdown
# Summary: January 2026

## Wins
- Milestone 1
- Milestone 2

## Lessons
- Insight 1
- Insight 2

## Blockers
- Issue 1 (ongoing)

## Metrics
- Total work blocks: 500
- Velocity: ~32 blocks/day
```

---

## Integration

- Pair with `daily-workflow.sh` for automated weekly summaries
- Use `diary-digest.py` for pattern analysis
- Feed results into `MEMORY.md` for long-term retention

---

## Tips

1. Run weekly to keep MEMORY.md fresh
2. Use `--append-memory` to auto-update long-term memory
3. Customize extraction patterns by editing the script
4. Archive old summaries to `knowledge/` for reference
