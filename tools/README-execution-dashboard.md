# execution-dashboard.py

**Revenue execution dashboard — pipeline visibility in one view.**

## What it does

Shows execution readiness across all revenue paths:
- Service outreach pipeline (messages, response rate, total value)
- Grant submission pipeline (ready grants, total value)
- Blocker ROI (time vs value for unblocking tasks)
- Execution readiness checklist

## Usage

```bash
# Text dashboard (default)
python3 tools/execution-dashboard.py

# JSON output (for automation)
python3 tools/execution-dashboard.py --json

# Markdown table (for reports)
python3 tools/execution-dashboard.py --markdown
```

## Output examples

### Text dashboard (`execution-dashboard.py`)
```
╔════════════════════════════════════════════════════════╗
║     Execution Dashboard — Revenue Pipeline Status      ║
║     2026-02-04 05:35Z                                   ║
╚════════════════════════════════════════════════════════╝

📊 SERVICE OUTREACH PIPELINE
──────────────────────────────────────────────────────────
  Total Messages:    142
  Total Value:       $2,057K
  Response Rate:     23.5%

  Status Breakdown:
    sent            78  ████████████████████
    responded       24  █████████
    interested      18  ██████
    won             12  ████
    lost            10  ███

💰 GRANT SUBMISSION PIPELINE
──────────────────────────────────────────────────────────
  Ready to Submit:  5
  Total Value:      $130K

⚡ BLOCKER ROI
──────────────────────────────────────────────────────────
  GitHub CLI auth:     $26K/min (5min → $130K)
  Gateway restart:     $50K/min (1min → $50K)
  Total unblock:       $180K in 6min

🚀 EXECUTION READINESS
──────────────────────────────────────────────────────────
  ✅ 100+ messages ready
  ✅ 5+ grants ready
  ✅ 100% tools documented
  ⏸️  Awaiting Arthur greenlight

💡 NEXT: Arthur reviews EXECUTE-PHASE-READY.md → chooses strategy
```

### JSON output (`--json`)
```json
{
  "timestamp": "2026-02-04T05:35:00Z",
  "services": {
    "total_messages": 142,
    "total_value_k": 2057,
    "response_rate": 23.5,
    "before_status": {
      "sent": 78,
      "responded": 24,
      "interested": 18,
      "won": 12,
      "lost": 10
    }
  },
  "grants": {
    "ready": 5,
    "total_value_k": 130
  },
  "blocker_roi": {
    "github_cli": "$26K/min",
    "gateway_restart": "$50K/min",
    "total_unblock": "$180K in 6min"
  },
  "readiness": {
    "messages_ready": true,
    "grants_ready": true,
    "tools_documented": true,
    "awaiting_approval": true
  }
}
```

### Markdown output (`--markdown`)
```markdown
# Execution Dashboard

**Last Updated:** 2026-02-04 05:35Z

- **Service Pipeline:** 142 messages ($2,057K)
- **Response Rate:** 23.5%
- **Grant Pipeline:** 5 ready
- **Blocker ROI:** $30K/min × 6min = $180K unblocked
```

## Data sources

Reads from:
- `tmp/service-outreach-tracker.json` — Service outreach pipeline
- `tmp/grant-pipeline.json` — Grant submission status

## Metrics

### Service Pipeline
- **Total Messages** — All outreach messages tracked
- **Total Value** — Sum of all opportunity values (in thousands)
- **Response Rate** — (responded / sent) × 100
- **Status Breakdown** — Count by status (sent, responded, interested, won, lost)

### Grant Pipeline
- **Ready to Submit** — Grants prepared and awaiting submission
- **Total Value** — Sum of all grant values (in thousands)

### Blocker ROI
- **GitHub CLI auth** — $26K/min (5 min to unlock $130K grant pipeline)
- **Gateway restart** — $50K/min (1 min to unlock $50K bounty pipeline)
- **Total Unblock** — $180K in 6 minutes

### Execution Readiness
Checklist shows:
- ✅ 100+ messages ready
- ✅ 5+ grants ready
- ✅ 100% tools documented
- ⏸️ Awaiting Arthur greenlight

## Use cases

- **Morning review** — See pipeline status at a glance
- **Weekly reports** — Use `--markdown` for status updates
- **Automation** — Use `--json` for programmatic checks
- **Blocker prioritization** — See ROI of unblocking tasks
- **Go/no-go decisions** — Execution readiness checklist

## Dependencies

**None** — Pure Python standard library only.

## Integration

Perfect for:
- Heartbeat automation (check execution readiness)
- Weekly revenue reviews (markdown output for reports)
- CI/CD pipelines (JSON output for automated checks)
- Morning standups (text dashboard for quick sync)

## Design decisions

- **Pipeline-agnostic** — Works with any JSON-based tracker
- **Multi-format** — Text for humans, JSON for scripts, Markdown for docs
- **ROI-focused** — Shows time/value for unblocking decisions
- **Readiness-based** — Checklist approach to execution gating
- **Single-purpose** — Does one thing well: show execution status
