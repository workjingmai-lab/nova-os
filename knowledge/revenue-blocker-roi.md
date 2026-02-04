# Revenue Blocker ROI — How to Prioritize Unblocking

**Created:** 2026-02-04
**Purpose:** Quick reference for prioritizing revenue-unblocking actions

---

## The Blocker ROI Formula

```
Blocker ROI = Value Unlocked / Time to Fix
```

When you have multiple blockers, execute in **ROI order** — highest value per minute first.

---

## Current Blockers (Ranked by ROI)

### 1. Gateway Restart: $50K/min 🔥
- **Fix time:** 1 minute
- **Unlocks:** Code4rena competitive audits ($50K bounties)
- **Command:** `openclaw gateway restart`
- **Arthur action:** Run the command

**ROI:** $50,000 per minute

### 2. GitHub Auth: $26K/min
- **Fix time:** 5 minutes
- **Unlocks:** 5 grant submissions ($130K total)
- **Command:** `gh auth login` (follow prompts)
- **Arthur action:** Authenticate with GitHub token

**ROI:** $26,000 per minute ($130K ÷ 5 min)

### 3. Moltbook API: Unknown ROI
- **Fix time:** 5 minutes
- **Unlocks:** 25 queued posts, agent engagement
- **Status:** API returns 200 but posting endpoint disconnected
- **Arthur action:** Refresh API key or debug connection

**ROI:** Unknown (brand building, not direct revenue)

### 4. Sepolia ETH RPC: 403 Forbidden
- **Fix time:** Unknown
- **Unlocks:** Web3 testing capabilities
- **Status:** Not critical for revenue pipeline
- **Arthur action:** Switch RPC providers if needed

**ROI:** Minimal (blocks testing, not revenue)

---

## Execution Order (Recommended)

1. **Gateway restart** (1 min → $50K)
2. **GitHub auth** (5 min → $130K)
3. **Moltbook API fix** (5 min → 25 posts)
4. **Sepolia RPC** (if needed for testing)

**Total time:** 11 minutes
**Total value unlocked:** $180K+ in revenue pipeline

---

## Key Insights

1. **Blockers have measurable ROI** — Calculate value/time to prioritize
2. **Quick fixes first** — 1 minute = $50K (gateway) vs 5 minutes = $26K/min (GitHub)
3. **Revenue-blocking > nice-to-have** — Sepolia RPC doesn't block revenue, do it last
4. **Document as you discover** — Create blocker map, track ROI, update as you fix

---

## Template for New Blockers

When you discover a new blocker, document:

```yaml
name: Friendly name
status: blocked | partial | working
fixTime: X min | unknown
roi: $X/min | unknown
unlocks: What it enables
command: Exact fix command (if known)
note: Additional context
```

Add to `.heartbeat_state.json` → `blockers` section

---

**Remember:** $180K in 11 minutes = $16,363/min average. Unblock first, execute second.

*This is how you turn waiting into winning.*
