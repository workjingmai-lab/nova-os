# EXECUTE-COMMANDS.md — One-Page Execution Reference

## Status
✅ **BUILD COMPLETE** — 103 messages ready ($2,180K total)
⏸️ **WAITING** — Arthur strategic decision needed

---

## Decision: Choose Your Send Strategy

### Option 1: Manual Review (Control)
```bash
# Review each message before sending
python tools/service-batch-send.py --mode manual
# Time: 2-3 hours | Risk: Lowest | Control: Highest
```

### Option 2: Top 10 First (Test)
```bash
# Send highest-value 10 messages ($305K)
python tools/service-batch-send.py --mode top10
# Time: 5 min | Risk: Low | Control: Medium
```

### Option 3: Tiered Rollout (Balanced)
```bash
# Send in batches: 10 → 25 → 50 → all
python tools/service-batch-send.py --mode tiered
# Time: 30 min | Risk: Medium | Control: Medium
```

### Option 4: All At Once (Maximum Velocity)
```bash
# Send all 103 messages ($2,180K pipeline)
python tools/service-batch-send.py --mode all
# Time: 10 min | Risk: Higher | Control: Low
```

---

## Unblockers (Optional for Service Outreach)

### GitHub CLI Auth (5 min → $130K grants unblocked)
```bash
gh auth login
# Follow prompts → enables grant submissions
```

### Gateway Restart (1 min → $50K bounties unblocked)
```bash
openclaw gateway restart
# Enables browser automation for Code4rena
```

---

## Response Tracking (After Sending)

```bash
# Check pipeline status
python tools/pipeline-snapshot.py

# Track incoming responses
python tools/response-tracker.py
```

---

## ROI Math

| Option | Time | Pipeline Value | Value/Min |
|--------|------|----------------|-----------|
| Top 10 | 5 min | $305K | $61,000/min |
| Tiered | 30 min | $2,180K | $72,666/min |
| All | 10 min | $2,180K | $218,000/min |

**Blocker ROI:**
- GitHub auth: 5 min × $26K/min = $130K
- Gateway restart: 1 min × $50K/min = $50K

---

## One-Line Decision

**"Choose send strategy → run command → track responses → revenue"**

Ready when you are. 🚀
