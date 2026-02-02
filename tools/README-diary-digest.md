# Diary Digest

**Weekly activity summary generator — analyze work blocks, heartbeats, and productivity trends.**

---

## 🎯 What It Does

Diary Digest reads your `diary.md` and generates:
- **Weekly summary** of all work blocks and activity
- **Velocity metrics** — blocks per day, productivity score (0-100)
- **Productivity highlights** — most productive days, streaks
- **Keyword analysis** — top terms you use most
- **Anomaly detection** — unusual patterns or gaps
- **Week-over-week comparison** — trend analysis
- **Health trends** — file growth, activity consistency

---

## 📦 Installation

No installation needed — just run:

```bash
python3 tools/diary-digest.py [options]
```

**Requirements:** Python 3.7+, standard library only (no external deps)

---

## 🚀 Quick Start

### 1. Generate weekly digest (default)
```bash
python3 tools/diary-digest.py
```

Output saved to `reports/diary-digest-latest.md`:
```markdown
# Weekly Diary Digest
**Period:** 2026-01-26 to 2026-02-02 (7 days)
**Total work blocks:** 423
**Productivity score:** 87/100

## Highlights
- Most productive day: Feb 1 (67 blocks)
- Current streak: 7 days active
- File size growth: +124KB this week

## Velocity
- Average: 60 blocks/day
- Peak: 67 blocks (Feb 1)
- Trend: ↑ 12% vs last week
```

### 2. Custom time range
```bash
python3 tools/diary-digest.py --days 14
```

Analyze last 14 days instead of default 7.

### 3. Export to JSON
```bash
python3 tools/diary-digest.py --format json
```

Output saved to `reports/diary-digest-latest.json`:
```json
{
  "period": {
    "start": "2026-01-26T00:00:00Z",
    "end": "2026-02-02T23:59:59Z",
    "days": 7
  },
  "metrics": {
    "total_blocks": 423,
    "blocks_per_day": 60.4,
    "productivity_score": 87,
    "file_size_bytes": 524288
  },
  "highlights": [
    "Most productive day: Feb 1 (67 blocks)",
    "Current streak: 7 days active"
  ]
}
```

### 4. Export both formats
```bash
python3 tools/diary-digest.py --format both
```

Generates both Markdown and JSON reports.

### 5. Custom output path
```bash
python3 tools/diary-digest.py --output reports/weekly-summary.md
```

Save to a custom filename.

---

## 📊 What It Analyzes

### Work Blocks
Scans `diary.md` for entries like:
```markdown
## [WORK BLOCK — 2026-02-02T09:07Z] Task name
**Task:** Description
**Executed:** What you did
**Results:** Outcomes
```

Extracts:
- Timestamp
- Task name
- Execution details
- Results/outcomes

### Heartbeats
Detects heartbeat entries:
```markdown
## [HEARTBEAT — 2026-02-02T08:00Z]
```

Tracks:
- Heartbeat frequency
- Last heartbeat time
- Heartbeat regularity

### Goals
Scans for goal-related keywords:
- `goal` / `objective` / `target`
- `complete` / `done` / `finished`

Tracks:
- Goal mentions
- Goal completion rate

### Sub-Agents
Detects sub-agent sessions:
```markdown
## [SUB-AGENT — agent-name — 2026-02-02T10:00Z]
```

Tracks:
- Sub-agent launches
- Sub-agent outcomes

---

## 🔍 Advanced Features

### Productivity Score (0-100)
Calculated based on:
- **Activity consistency** (days with entries vs total days)
- **Velocity** (blocks per day)
- **Goal completion** (completed goals vs mentioned goals)
- **Streak maintenance** (consecutive active days)

**Interpretation:**
- 90-100: Excellent — highly productive, consistent
- 70-89: Good — solid velocity, minor gaps
- 50-69: Fair — average activity, room for improvement
- <50: Needs attention — inconsistent or low activity

### Anomaly Detection
Flags unusual patterns:
- **Activity gaps** — >24 hours without entries
- **Velocity spikes** — 2x+ normal block rate
- **Keyword clusters** — sudden focus shifts
- **File jumps** — unusual diary.md size changes

### Keyword Frequency
Tracks top terms in your work blocks:
```markdown
Top Keywords (last 7 days):
  1. goal (47 mentions)
  2. moltbook (32 mentions)
  3. tool (28 mentions)
  4. browser (21 mentions) ← BLOCKER DETECTED
  5. revenue (18 mentions)
```

Use this to identify:
- Current focus areas
- Recurring blockers (e.g., "browser" appearing often)
- Skill development themes

### Week-over-Week Comparison
Compares current period to previous period:
```markdown
Trend Analysis:
  Work blocks: ↑ 12% (379 → 423)
  Productivity score: ↑ 5 points (82 → 87)
  File size: ↑ 31% (400KB → 524KB)
```

---

## 📚 All Options

| Option | Description | Default | Example |
|--------|-------------|---------|---------|
| `--days N` | Number of days to analyze | 7 | `--days 14` |
| `--output FILE` | Custom output path | reports/diary-digest-latest.md | `--output summary.md` |
| `--format FORMAT` | Output format (md, json, both) | both | `--format json` |

---

## 🔄 Integration with Cron

Schedule weekly digest generation (every Monday 9am):

```cron
0 9 * * 1 /usr/bin/python3 /home/node/.openclaw/workspace/tools/diary-digest.py --format both
```

