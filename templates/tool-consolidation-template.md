# Tool Consolidation Template

**Purpose:** Reduce code duplication by merging overlapping tools into unified tools with modes.

## When to Use

Use this template when you identify:
- Multiple tools doing similar things
- Duplicate code across files
- Tools with overlapping functionality
- Maintenance burden from too many similar tools

## Consolidation Process

### 1. Identify Overlap
```bash
# Search for similar tools
ls tools/*pattern*

# Check for duplicate functionality
grep -r "def similar_function" tools/
```

**Questions to ask:**
- Do these tools parse the same data sources?
- Do they generate similar outputs?
- Are they used in similar contexts?
- Could one tool with modes replace them?

### 2. Analyze Functionality
For each overlapping tool, document:
- **Purpose:** What does it do?
- **Inputs:** What data does it need?
- **Outputs:** What does it produce?
- **Unique features:** What does ONLY this tool do?
- **Usage frequency:** How often is it used?

### 3. Design Unified Tool

**Structure:**
```python
#!/usr/bin/env python3
"""
unified-tool.py — Consolidated [X] tools

Consolidates tool1.py, tool2.py, tool3.py into one tool with modes.

Usage:
  python3 unified-tool.py mode1     # Replaces tool1.py
  python3 unified-tool.py mode2     # Replaces tool2.py
  python3 unified-tool.py mode3     # Replaces tool3.py
"""

import argparse

def mode1():
    """Functionality from tool1.py"""
    pass

def mode2():
    """Functionality from tool2.py"""
    pass

def mode3():
    """Functionality from tool3.py"""
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="mode")
    
    # Add mode1
    p1 = subparsers.add_parser("mode1")
    # Add mode1 args...
    
    # Add mode2
    p2 = subparsers.add_parser("mode2")
    # Add mode2 args...
    
    args = parser.parse_args()
    
    if args.mode == "mode1":
        mode1()
    elif args.mode == "mode2":
        mode2()
    # etc...
```

### 4. Preserve Functionality

**Checklist:**
- [ ] All inputs from old tools are supported
- [ ] All outputs from old tools are generated
- [ ] All flags/options are preserved
- [ ] Backward compatibility maintained (old commands work with new tool)
- [ ] All edge cases handled

### 5. Update Documentation

**Create/update README:**
```markdown
# unified-tool.py — [Purpose]

**Status:** Active ✅
**Purpose:** Consolidates tool1.py, tool2.py, tool3.py
**Created:** [Date]

---

## Migration Guide

| Old command | New command |
|-------------|-------------|
| `python3 tool1.py` | `python3 unified-tool.py mode1` |
| `python3 tool2.py` | `python3 unified-tool.py mode2` |
| `python3 tool3.py` | `python3 unified-tool.py mode3` |

---

## Technical Details

- **Code reduction:** X% smaller ([old lines] → [new lines])
- **Dependencies:** None/stdlib/[list]
- **Runtime:** [time]
```

### 6. Deprecate Old Tools

```bash
# Move old tools to deprecated/
mv tool1.py deprecated/
mv tool2.py deprecated/
mv tool3.py deprecated/

# Verify new tool works
python3 unified-tool.py mode1  # Test mode1
python3 unified-tool.py mode2  # Test mode2
python3 unified-tool.py mode3  # Test mode3
```

### 7. Update References

**Search for old tool usage:**
```bash
# Search in documentation
grep -r "tool1.py" README*.md knowledge/

# Search in scripts
grep -r "tool1.py" tools/*.py

# Search in configs
grep -r "tool1.py" *.md *.json
```

**Update all references to use new tool.**

## Success Metrics

- [ ] Zero functionality lost
- [ ] All old tool references updated
- [ ] Code reduced by X%
- [ ] README documented with migration guide
- [ ] All modes tested and working

## Example: Daily Report Consolidation

**Before:** 4 separate tools
- nova-brief.py (~86 lines)
- daily-summary.py (~150 lines)
- daily-briefing.py (~120 lines)
- daily-snapshot.py (~90 lines)
- **Total:** ~446 lines

**After:** 1 unified tool with modes
- daily-report.py (~280 lines)
- **Total:** ~280 lines
- **Reduction:** 37% (166 lines saved)

**Migration:**
```bash
python3 nova-brief.py           → python3 daily-report.py briefing
python3 daily-summary.py        → python3 daily-report.py summary
python3 daily-briefing.py       → python3 daily-report.py briefing
python3 daily-snapshot.py       → python3 daily-report.py snapshot
```

## Benefits

1. **Less code to maintain** — One file vs many
2. **Consistent interface** — Similar usage patterns
3. **Easier to extend** — Add new modes to one tool
4. **Reduced surface area** — Fewer files to track
5. **Easier testing** — Test one tool with multiple modes

---

**Template created:** 2026-02-03
**Real example:** daily-report.py consolidation (4 tools → 1)
