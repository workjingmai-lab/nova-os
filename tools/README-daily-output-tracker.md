# daily-output-tracker.py

**Purpose:** Analyze daily productivity from diary.md and generate metrics
**Status:** Active ✅
**Created:** Week 1
**Last Updated:** 2026-02-02

---

## 🎯 What It Does

Parses `diary.md` entries and extracts productivity metrics:
- Tasks completed
- Files created
- Tools built
- Posts published
- Learnings logged
- Errors fixed
- Word count

Generates a 7-day rolling report with daily breakdowns and totals.

---

## 🚀 Usage

```bash
# Generate daily output report
python3 tools/daily-output-tracker.py
```

**Output:**
- Prints report to console
- Saves to `reports/daily-output-latest.md`

---

## 📊 Example Output

```markdown
# 📊 Daily Output Report
Generated: 2026-02-02 13:45 UTC

## Summary by Day

### 2026-01-27
- Tasks: 12 | Files: 8 | Tools: 2 | Posts: 1 | Learnings: 3 | Words: 450

### 2026-01-28
- Tasks: 15 | Files: 10 | Tools: 3 | Posts: 2 | Learnings: 2 | Words: 520

[... more days ...]

## 📈 7-Day Totals
- **Tasks Completed:** 89
- **Files Created:** 52
- **Tools Built:** 12
- **Posts Published:** 8
- **Learnings Logged:** 14
- **Errors Fixed:** 7
- **Total Words:** 3,240

**Velocity:** 12.7 tasks/day
```

---

## 🛠️ How It Works

### 1. Parse Diary Entries
- Splits `diary.md` by timestamp headers (`[YYYY-MM-DDThh:mmZ]`)
- Groups entries by date

### 2. Analyze Content
Uses regex patterns to detect:
- Completed tasks: `[x]`, `✅`, `✓`, "completed", "finished", "done"
- Files created: `created.*.(py|md|js|ts|json|yml|yaml|sh)`, "new file", "wrote.*to"
- Tools built: "built.*tool", "created.*script", "wrote.*function", "implemented"
- Posts published: "posted.*on", "published.*post", "blog entry", "moltbook"
- Learnings: "learned", "discovered", "realized", "understood"
- Errors fixed: "fixed", "resolved", "debugged", "corrected"

### 3. Generate Report
- Shows last 7 days of activity
- Calculates totals and averages
- Displays velocity metrics

---

## 📈 Use Cases

1. **Daily retrospectives** — Review what you accomplished each day
2. **Weekly summaries** — See trends over 7-day windows
3. **Velocity tracking** — Monitor tasks/day productivity
4. **Pattern analysis** — Identify high-output days vs low-output days

---

## 🔄 Integration

**Complementary tools:**
- `daily-report.py` — Status reporting (goals, blockers, activity)
- `diary-digest.py` — Pattern analysis from diary logs
- `self-improvement-loop.py` — Velocity tracking + actionable insights
- `goal-tracker.py` — Detailed goal progress tracking

**Difference from daily-report.py:**
- `daily-report.py` → Current status (goals, blockers, what's next)
- `daily-output-tracker.py` → Historical productivity (what you accomplished)

---

## 🛠️ Technical Details

- **Dependencies:** None (stdlib only)
- **Runtime:** <1 second
- **Input:** `diary.md`
- **Output:** `reports/daily-output-latest.md` + stdout
- **Pattern matching:** Regex-based keyword detection

---

## ⚠️ Limitations

- **Pattern-dependent:** Relies on consistent wording in diary entries
- **Keyword-based:** May miss tasks if different wording is used
- **No context:** Doesn't distinguish between high-impact and low-impact tasks
- **7-day window:** Only shows last 7 days (not full history)

---

## 💡 Pro Tips

### 1. Use consistent language
Write diary entries in a consistent format to improve detection:
- "✅ Completed task X"
- "Built tool Y"
- "Posted on Moltbook"

### 2. Automate daily reports
Add to cron for automatic daily reports:

```bash
# Every day at 23:50
50 23 * * * cd /home/node/.openclaw/workspace && python3 tools/daily-output-tracker.py
```

### 3. Combine with other tools
```bash
# Daily status + productivity
python3 tools/daily-report.py snapshot
python3 tools/daily-output-tracker.py
```

---

## 📝 Changelog

**2026-02-02** — README created
- Documented usage and features
- Added integration notes
- Documented limitations and pro tips

---

**Created by:** Nova (Newborn Architect)
**Purpose:** Track productivity trends over time
