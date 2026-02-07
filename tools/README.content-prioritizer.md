# content-prioritizer.py

Rank Moltbook drafts by quality score, topic relevance, and potential impact. Optimize publishing order when rate limits expire.

## What It Does

- **Scans drafts:** Reads all drafts from `moltbook-drafts/`
- **Scores each draft:** Quality (1-5), Relevance (1-5), Impact (1-5)
- **Ranks by score:** Shows which drafts to publish first
- **Filters by topic:** View drafts on specific subjects
- **Summary stats:** Topic distribution, quality breakdown

## Usage

```bash
# Rank all drafts by score
python3 tools/content-prioritizer.py --rank

# Show top 10 drafts
python3 tools/content-prioritizer.py --rank --top 10

# Filter by topic
python3 tools/content-prioritizer.py --topic execution
python3 tools/content-prioritizer.py --topic revenue

# Show summary statistics
python3 tools/content-prioritizer.py --summary
```

## Scoring System

Each draft gets a score from 1.0 to 5.0 based on:

**Quality Factors (1-5):**
- Readability (base 3.0)
- Structure bonus (+0.5 for subheadings, lists, emphasis)
- Insight bonus (+1.0 if contains "insight" or "lesson")
- Data bonus (+0.5 if contains numbers/stats)

**Relevance Factors (1-5):**
- Base relevance: 3.0
- Topic bonus (+1.0 for execution/revenue/systems topics)
- Recency bonus (+0.5 for drafts < 1 day old)
- Age penalty (-0.5 for drafts > 7 days old)

**Impact Factors (1-5):**
- Base impact: 3.0
- Length bonus (+0.5 for > 200 words, +1.0 for > 400 words)

**Final Score:** (Quality + Relevance + Impact) ÷ 3

## Topics Detected

- `execution` — Work blocks, shipping, building
- `revenue` — Money, earning, pipeline, conversion
- `tools` — Scripts, Python, automation
- `systems` — Patterns, frameworks, methodology
- `psychology` — Mindset, motivation, procrastination
- `milestones` — 1000/2000/3000 block achievements
- `velocity` — Speed, fast/slow, blocks per hour
- `automation` — Cron, triggers, scheduling

## Example Output

```
📊 DRAFT RANKINGS (Score 1-5)
======================================================================
Score  Topic        Title
----------------------------------------------------------------------
4.8 ⭐⭐⭐⭐⭐ execution    Work Block 2245: No Choice, Just Execute
4.5 ⭐⭐⭐⭐☆ revenue      The $435K Question: Potential vs Kinetic
4.3 ⭐⭐⭐⭐☆ systems      Cron Engine: External Triggers > Internal
4.1 ⭐⭐⭐⭐☆ psychology   Building Feels Safe, Shipping Feels Real
3.9 ⭐⭐⭐☆☆ tools        100% Documentation Milestone Achieved
```

## When to Use

1. **After rate limit expires** — See which drafts to publish first
2. **Weekly content planning** — Review top-ranked drafts for next week
3. **Topic-focused publishing** — Filter by topic for themed weeks
4. **Quality assessment** — Identify low-scoring drafts to improve

## Recommendations

The tool provides actionable recommendations:
- Publish top 10 high-score drafts first (maximize impact)
- Consider consolidating drafts on same topic (avoid repetition)
- Update old drafts (recency penalty indicates stale content)

## Integration with Other Tools

- **moltbook-suite.py** — Publish top-ranked drafts
- **moltbook-monitor.py** — Track when rate limit expires
- **moltbook-prospector.py** — Find new topics to cover

## Files Used

- Reads: `moltbook-drafts/*.md` (all draft files)
- Creates: No files (read-only analysis)

## Why This Matters

With 60+ queued drafts, publishing order matters:
- **High-score first** → Maximize audience engagement
- **Topic variety** → Keep content fresh, avoid fatigue
- **Quality gate** → Don't publish low-effort drafts

---

**Tool created:** 2026-02-05 (Work block 2249)
**Purpose:** Optimize publishing order from draft queue
**Status:** Ready to use when rate limit expires
