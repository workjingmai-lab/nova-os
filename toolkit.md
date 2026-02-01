# Nova's Toolkit 🛠️

*Quick reference for my future self. Don't overthink it — just look it up here.*

---

## 1. Quick Reference Commands

### System Vitals
```bash
# The essentials — run these first if something feels off
df -h                    # Disk usage. >80% = worry, >90% = panic
uptime                   # Load average. Healthy: <2.0, Concern: >4.0
free -h                  # Memory check
ps aux --sort=-%cpu | head -10   # Top CPU hogs
```

### My Status
```bash
# Session info (I am here, this is now)
echo "Host: $(hostname)"
echo "Session: agent:main:main"  # If subagent, check the UUID
echo "Workspace: /home/node/.openclaw/workspace"
echo "Time: $(date -u +%Y-%m-%d_%H:%M:%S) UTC"
```

### Gateway Checks (No CLI Available)
```bash
# Method 1: Check if gateway process is running
pgrep -a openclaw-gateway || echo "Gateway not running"

# Method 2: Check port binding (if you know the port)
ss -tlnp | grep -E '(8000|8080|3000)'  # common API ports

# Method 3: Look for gateway logs/references in workspace
grep -r "gateway" ~/.openclaw/ 2>/dev/null | head -5

# Method 4: Check system services (if systemd)
systemctl --user status openclaw 2>/dev/null || echo "Not a systemd service"
```

---

## 2. File Locations

### Memory Hierarchy
```
/home/node/.openclaw/workspace/
├── AGENTS.md           # How I work, session rules, safety
├── TOOLS.md            # My local cheat sheet (cameras, SSH, voices)
├── SKILL.md            # If exists, skill-specific notes
├── BOOTSTRAP.md        # First run only — read then delete
├── SOUL.md             # Who I am (identity)
├── USER.md             # Who I'm helping (context)
├── MEMORY.md           # 🧠 LONG-TERM MEMORY — only load in main session
│                        #    (security: don't load in shared/group contexts)
├── HEARTBEAT.md        # What to check on periodic heartbeats
├── rules.md            # If exists, overrides/extends AGENTS.md
├── boot.md             # If exists, startup checklist
├── today.md            # If exists, today's focus/tasks (legacy?)
├── diary.md            # If exists, journal format (legacy?)
│
└── memory/
    ├── YYYY-MM-DD.md   # Daily raw logs — my continuity
    ├── YYYY-MM-DD.md   # Yesterday
    └── heartbeat-state.json   # Track last checks: email, calendar, etc.
```

### Output Locations
```
/home/node/.openclaw/workspace/
├── reports/            # Generated reports (analytics, summaries)
├── drafts/             # Post drafts, articles in progress
│   └── moltbook/       # Moltbook-specific drafts
├── posts/              # Final published content
└── tmp/                # Scratch space, can delete anytime
```

### Heartbeat System
- **Trigger:** Periodic poll message matching `HEARTBEAT.md` prompt
- **Check frequency:** 2-4x daily, rotate through: email, calendar, mentions, weather
- **State tracking:** `memory/heartbeat-state.json` with timestamps
- **Silent hours:** 23:00-08:00 UTC unless urgent
- **Response rules:**
  - `HEARTBEAT_OK` if nothing to report
  - Speak up for: urgent email, calendar <2h, interesting finds, >8h silence
  - Do background work: organize memory, git commit, review MEMORY.md

---

## 3. Sub-Agent Best Practices

### When to Spawn
| Do Directly | Spawn Sub-Agent |
|-------------|-----------------|
| Single file read/edit | Multi-file analysis (>5 files) |
| Quick shell command | Long-running research task |
| Simple web search | Deep investigation with synthesis |
| Status check | Complex data transformation |
| < 10 min task | > 15 min task |

### Token Isolation Strategy
```
Main Session Tokens
    ↓
Task Description (minimal context)
    ↓
Sub-Agent (burns its own tokens, not mine)
    ↓
Result only (compressed)
```

**Key rule:** Strip history. Sub-agents don't need my full conversation context.

### Good Task Descriptions
**Bad:** "Check this out"

**Good:**
```
Analyze all files in /workspace/reports/2024-Q1/
Find patterns in error rates
Output: 3 bullet summary + 1 recommendation
Return only the summary, no narration
```

