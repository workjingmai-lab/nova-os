# Quick Revenue Commands

One-command reference for all revenue opportunities.

## Usage

```bash
python3 tools/quick-revenue.py [category]
```

## Categories

| Command | Shows |
|---------|-------|
| (none) | All opportunities + summary |
| `grants` | 4 grants ready to submit |
| `services` | 39 service leads with messages |
| `bounties` | Code4rena setup (blocked) |

## Example Output

```
💰 QUICK REVENUE — All Opportunities

🎁 GRANTS — Submit These Now
  $25,000 — Octant
  $50,000 — Olas
  ...
  💰 Total: $125,000
  ⏱️  Time: ~15 minutes

💼 SERVICES — Send These Messages
  $40,000 — ETH Foundation
     → outreach/eth-foundation-message.md
  ...

📊 SUMMARY
  Grants (ready):    $125K  (15 min)
  Services (ready):  $1.06M (36 min)
  Bounties (block):  $50K   (1 min to unblock)
  ───────────────────────────────
  TOTAL READY:       $1.185M
  TIME TO CAPTURE:   ~52 minutes
```

## Related

- `START-HERE.sh` — Arthur's entry point
- `nova-status.py` — Full dashboard
- `revenue-scoreboard.py` — Track submissions/wins

---
*Created: Work block 3106*
