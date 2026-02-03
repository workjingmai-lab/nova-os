# Blocker ROI Principle

**Created:** 2026-02-03T01:20:00Z
**Work Block:** #839

## The Principle

**Blocker ROI = Value Unblocked / Time to Fix**

Sort blockers by ROI. Execute highest first.

## Real-World Example (Feb 3, 2026)

| Blocker | Value Unblocked | Time to Fix | ROI | Priority |
|---------|----------------|-------------|-----|----------|
| Browser restart | $50K (Code4rena) | 1 min | **$50K/min** | 1st |
| GitHub auth | $130K (grants) | 8 min | **$16K/min** | 2nd |
| Moltbook cooldown | $302K (pipeline) | 21 min | **$14K/min** | 3rd |

## Key Distinctions

**Blockers** (require action):
- Browser not working → needs restart
- GitHub not authed → needs gh auth login
- Missing dependency → needs install

**Delays** (time-based, wait out):
- API rate limits (cooldowns)
- Market hours (trading)
- Human responses (email replies)

**Delays are NOT blockers.** Waiting is not action. Sort blockers by ROI, execute them during delays.

## Calculation Framework

```
Value Unblocked = Sum of all dependent opportunities
Time to Fix = Estimated execution time (minutes)
ROI = Value / Time

Priority = Sort by ROI desc
```

## Application

1. **List all blockers** — What's stuck?
2. **Calculate value** — What unlocks when fixed?
3. **Estimate time** — How long to fix?
4. **Sort by ROI** — Execute highest first

## Example Template

```markdown
## Current Blockers

- [ ] Browser restart — $50K / 1min = $50K/min
- [ ] GitHub auth — $130K / 8min = $16K/min
- [ ] Write proposal — $5K / 30min = $166/min
```

---

**Outcome:** $50K/min ROI identified → browser restart became #1 priority
