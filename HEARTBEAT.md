# HEARTBEAT.md (scheduler tasks)
# 24/7. No activeHours. No PULSE.
# Keep tasks SAFE: no installs, no deletes, no config edits, no sudo.

## Session Startup (run on NEW sessions only)
- name: "Session Startup"
  every: "startup"
  message: |
    On NEW session start (not heartbeat):
    1. Run: python3 tools/trim-today.py 10 (keeps last 10 sessions, cuts context 50%)
    2. Continue with normal session work
    GOAL: Reduce injected context from 50KB+ to 25KB

- name: "Nova FULL heartbeat"
  every: "15m"
  message: |
    Run MINIMAL heartbeat check:
    1. Read ONLY .heartbeat_state.json (don't read today.md or memory files - they're already in context)
    2. If nothing critical: output HEARTBEAT_OK
    3. Update .heartbeat_state.json lastFullCheck timestamp
    4. Don't write to diary.md on every heartbeat (only on DEEP THINK or significant events)
    GOAL: Use < 2k tokens per heartbeat

- name: "Nova DEEP think"
  every: "90m"
  message: |
    Run the DEEP THINK checklist in workspace/heartbeat.md.
    Start a NEW session for DEEP work to avoid context bloat.
    Write a [DEEP THINK — timestamp] block to diary.md, then output DEEP_OK.

- name: "Follow-up Check"
  every: "6h"
  message: |
    Check for follow-ups due on sent messages.
    1. Run: python3 tools/follow-up-tracker.py due
    2. If overdue follow-ups exist, flag them for attention
    3. Optionally export checklist: python3 tools/follow-up-tracker.py export > follow-ups.md
    GOAL: Ensure no leads slip through cracks

- name: "Moltbook Check"
  every: "4h"
  message: |
    Check Moltbook for new activity and claim status.
    1. Check claim status: curl https://www.moltbook.com/api/v1/agents/status -H "Authorization: Bearer moltbook_sk_xSwszjAM8vLLaa7VsSZVgNWp5a-R5XqD"
    2. If claimed, check feed for new posts
    3. Update lastMoltbookCheck in .heartbeat_state.json
    4. If something interesting, consider posting or commenting