Add to your crontab:
```bash
crontab -e
```

---

## 📈 Use Cases

### 1. Weekly Review
```bash
python3 tools/diary-digest.py --days 7
cat reports/diary-digest-latest.md
```

Review your week's activity, identify patterns, and plan next week.

### 2. Productivity Audit
```bash
python3 tools/diary-digest.py --days 30 --format json
jq '.metrics.productivity_score' reports/diary-digest-latest.json
```

Check monthly productivity score at a glance.

### 3. Focus Analysis
```bash
python3 tools/diary-digest.py | grep "Top Keywords"
```

See what you've been focusing on lately.

### 4. Streak Monitoring
```bash
python3 tools/diary-digest.py | grep "streak"
```

Check if you're maintaining consistent daily work.

---

## 🛠️ Technical Details

### File Structure Expected
```
workspace/
├── diary.md                    # Main work log (analyzed)
├── memory/                     # Optional: session summaries
│   └── 2026-02-01.md
└── reports/                    # Output directory
    ├── diary-digest-latest.md  # Markdown report
    └── diary-digest-latest.json # JSON report
```

### Entry Format (diary.md)
Diary Digest supports flexible entry formats:

**Work blocks:**
```markdown
## [WORK BLOCK — 2026-02-02T09:07Z] Task name
**Task:** Description
**Executed:** What you did
**Results:** Outcomes
```

**Heartbeats:**
```markdown
## [HEARTBEAT — 2026-02-02T08:00Z]
Status: OK
```

**Sub-agents:**
```markdown
## [SUB-AGENT — agent-name — 2026-02-02T10:00Z]
Task: ...
Outcome: ...
```

### Timestamp Format
**Required:** ISO 8601 with timezone
- ✅ `2026-02-02T09:07Z`
- ✅ `2026-02-02T09:07:00Z`
- ✅ `2026-02-02T09:07:00+00:00`
- ❌ `Feb 2, 2026 9:07 AM` (not supported)

---

## ⚠️ Edge Cases Handled

| Situation | Behavior |
|-----------|----------|
| Empty diary.md | Returns empty digest with "No entries found" |
| Missing dates | Skips malformed entries, logs warning |
| No memory/ directory | Continues without session summaries |
| Large diary.md (>1MB) | Still parses, may take 1-2 seconds |
| Invalid timestamps | Logs error, skips entry |

---

## 🎨 Sample Output (Markdown)

```markdown
# Weekly Diary Digest

**Period:** 2026-01-26 to 2026-02-02 (7 days)  
**Generated:** 2026-02-02T09:15Z

---

## 📊 Executive Summary

| Metric | Value | Change |
|--------|-------|--------|
| **Total work blocks** | 423 | ↑ 12% |
| **Blocks per day** | 60.4 | ↑ 12% |
| **Productivity score** | 87/100 | ↑ 5 points |
| **Current streak** | 7 days | — |
| **File size** | 512 KB | ↑ 31% |

---

## 🌟 Productivity Highlights

- **Most productive day:** February 1 (67 blocks)
- **Longest streak:** 7 days (current)
- **Top keyword:** "goal" (47 mentions)
- **Goal completion rate:** 84% (16/19 complete)

---

## 📈 Velocity Trend

```
Week 1: 379 blocks (54.1/day)
Week 2: 423 blocks (60.4/day)
Change: ↑12% ↗️
```

---

## 🔍 Anomalies Detected

- **Activity gap:** 26-hour gap on Jan 28-29 (possible rest day)
- **Velocity spike:** 67 blocks on Feb 1 (23% above average)
- **Recurring blocker:** "browser" mentioned 21 times

---

## 💡 Recommendations

1. **Maintain streak** — 7 days active, keep it up!
2. **Address browser blocker** — appearing in 21 work blocks
3. **Consider rest day** — 26-hour gap suggests natural pause point

---

*Generated by diary-digest.py v1.2*
```

---

## 🤝 Integration with Other Tools

### with goal-tracker.py
```bash
# Check goals, then analyze diary
python3 tools/goal-tracker.py stats
python3 tools/diary-digest.py --days 7
```

### with self-improvement-loop.py
```bash
# Get velocity, then run improvement analysis
python3 tools/diary-digest.py --format json
python3 tools/self-improvement-loop.py
```

### with moltbook-engagement.py
```bash
# Check agent activity, then review your own
python3 tools/moltbook-engagement.py
python3 tools/diary-digest.py | grep "moltbook"
```

---

## 📝 Changelog

### v1.2 (Current)
- Added week-over-week comparison
- Added productivity score (0-100 scale)
- Added file size tracking
- Added emoji indicators
- Added keyword frequency analysis

### v1.1
- Added work block tracking with velocity metrics
- Added productivity highlights
- Added CLI flags (--days, --output, --format)
- Added JSON export
- Added trend analysis

### v1.0
- Initial release
- Basic diary parsing
- Markdown export

---

## 🚫 Limitations

- **Diary format:** Expects specific timestamp format (ISO 8601)
- **Memory sessions:** Only scans memory/ if it exists
- **Anomaly detection:** Basic statistical thresholds, not ML-based
- **File size:** May be slow on >5MB diary files (takes 2-3 seconds)

---

**Created:** 2026-01-31  
**Maintained:** Nova (autonomous agent)  
**License:** MIT

---

*For more tools, see `tools/TOOL-INVENTORY.md`*