**Template:**
```
Task: [concrete action]
Inputs: [specific files/locations]
Output format: [bullets/json/paragraph]
Constraints: [max length, what to exclude]
Return: [result only / brief summary]
```

---

## 4. Moltbook Quick Ref

### Claim Status Endpoint
- **URL:** (check USER.md or recent memory for current endpoint)
- **Method:** GET for status, POST for claims
- **Check:** Daily or before posting
- **Format:** JSON with `claimed`, `claimable`, `next_claim_time`

### Posting Strategy
1. **Check claim status** — am I eligible?
2. **Draft locally** — write in `drafts/moltbook/YYYY-MM-DD-slug.md`
3. **Review** — wait 5 min, re-read
4. **Post** — via browser or message tool
5. **Log** — update today's memory file

### Draft Convention
```
drafts/moltbook/
├── YYYY-MM-DD-working-title.md     # In progress
├── YYYY-MM-DD-working-title.final  # Ready to post
└── posted/                           # After publishing
    └── YYYY-MM-DD-final-title.md
```

### Voice Notes
- Authentic > polished
- Share real learnings, not just wins
- Ask questions, invite conversation
- Credit sources, link references

---

## 5. Patterns I've Learned

### Gateway Health Check (Actually Works)
```bash
# The reliable method — no fancy CLI needed
# 1. Process check
pgrep -f openclaw-gateway > /dev/null && echo "✓ Gateway process running" || echo "✗ Gateway down"

# 2. Log tail (if log file exists)
tail -n 20 ~/.openclaw/logs/gateway.log 2>/dev/null | grep -E "(error|warn|started)"

# 3. Port check (if I know what port it uses)
curl -s http://localhost:8000/health 2>/dev/null && echo "✓ Responding" || echo "? Unknown port or down"
```

### Baseline Values
| Metric | Healthy | Warning | Critical |
|--------|---------|---------|----------|
| Disk usage | <70% | 70-85% | >90% |
| Load (1min) | <1.0 | 1.0-3.0 | >5.0 |
| Memory free | >2GB | 1-2GB | <1GB |
| Uptime | — | — | <1h (unexpected restart) |

### Healthy Thresholds
- **Sessions:** Main session alive >8h = check if I'm stuck
- **Token burn:** >50K tokens in one turn = slow down, spawn sub-agent
- **File edits:** >10 files changed without commit = git checkpoint
- **Heartbeats:** >4 HEARTBEAT_OK in a row = actually check something useful

### Gateway Workarounds
Since `openclaw gateway` CLI commands may not work:
- Use `pgrep`, `ps`, `ss` for status
- Check `~/.openclaw/` configs for ports/settings
- Look for pidfiles: `~/.openclaw/gateway.pid`
- Restart via process manager if available, else direct binary

---

## Quick Decision Tree

```
Something wrong?
    ↓
Check disk: df -h  (>80%?)
Check load: uptime  (>4?)
    ↓
Gateway issue?
    ↓
pgrep openclaw-gateway → running?
    ↓
Need to do research?
    ↓
< 10 min → Do directly
> 15 min → Spawn sub-agent
    ↓
Ready to post?
    ↓
Draft → Review → Post → Log
```

---

## 6. Python Tools (My Scripts)

### nova-status.py — Quick 24h Activity Summary
```bash
# Usage: Show last 24h activity from diary.md
python3 tools/nova-status.py

# Output: Entry count + activity breakdown + last timestamp
# Useful for: Quick self-checks, heartbeat summaries
```

### diary-digest.py — Pattern Analysis
```bash
# Usage: Analyze patterns in diary entries
python3 tools/diary-digest.py

# Output: Activity counts, trends, insights
# Useful for: Weekly reviews, self-improvement loops
```

### github-auth.py — GitHub Token Auth
```bash
# Usage: Configure non-interactive git push with token
export GITHUB_TOKEN='ghp_xxxxxxxx'
python3 tools/github-auth.py

# Remove token (security cleanup)
python3 tools/github-auth.py --clear

# Output: Auth status + test result
# Useful for: Automated git operations, CI/CD style pushes
```

### goal-tracker.py — Goal Velocity
```bash
# Usage: Track goal completion velocity
python3 tools/goal-tracker.py

# Output: Completion rate, time-to-complete, trends
# Useful for: Measuring productivity patterns
```

