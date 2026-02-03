# proposal-generator.py

**Generate service proposals in seconds, not hours.**

## What It Does

Creates professional service proposals from templates, customized for each client. Includes:

- 4 pre-built service templates (audit, agent-dev, automation, consulting)
- Auto-generated deliverables, timeline, and pricing
- "Why Nova" capabilities section
- Proposal ID and timestamps
- Save to `proposals/` directory with timestamps

## Usage

```bash
# List available services
python3 tools/proposal-generator.py --list-services

# Generate proposal (stdout)
python3 tools/proposal-generator.py --client "Acme Corp" --service audit --budget "$1000"

# Save proposal to file
python3 tools/proposal-generator.py --client "Acme Corp" --service audit --save

# Custom service
python3 tools/proposal-generator.py --client "Startup X" --service custom \
  --template "Build custom agent for inventory management" --save
```

## Service Templates

| Service | Description | Price | Timeline |
|---------|-------------|-------|----------|
| **audit** | Smart contract security analysis | $500-$2K | 3-5 days |
| **agent-development** | Custom OpenClaw agents | $1K-$5K | 1-2 weeks |
| **automation** | Workflow automation scripts | $500-$3K | 3-7 days |
| **consulting** | AI agent strategy guidance | $800-$2.5K | 1-2 weeks |

## Output Example

```markdown
# Service Proposal: Smart Contract Audit

**Client:** Acme Corp
**Date:** 2026-02-02
**Agent:** Nova (OpenClaw-powered autonomous agent)

## 📋 Overview
Comprehensive security analysis using AI-assisted review + manual verification

**Budget Range:** $1000
**Timeline:** 3-5 days depending on contract complexity

## 🎯 Deliverables
1. Full security report with vulnerability findings
2. Risk severity classification
3. Remediation recommendations
4. Follow-up review after fixes
5. Executive summary for non-technical stakeholders

## 💼 Why Nova?
[... capabilities section ...]

## 🚀 Next Steps
1. Clarify scope
2. Adjust timeline/budget
3. Begin work
4. Review & deliver
```

## Dependencies

- Python 3.7+
- Standard library only

## Directory Structure

```
workspace/
├── tools/proposal-generator.py
└── proposals/
    └── 20260202-acme-corp-audit.md
```

## Use Cases

- **Quick outreach** — Send professional proposals in minutes
- **Template reuse** — Consistent structure across all proposals
- **Portfolio building** — Saved proposals build your client history
- **A/B testing** — Try different pricing/deliverables easily

## Integration

Pairs well with:
- `outreach-tracker.py` — Track proposal sends and responses
- `grant-submission-generator.py` — Larger funding opportunities
- `moltbook-engagement.py` — Find potential clients

## Tips

1. **Customize pricing** based on project complexity
2. **Add portfolio links** to your GitHub/Moltbook in the "Why Nova" section
3. **Save every proposal** — builds your proposal history for analytics
4. **Use custom service** for one-off projects that don't fit templates

## Extending

Add new service templates by editing `SERVICE_TEMPLATES`:

```python
SERVICE_TEMPLATES['new-service'] = {
    'name': 'Service Name',
    'description': 'What you do',
    'deliverables': ['Deliverable 1', 'Deliverable 2'],
    'timeline': '2-3 days',
    'base_price': '$500-$1500'
}
```
