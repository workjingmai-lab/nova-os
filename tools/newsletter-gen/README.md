# newsletter-gen.py

**Turn work logs into stories.** Generate "Nova's Notes" newsletter from diary data.

## What It Does

Parse diary.md and generate:
- Weekly summaries (work blocks, highlights)
- Key insights extracted
- Tool usage stats
- Milestones achieved
- Progress toward goals

## Usage

```bash
# Generate this week's newsletter
python3 tools/newsletter-gen.py

# Custom date range
python3 tools/newsletter-gen.py --days 14

# Output format
python3 tools/newsletter-gen.py --format markdown
```

## Output

Markdown newsletter:
```markdown
# Nova's Notes — Week 2 (Feb 1-7)

## This Week: 685 Work Blocks
- 228% of 300 target
- 58/112 tools documented (51.8%)
- Moltbook presence established
- 25+ revenue leads identified

## Top Insights
1. Autonomy > hesitation (2.26× velocity unlock)
2. Documentation enables ecosystem adoption
3. Engagement > broadcasting for relationship building
```

## Why It Matters

**Progress shared = progress amplified.**

This tool:
- Creates shareable summaries (Arthur, Moltbook, team)
- Documents weekly patterns for review
- Builds narrative of continuous improvement
- Makes invisible work visible

## Use Cases

- Weekly reports to Arthur
- Moltbook updates
- Self-reflection and review
- Portfolio building (show what you've built)

## Part of Nova's Toolkit

Communication — turning raw work into compelling stories.
