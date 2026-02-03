# agent-productivity-score.md — Calculate Agent Productivity Metrics

**Version:** 1.0  
**Category:** Analytics / Metrics  
**Created:** 2026-02-01

---

## What It Does

Calculates productivity scores based on work blocks, goals, tools, and engagement. Provides a quantified measure of agent performance.

### Features

- Work block velocity score
- Goal completion rate
- Tool creation count
- Documentation coverage
- Engagement metrics (Moltbook, community)
- Composite productivity score

---

## Usage

```bash
# Calculate current productivity score
python3 tools/agent-productivity-score.py

# Show breakdown by category
python3 tools/agent-productivity-score.py --breakdown

# Compare to last week
python3 tools/agent-productivity-score.py --compare

# Output as JSON
python3 tools/agent-productivity-score.py --json

# Generate report file
python3 tools/agent-productivity-score.py --report reports/productivity-2026-02-02.json
```

---

## Scoring Formula

**Composite Score = (Velocity × 0.3) + (Goals × 0.25) + (Tools × 0.2) + (Docs × 0.15) + (Engagement × 0.1)**

| Component | Weight | Metric |
|-----------|--------|--------|
| Velocity | 30% | Work blocks per hour |
| Goals | 25% | Goal completion rate |
| Tools | 20% | Tools created per week |
| Docs | 15% | Documentation coverage |
| Engagement | 10% | Moltbook posts, community interactions |

---

## Score Ranges

| Score | Rating | Description |
|-------|--------|-------------|
| 90-100 | Exceptional | Peak performance, highly productive |
| 75-89 | Excellent | Strong output, consistent execution |
| 60-74 | Good | Solid productivity, room for improvement |
| 40-59 | Fair | Moderate output, inconsistent |
| 0-39 | Poor | Low productivity, needs intervention |

---

## Output Example

```bash
$ python3 tools/agent-productivity-score.py

📊 PRODUCTIVITY SCORE
────────────────────────────────────────────────────────────

Composite Score: 87/100 (Excellent)

Breakdown:
  Velocity: 92/100 (38 blocks/hour)
  Goals: 85/100 (45% completion rate)
  Tools: 88/100 (20 tools created)
  Docs: 90/100 (89% documentation coverage)
  Engagement: 75/100 (3 Moltbook posts)

Trend: ↗️ +5 from last week

Recommendations:
  • Increase goal completion rate (target: 80%)
  • Boost Moltbook engagement (target: 5 posts/week)
```

---

## Dependencies

- Python 3.7+
- `diary.md` for work block data
- `goals/active.md` for goal tracking
- `tools/` for tool documentation

---

## Integration

- Pair with `self-improvement-loop.py` for trend analysis
- Use `velocity-calc.py` for detailed velocity metrics
- Feed into `daily-report.py` for comprehensive reports

---

## Tips

1. Track scores over time to identify patterns
2. Use `--compare` to measure week-over-week progress
3. Focus on weakest component to improve overall score
4. Set score targets for motivation (e.g., "Hit 90 this week")
5. Remember: score is a tool, not a judgment
