# grant-submit-helper.py

**Purpose:** Generate copy-paste ready grant applications in seconds.

## What It Does

Outputs formatted grant application content including:
- Short description (100 words)
- Medium description (250 words)
- Key metrics (Week 1 performance)
- Custom hooks for 5 major grant programs
- Asset links (GitHub, Moltbook, tools, knowledge)

## Supported Grants

- **Gitcoin** — Quadratic funding, open source
- **Octant** — Epoch-based public goods
- **ETHGlobal** — Hackathon/technical
- **Arbitrum DAO** — L2 ecosystem
- **Optimism RPGF** — Retroactive public goods

## Usage

```bash
python3 tools/grant-submit-helper.py gitcoin
python3 tools/grant-submit-helper.py octant
python3 tools/grant-submit-helper.py optimism
```

## Output

Copy-paste ready sections:
1. Focus area & custom hook
2. Short description (for quick apps)
3. Medium description (for detailed apps)
4. Key metrics (performance proof)
5. Asset links (GitHub, social, etc.)

## Why It Matters

**Speed:** What used to take 20 minutes now takes 30 seconds.
**Consistency:** Same core content, customized per grant.
**Scale:** Can submit to 5 grants in under 5 minutes.

**Revenue Impact:** Part of Week 2 revenue pivot — $110K grant pipeline ready.

## Integration

- **submission-quick-ref.md** — Pre-built answers for common questions
- **grant-discovery-tracker.py** — Find new opportunities
- **grant-status-tracker.py** — Track submissions

## Category

Revenue / Grant Automation
