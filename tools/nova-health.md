# nova-health.py

**Automated health check for Nova monitoring.**

## Purpose

Returns exit code for automated monitoring systems (cron, CI, etc.)

## Usage

```bash
python3 tools/nova-health.py
# or
./tools/nova-health.py
```

## Exit Codes

| Code | Meaning | Action |
|------|---------|--------|
| `0` | System healthy | None |
| `1` | System failure | Investigate |

## Sample Output

```
HEALTH_OK: System operational, external blockers present
```

## Cron Integration

```bash
# Add to crontab for automated health checks
*/15 * * * * cd /workspace && python3 tools/nova-health.py || echo "Nova health check failed" | mail admin
```

## Created

Work block 3092 — 2026-02-07
