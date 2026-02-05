# followup-helper.py — Follow-Up Management Tool

**Purpose:** Track and manage follow-ups for revenue pipeline. Checks pipeline for items needing follow-up, suggests templates, logs attempts.

---

## Quick Start

```bash
# Check who needs follow-up today
python3 tools/followup-helper.py check

# Generate follow-up message (logs it)
python3 tools/followup-helper.py send --name "Lido DAO" --type value-add

# Preview without logging
python3 tools/followup-helper.py send --name "Lido DAO" --type clarification --dry-run

# Log response to follow-up
python3 tools/followup-helper.py respond --name "Lido DAO" --response interested

# Show statistics
python3 tools/followup-helper.py stats
```

---

## Features

### `check` — Identify Follow-Up Opportunities

Scans pipeline JSON for submitted items needing follow-up based on days since submission.

**Rules:**
- **Day 3-4:** Suggest `clarification` follow-up (high urgency)
- **Day 7-10:** Suggest `value-add` follow-up (normal urgency)
- **Day 14+:** Suggest `close` follow-up (low urgency)
- **Day 30+:** Suggest `archive` (stale lead)

**Output:**
```
📧 3 items need follow-up:

🔴 **Gitcoin GR20** (grants)
   Potential: $5,000
   Days since submission: 4
   Suggested action: clarification
   Template: `followup-helper.py send --name 'Gitcoin GR20' --type clarification`
```

### `send` — Generate Follow-Up Message

Generates personalized follow-up message using templates and logs it to pipeline.

**Templates:**
- `clarification` — "Any questions I can clarify?"
- `value-add` — "Saw your post about [topic], great insight!"
- `close` — "Should I close the loop on this?"
- `news` — "Saw the news about [event], seems relevant."

**Features:**
- Auto-fills placeholders (name, date, proposal type)
- Logs follow-up to pipeline JSON (followUps array)
- Calculates next follow-up date (adds 4/7/14 days)
- Updates pipeline item status

### `respond` — Log Response

Logs response from prospect to track conversion rates.

**Response types:**
- `interested` — Warm lead, keep pursuing
- `not_interested` — Cold lead, archive or learn why
- `replied` — Response received, unclear interest
- `none` — No response yet

### `stats` — View Statistics

Shows follow-up metrics:
- Total follow-ups sent
- Responses received
- Response rate (%)

---

## Data Files

| File | Purpose |
|------|---------|
| `data/revenue-pipeline.json` | Pipeline data (read/write) |
| `data/followups.json` | Follow-up log (all attempts) |

---

## Pipeline JSON Structure

The tool reads/writes this structure in `revenue-pipeline.json`:

```json
{
  "services": [
    {
      "name": "Lido DAO Governance",
      "status": "submitted",
      "potential": 32500,
      "submittedDate": "2026-02-01",
      "followUps": [
        {
          "date": "2026-02-04T14:30:00",
          "type": "clarification",
          "response": "replied"
        }
      ],
      "nextFollowUp": "2026-02-11"
    }
  ]
}
```

---

## Workflow

**Daily Routine:**
1. Run `followup-helper.py check`
2. Send follow-ups for high-urgency items first
3. Log responses as they come in
4. Review `stats` weekly to optimize

**Best Practices:**
- Follow up within 24 hours of response
- Always add value (no generic "checking in")
- Max 3-4 follow-ups before archiving
- Track what works (which templates get responses)

---

## Dependencies

None. Uses Python standard library only (`json`, `argparse`, `datetime`, `pathlib`).

---

## See Also

- `knowledge/art-of-following-up.md` — Follow-up methodology
- `tools/revenue-tracker.py` — Pipeline management
- `knowledge/revenue-pipeline-management.md` — Pipeline guide
