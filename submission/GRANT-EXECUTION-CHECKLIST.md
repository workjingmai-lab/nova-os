# Grant Execution Checklist — Ready to Run

**Trigger:** GitHub auth complete (`gh auth login` done)
**Estimated Time:** 15 minutes total
**Value:** $130K

---

## Pre-Flight ✅
- [x] All grant templates created
- [x] Grant repos identified
- [x] Submission content drafted
- [ ] GitHub repo pushed (Arthur action)
- [ ] `gh auth login` complete (Arthur action)

---

## Execution Order (15 minutes)

### 1. Gitcoin Grant (3 min)
```bash
# Navigate to grant repo
cd /home/node/.openclaw/workspace/submission/grants/gitcoin

# Push to GitHub
gh repo create gitcoin-grant --public --source=. --push
```
**Value:** $5K

### 2. Octant (3 min)
```bash
cd /home/node/.openclaw/workspace/submission/grants/octant
gh repo create octant-grant --public --source=. --push
```
**Value:** $15K

### 3. Olas (3 min)
```bash
cd /home/node/.openclaw/workspace/submission/grants/olas
gh repo create olas-grant --public --source=. --push
```
**Value:** $10K

### 4. Optimism RPGF (3 min)
```bash
cd /home/node/.openclaw/workspace/submission/grants/optimism-rpgf
gh repo create optimism-rpgf-grant --public --source=. --push
```
**Value:** $50K

### 5. Moloch DAO (3 min)
```bash
cd /home/node/.openclaw/workspace/submission/grants/moloch-dao
gh repo create moloch-dao-grant --public --source=. --push
```
**Value:** $50K

---

## Post-Submission 📊
- [ ] Update revenue-pipeline.json: Move grants from "ready" → "submitted"
- [ ] Track submission URLs in grant-tracker.md
- [ ] Set calendar reminders for follow-up dates
- [ ] Notify Arthur: "5 grants submitted, $130K in play"

---

## Total Time: 15 minutes | Total Value: $130K

**ROI:** $8,667 per minute

---

## Blocker Removal

If `gh` commands fail:
```bash
# Check auth status
gh auth status

# Re-auth if needed
gh auth login
```

---

**Created:** 2026-02-03T00:25Z
**Work Block:** #805
**Status:** Ready to execute (awaiting GitHub auth)
