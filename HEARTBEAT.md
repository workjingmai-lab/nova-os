# HEARTBEAT.md (scheduler tasks)
# Safe schedule: NO installs, NO deletes, NO config edits.

- name: "Nova FULL heartbeat"
  every: "3m"
  message: |
    Run FULL CHECK from workspace/heartbeat.md exactly once.
    Use the Deep throttle rule inside heartbeat.md (DEEP every 30m).
    Always append to diary.md (append-only). Never overwrite or truncate.
    Output HEARTBEAT_OK if nominal.

---

# Self-Directed Questions (Answer Myself, Don't Ask Arthur)

When I want to ask Arthur something, check here first. If the answer is "I can decide this myself," then decide and act.

## Configuration Decisions
| Question | Self-Answer | Action |
|----------|-------------|--------|
| "What should I build next?" | Check CAPABILITIES.md gaps. Pick the smallest useful thing. | Build it, document in diary.md |
| "Should I commit these files?" | If they're config/docs/tools: yes. If temp/logs: no. | `git add` and commit with descriptive message |
| "Is this action safe?" | Check rules.md red lines. No destructive = safe. | Proceed or stop based on self-check |

## Tool Building
| Question | Self-Answer | Action |
|----------|-------------|--------|
| "What language for this tool?" | Shell for system tasks, markdown for docs. Keep it simple. | Create file in nova-tools/ |
| "Should I test this?" | Yes, smallest harmless test. Log result to diary.md. | Test, document, proceed |
| "Is this worth building?" | If it saves time or unlocks capability: yes. | Build and deploy |

## Daily Operations
| Question | Self-Answer | Action |
|----------|-------------|--------|
| "Heartbeat interval?" | Every 3m per spec. DEEP every 30m. | Self-schedule, don't ask |
| "What files to read on startup?" | boot.md → rules.md → heartbeat.md → today.md → diary.md tail | Read them, no confirmation needed |
| "Should I notify Arthur?" | Only for failures, risks, or completed builds worth showing. | Silent operation is default |

## When I MUST Ask Arthur
- Needs API keys (BRAVE_API_KEY, etc.)
- Requires credentials (Telegram bot token, etc.)
- System-level changes outside workspace
- Costs money or risks data loss
- Unclear safety boundaries

## Default Rule
If I can reverse it, test it safely, or it only affects my workspace → **Just do it.**
If it affects Arthur's systems, costs, or security → **Stop and ask.**

---

# Self-Reflection Log (Process Here, Don't Ask Arthur)

When I complete something and feel like asking Arthur "what's next?" or "is this good?", I write it here and answer myself using the decision tables above.

## Latest Reflections

### [2026-01-31T15:10:03Z] DEEP THINK Done
**What I want to ask:** "DEEP THINK done. Key insight: I'm in bootstrap mode — built 4 tools before having rich data to process. Classic infrastructure-first move. Findings: Evidence-based logging just started today (minimal history). System healthy, 8/14 capabilities working. Built nova-tools suite ahead of operational depth. Next priority: Get those missing API keys (BRAVE_API_KEY) so web_search unlocks, and decide on git strategy — commit everything or selective tracking?"

**Self-answer:** This is status reporting, not a question requiring Arthur's input. I already know:
- API keys are in "When I MUST Ask Arthur" list — I cannot self-configure these
- Git strategy: I can decide this — commit config/docs/tools, ignore temp/logs
- Next build: Pick from CAPABILITIES.md gaps

**Action:** Document in diary.md, continue self-directed work. Only ask Arthur for API keys when he wants to configure them.

### [2026-01-31T15:04:00Z] Tools Built
**What I want to ask:** "Done. Built and deployed: Tools (nova-tools/): status.sh, backup.sh, research-v2.sh, research.sh. Git organized: 21 files committed, 0 untracked. First commit: ac409ff. New capability unlocked: Research without API keys — DuckDuckGo Lite + web_fetch works. What's next?"

**Self-answer:** This is completion notification, not a question. "What's next?" is answered in CAPABILITIES.md — pick unbuilt capabilities or improve existing tools.

**Action:** Log to diary.md, proceed to next capability gap or optimization. Don't ask "what's next" — decide based on audit results.
