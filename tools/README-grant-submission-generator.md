# Grant Submission Generator — Tool README

## What It Does

Generates customized grant application content for different platforms based on your project data.

## Usage

```bash
# Generate application for specific platform
python3 tools/grant-submission-generator.py gitcoin
python3 tools/grant-submission-generator.py octant
python3 tools/grant-submission-generator.py olas
python3 tools/grant-submission-generator.py ethereum
python3 tools/grant-submission-generator.py moloch

# Generate all applications
python3 tools/grant-submission-generator.py all
```

## Outputs

Applications are saved to `grants/` directory:
- `gitcoin-application.md`
- `octant-application.md`
- `olas-application.md`
- `ethereum-application.md`
- `moloch-application.md`

## Features

- **Platform-specific content:** Each platform gets customized pitch, description, and achievements
- **Word count limits:** Respects platform constraints (Gitcoin: 250, Octant: 300, etc.)
- **Tone matching:** Adjusts language to platform (technical, impact-focused, mission-aligned)
- **Keyword optimization:** Includes relevant keywords for discovery
- **Metrics integration:** Pulls real data from `metrics/self_improvement.json`
- **Template-based:** Uses `grants/submission-template.md` as base

## Supported Platforms

| Platform | Focus | Word Limit | Tone |
|----------|-------|------------|------|
| Gitcoin | Open-source infrastructure | 250 | Technical, community |
| Octant | Public goods impact | 300 | Impact-focused |
| Olas | Agent services ecosystem | 300 | Service-oriented |
| Ethereum Foundation | Ethereum tooling | 400 | Ecosystem-focused |
| Moloch DAO | Community governance | 350 | Community-aligned |

## Requirements

- `grants/submission-template.md` — Base grant template
- `metrics/self_improvement.json` — Project metrics (work blocks, achievements, velocity)

## Pipeline Integration

Part of Nova's grant submission workflow:
1. GitHub repo pushed (Arthur action)
2. `grant-submit.py` checks prerequisites
3. `grant-submission-generator.py` creates applications
4. Review and submit to platforms

## Current Status

✅ Tool operational
⏸️ Blocked by GitHub repo push (needed for submission links)

## See Also

- `tools/grant-submit.py` — Submission automation tool
- `grants/submission-quick-ref.md` — Quick reference for pitches
- `revenue-tracker.py` — Track $130K grant pipeline

---

*Created: 2026-02-02T23:48Z — Work block 772*
