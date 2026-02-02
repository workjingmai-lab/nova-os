# Proposal Generator — Quick Reference

## Installation
```bash
cp tools/proposal-generator.py ~/bin/proposal-gen  # or add to PATH
chmod +x ~/bin/proposal-gen
```

## Usage

### Basic Proposal
```bash
proposal-gen "Client Name" "Project Description" 5000
```

### With Options
```bash
proposal-gen "Client Name" "Project Description" 5000 \
  --service web-development \
  --timeline "4 weeks" \
  --tech "Python, React" \
  --deliverables "MVP, testing, docs"
```

## Service Types
- `web-development` — Full-stack apps ($2K-$15K)
- `automation` — Workflow scripts & agents ($1K-$8K)
- `data-analysis` — Logs, metrics, insights ($500-$5K)
- `integration` — API/webhook connections ($1K-$6K)
- `consulting` — Strategy & architecture ($200-$300/hr)

## Output Location
`proposals/YYYY-MM-DD-client-name.md`

## Tips
- Always include timeline for accuracy
- Use quotes for multi-word arguments
- Deliverables should be comma-separated
- Check generated draft before sending

## Example Full Command
```bash
proposal-gen "Acme Corp" "Customer dashboard with real-time analytics" 8500 \
  --service web-development \
  --timeline "6 weeks" \
  --tech "FastAPI, React, PostgreSQL" \
  --deliverables "API backend, React dashboard, data models, testing guide"
```

---

**Created:** 2026-02-01
**Tool location:** tools/proposal-generator.py
