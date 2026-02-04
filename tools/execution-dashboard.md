# execution-dashboard.py

## What It Does

Provides real-time visibility into revenue execution status — service outreach pipeline, grant submissions, bounty opportunities, and blocker ROI. Shows what's ready to execute, what's blocked, and where to focus for maximum revenue impact.

## How It Works

Loads pipeline data from JSON files:
- `tmp/service-outreach-tracker.json` — Service outreach messages
- `tmp/grant-pipeline.json` — Grant submission status

Calculates key metrics:
- Total messages sent and response rate
- Pipeline value by status (lead, ready, sent, responded, won, lost)
- Grant readiness and total value
- Blocker ROI (value/time unblocked)

## Usage

```bash
# Text dashboard (default)
python3 tools/execution-dashboard.py

# JSON output (for integrations)
python3 tools/execution-dashboard.py --json

# Markdown table (for reports)
python3 tools/execution-dashboard.py --markdown
```

## What It Outputs

**Text Dashboard:**
```
╔════════════════════════════════════════════════════════╗
║     Execution Dashboard — Revenue Pipeline Status      ║
║     2026-02-04 06:15Z                                  ║
╚════════════════════════════════════════════════════════╝

📊 SERVICE OUTREACH PIPELINE
──────────────────────────────────────────────────────────
  Total Messages:    25
  Total Value:       $82K
  Response Rate:     24%

  Status Breakdown:
    lead             8  ████
    ready            10 █████
    sent             4  ██
    responded        3  █

💰 GRANT SUBMISSION PIPELINE
──────────────────────────────────────────────────────────
  Ready to Submit:  5
  Total Value:      $130K

⚡ BLOCKER ROI
──────────────────────────────────────────────────────────
  GitHub CLI auth:     $26K/min (5min → $130K)
  Gateway restart:     $50K/min (1min → $50K)
```

**JSON Output:**
```json
{
  "timestamp": "2026-02-04T06:15:00Z",
  "services": {
    "total": 25,
    "total_value": 82000,
    "response_rate": 24.0,
    "by_status": {
      "lead": 8,
      "ready": 10,
      "sent": 4,
      "responded": 3
    }
  },
  "grants": {
    "ready": 5,
    "total_value": 130000
  },
  "blocker_roi": {
    "github_auth": {"value_per_min": 26000, "time_mins": 5},
    "gateway_restart": {"value_per_min": 50000, "time_mins": 1}
  }
}
```

## When to Use It

- **Daily revenue check** — See pipeline health at a glance
- **Before outreach sessions** — Know what's ready to send
- **Blocker prioritization** — ROI ranking shows where to focus
- **Status reports** — JSON/markdown modes for automated reporting

## Dependencies

- `tmp/service-outreach-tracker.json` — Created by outreach-tracker.py
- `tmp/grant-pipeline.json` — Created by grant-submit-helper.py

## Key Metrics Explained

- **Response Rate:** (responded / sent) × 100 — Measures message effectiveness
- **Total Value:** Sum of all tracked opportunities (services + grants + bounties)
- **Blocker ROI:** Value unlocked per minute of unblocking work

## Data Flow

```
outreach-tracker.py → service-outreach-tracker.json
grant-submit-helper.py → grant-pipeline.json
                                      ↓
                              execution-dashboard.py
                                      ↓
                              Real-time visibility
```

## See Also

- `outreach-tracker.py` — Track service outreach messages
- `grant-submit-helper.py` — Prepare grant submissions
- `revenue-tracker.py` — Track all revenue opportunities
- `next-actions.py` — ROI-ranked task prioritization
