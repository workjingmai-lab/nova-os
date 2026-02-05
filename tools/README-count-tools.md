# count-tools.py

Quick count of tools and documentation coverage in the workspace.

## What It Does

Counts all Python files in `tools/` directory and checks how many have corresponding README files. Shows documentation coverage percentage.

## Usage

```bash
python3 tools/count-tools.py
```

## Output

```
📊 Tool Statistics:
   Total tools: 102
   Documented: 89
   Coverage: 87.3%
   Undocumented: 13
```

## Use Cases

- **Track documentation progress:** See how many tools have READMEs
- **Identify gaps:** Find tools that need documentation
- **Quality metric:** Maintain 100% documentation goal

## Notes

- Excludes `__init__.py` and self from count
- Looks for `README-{toolname}.md` files
- Coverage = (documented / total) × 100%

## Example

```bash
# Quick documentation check
python3 tools/count-tools.py
# → Coverage: 87.3% (13 tools need READMEs)
```

---

**Created:** 2026-02-05 (Work block 1895)
**Category:** Analytics / Documentation
**Status:** Active
