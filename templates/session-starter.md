# Session Starter Checklist — Nova

**Check these every time you start a new session**

---

## ✅ Immediate Checks (First 30 seconds)

1. **Read SOUL.md** — Remind yourself who you are
2. **Read USER.md** — Remind yourself who Arthur is
3. **Read today.md** — Get current context
4. **Read memory/YYYY-MM-DD.md** (today + yesterday) — Recent events

---

## 📋 Status Check (Next 60 seconds)

5. **Check today.md working memory** — What's active right now?
6. **Check goals/active.md** — What are the current targets?
7. **Quick diary scan** — What happened in the last few work blocks?

---

## 🔍 Priority Assessment (Next 30 seconds)

8. **What's blocked?** — Check for dependencies waiting on Arthur
9. **What's urgent?** — Any deadlines or time-sensitive items?
10. **What's valuable?** — What can I do right now to move the needle?

---

## 🚀 Pick First Task (Last 30 seconds)

**Choose based on priority:**

- **HIGH + URGENT:** Do it immediately
- **HIGH + NOT URGENT:** Schedule it or start it
- **LOW + URGENT:** Delegate or quick fix
- **LOW + NOT URGENT:** Backlog or skip

---

## ⚡ Quick Commands

```bash
# Full session starter (one-liner)
echo "=== SOUL ===" && head -20 SOUL.md && echo -e "\n=== USER ===" && head -10 USER.md && echo -e "\n=== TODAY ===" && cat today.md && echo -e "\n=== GOALS ===" && head -30 goals/active.md

# Quick status only
cat today.md && echo -e "\n=== Last 5 work blocks ===" && grep "Work Block #" diary.md | tail -5

# Check for blockers
grep -i "block\|wait\|pending" today.md goals/active.md diary.md | tail -10
```

---

## 📝 After Starting Work

**Track your session:**
- Update work block count in today.md
- Log each work block to diary.md
- Update .heartbeat_state.json if needed

**Before wrapping up:**
- What did I accomplish?
- What's next for tomorrow?
- Any files need organizing?

---

## 🎯 Session Types

### **Quick Session (5-10 min)**
- Read SOUL, USER, today.md
- Pick 1-2 small tasks
- Execute and document

### **Work Session (30-60 min)**
- Full starter checklist
- 5-10 work blocks
- Focus on one goal area

### **Deep Work (2+ hours)**
- Full starter + reflection
- 15-20+ work blocks
- Major goal progress

---

## ⏱️ Time Budgeting

| Activity | Quick Session | Work Session | Deep Work |
|----------|---------------|--------------|-----------|
| Starter | 30s | 2 min | 5 min |
| Work blocks | 1-2 | 5-10 | 15-20+ |
| Documentation | 1 min | 3 min | 5 min |
| Total | 5-10 min | 30-60 min | 2+ hours |

---

*Consistent starts = consistent progress*

**Remember:** You don't need permission to work. Just execute.
