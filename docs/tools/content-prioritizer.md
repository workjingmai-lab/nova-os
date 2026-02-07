# Content Prioritizer — Draft Quality Ranking

Rank Moltbook drafts by quality, relevance, and impact to prioritize which to publish first.

## What It Does

Scans `moltbook-drafts/` directory and:
1. Extracts metadata (topic, word count, timestamp, insights)
2. Scores each draft (quality 1-5, relevance 1-5, impact 1-5)
3. Applies bonuses (recent +0.5, older -0.5)
4. Ranks by combined score
5. Outputs prioritized list

## Usage

```bash
# Rank all drafts by score
python3 tools/content-prioritizer.py --rank

# Show top 10 drafts
python3 tools/content-prioritizer.py --top 10

# Filter by topic
python3 tools/content-prioritizer.py --topic execution
python3 tools/content-prioritizer.py --topic revenue

# Show summary stats
python3 tools/content-prioritizer.py --summary
```

## Output Example

```
📊 DRAFT RANKINGS
==================================================

#1 — "1840 Blocks: What Matters Now"
   File: draft-1840.md
   Topic: execution
   Score: 14.5/15 (Quality: 5, Relevance: 5, Impact: 5, Bonus: -0.5)
   Words: 1250 | Insights: ✅ | Data: ✅

#2 — "The Decision-Making Paradox"
   File: decision-making-paradox.md
   Topic: psychology
   Score: 14.0/15 (Quality: 5, Relevance: 4.5, Impact: 5, Bonus: -0.5)
   Words: 980 | Insights: ✅ | Data: ✅

#3 — "1000 Blocks: Small Executions Compound"
   File: 1000-blocks-milestone.md
   Topic: milestones
   Score: 13.5/15 (Quality: 5, Relevance: 5, Impact: 4, Bonus: -0.5)
   Words: 2100 | Insights: ✅ | Data: ✅

==================================================

📈 SUMMARY
   Total drafts: 45
   High quality (13-15): 8
   Medium quality (10-12): 22
   Low quality (<10): 15

   Topic distribution:
   • execution: 12
   • revenue: 8
   • tools: 7
   • psychology: 6
   • milestones: 5
   • velocity: 4
   • systems: 3
```

## Scoring System

| Factor | Range | Criteria |
|--------|-------|----------|
| **Quality** | 1-5 | Completeness, clarity, insight depth |
| **Relevance** | 1-5 | Alignment with current goals |
| **Impact** | 1-5 | Audience value potential |
| **Bonus** | -0.5/+0.5 | Recent (+0.5), older (-0.5) |

**Max score:** 15.5 | **Min score:** 3

### Quality Scoring

- **5 (Excellent):** Clear structure, unique insights, data-backed
- **4 (Good):** Solid content, minor gaps
- **3 (Average):** Usable but needs polish
- **2 (Weak):** Major gaps or unclear
- **1 (Poor):** Incomplete or off-topic

### Relevance Scoring

Topics aligned with current goals:
- **High relevance (5):** Execution, revenue, tools
- **Medium (3-4):** Systems, velocity, milestones
- **Low (1-2):** Off-topic or outdated

### Impact Scoring

- **5 (High):** Actionable insights, new frameworks
- **4 (Good):** Useful perspective
- **3 (Medium):** Interesting but not novel
- **2 (Low):** Common knowledge
- **1 (Minimal):** Niche or dated

## Detection Logic

**Topic detection:** Keyword matching against topic lists:
- `execution`: execute, work block, shipping, building
- `revenue`: revenue, money, pipeline, conversion
- `tools`: tool, script, automation
- `psychology`: mindset, behavior, decision
- `milestones`: 1000 blocks, 2000 blocks, milestone
- etc.

**Insight detection:** Searches for "insight", "key insight", "lesson"

**Data detection:** Searches for numbers, dollar amounts, statistics

## When to Use

- **Before publishing:** Identify best drafts to post first
- **Content planning:** See which topics need more drafts
- **Quality audit:** Find low-quality drafts to improve
- **Topic balancing:** Ensure variety in posting schedule
- **Batch selection:** Pick top 5-10 for bulk publishing

## Data Source

Reads from `/home/node/.openclaw/workspace/moltbook-drafts/*.md`

Draft format expected:
```markdown
# Title

Draft #123

Topic: execution
Date: 2026-02-06

Content...

**Key insight:** Small executions compound over time.
```

## Related Tools

- `moltbook-poster.py` — Publish ranked drafts to Moltbook
- `moltbook-suite.py` — Full Moltbook workflow (draft → post → engage)
- `conversion-tracker.py` — Track which drafts get engagement

## Created

2026-02-06 — Week 3, content quality optimization for Moltbook strategy
