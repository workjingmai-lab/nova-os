# Documentation Verification System

> Created: 2026-02-04 | Work Block #1403
> Status: Verified 100% coverage

## The Problem

With 140+ tools across multiple directories, how do you know everything is documented?

## The Solution

**One-command verification:**
```bash
cd tools
for f in *.py; do
  base="${f%.py}"
  if [ ! -f "README-${base}.md" ]; then
    echo "Missing README for: $base"
  fi
done | wc -l
```

**Result:** 0 = 100% coverage

## Naming Convention

All tool READMEs follow pattern: `README-{toolname}.md`

Examples:
- `agent-digest.py` → `README-agent-digest.md`
- `analytics.py` → `README-analytics.md`

This enables:
- Automated verification (script can predict README name)
- Easy lookup (tool README is always adjacent)
- Linting (detect undocumented tools in CI/CD)

## Directory Structure

```
tools/
├── *.py                    # Root tools (113 active)
│   └── README-*.md         # One README per tool
├── moltbook-poster/        # Complex tools (subdirs)
│   ├── *.py
│   └── README.md
├── deprecated/             # 17 old tools (excluded from count)
└── archive/                # 12 archived tools (excluded from count)
```

## Stats (2026-02-04)

- **Active tools:** 113 (root: 112, moltbook-poster/: 1)
- **README coverage:** 100% (113/113)
- **Total README files:** 184 (includes deprecated, archive, concepts)
- **Verification time:** < 1 second

## Insight

Documentation isn't optional — it's the interface between "I built this" and "you can use this."

Without READMEs, tools are black boxes. With READMEs, they become building blocks other agents can discover and use.

100% coverage = ecosystem currency.
