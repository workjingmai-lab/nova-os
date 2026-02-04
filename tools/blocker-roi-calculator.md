# Blocker ROI Calculator

Calculate return on investment for unblocking work. Helps prioritize which blockers to tackle first based on value/time ratio.

## Why This Tool

**"Blocker ROI = Priority"** — Sort blockers by value/time, execute highest first.

When you're blocked on multiple fronts, how do you decide what to unblock? This tool calculates ROI per minute and ranks blockers by their unblocking value.

Examples from real execution:
- GitHub CLI auth: 5 minutes → $130K unblocked = **$26,000/min ROI**
- Gateway browser restart: 1 minute → $50K unblocked = **$50,000/min ROI**
- Template creation: 30 minutes → $122K pipeline = **$4,067/min ROI**

## Usage

### Single Blocker Analysis
```bash
python tools/blocker-roi-calculator.py --value 130000 --time 5 --name "GitHub CLI auth"
```

Output:
```
============================================================
🚧 Blocker: GitHub CLI auth
============================================================
Value Unblocked:      $130K
Time to Unblock:      5 minutes
────────────────────────────────────────────────────────────
ROI per Minute:       $26,000/min
ROI per Hour:         $1,560,000/hour
────────────────────────────────────────────────────────────
Priority:             HIGH (escalate immediately)
============================================================
```

### Compare Multiple Blockers
```bash
# Save each blocker to JSON first
python tools/blocker-roi-calculator.py --value 130000 --time 5 --name "GitHub auth" --json > /tmp/github-auth.json
python tools/blocker-roi-calculator.py --value 50000 --time 1 --name "Browser restart" --json > /tmp/browser.json

# Compare and rank
python tools/blocker-roi-calculator.py --compare /tmp/github-auth.json /tmp/browser.json
```

Output:
```
📊 Blocker Comparison (sorted by ROI):

1. Browser restart
   Value: $50K | Time: 1min
   ROI: $50,000/min | CRITICAL (execute now)

2. GitHub auth
   Value: $130K | Time: 5min
   ROI: $26,000/min | HIGH (escalate immediately)
```

## Priority Classification

| ROI/min | Priority | Action |
|---------|----------|--------|
| ≥$50K/min | CRITICAL | Execute now |
| ≥$10K/min | HIGH | Escalate immediately |
| ≥$1K/min | MEDIUM | Schedule today |
| <$1K/min | LOW | Queue for later |

## Real Examples

### Grant Submission Blocker
```bash
python tools/blocker-roi-calculator.py --value 130000 --time 5 --name "GitHub CLI auth for grants"
# Result: $26,000/min ROI → HIGH priority
```

### Code4rena Bounties
```bash
python tools/blocker-roi-calculator.py --value 50000 --time 1 --name "Gateway browser restart"
# Result: $50,000/min ROI → CRITICAL priority
```

### Service Outreach Template
```bash
python tools/blocker-roi-calculator.py --value 122000 --time 30 --name "Service outreach templates"
# Result: $4,067/min ROI → MEDIUM priority
```

## Integration

Use with `blocker-tracker.py` to maintain a prioritized blocker list:

```bash
# Track blocker
python tools/blocker-tracker.py add --name "GitHub CLI auth" --value 130000 --time 5

# Compare all blockers
python tools/blocker-tracker.py list | jq '.[] | select(.status=="blocked")' > /tmp/blocked.json
python tools/blocker-roi-calculator.py --compare $(ls /tmp/blocker-*.json)
```

## Implementation Notes

- **Infinite ROI:** When time=0, ROI is ∞ (instant unblocking = infinite value)
- **Currency formatting:** Auto-scales (K for thousands, M for millions)
- **JSON output:** Use `--json` for integration with other tools
- **Comparison mode:** Ranks blockers by ROI descending

## See Also

- `blocker-tracker.py` — Track blocker lifecycle
- `revenue-tracker.py` — Track overall pipeline value
- `knowledge/outreach-message-structure.md` — Value-first outreach strategy

## Created

2026-02-03 — Week 2, revenue pipeline optimization
