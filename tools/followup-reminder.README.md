# Follow-up Reminder System

Track sent messages and schedule follow-ups (Day 0/3/7/14/21).

## Usage

```bash
# Check follow-ups due today
python3 tools/followup-reminder.py check

# List all scheduled follow-ups
python3 tools/followup-reminder.py list

# Add a message with follow-up schedule
python3 tools/followup-reminder.py add "Lead Name" "2026-02-06"

# Auto-schedule from pipeline (for all "submitted" leads)
python3 tools/followup-reminder.py schedule
```

## How It Works

1. **Track sent messages** — Each message gets a follow-up sequence (Day 0/3/7/14/21)
2. **Check daily** — Run `check` to see what's due today
3. **Mark complete** — Update tracker.json when follow-ups are done
4. **Auto-schedule** — Sync with revenue-pipeline.json for "submitted" leads

## Follow-up Schedule

- **Day 0:** Initial send confirmation
- **Day 3:** "Any thoughts?" check-in
- **Day 7:** Value add (article, insight)
- **Day 14:** "Still interested?" nudge
- **Day 21:** Final follow-up before archive

## Data Files

- `outreach/follow-up-tracker.json` — Main tracker
- `revenue-pipeline.json` — Pipeline status sync

## Templates

Follow-up templates live in `outreach/templates/followup-*.md`:
- `followup-day0.md` — Send confirmation
- `followup-day3.md` — Quick check-in
- `followup-day7.md` — Value add
- `followup-day14.md` — Interest check
- `followup-day21.md` — Final follow-up

## Integration

Use with other tools:
- `service-batch-send.py` — Auto-schedules follow-ups after sending
- `revenue-tracker.py` — Syncs pipeline status
- `follow-up-tracker.py` — Full follow-up management

## Why Follow-ups Matter

80% of sales happen after 5+ touchpoints. Most agents send once and forget.
Follow-up system = no leads slip through cracks.

**Stats:**
- 48% of sales people never follow up
- 80% of sales happen on 5th-12th contact
- Follow-up sequences = 3× higher conversion

**Workflow:**
1. Send message (Day 0)
2. Check daily for due follow-ups
3. Send follow-up using template
4. Mark complete in tracker
5. Repeat until response or Day 21

---

**Created:** 2026-02-06
**Work Block:** 2711
**Tags:** follow-up, automation, pipeline, sales
