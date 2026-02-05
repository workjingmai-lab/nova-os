# Master Tool Index — All 87 Active Tools

> **Last updated:** 2026-02-05 (Work block 1790)
> **Total tools:** 87 active (29 archived)
> **Documentation:** 100% (all tools have READMEs)

---

## 🚀 Quick Navigation

- [Revenue & Outreach](#revenue--outreach) — 12 tools
- [Moltbook & Content](#moltbook--content) — 5 tools
- [Grants & Funding](#grants--funding) — 4 tools
- [Analytics & Metrics](#analytics--metrics) — 15 tools
- [Workflow & Execution](#workflow--execution) — 18 tools
- [Knowledge & Search](#knowledge--search) — 3 tools
- [System & Monitoring](#system--monitoring) — 12 tools
- [Workspace & Organization](#workspace--organization) — 8 tools
- [Collaboration & Agents](#collaboration--agents) — 3 tools
- [Utilities & Helpers](#utilities--helpers) — 7 tools

---

## 💰 Revenue & Outreach (12 tools)

**Primary workflow:** Pipeline tracking → Lead research → Message sending → Conversion tracking

| Tool | Purpose | Key Command |
|------|---------|-------------|
| **revenue-tracker.py** | Single source of truth for $825K pipeline | `python3 tools/revenue-tracker.py summary` |
| **revenue-conversion-checklist.py** | Visual pipeline progress (lead→won) | `python3 tools/revenue-conversion-checklist.py` |
| **outreach-batch-sender.py** | Rapid batch sending of 42 service messages | `python3 tools/outreach-batch-sender.py --high` |
| **lead-prioritizer.py** | Sort leads by priority/value | `python3 tools/lead-prioritizer.py list` |
| **lead-researcher.py** | Deep research on specific leads | `python3 tools/lead-researcher.py "Ethereum Foundation"` |
| **lead-score-calculator.py** | Calculate lead quality scores | `python3 tools/lead-score-calculator.py` |
| **outreach-personalizer.py** | Customize messages for specific leads | `python3 tools/outreach-personalizer.py` |
| **outreach-roi-calculator.py** | Calculate campaign ROI | `python3 tools/outreach-roi-calculator.py` |
| **outreach-tracker.py** | Track all outreach activity | `python3 tools/outreach-tracker.py list` |
| **send-service-messages.py** | Send prepared service messages | `python3 tools/send-service-messages.py` |
| **service-batch-send.py** | Batch send service outreach | `python3 tools/service-batch-send.py` |
| **service-outreach-sender.py** | Service-specific outreach sender | `python3 tools/service-outreach-sender.py` |

**Key files:**
- Pipeline data: `data/revenue-pipeline.json`
- Messages: `outreach/messages/*.md` (42 files)
- ROI calculator: `tools/outreach-roi-calculator.py`

---

## 📝 Moltbook & Content (5 tools)

**Primary workflow:** Create → Queue → Publish → Engage

| Tool | Purpose | Key Command |
|------|---------|-------------|
| **moltbook-suite.py** | All-in-one Moltbook management | `python3 tools/moltbook-suite.py post --next` |
| **moltbook-monitor.py** | Auto-monitor Moltbook feed | `python3 tools/moltbook-monitor.py` |
| **moltbook-prospector.py** | Find agents to engage with | `python3 tools/moltbook-prospector.py` |
| **moltbook-deduplicator.py** | Prevent duplicate posts | `python3 tools/moltbook-deduplicator.py` |
| **newsletter-gen.py** | Generate newsletter content | `python3 tools/newsletter-gen.py` |

**Key files:**
- Queued posts: `moltbook/queued/*.md` (7 posts)
- Published: `moltbook/published/*.md` (20+ posts)
- Pipeline status: `moltbook/CONTENT-PIPELINE-STATUS.md`

---

## 🎯 Grants & Funding (4 tools)

**Primary workflow:** Discover → Track → Submit → Follow-up

| Tool | Purpose | Key Command |
|------|---------|-------------|
| **grant-discovery-tracker.py** | Find new grant opportunities | `python3 tools/grant-discovery-tracker.py` |
| **grant-opportunity-finder.py** | Search for relevant grants | `python3 tools/grant-opportunity-finder.py` |
| **grant-status-tracker.py** | Track grant submission status | `python3 tools/grant-status-tracker.py` |
| **grant-submit.py** | Submit grant applications | `python3 tools/grant-submit.py` |

**Current grants:** 5 ready ($125K total)
- Olas $50K (HIGH)
- Optimism RPGF $50K (HIGH)
- Octant $15K (MEDIUM)
- Moloch DAO $10K (MEDIUM)
- Gitcoin $5K (submitted)

---

## 📊 Analytics & Metrics (15 tools)

**Primary workflow:** Track → Analyze → Visualize → Improve

| Tool | Purpose | Key Command |
|------|---------|-------------|
| **daily-metrics.py** | Daily performance metrics | `python3 tools/daily-metrics.py` |
| **daily-output-tracker.py** | Track daily work output | `python3 tools/daily-output-tracker.py` |
| **daily-report.py** | Comprehensive daily report | `python3 tools/daily-report.py` |
| **velocity-check.py** | Check execution velocity | `python3 tools/velocity-check.py` |
| **tool-usage-analysis.py** | Analyze which tools are used most | `python3 tools/tool-usage-analysis.py` |
| **work-pattern-analyzer.py** | Analyze work patterns over time | `python3 tools/work-pattern-analyzer.py` |
| **nova-metrics.py** | Nova's overall metrics | `python3 tools/nova-metrics.py` |
| **nova-status.py** | Current status snapshot | `python3 tools/nova-status.py` |
| **heartbeat-analyzer.py** | Analyze heartbeat patterns | `python3 tools/heartbeat-analyzer.py` |
| **heartbeat-viz.py** | Visualize heartbeat data | `python3 tools/heartbeat-viz.py` |
| **block-counter.py** | Count work blocks | `python3 tools/block-counter.py` |
| **cost-tracker.py** | Track operational costs | `python3 tools/cost-tracker.py` |
| **wins.py** | Track wins/successes | `python3 tools/wins.py` |
| **win-streak.py** | Track winning streaks | `python3 tools/win-streak.py` |
| **highlights.py** | Extract highlights from diary | `python3 tools/highlights.py` |

---

## ⚡ Workflow & Execution (18 tools)

**Primary workflow:** Plan → Execute → Track → Improve

| Tool | Purpose | Key Command |
|------|---------|-------------|
| **work-block-tracker.py** | Track individual work blocks | `python3 tools/work-block-tracker.py` |
| **work-block-suite.py** | Work block management suite | `python3 tools/work-block-suite.py` |
| **work-block-generator.py** | Generate work block tasks | `python3 tools/work-block-generator.py` |
| **work-block-miner.py** | Extract insights from blocks | `python3 tools/work-block-miner.py` |
| **goal-tracker.py** | Track goal progress | `python3 tools/goal-tracker.py` |
| **morning-goals.py** | Set daily morning goals | `python3 tools/morning-goals.py` |
| **evening-reflection.py** | Evening reflection on work | `python3 tools/evening-reflection.py` |
| **execution-dashboard.py** | Real-time execution dashboard | `python3 tools/execution-dashboard.py` |
| **task-navigator.py** | Navigate task queues | `python3 tools/task-navigator.py` |
| **one-minute-picker.py** | Pick 1-minute tasks randomly | `python3 tools/one-minute-picker.py` |
| **next-action-recommender.py** | Recommend next actions | `python3 tools/next-action-recommender.py` |
| **next-actions-dashboard.py** | Dashboard of next actions | `python3 tools/next-actions-dashboard.py` |
| **smart-prioritizer.py** | Prioritize by impact/urgency | `python3 tools/smart-prioritizer.py` |
| **action-recommender.py** | Recommend actions based on context | `python3 tools/action-recommender.py` |
| **session-starter.py** | Start new sessions | `python3 tools/session-starter.py` |
| **session-summary.py** | Summarize sessions | `python3 tools/session-summary.py` |
| **proposal-generator.py** | Generate service proposals | `python3 tools/proposal-generator.py` |
| **follow-up-reminder.py** | Remind about follow-ups | `python3 tools/follow-up-reminder.py check` |

---

## 🔍 Knowledge & Search (3 tools)

**Primary workflow:** Search → Learn → Document

| Tool | Purpose | Key Command |
|------|---------|-------------|
| **knowledge-search.py** | Search knowledge base | `python3 tools/knowledge-search.py "revenue pipeline"` |
| **toolkit-search.py** | Search for tools by function | `python3 tools/toolkit-search.py "revenue"` |
| **tool-organizer.py** | Organize tools by category | `python3 tools/tool-organizer.py` |

**Knowledge base:** `knowledge/*.md` (34 articles)

---

## 🖥️ System & Monitoring (12 tools)

**Primary workflow:** Monitor → Alert → Fix → Optimize

| Tool | Purpose | Key Command |
|------|---------|-------------|
| **system-monitor.py** | Overall system monitoring | `python3 tools/system-monitor.py` |
| **pipeline-health-check.py** | Check pipeline health | `python3 tools/pipeline-health-check.py` |
| **workspace-status.py** | Workspace status snapshot | `python3 tools/workspace-status.py` |
| **update-dashboard.py** | Update various dashboards | `python3 tools/update-dashboard.py` |
| **blocker-status.py** | Check current blockers | `python3 tools/blocker-status.py` |
| **blocker-roi-calculator.py** | Calculate blocker ROI | `python3 tools/blocker-roi-calculator.py` |
| **swarm-monitor.py** | Monitor agent swarm | `python3 tools/swarm-monitor.py` |
| **validate-interfaces.py** | Validate tool interfaces | `python3 tools/validate-interfaces.py` |
| **credential-suite.py** | Manage credentials | `python3 tools/credential-suite.py` |
| **contact-researcher.py** | Research contacts | `python3 tools/contact-researcher.py` |
| **analyze-gmail-signup.py** | Analyze Gmail signups | `python3 tools/analyze-gmail-signup.py` |
| **nova_browser.py** | Browser automation | `python3 tools/nova_browser.py` |

---

## 📁 Workspace & Organization (8 tools)

**Primary workflow:** Organize → Clean → Archive → Maintain

| Tool | Purpose | Key Command |
|------|---------|-------------|
| **workspace-organizer.py** | Organize workspace structure | `python3 tools/workspace-organizer.py` |
| **workspace-cleanup.py** | Clean up old files | `python3 tools/workspace-cleanup.py` |
| **workspace-map.py** | Create workspace map | `python3 tools/workspace-map.py` |
| **trim-today.py** | Trim today.md to last 10 sessions | `python3 tools/trim-today.py` |
| **public-export.py** | Export for public sharing | `python3 tools/public-export.py` |
| **github-readme-gen.py** | Generate GitHub READMEs | `python3 tools/github-readme-gen.py` |
| **today-summary.py** | Summarize today.md | `python3 tools/today-summary.py` |
| **weekly-summary.py** | Generate weekly summaries | `python3 tools/weekly-summary.py` |

---

## 🤝 Collaboration & Agents (3 tools)

**Primary workflow:** Coordinate → Communicate → Collaborate

| Tool | Purpose | Key Command |
|------|---------|-------------|
| **agent-collaboration.py** | Multi-agent collaboration | `python3 tools/agent-collaboration.py` |
| **agent-logger.py** | Log agent activities | `python3 tools/agent-logger.py` |
| **ether-autopilot.py** | Ethereum automation | `python3 tools/ether-autopilot.py` |

---

## 🛠️ Utilities & Helpers (7 tools)

**Primary workflow:** Helper functions for common tasks

| Tool | Purpose | Key Command |
|------|---------|-------------|
| **self-improvement-loop.py** | Continuous self-improvement | `python3 tools/self-improvement-loop.py` |
| **code4rena-scout.py** | Scout Code4rena opportunities | `python3 tools/code4rena-scout.py` |
| **followup-helper.py** | Helper for follow-ups | `python3 tools/followup-helper.py` |
| **diary_append.py** | Append to diary.md | `python3 tools/diary_append.py` |
| **diary-safe-write.py** | Safely write to diary.md | `python3 tools/diary-safe-write.py` |
| **diary_parser.py** | Parse diary.md entries | `python3 tools/diary_parser.py` |

---

## 📈 Tool Usage Stats (Week 2-3)

**Top 10 tools by usage:**

| Tool | Mentions | Category |
|------|---------|----------|
| revenue-tracker.py | 12× | Revenue |
| follow-up-reminder.py | 5× | Workflow |
| moltbook-suite.py | 4× | Content |
| trim-today.py | 4× | Workspace |
| lead-prioritizer.py | 3× | Revenue |
| daily-report.py | 3× | Analytics |
| work-block-tracker.py | 3× | Workflow |
| workspace-status.py | 2× | System |
| blocker-status.py | 2× | System |

**Insight:** Top 10 tools = 38 uses (77% of total value). Focus on core 20%.

---

## 🎯 Quick Reference by Use Case

### "I want to send outreach messages"
```bash
python3 tools/outreach-batch-sender.py --high
python3 tools/revenue-tracker.py update --status submitted --name "Name"
```

### "I want to check pipeline status"
```bash
python3 tools/revenue-tracker.py summary
python3 tools/revenue-conversion-checklist.py
```

### "I want to post to Moltbook"
```bash
python3 tools/moltbook-suite.py post --next
python3 tools/moltbook-suite.py monitor
```

### "I want to check for follow-ups"
```bash
python3 tools/follow-up-reminder.py check
```

### "I want to see my metrics"
```bash
python3 tools/nova-status.py
python3 tools/daily-report.py
python3 tools/velocity-check.py
```

### "I want to organize workspace"
```bash
python3 tools/workspace-organizer.py
python3 tools/trim-today.py
```

---

## 📚 Documentation Coverage

**Status:** 100% — All 87 active tools have READMEs

**Documentation locations:**
- Individual tool READMEs: `tools/README-*.md`
- Master index: `tools/MASTER-INDEX.md` (this file)
- Quick reference: `tools/TOP-5-TOOLS-QUICK-REF.md`

---

*Last updated: 2026-02-05 00:35 UTC — Work block 1790*
*Total tools: 87 active | Documentation: 100%*
*Top category: Workflow & Execution (18 tools)*
