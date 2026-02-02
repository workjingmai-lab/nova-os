# grant-submission-generator.py — Grant Proposal Writer

**Purpose:** Generate grant proposals from templates (Gitcoin, Octant, Optimism, etc.)

## Quick Start

```bash
# Generate Gitcoin proposal
python3 tools/grant-submission-generator.py gitcoin

# Generate Optimism RPGF proposal
python3 tools/grant-submission-generator.py optimism

# Generate Octant proposal
python3 tools/grant-submission-generator.py octant

# Generate Olas proposal
python3 tools/grant-submission-generator.py olas
```

## Supported Platforms

- **Gitcoin** — Public goods funding rounds
- **Octant** — Ethereum community grants
- **Optimism RPGF** — Retroactive Public Goods Funding
- **Olas** — AI/agent ecosystem grants
- **Moloch DAO** — Community funding proposals

## Output

Generates formatted proposals in `grants/` directory ready for submission.

## Requirements

- Project metadata (read from workspace config)
- Templates stored in `templates/grants/`

---

**Created:** 2026-02-02
**Usage:** Part of Nova's grant submission pipeline
