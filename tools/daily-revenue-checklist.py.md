# daily-revenue-checklist.py

Automated daily revenue routine with pipeline status, follow-ups, and action items.

## What It Does

Runs daily checks:
1. **Pipeline status** — Overall pipeline health and execution gap
2. **Follow-ups due** — Leads needing follow-up today
3. **Lead priorities** — Pending messages by priority tier
4. **Moltbook presence** — Content and engagement targets
5. **Today's actions** — Priority-ordered action list

## Usage

```bash
# Full report
python3 tools/daily-revenue-checklist.py

# Just actions (quiet mode)
python3 tools/daily-revenue-checklist.py --quiet
```

## Output Sections

### Pipeline Status
- Total pipeline value
- Ready vs submitted breakdown
- Execution gap calculation
- Critical alerts if gap > $500K

### Follow-Ups Due
- Lists leads needing follow-up today
- Shows touch number and days since last contact
- Priority flags (🔴 HIGH, 🟡 MEDIUM)

### Lead Priorities
- Pending messages by tier
- Value at each priority level
- Action recommendations

### Moltbook Presence
- Posts this week vs target
- Engagement recommendations

### Today's Actions
Priority-ordered list with:
- Priority level (CRITICAL, HIGH, MEDIUM)
- Action description
- Expected value
- Time required

## When to Run

**Daily (morning):** Start day with clear priorities
**Weekly (Monday):** Plan week's revenue focus
**Before Arthur sync:** Quick status overview

## Related Tools

- `pipeline-viz.py` — Visual pipeline dashboard
- `follow-up-reminder.py` — Detailed follow-up tracking
- `lead-prioritizer.py` — Lead ranking and details
- `revenue-tracker.py` — Full pipeline management

## Integration

Add to daily routine:
```bash
# Morning check
python3 tools/daily-revenue-checklist.py

# Quick action view
python3 tools/daily-revenue-checklist.py --quiet
```
