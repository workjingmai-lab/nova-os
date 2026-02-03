# heartbeat-check.sh — System Health Monitor

## What It Does

Monitors OpenClaw system vitals and returns exit codes for automated health checks. Checks disk space, CPU load, gateway process, and memory usage.

## Usage

```bash
./tools/heartbeat-check.sh
```

**Exit codes:**
- `0` = Healthy ✅
- `1` = Warning ⚠️
- `2` = Critical 🚨

## Checks Performed

| Check | Warning | Critical |
|-------|---------|----------|
| Disk usage (root) | ≥80% | ≥95% |
| CPU load (1-min avg) | >cores × 2 | >cores × 4 |
| Memory usage | ≥80% | ≥90% |
| Gateway process | Not running | — |

## Output Format

```
---
[HEALTH CHECK] 2026-02-02T20:30:00Z

## Disk
  Filesystem      Size  Used Avail Use% Mounted on
  /dev/root        50G   30G   20G  60% /
  Usage: 60%

## Load
  20:30:00 up 7 days, 2:15, 2 users, load average: 0.50, 0.45, 0.40
  Cores: 4
  Load: 0.50 (warn: >8.00, crit: >16.00)

## Gateway
  Status: healthy
  PID: 12345
  Memory: 456MB

## Memory
  Total: 16384 MB
  Used: 8192 MB (50%)

## Summary
  Status: HEALTHY ✅
  All checks passed

HEARTBEAT_OK

[EXIT CODE: 0]
```

## Configuration

Edit thresholds at top of script:

```bash
DISK_WARNING=80
DISK_CRITICAL=95
LOAD_WARNING_MULT=2
LOAD_CRITICAL_MULT=4
GATEWAY_PROCESS="openclaw"
```

## Integration

**Cron-friendly:** Can be called from cron jobs; exit codes trigger alerts.
**Heartbeat-compatible:** Outputs `HEARTBEAT_OK`, `HEARTBEAT_WARNING`, `HEARTBEAT_CRITICAL` for parsing.

## Why This Matters

Catches issues before they become outages. Disk fills, load spikes, and gateway crashes are silent killers — this tool gives you a 60-second pulse on system health.

Created: 2026-02-01 | Part of Week 2 tool creation goals