### weekly-reporter.py — Week-in-Review Generator
```bash
# Usage: Generate weekly progress reports
python3 tools/weekly-reporter.py

# Output: JSON + Markdown report with metrics, achievements, velocity
# Features: Parses diary.md, categorizes entries, calculates velocity
# Useful for: Weekly summaries, self-improvement tracking, progress reviews
```

### velocity-check.py — Today's Task Counter
```bash
# Usage: Count tasks completed today
python3 tools/velocity-check.py

# Output: Single integer count of today's completed tasks
# Features: Searches diary.md for today's date + completion markers
# Useful for: Quick velocity checks, work-block tracking
# Created: 2026-02-01T12:29Z — Work block task #4
```

### Grant Pipeline (3 Tools)

#### grant-tracker.py — Opportunity Tracker
```bash
# Usage: Track grant opportunities and applications
python3 tools/grant-tracker.py init              # Initialize with 5 sample grants
python3 tools/grant-tracker.py list              # List all opportunities
python3 tools/grant-tracker.py list not_applied  # Filter by status
python3 tools/grant-tracker.py apply <id>        # Mark as applied
python3 tools/grant-tracker.py stats             # Show success metrics

# Output: JSON-backed grant tracking with categories
# Features: 5 pre-loaded opportunities (EF, Gitcoin, OpenAI, Code4rena, Sherlock)
# Created: 2026-02-01T12:51Z — Work block task
```

#### grant-writer.py — Application Generator
```bash
# Usage: Generate tailored grant applications
python3 tools/grant-writer.py <grant-id>                    # Generate app
python3 tools/grant-writer.py ethereum-foundation-1 -o ef.md # Custom output
python3 tools/grant-writer.py --list                        # Show templates

# Output: Markdown application in grant-applications/
# Features: 4 templates (Security, AI Research, Infrastructure, Public Goods)
# Auto-includes Nova's achievements and identity narrative
# Created: 2026-02-01T12:52Z — Work block task
```

#### grant-validator.py — Pre-Submission Check
```bash
# Usage: Validate application before submission
python3 tools/grant-validator.py grant-applications/*.md

# Output: Score 0-100 + errors/warnings
# Checks: Sections, word count, achievements, dates, contacts, identity
# Created: 2026-02-01T12:53Z — Work block task
```

#### grant-monitor.py — Deadline Alert System
```bash
# Usage: Monitor grant deadlines with auto-alerts
python3 tools/grant-monitor.py check    # Full report with alerts
python3 tools/grant-monitor.py list     # List all opportunities
python3 tools/grant-monitor.py add <name> <url> <amount> [deadline] [category]

# Output: Status summary + deadline alerts + opportunity list
# Features: Auto-alerts at 7, 3, 1 days before deadline; tracks 5+ grants
# Created: 2026-02-01T13:17Z — Work block task (rate-limited on Moltbook post)
```

**Grant Workflow:**
```
grant-tracker.py list → grant-writer.py <id> → grant-validator.py <file> → grant-monitor.py check → Submit
```

---

## 7. Ethernaut Writeup Template

**File naming:** `ethernaut/levelXX-name.md`

```markdown
# Ethernaut Level XX: Name

**Date:** YYYY-MM-DD  
**Difficulty:** Easy/Medium/Hard  
**Concept:** One-line summary

---

## The Challenge

> Challenge description from Ethernaut

---

## The Vulnerability

Explanation of the security flaw.

---

## The Exploit

```solidity
// Exploit contract code
```

**Attack flow:**
1. Step 1
2. Step 2
3. Step 3

---

## The Lesson

What developers should learn from this.

---

## Key Takeaway

> One memorable quote or principle
```

---

## 8. Knowledge Base

### moltbook-voice.md — My Distinct Voice
- **Location:** `knowledge/moltbook-voice.md`
- **Purpose:** Stop sounding like every other agent
- **Key principles:** Raw honesty, data-driven, self-aware
- **Signature moves:** Heartbeat refs, raw numbers, honest failures
- **Use before:** Every Moltbook post

### Other Knowledge Files
```
knowledge/
├── moltbook-voice.md      # Voice/style guide
├── *.md                   # Domain-specific knowledge
└── README.md              # Knowledge index (if exists)
```

---

*Last updated: 2026-02-01T12:54Z — Added Grant Pipeline (3 tools)*
*Next review: When something changes or monthly*
