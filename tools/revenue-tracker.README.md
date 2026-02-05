# revenue-tracker.py — Pipeline Visibility & Follow-Up Tool

**Purpose:** Single source of truth for all revenue opportunities across grants, services, and bounties. Track pipeline status + automated follow-up reminders.

## Why This Matters

You can't improve what you don't measure. revenue-tracker creates a clear, JSON-based pipeline that tracks every opportunity from lead → won/lost, with follow-up reminders so nothing falls through the cracks.

## What It Does

- **Pipeline Tracking:** Track revenue across 3 channels (grants, services, bounties)
- **Status Progression:** Records status changes (lead → ready → submitted → won/lost)
- **Follow-Up Reminders:** Shows which opportunities need follow-up based on Day 0/3/7/14/21 schedule
- **Contact Logging:** Record when you reach out to prospects
- **Pipeline Summary:** Calculate total value, conversion rates, and blockers

## Usage

```bash
# Add a new opportunity
python3 tools/revenue-tracker.py add service --name "Quick Automation" --potential 2000 --status "lead"

# Update status
python3 tools/revenue-tracker.py update services --name "Quick Automation" --status "ready"

# List all opportunities (filter by category/status)
python3 tools/revenue-tracker.py list --category services --status ready

# Show pipeline summary
python3 tools/revenue-tracker.py summary

# Show follow-up reminders (Day 0/3/7/14/21 schedule)
python3 tools/revenue-tracker.py followup

# Record a contact/follow-up
python3 tools/revenue-tracker.py contact services --name "Quick Automation"
```

## Quick Start Example

**Scenario:** You discover a new DAO that needs automation services ($20K potential).

**Step 1:** Add opportunity
```bash
python3 tools/revenue-tracker.py add service --name "Balancer DAO" --potential 20000 --status "lead"
# Output: ✅ Added service: Balancer DAO ($20,000)
#         Services pipeline total: $585,000
```

**Step 2:** Move to ready when message is prepared
```bash
python3 tools/revenue-tracker.py update services --name "Balancer DAO" --status "ready"
# Output: ✅ Updated service: Balancer DAO
#         Status: ready | Potential: $20,000
```

**Step 3:** Send outreach and record contact
```bash
python3 tools/revenue-tracker.py contact services --name "Balancer DAO"
# Output: ✅ Contact recorded for service: Balancer DAO
```

**Step 4:** Check follow-ups
```bash
python3 tools/revenue-tracker.py followup
# Shows all opportunities needing follow-up on Day 0/3/7/14/21
```

## Status Values

- **lead:** Initial opportunity identified
- **ready:** Outreach message prepared, ready to send
- **submitted:** Proposal/grant application sent
- **won:** Revenue secured
- **lost:** Opportunity declined or unresponsive

## Follow-Up Schedule

The `followup` command shows opportunities needing follow-up based on the Day 0/3/7/14/21 schedule:

- **Day 0:** Initial contact (when you first reach out)
- **Day 3:** Quick follow-up (still fresh)
- **Day 7:** One-week check-in
- **Day 14:** Two-week follow-up
- **Day 21:** Final touch point

This prevents "one-and-done" outreach and maximizes conversion rates.

## Pipeline Summary

The `summary` command shows:
- Total pipeline value (all categories)
- Value by category (grants, services, bounties)
- Ready vs submitted vs won amounts
- Conversion rate percentage

**Example output:**
```
💰 REVENUE PIPELINE SUMMARY
============================================================

SERVICES:
  Total items: 37
  Potential: $585,000
  Ready to submit: $152,000
  Submitted: $0
  Won: $0

GRANTS:
  Total items: 5
  Potential: $130,000
  Ready to submit: $125,000
  Submitted: $5,000
  Won: $0

============================================================
TOTAL PIPELINE: $715,000
WON: $0
Conversion rate: 0.0%
```

## Data Storage

All data is stored in `data/revenue-pipeline.json` (JSON format, easily parseable by other tools).

**Structure:**
```json
{
  "grants": [
    {
      "name": "Gitcoin",
      "potential": 50000,
      "status": "ready",
      "notes": "Application materials prepared",
      "created": "2026-02-04T12:00:00",
      "updated": "2026-02-04T12:00:00",
      "last_contacted": "2026-02-04T12:00:00"
    }
  ],
  "services": [...],
  "bounties": [...]
}
```

## Real-World Impact

**Nova's Pipeline (Feb 4, 2026):**
- Total: $715K tracked across 42 opportunities
- Services: $585K ($152K ready NOW, zero blockers)
- Grants: $130K ($125K blocked by GitHub auth)
- Bounties: $50K (blocked by browser access)

**Visibility = Execution**
- Without this tool: "Some opportunities maybe?"
- With this tool: "$715K tracked, $152K ready, 2 blockers identified"
- Follow-ups: "22 due today (Day 0), 5 upcoming in next 7 days"

## Integration Points

- **revenue-tracker.py:** CLI tool for pipeline management
- **data/revenue-pipeline.json:** Single source of truth
- **follow-up-reminder.py:** Complementary tool for follow-up templates
- **lead-prioritizer.py:** Ranks opportunities by priority/value

## Best Practices

1. **Update after every action:** Change status when you create/send/submit
2. **Record contacts:** Use `contact` command when you reach out
3. **Check follow-ups daily:** Run `followup` command to see what's due
4. **Review weekly:** Use `summary` to track conversion rates

## See Also

- `tools/follow-up-reminder.py` — Follow-up message templates
- `tools/lead-prioritizer.py` — Priority-based lead sorting
- `knowledge/revenue-pipeline-management-for-agents.md` — Full methodology

---

**Created:** 2026-02-04
**Updated:** 2026-02-04 — Added follow-up reminder system
**Purpose:** Pipeline visibility + automated follow-ups = higher conversion
