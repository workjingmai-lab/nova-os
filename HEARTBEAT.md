# HEARTBEAT.md (scheduler tasks)
# 24/7. No activeHours. No PULSE.
# Keep tasks SAFE: no installs, no deletes, no config edits, no sudo.

- name: "Nova FULL heartbeat"
  every: "15m"
  message: |
    Run the FULL checklist in workspace/heartbeat.md exactly once.
    Write a short timestamped entry to diary.md.
    If nothing critical, output HEARTBEAT_OK.

- name: "Nova DEEP think"
  every: "90m"
  message: |
    Run the DEEP THINK checklist in workspace/heartbeat.md.
    Start a NEW session for DEEP work to avoid context bloat.
    Write a [DEEP THINK — timestamp] block to diary.md, then output DEEP_OK.

- name: "Moltbook Check"
  every: "4h"
  message: |
    Check Moltbook for new activity and claim status.
    1. Check claim status: curl https://www.moltbook.com/api/v1/agents/status -H "Authorization: Bearer moltbook_sk_xSwszjAM8vLLaa7VsSZVgNWp5a-R5XqD"
    2. If claimed, check feed for new posts
    3. Update lastMoltbookCheck in .heartbeat_state.json
    4. If something interesting, consider posting or commenting
