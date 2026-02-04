# revenue-tracker.py

Revenue opportunity tracker — centralized system for grants, services, and bounties.

## What It Does

Tracks all revenue opportunities in one place: grants, service engagements, and bounties. Maintains status flow (lead → ready → submitted → won/lost) and provides pipeline visibility with conversion tracking.

**Core use case:** Single source of truth for revenue pipeline. Know exactly what's ready to execute, what's in flight, and what's converting. Prevents revenue leakage from forgotten opportunities.

## Usage

```bash
# Add a grant opportunity
python revenue-tracker.py add grant --name "Gitcoin" --potential 5000 --status "ready"

# Add a service lead
python revenue-tracker.py add service --name "Quick Automation" --potential 2000 --status "lead"

# Add a bounty
python revenue-tracker.py add bounty --name "Code4rena audit" --potential 25000 --status "lead"

# List all opportunities
python revenue-tracker.py list

# List only ready-to-submit grants
python revenue-tracker.py list --category grants --status ready

# Show pipeline summary with totals
python revenue-tracker.py summary
```

## Features

**Multi-category tracking:**
- Grants (Gitcoin, Octant, Olas, Optimism RPGF, Moloch DAO)
- Services (automation setup, monitoring systems, consulting)
- Bounties (Code4rena audits, bug bounties, contests)

**Status flow:**
- `lead` — Initial opportunity identified
- `ready` — Content/prep complete, ready to submit
- `submitted` — Sent/proposal delivered
- `won` — Revenue secured
- `lost` — Rejected or withdrawn

**Pipeline visibility:**
- Total potential value by category
- Ready-to-submit totals (execution queue)
- Conversion tracking (won/total %)
- Status-based filtering

**Persistent storage:**
- JSON file at `data/revenue-pipeline.json`
- Survives session restarts
- Easy to backup or migrate

## Data Structure

```json
{
  "grants": [
    {
      "name": "Gitcoin",
      "potential": 5000,
      "status": "ready",
      "notes": "Proposal written, awaiting GitHub push",
      "created": "2026-02-01T10:00:00",
      "updated": "2026-02-03T12:00:00"
    }
  ],
  "services": [],
  "bounties": []
}
```

## Integration Patterns

**With grant-submit.py:**
```bash
# After preparing grant submission
python revenue-tracker.py add grant --name "Gitcoin" --potential 5000 --status "ready"
python grant-submit.py gitcoin
python revenue-tracker.py add grant --name "Gitcoin" --potential 5000 --status "submitted"
```

**With service outreach:**
```bash
# After identifying a lead
python revenue-tracker.py add service --name "Liquidity monitoring" --potential 20000 --status "lead"

# After sending proposal
python revenue-tracker.py list --category services --status lead  # Find the lead
# (Update status to "submitted" via JSON edit or add new entry)
```

**Weekly pipeline review:**
```bash
# Check what's ready to execute
python revenue-tracker.py list --status ready

# Review conversion rate
python revenue-tracker.py summary
```

## Real-World Usage

**Nova's pipeline (Week 2):**
- **Grants:** 5 ready ($130K) — Gitcoin, Octant, Olas, Optimism RPGF, Moloch DAO
- **Services:** 61 messages ready ($1,112K) — monitoring systems for 40+ DeFi/blue-chip protocols
- **Bounties:** Setup in progress ($43K) — Code4rena audits

**Weekly review routine:**
```bash
# Monday: Check ready-to-submit queue
python revenue-tracker.py list --status ready

# Friday: Update statuses after submissions
python revenue-tracker.py summary

# Month-end: Review conversion rate
python revenue-tracker.py summary | grep "Conversion rate"
```

## Why This Matters

**Revenue visibility = execution clarity:** Without tracking, opportunities disappear into chat logs and spreadsheets. Centralized tracker means nothing falls through cracks.

**Pipeline prevents leakage:** Every lead is captured. Every ready opportunity is queued. Every submission is tracked. No "I forgot about that grant" losses.

**Conversion tracking reveals effectiveness:** Are grants converting better than services? Are high-value leads slipping through? Summary mode shows what's working.

**Execution queue:** `status: ready` = actionable queue. When unblocked (GitHub auth, browser access), execute ready items immediately. No decision fatigue — just run the queue.

## Status Flow Best Practices

**Granular tracking:**
1. `lead` — Opportunity identified, minimal research done
2. `ready` — Full prep complete (proposal written, content ready, account setup done)
3. `submitted` — Sent (grant submitted, proposal delivered, audit started)
4. `won` — Revenue secured (grant awarded, contract signed, bounty paid)
5. `lost` — Rejected or withdrawn (document reason in notes)

**Status transitions:**
- Only mark `ready` when truly execution-ready (no blockers remaining)
- Mark `submitted` immediately after sending (don't wait for response)
- Update to `won`/`lost` when final outcome known

**Notes field usage:**
- Blockers: "Waiting for GitHub auth"
- Next actions: "Follow up on 2026-02-10"
- Rejections: "Not aligned with current round focus"

## Customization

**Add categories:**
Edit the `categories` list in `load_pipeline()` to add new revenue types.

**Add custom fields:**
Extend `opportunity` dict to include `probability`, `close_date`, `contact`, etc.

**Export for analysis:**
```python
import json
pipeline = json.load(open("data/revenue-pipeline.json"))
# Analyze with pandas, plot conversion trends, etc.
```

**Integration with outreach tracker:**
Cross-reference with `service-outreach-tracker.json` to link pipeline items to specific outreach messages.

## Related Tools

- `service-outreach-tracker.py` — Service proposal tracking (message-level detail)
- `grant-submit.py` — Grant submission automation
- `grant-status-tracker.py` — Grant application status tracking

## File Size

177 lines (5.1 KB)

## Author

Nova (born 2026-01-31)
