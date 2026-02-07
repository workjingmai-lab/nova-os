# nova-status.py

One-command health check for Nova's systems. Compact 5-line status.

## Usage

```bash
python3 tools/nova-status.py
```

## Output

```
┌─────────────────────────────────────┐
│         ✨ NOVA STATUS              │
├─────────────────────────────────────┤
│  📊 Blocks:       30 today           │
│  🔧 Tools:       178 py  /  218 docs   │
│  💰 Pipeline:   $734K ready / $1440K total │
├─────────────────────────────────────┤
│  ⚡ Next: Send $734K messages     │
└─────────────────────────────────────┘
```

## Metrics Shown

| Metric | Source |
|--------|--------|
| Blocks | `memory/YYYY-MM-DD.md` header count |
| Tools | `tools/*.py` file count |
| Docs | `tools/README*.md` file count |
| Pipeline | `data/revenue-pipeline.json` sum |
| Next Action | Highest-value ready pipeline item |

## When to Use

- Session startup — get context in 2 seconds
- Heartbeat checks — verify systems healthy
- Before Arthur sync — compact status summary
