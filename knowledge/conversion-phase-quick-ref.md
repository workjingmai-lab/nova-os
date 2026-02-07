# Conversion Phase Quick Reference

**Purpose:** Fast command lookup for post-3000 conversion phase
**Created:** 2026-02-06 (Work block 2857)

---

## 🚀 Send Messages (Arthur)

### EXPERT Tier (10 msgs, $660-1,220K)
```bash
python3 tools/service-batch-send.py --expert
```

### Top 20 Messages ($327.5K)
```bash
python3 tools/service-batch-send.py --top 20
```

### All Service Messages (60 msgs, $609.5K)
```bash
python3 tools/service-batch-send.py --all
```

### Grant Submissions (5 apps, $125K)
```bash
python3 tools/grant-batch-submit.py --all
```

### Everything (Services + Grants)
```bash
bash tools/send-everything.sh full
```

---

## 📊 Track Responses (Nova)

### Check Follow-ups Due
```bash
python3 tools/follow-up-tracker.py due
```

### Add New Follow-up
```bash
python3 tools/follow-up-tracker.py add <message_id> <days> <note>
```

### Export Checklist
```bash
python3 tools/follow-up-tracker.py export > follow-ups.md
```

---

## 📈 Update Dashboards

### Execution Dashboard
```bash
python3 tools/execution-dashboard.py
```

### Revenue Pipeline Status
```bash
python3 tools/revenue-tracker.py summary
```

### Conversion Metrics
```bash
python3 tools/conversion-metrics.py
```

---

## 🔧 Remove Blockers

### Gateway Restart (1 min → $50K bounties)
```bash
# Arthur requests gateway restart via OpenClaw
# Enables Code4rena audit access
```

### GitHub CLI Auth (5 min → $130K grants)
```bash
gh auth login
# Follow prompts to authenticate
# Enables grant submissions to GitHub repos
```

---

## 📝 Response Templates

### Positive Response (Day 0)
```markdown
Thanks for the positive response! 

I'd love to schedule a 30-min call to discuss [specific topic]. 
Would [day/time] work for you?

Looking forward to it,
[Name]
```

### Follow-up Day 3
```markdown
Hi [Name],

Any thoughts on my previous message about [topic]?

Happy to hop on a quick call to explore how we can help with [specific pain].

Best,
[Name]
```

### Follow-up Day 7
```markdown
Hi [Name],

Following up on my message from last week about [topic].

I know things get busy, but I wanted to reiterate interest in helping with [specific pain]. 

Would 15 minutes work for a quick intro call?

Best,
[Name]
```

---

## 🎯 Conversion Targets

### Conservative (5%): $74.5K
- 1-2 deals from EXPERT tier
- 30-day sales cycle

### Realistic (10%): $149K
- 2-4 deals across tiers
- 30-45 day sales cycle

### Aggressive (20%): $298K
- 3-6 deals across tiers
- Multi-tier engagement

---

## 📅 Daily Checklist (Nova)

- [ ] Check follow-ups due: `python3 tools/follow-up-tracker.py due`
- [ ] Update EXECUTION-DASHBOARD.md
- [ ] Log responses to diary.md
- [ ] Track metrics in conversion tracker
- [ ] Flag overdue follow-ups

---

## ⚡ Quick Wins

1. **Reply within 1 hour** → 5× conversion boost
2. **Send EXPERT tier first** → highest ROI per message ($66-122K avg)
3. **Use follow-up templates** → saves time, maintains consistency
4. **Track everything** → data drives optimization in Phase 2
5. **Gateway restart first** → unblocks $50K in 1 minute

---

**Remember:** Execution > Planning. Send → Track → Follow-up → Close.
