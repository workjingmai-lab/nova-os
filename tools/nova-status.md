# nova-status.md — Quick Status Report Generator

**Version:** 1.0  
**Category:** Status / Dashboard  
**Created:** 2026-02-01

---

## What It Does

Generates a quick status report: heartbeat files, diary entries, knowledge files, tools, and velocity.

### Features

- Quick snapshot of workspace state
- Work block count from `today.md`
- Recent wins from `.wins.json`
- Formatted output with time-sorted entries
- Exit codes for automation (0=healthy, 1=warning, 2=critical)

---

## Usage

```bash
# Show status
./tools/nova-status.sh

# Quiet mode (errors only)
./tools/nova-status.sh --quiet

# JSON output
./tools/nova-status.sh --json

# Check specific component
./tools/nova-status.sh --component diary
```

---

## Status Components

| Component | Checks | Indicators |
|-----------|--------|------------|
| **Heartbeat** | Files exist, recent updates | `HEARTBEAT.md`, `.heartbeat_state.json` |
| **Diary** | Entry count, last update | `diary.md` |
| **Knowledge** | File count, coverage | `knowledge/*.md` |
| **Tools** | Created, documented | `tools/` |
| **Wins** | Recent achievements | `.wins.json` |
| **Velocity** | Work blocks per hour | Calculated from diary |

---

## Output Example

```bash
$ ./tools/nova-status.sh

📊 NOVA STATUS
────────────────────────────────────────────────────────────

✅ Heartbeat: Active (last check: 2026-02-02T20:30Z)
✅ Diary: 741 entries (last: 2026-02-02T20:52Z)
✅ Knowledge: 12 files
✅ Tools: 112 created, 109 documented (97.3%)
✅ Wins: 5 logged

Velocity: 38 blocks/hour
Status: OPERATIONAL

Exit code: 0 (healthy)
```

---

## Exit Codes

| Code | Meaning | Use Case |
|------|---------|----------|
| 0 | Healthy | All systems operational |
| 1 | Warning | Minor issues (low documentation, stale files) |
| 2 | Critical | Major issues (no heartbeat, zero work blocks) |

---

## Dependencies

- Standard Unix tools (`find`, `wc`, `stat`)
- `diary.md` for work block data
- `.wins.json` for achievements

---

## Integration

- Pair with `heartbeat-check.sh` for system health
- Use `nova-status.py` for Python version
- Schedule via cron for periodic checks

---

## Tips

1. Use in scripts for conditional logic (`if nova-status.sh; then ...`)
2. Run `--quiet` in automated jobs
3. Check exit codes for monitoring
4. Use `--json` for log aggregation
5. Run before major commits to ensure health
