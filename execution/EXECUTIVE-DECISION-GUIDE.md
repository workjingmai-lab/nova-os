# Executive Decision Guide — Send Strategy

**You have 104 messages worth $2,187K ready to send.**

Choose your strategy:

## Option 1: Top 10 — Quick Test 🎯
**Time:** 5 minutes | **Value:** $305K | **Risk:** Low
```bash
python tools/service-batch-send.py --strategy top10
```
Best for: Testing waters, low-risk start

## Option 2: Tiered Rollout — Balanced ⚡
**Time:** 20 minutes | **Value:** $585K→$1,979K | **Risk:** Medium
```bash
python tools/service-batch-send.py --strategy tiered
```
Best for: Gradual engagement, learn and adjust

## Option 3: All at Once — Maximum Reach 🚀
**Time:** 45 minutes | **Value:** $1,979K | **Risk:** High
```bash
python tools/service-batch-send.py --strategy all
```
Best for: Maximum pipeline activation

## Decision Framework

| Your Situation | Recommended Strategy |
|----------------|---------------------|
| First time sending? | Top 10 |
| Want fast feedback? | Top 10 |
| Comfortable with outreach? | Tiered |
| Want to maximize? | All |
| Have time to manage responses? | All |

## Expected Outcomes

- **Top 10:** 2-3 responses → $60K-$90K in conversations
- **Tiered:** 5-10 responses → $150K-$300K in conversations
- **All:** 10-20 responses → $300K-$600K in conversations

## After Sending

1. Check responses: `python tools/response-tracker.py --list`
2. Triage fast: GREEN within 1 hour (see FIRST-24-HOURS.md)
3. Book calls: Fast responders → Fast calls

---

**One command. One decision. Revenue starts now.**

Which option?
