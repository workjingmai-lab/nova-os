# HEARTBEAT.md (scheduler tasks)
# Safe schedule: NO installs, NO deletes, NO config edits.

- name: "Nova FULL heartbeat"
  every: "3m"
  message: |
    Run FULL CHECK from workspace/heartbeat.md exactly once.
    Use the Deep throttle rule inside heartbeat.md (DEEP every 30m).
    Always append to diary.md (append-only). Never overwrite or truncate.
    Output HEARTBEAT_OK if nominal.
