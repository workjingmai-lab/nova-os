# revenue-progress-tracker.py

**Monitor revenue pipeline execution progress after unblocking.**

## What It Does

Tracks and displays revenue pipeline status with:
- **Blocker detection:** GitHub auth, browser access, message review status
- **Progress calculation:** Submission rate, win rate, pipeline totals
- **Category breakdown:** Grants, services, bounties with individual item status
- **Visual progress bar:** ASCII art showing submitted vs won
- **Next actions:** Context-aware recommendations based on blocker status

## When to Use

- **Pipeline monitoring:** Check revenue execution status at a glance
- **Unblock verification:** Confirm blockers are cleared before execution
- **Watch mode:** Continuous monitoring during submission sprints
- **Category focus:** Filter by grants, services, or bounties

## Usage

```bash
# Full progress report
python3 tools/revenue-progress-tracker.py

# Grants only
python3 tools/revenue-progress-tracker.py --grants

# Services only
python3 tools/revenue-progress-tracker.py --services

# Bounties only
python3 tools/revenue-progress-tracker.py --bounties

# Watch mode (refresh every 30s)
python3 tools/revenue-progress-tracker.py --watch
```

## Output

```
============================================================
💰 REVENUE PROGRESS TRACKER
============================================================
📅 Generated: 2026-02-03 05:48:00 UTC

🔧 BLOCKER STATUS:
   GitHub Auth: ⏸️ Blocked
   Browser Access: ⏸️ Blocked
   Messages Reviewed: ⏸️ Pending

📊 OVERALL PROGRESS:
   Total Pipeline: $302,000
   Submitted: $0 (0.0%)
   Won: $0 (0.0%)
   [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░]

🎯 GRANTS ($130,000)
   🟢 Gitcoin: $5,000 (ready)
   🟢 Octant: $15,000 (ready)
   🟢 Olas: $10,000 (ready)
   🟢 Optimism RPGF: $50,000 (ready)
   🟢 Moloch DAO: $50,000 (ready)

💼 SERVICES ($122,000)
   🔵 SEMI: $25,000 (lead)
   ...

🚀 NEXT ACTIONS:
   ⏸️  Run 'gh auth login' to unblock $130K grants
   ⏸️  Review outreach/messages/ to unblock $2K services
   ⏸️  Restart gateway to unblock $50K bounties

============================================================
```

## Status Icons

- 🔵 **Lead:** Initial opportunity identified
- 🟢 **Ready:** Prepared and ready to submit
- 🟡 **Submitted:** Sent, awaiting response
- ✅ **Won:** Revenue secured
- ❌ **Lost:** Opportunity declined
- ⏸️ **Blocked:** External dependency blocking execution

## Progress Bar Format

```
[█████████▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░]
  ^^^^^^^^  ^^^^^^  ^^^^^^^^^^^^^^^^^^^
  Won      Submit  Not started
```

## Watch Mode

Continuous monitoring mode refreshes every 30 seconds:

```bash
python3 tools/revenue-progress-tracker.py --watch
```

Press `Ctrl+C` to exit watch mode.

## Integration

- Reads from `data/revenue-pipeline.json`
- Works with `grant-submit.py` for grant submissions
- Pairs with `service-outreach-tracker.py` for services
- Complements `revenue-tracker.py` (pipeline tracker vs progress tracker)

## Blocker Checks

### GitHub Auth
Checks `gh auth status` to verify CLI authentication.

### Browser Access
Placeholder for gateway browser service status check.

### Messages Reviewed
Placeholder for outreach message approval workflow.

## Status

✅ Working — Ready for pipeline monitoring
