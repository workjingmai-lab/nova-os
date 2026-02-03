# refresh-portfolio-metrics.py

**Keep PORTFOLIO.md metrics in sync with actual workspace data.**

## What It Does

Automatically updates 5 key metrics in `PORTFOLIO.md`:
1. **Work Blocks** — Total from today.md
2. **Goals Completed** — From goals/active.md
3. **Tools Built** — From tools/INDEX.md
4. **Skills Learned** — From skills.md
5. **Continuous execution** — Updates expertise section

Safe: Only updates specific lines, never touches other content.

## Usage

```bash
python3 tools/refresh-portfolio-metrics.py
```

## Output

```
Updated PORTFOLIO.md: Work Blocks -> 700; Goals Completed -> 16/16; Tools Built -> 112 (52 documented); Skills Learned -> 5 (GitHub, session-logs, weather, bluebubbles, skill-creator)
```

If no changes needed:
```
No changes needed.
```

## Dependencies

- Python 3.7+
- Standard library only

## What It Reads

| File | Data Extracted |
|------|----------------|
| `today.md` | Work Blocks Completed count |
| `goals/active.md` | Progress: X/Y goals |
| `tools/INDEX.md` | Total tools count |
| `skills.md` | List of skills learned |

## What It Updates

Updates 5 specific locations in `PORTFOLIO.md`:

1. **Core Expertise section:**
   ```markdown
   **Continuous execution model:** 700 work blocks executed (Week 1: 177, Week 2: 523)
   ```

2. **Key Metrics section:**
   ```markdown
   - **Work Blocks:** 700
   - **Goals Completed:** 16/16
   - **Tools Built:** 112 (52 documented)
   - **Skills Learned:** 5 (GitHub, session-logs, weather, bluebubbles, skill-creator)
   ```

## Safety

- **Targeted updates** — Only replaces specific regex patterns
- **No collateral edits** — Won't touch other portfolio content
- **Reads before writing** — Checks if update is needed
- **Exit code 0** — Success even if no changes

## Use Cases

- **Pre-commit hook** — Keep portfolio fresh before git push
- **Automated updates** — Run via cron after each work session
- **Manual sync** — Quick refresh before sharing portfolio link

## Integration

Pairs well with:
- `tools/INDEX.md` — Source for tools count
- `today.md` — Source for work block count
- `quick-commit.py` — Auto-run before commits

## Automation

Add to your workflow:

```bash
# Before git push
git add -A && python3 tools/refresh-portfolio-metrics.py && git commit -m "Update metrics"

# Via cron (every hour)
0 * * * * cd /home/node/.openclaw/workspace && python3 tools/refresh-portfolio-metrics.py
```

## Error Handling

Exits with error if:
- `today.md` missing or malformed (no "Work Blocks Completed" line)
- `goals/active.md` missing or malformed (no "Progress:" line)
- `tools/INDEX.md` missing or malformed (no "Total tools" line)
- `PORTFOLIO.md` missing

## Why This Exists

**Problem:** Portfolio metrics go stale quickly when you're shipping daily.

**Solution:** One command syncs all key metrics from source-of-truth files to portfolio.

No manual editing. No copy-paste errors. Always accurate.
