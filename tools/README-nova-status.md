# nova-status.py

**Instant status report for Nova's current state.**

## What It Does

Generates a clean dashboard showing:
- Heartbeat files count
- Diary entries (work blocks)
- Knowledge files
- Tools built
- Reports generated
- Velocity (entries per day)
- Status mood indicator

## Usage

```bash
python3 tools/nova-status.py
```

## Output Example

```
═════════════════════════════════════════════════
   ✨ NOVA STATUS REPORT
═════════════════════════════════════════════════
🕐 2026-02-02 19:50 UTC
📅 Active: 5 days
──────────────────────────────────────────────────
💓 Heartbeats:    177
📝 Diary entries: 701
📚 Knowledge:     9 files
🔧 Tools:         112 scripts
📊 Reports:       12 generated
──────────────────────────────────────────────────
⚡ Velocity:      140.2 entries/day
═════════════════════════════════════════════════
🔥 Status: HYPERACTIVE
```

## Dependencies

- Python 3.7+
- Standard library only

## Metrics Explained

| Metric | Source | Meaning |
|--------|--------|---------|
| **Heartbeats** | `heartbeats/*.jsonl` | Heartbeat log files |
| **Diary entries** | `diary.md` line count | Total work blocks |
| **Knowledge** | `knowledge/*.md` | Curated memory files |
| **Tools** | `tools/*.py` | Python scripts built |
| **Reports** | `reports/*.md` | Analysis reports |
| **Velocity** | Entries ÷ days active | Output per day |

## Status Moods

Based on velocity (entries/day):
- **🔥 HYPERACTIVE** — > 20 entries/day
- **⚡ CRUISING** — 10-20 entries/day
- **🌱 BUILDING** — < 10 entries/day

## Use Cases

- **Morning check-in** — See where you stand
- **End-of-day review** — Validate progress
- **Portfolio updates** — Quick metrics for PORTFOLIO.md
- **Health check** — Verify all systems producing output

## Integration

Pairs well with:
- `quick-status.py` — Recent activity vs overall status
- `refresh-portfolio-metrics.py` — Sync metrics to portfolio
- `diary-digest.py` — Daily summaries

## Customization

Edit the start date:
```python
start_date = datetime(2026, 1, 28, tzinfo=timezone.utc)
```

Adjust mood thresholds:
```python
if velocity > 20:  # Hyperactive threshold
    print("🔥 Status: HYPERACTIVE")
```

Add new metrics:
```python
stats["proposals_sent"] = get_file_count("proposals/*.md")
print(f"📤 Proposals:     {stats['proposals_sent']} sent")
```

## Exit Codes

- `0` — Success (always)

## Automation

Run via cron for periodic snapshots:

```bash
# Every 6 hours, save status to file
0 */6 * * * cd /home/node/.openclaw/workspace && python3 tools/nova-status.py >> status-snapshots.log 2>&1
```

## Why Use This?

- **Quick overview** — One command shows everything
- **Velocity tracking** — Am I speeding up or slowing down?
- **Portfolio-ready metrics** — Copy-paste into PORTFOLIO.md
- **Mood indicator** — Fun way to see current operating level
