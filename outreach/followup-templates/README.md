# Follow-Up Templates

**5-touch sequence over 14 days**

## Usage

Copy templates to target-specific files:
```bash
# DAO outreach
cp day-03-value-add.md outreach/followups/lido-dao-day3.md
cp day-07-question.md outreach/followups/lido-dao-day7.md

# Customize each with:
- Target name
- Specific pain point
- Relevant insight/case study
```

## Sequence Structure

| Day | Type | Purpose | Response Rate |
|-----|------|---------|---------------|
| 0 | Initial | Value message | 20% |
| 3 | Value-add | Insight, article, case study | 15% |
| 7 | Question | "Thoughts?", "Questions?" | 10% |
| 10 | New angle | Different perspective | 8% |
| 14 | Breakup | Close the loop | 15-25% |

**Expected total response rate:** 50-60% (vs 20% with single message)

## Tracking

Update revenue tracker after each touch:
```bash
python3 tools/revenue-tracker.py update services \
  --name "Lido DAO Governance" \
  --notes "Day 3 follow-up sent 2026-02-07"
```

## Templates

1. **day-03-value-add.md** — Share relevant insight/case study
2. **day-07-question.md** - Engagement question
3. **day-10-new-angle.md** — Different problem angle
4. **day-14-breakup.md** — Close the loop (highest response rate)

**Key:** Always add value. Never "just checking in."
