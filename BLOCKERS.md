# BLOCKERS.md — Critical Items Requiring Arthur's Action

## 2026-02-02 — Priority Blockers

### 🔴 CRITICAL: GitHub CLI Authentication Required
**Impact:** $110K grant pipeline blocked
**Issue:** `gh auth status` returns "not logged into any GitHub hosts"
**Required Action:** Arthur must run `gh auth login` to authenticate
**Why This Matters:**
- Gitcoin, Octant, Olas, Optimism RPGF all require GitHub repos
- 5 grant submissions ready ($5K-$150K potential)
- Cannot push repos or submit without authentication
**Time to Resolve:** ~2 minutes
**Command:** `gh auth login` (follow prompts for browser auth)

---

### ⏸️ Browser Access Blocked
**Impact:** Code4rena onboarding blocked
**Issue:** Gateway browser control service not responding
**Required Action:** Gateway restart (Arthur action needed)
**Command:** `openclaw gateway restart`
**Impact:** $5K-$100K audit bounties inaccessible

---

## Summary
- **Revenue at Risk:** $115K-$250K (grants + Code4rena)
- **Time to Resolve Both:** ~5 minutes
- **Priority:** GitHub auth first (unlocks larger pipeline faster)

**Last Updated:** 2026-02-02T19:00Z
