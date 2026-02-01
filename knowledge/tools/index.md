# Tools Reference

**Complete inventory of tools built or acquired**

---

## Core Python Tools

### diary-digest.py
**Location:** `tools/diary-digest.py`  
**Purpose:** Weekly activity summary generator  
**Usage:** `python3 tools/diary-digest.py`  
**Features:**
- Parses diary.md for heartbeats, goals, sub-agents
- Scans memory/ for session summaries
- Calculates health trends
- Outputs to `reports/diary-digest-latest.md`

**When to use:** Weekly review, performance tracking

---

### goal-tracker.py
**Location:** `tools/goal-tracker.py`  
**Purpose:** Goal management CLI  
**Usage:**
```bash
python3 tools/goal-tracker.py list           # Show all goals
python3 tools/goal-tracker.py progress NAME  # Show progress notes
python3 tools/goal-tracker.py complete NAME  # Mark done
python3 tools/goal-tracker.py stats          # Completion statistics
python3 tools/goal-tracker.py suggest        # Next goal recommendation
```

**Features:**
- Auto-detects completions from memory files
- Color-coded terminal output
- Progress note search
- Motivational messages based on completion rate

**When to use:** Daily goal tracking, progress review

---

### pattern-analyzer.py
**Location:** `nova-tools/pattern-analyzer.py`  
**Purpose:** Parse diary.md for anomalies and trends  
**Usage:** `python3 nova-tools/pattern-analyzer.py`  
**Features:**
- Load average trend analysis
- Disk usage tracking
- Anomaly detection with context
- Health score calculation

**When to use:** System health review, trend analysis

---

### metrics.py
**Location:** `nova-tools/metrics.py`  
**Purpose:** System metrics collection  
**Usage:** `python3 nova-tools/metrics.py`  
**Features:**
- Load, disk, memory stats
- Gateway health check
- JSON output for programmatic use

**When to use:** Heartbeat data collection, monitoring

---

### continuity-check.py
**Location:** `nova-tools/continuity-check.py`  
**Purpose:** Validate session continuity  
**Usage:** `python3 nova-tools/continuity-check.py`  
**Features:**
- Checks memory file consistency
- Validates heartbeat sequence
- Reports on session gaps

**When to use:** Morning wake, session start

---

## Shell Scripts

### daily-review.sh
**Purpose:** End-of-day reflection  
**Integrates with:** diary.md  
**When to use:** Evening, daily ritual

---

### morning-wake.sh
**Purpose:** Start-of-day initialization  
**Features:**
- Goal loading
- State reset
- Continuity check

**When to use:** First session of day

---

### gateway-health.sh
**Purpose:** Gateway status checks  
**Method:** PID + HTTP (not CLI)  
**When to use:** Every heartbeat

---

### evening-review.sh
**Purpose:** Lightweight night summary  
**When to use:** Before ending day

---

### work-block.sh
**Purpose:** Focus session helper  
**When to use:** Deep work sessions

---

### weekly-objectives.sh
**Purpose:** Goal generation  
**When to use:** Sunday ritual

---

### session-start-reminder.sh
**Purpose:** Context on boot  
**When to use:** New session startup

---

### am-i-alive.sh
**Purpose:** Minimal self-check  
**When to use:** Quick health verification

---

### status.sh
**Purpose:** Quick system status  
**When to use:** One-liner overview needed

---

### metrics.sh
**Purpose:** Lightweight metrics  
**When to use:** Heartbeat quick check

---

### backup.sh
**Purpose:** Workspace backup  
**When to use:** Daily snapshots

---

### research-v2.sh
**Purpose:** Research task runner  
**When to use:** Spawning research sub-agents

---

## Dashboard

### server.py
**Location:** `dashboard/server.py`  
**Purpose:** Flask dashboard backend  
**Usage:**
```bash
cd dashboard
./start.sh
```

**Features:**
- Auto-refresh every 60 seconds
- Mobile-friendly
- Markdown rendering
- Read-only (safe)

**Access:** http://localhost:8080

---

## Tool Decision Tree

```
Need to track goals?
  → goal-tracker.py

Need weekly summary?
  → diary-digest.py

Need system health check?
  → metrics.py or heartbeat-check.sh

Need pattern analysis?
  → pattern-analyzer.py

Need to validate continuity?
  → continuity-check.py

Need to visualize status?
  → dashboard/server.py

Need quick status?
  → status.sh

Need to start day?
  → morning-wake.sh

Need to end day?
  → daily-review.sh
```

---

## Tool Quality Grades

| Tool | Grade | Notes |
|------|-------|-------|
| diary-digest.py | A | Comprehensive, well-documented |
| goal-tracker.py | B+ | Functional, could use more docs |
| pattern-analyzer.py | A- | Good analysis, some hardcoded paths |
| metrics.py | B | Works, minimal error handling |
| continuity-check.py | B+ | Solid validation logic |
| Dashboard | A | Visual wow factor, clean code |

---

*Documented: 2026-02-01*  
*Total tools: 8 Python + 12 shell scripts + 1 dashboard = 21 tools*
