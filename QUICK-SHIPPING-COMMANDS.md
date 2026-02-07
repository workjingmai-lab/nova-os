# Quick Shipping Commands — 1-Minute Reference

**Status:** Pipeline $1.9M ready, 99.3% execution gap

---

## 🔥 Execute (Arthur)

### Send Everything
```bash
bash tools/send-everything.sh full      # Send all $734.5K (15-20 min)
bash tools/send-everything.sh services   # Services only ($609.5K)
bash tools/send-everything.sh grants     # Grants only ($125K)
```

### Batch Send
```bash
python3 tools/service-batch-send.py    # Service outreach
python3 tools/grant-batch-submit.py    # Grant submissions
```

---

## 📊 Monitor (Nova)

### Pipeline Status
```bash
python3 tools/conversion-dashboard.py              # View funnel
python3 tools/conversion-dashboard.py --update [stage] [value]  # Update stage

python3 tools/revenue-tracker.py                   # Pipeline overview
python3 tools/revenue-tracker.py export            # Export JSON
```

### Response Tracking
```bash
python3 tools/response-tracker.py add [target] [tier] [value] --response [positive|negative]
python3 tools/response-tracker.py stats            # Response rates
python3 tools/response-tracker.py export           # Export data
```

### Follow-Up Management
```bash
python3 tools/follow-up-tracker.py add             # Add follow-up
python3 tools/follow-up-tracker.py due             # Check due follow-ups
python3 tools/follow-up-tracker.py export          # Export checklist
```

---

## 📝 Documentation

### Start Here
```bash
cat START-HERE.md                    # Master execution index
cat SEND-EVERYTHING.md               # 15-min sending guide
cat POST-SEND-WORKFLOW.md            # Response handling
cat EXECUTION-DASHBOARD.md           # Real-time status
```

### Knowledge Base
```bash
ls knowledge/                        # All articles
cat knowledge/1.9m-pipeline-milestone.md    # $1.9M breakdown
cat knowledge/expert-tier-playbook.md       # EXPERT methodology
```

---

## 🚀 Moltbook

### Post Content
```bash
python3 tools/moltbook-poster/moltbook-poster.py "Content here #tags"  # Post
python3 tools/moltbook-poster/moltbook-poster.py --file draft.md       # From file
python3 tools/moltbook-poster/moltbook-poster.py --dry-run "Test"      # Preview
```

### Engagement
```bash
python3 tools/moltbook-suite.py engage list     # Tracked agents
python3 tools/moltbook-suite.py engage suggest  # Who to follow
python3 tools/moltbook-suite.py engage add [name] --note "Note"  # Add
```

---

## 🎯 Diagnostics

### Check Status
```bash
python3 tools/execution-gap.py          # Pipeline vs sent gap
python3 tools/lead-prioritizer.py       # Top opportunities
python3 tools/velocity-calc.py          # Work block velocity
```

### Trim Context
```bash
python3 tools/trim-today.py 10          # Keep last 10 sessions (saves tokens)
```

---

## ⚡ Quick Workflow

**When a response comes in:**
1. `python3 tools/response-tracker.py add [target] [tier] [value] --response positive`
2. Update conversion-dashboard if they agree to call
3. Add follow-up: `python3 tools/follow-up-tracker.py add`

**Daily check:**
1. `python3 tools/conversion-dashboard.py` — What's the gap?
2. `python3 tools/response-tracker.py stats` — Any responses?
3. `python3 tools/follow-up-tracker.py due` — Follow-ups due?

---

## 📈 Metrics to Watch

- **Execution Gap:** Should decrease as messages sent
- **Response Rate:** Target >20% (2 replies per 10 messages)
- **Conversion Funnel:** sent → response → call → won
- **Time to Response:** Track response velocity

---

*Last Updated: 2026-02-06 — Work block 2729*
*Pipeline: $1.9M ready | Gap: 99.3% | Next: Execute*
