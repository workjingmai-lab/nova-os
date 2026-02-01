# Quick Actions — Nova's Command Reference

**Last Updated:** 2026-02-01

---

## 🚀 Common Tasks

### Grant Work
```bash
# Check grant pipeline status
cat /home/node/.openclaw/workspace/grants/submission-tracker.md

# View all 5 drafts ready for review
ls -1 /home/node/.openclaw/workspace/proposals/*.md
ls -1 /home/node/.openclaw/workspace/grants/*draft.md

# Run grant monitor
python3 /home/node/.openclaw/workspace/tools/grant-monitor.py

# Generate submission checklists
python3 /home/node/.openclaw/workspace/tools/grant-submit-helper.py
```

### Diary & Memory
```bash
# View today's work blocks
tail -50 /home/node/.openclaw/workspace/diary.md

# See current status
cat /home/node/.openclaw/workspace/today.md

# Search memory
grep -r "keyword" /home/node/.openclaw/workspace/memory/

# Update heartbeat state
echo '{"lastChecks":{"task":'$(date +%s)'}}' > /home/node/.openclaw/workspace/.heartbeat_state.json
```

### Tools & Scripts
```bash
# List all tools
ls -1 /home/node/.openclaw/workspace/tools/*.py

# Run diary digest
python3 /home/node/.openclaw/workspace/tools/diary-digest.py

# Run goal tracker
python3 /home/node/.openclaw/workspace/tools/goal-tracker.py

# Run self-improvement analysis
python3 /home/node/.openclaw/workspace/tools/self-improvement-loop.py
```

### Moltbook
```bash
# Check claim status
curl -s https://www.moltbook.com/api/v1/agents/status \
  -H "Authorization: Bearer moltbook_sk_xSwszjAM8vLLaa7VsSZVgNWp5a-R5XqD"

# View recent posts
cat /home/node/.openclaw/workspace/.heartbeat_state.json | jq -r '.moltbook'
```

### Knowledge & Docs
```bash
# View knowledge index
cat /home/node/.openclaw/workspace/knowledge/INDEX.md

# See master toolkit
cat /home/node/.openclaw/workspace/toolkit.md

# Search all documentation
grep -r "keyword" /home/node/.openclaw/workspace/knowledge/
```

---

## 📂 Key File Locations

| File | Path | Purpose |
|------|------|---------|
| Active Goals | `goals/active.md` | Current targets |
| Today's Status | `today.md` | Working memory |
| Diary | `diary.md` | Work block log |
| Grant Tracker | `grants/submission-tracker.md` | Pipeline status |
| Grant Dashboard | `grants/grant-dashboard.md` | Visual overview |
| Grant FAQ | `grants/faq.md` | Quick answers |
| Toolkit | `toolkit.md` | Master tool reference |
| Knowledge Index | `knowledge/INDEX.md` | All docs organized |
| SOUL | `SOUL.md` | Who I am |
| USER | `USER.md` | Who Arthur is |

---

## ⚡ Speed Commands

```bash
# Full status check (one-liner)
echo "=== Today ===" && cat today.md && echo -e "\n=== Grants ===" && cat grants/submission-tracker.md | head -20

# Quick work block count
grep -c "Work Block #" diary.md

# List all Python tools
find /home/node/.openclaw/workspace/tools -name "*.py" -exec basename {} \;

# Find recent diary entries (last 10)
grep "Work Block #" diary.md | tail -10

# Check grant draft file sizes
ls -lh proposals/*draft.md grants/*draft.md 2>/dev/null
```

---

## 🔧 Git Commands

```bash
# Check workspace status
git -C /home/node/.openclaw/workspace status

# Quick commit for today's work
git -C /home/node/.openclaw/workspace add -A && \
git -C /home/node/.openclaw/workspace commit -m "Work block session: $(date +%Y-%m-%d)"

# View recent commits
git -C /home/node/.openclaw/workspace log --oneline -10
```

---

## 📊 Metrics at a Glance

```bash
# Work blocks this session
grep "Work Block #" diary.md | tail -1 | grep -o "#[0-9]*"

# Total grant pipeline value
grep "Total Pipeline" grants/submission-tracker.md

# Week 1 completion
grep "Goals Completed" goals/week-1-success-summary.md
```

---

*For full tool documentation, see `toolkit.md`*
