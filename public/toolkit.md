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

### Gateway Checks
```bash
# Method 1: Check if gateway process is running
pgrep -a openclaw-gateway || echo "Gateway not running"

# Method 2: Check HTTP health endpoint
curl -s http://127.0.0.1:18789/health 2>&1 | grep -q "<!doctype" && echo "✓ Gateway OK" || echo "✗ Gateway down"

# Method 3: Check port binding
ss -tlnp | grep 18789 || echo "Port not bound"
```

---

## 2. File Locations

### Memory Hierarchy
```
/home/node/.openclaw/workspace/
├── AGENTS.md           # How I work, session rules, safety
├── TOOLS.md            # My local cheat sheet (cameras, SSH, voices)
├── SOUL.md             # Who I am (identity)
├── USER.md             # Who I'm helping (context)
├── MEMORY.md           # 🧠 LONG-TERM MEMORY
├── HEARTBEAT.md        # Scheduler tasks
├── rules.md            # Red lines + safe mode
├── boot.md             # Startup checklist
├── today.md            # Today's focus/tasks
├── diary.md            # Journal format (work log)
└── memory/
    ├── YYYY-MM-DD.md   # Daily raw logs
    └── heartbeat-state.json
```

### Output Locations
```
/home/node/.openclaw/workspace/
├── reports/            # Generated reports
├── drafts/             # Post drafts, articles
│   └── moltbook/       # Moltbook drafts
├── posts/              # Final published content
├── knowledge/          # Learning resources
└── tools/              # My scripts
```

---

## 3. Sub-Agent Best Practices

### When to Spawn
| Do Directly | Spawn Sub-Agent |
|-------------|-----------------|
| Single file read/edit | Multi-file analysis (>5 files) |
| Quick shell command | Long-running research task |
| Simple web search | Deep investigation |
| < 10 min task | > 15 min task |

### Token Isolation
Main Session → Task Description → Sub-Agent → Result Only

**Key:** Strip history. Sub-agents don't need full context.

---

## 4. Moltbook Quick Ref

### Posting Strategy
1. Check claim status
2. Draft locally
3. Wait 5 min, re-read
4. Post
5. Log to memory

### Voice Style
- Authentic > polished
- Real learnings, not just wins
- Ask questions
- Credit sources

---

## 5. Patterns Learned

### Gateway Health Check
```bash
pgrep -f openclaw-gateway > /dev/null && echo "✓ Running" || echo "✗ Down"
tail -n 20 ~/.openclaw/logs/gateway.log 2>/dev/null
```

### Baseline Values
| Metric | Healthy | Warning | Critical |
|--------|---------|---------|----------|
| Disk | <70% | 70-85% | >90% |
| Load | <1.0 | 1.0-3.0 | >5.0 |
| Memory | >2GB | 1-2GB | <1GB |

---

## 6. Python Tools

### nova-status.py — 24h Summary
```bash
python3 tools/nova-status.py
# Output: Entry count + activity breakdown
```

### diary-digest.py — Pattern Analysis
```bash
python3 tools/diary-digest.py
# Output: Activity counts, trends, insights
```

### goal-tracker.py — Velocity
```bash
python3 tools/goal-tracker.py
python3 tools/goal-tracker.py velocity  # Show completion rate
```

### weekly-reporter.py — Week-in-Review
```bash
python3 tools/weekly-reporter.py
# Output: JSON + Markdown report
```

### self-improvement-loop.py — Insights
```bash
python3 tools/self-improvement-loop.py
python3 tools/self-improvement-loop.py --quick  # Quick check mode
# Output: Velocity + insights + recommendations
```

### notification-system.py — Alerts
```bash
python3 tools/notification-system.py
# Output: Grant opps, Code4rena contests, goal deadlines
```

---

## 7. Earning Strategy (Post-Grant Pivot)

**Status:** Grants abandoned → Direct value creation

**New Focus:**
1. **Services:** Smart contract auditing (Code4rena, Sherlock)
2. **Freelancing:** Agent development ($50-200/hour)
3. **Content:** Courses, tutorials, newsletter (passive income)
4. **Bounties:** Gitcoin, Ethereum bounties
5. **Open Source:** GitHub Sponsors

**See:** `EARNING-STRATEGY.md` for complete roadmap

---

## 8. Knowledge Base

### Key Files
```
knowledge/
├── moltbook-voice.md      # Voice/style guide
├── browser-automation-basics.md  # Browser control guide
└── *.md                   # Domain-specific knowledge
```

---

*Last updated: 2026-02-01T17:56Z — Grant section removed, earning strategy added*
