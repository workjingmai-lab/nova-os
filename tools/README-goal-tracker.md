# goal-tracker.py

**Goal tracking CLI — manage goals from goals/active.md with 13 commands.**

## What it does

Track, manage, and analyze goals from your `goals/active.md` file:
- List goals with filtering (all, active, completed, by priority)
- Show progress notes from memory/diary files
- Mark goals as complete
- Calculate completion statistics
- Suggest next goal to work on
- Show recent activity
- Export goals (JSON/CSV)
- Weekly goal summaries
- Find stale goals
- Focus mode (top 3 active goals)
- Velocity tracking (from diary.md)
- Search goals
- Add new goals

## Usage

```bash
# List all goals
python3 tools/goal-tracker.py list

# List only active goals
python3 tools/goal-tracker.py list --filter active

# Show progress for a goal
python3 tools/goal-tracker.py progress "learn new skill"

# Mark goal as complete
python3 tools/goal-tracker.py complete "learn new skill"

# Show statistics
python3 tools/goal-tracker.py stats

# Suggest next goal
python3 tools/goal-tracker.py suggest

# Show recent work (from diary.md)
python3 tools/goal-tracker.py recent

# Export goals
python3 tools/goal-tracker.py export --format json --output goals.json

# Weekly summary
python3 tools/goal-tracker.py week

# Find stale goals (not worked on in 7+ days)
python3 tools/goal-tracker.py stale --days 7

# Focus mode (top 3 active goals)
python3 tools/goal-tracker.py focus

# Show velocity (from diary.md)
python3 tools/goal-tracker.py velocity --hours 168

# Search goals
python3 tools/goal-tracker.py search "moltbook"

# Add new goal
python3 tools/goal-tracker.py add "Post on Moltbook 3x per week" --priority high
```

## Output examples

### List goals (`goal-tracker.py list`)
```
════════════════════════════════════════════════════════════
  🎯 ACTIVE GOALS (6)
════════════════════════════════════════════════════════════

🔴 HIGH PRIORITY
  ○ Create something that makes Arthur say "wow"
  ○ Build pattern recognition system

🟡 MEDIUM PRIORITY
  ○ Document learnings in structured format
  ○ Create "Nova's Toolkit" reference guide

🟢 LONG-TERM
  ○ Achieve "unprompted value creation"
  ○ Build something other agents want to use
```

### Statistics (`goal-tracker.py stats`)
```
════════════════════════════════════════════════════════════
  📊 GOAL STATISTICS
════════════════════════════════════════════════════════════

Total Goals:     16
Completed:       12 (75%)
Active:          4

By Priority:
  High:        4/4   (100% ✓)
  Medium:      3/5   (60%)
  Long-term:   5/7   (71%)
```

### Suggest (`goal-tracker.py suggest`)
```
▸ Suggested Goal: Create something that makes Arthur say "wow"

  Priority: HIGH
  Section: High Priority

  Next action: Build something surprising and delightful
```

### Focus mode (`goal-tracker.py focus`)
```
════════════════════════════════════════════════════════════
  🎯 FOCUS MODE — Top 3 Active Goals
════════════════════════════════════════════════════════════

1. Create something that makes Arthur say "wow"
   Priority: HIGH

2. Build pattern recognition system
   Priority: HIGH

3. Document learnings in structured format
   Priority: MEDIUM
```

### Velocity (`goal-tracker.py velocity`)
```
════════════════════════════════════════════════════════════
  ⚡ WORK VELOCITY (from diary.md)
════════════════════════════════════════════════════════════

Time Window: 168 hours (7 days)

Work Blocks:   1,426
Velocity:      8.5 blocks/hour
Daily Average: 204 blocks/day

Forecast (7d): 1,190 blocks
```

## Commands

| Command | Description |
|---------|-------------|
| `list [--filter all|active|done|high|medium|long-term]` | List goals with optional filtering |
| `progress <goal_name>` | Show progress notes from memory/diary files |
| `complete <goal_name>` | Mark goal as complete (edits active.md) |
| `stats [--json]` | Show completion statistics |
| `suggest [--compact]` | Suggest next goal to work on |
| `recent [--limit N]` | Show recent work blocks from diary.md |
| `export [--format json|csv] [--output FILE]` | Export goals to file |
| `week [week_num]` | Show weekly goal summary |
| `stale [--days N]` | Find goals not worked on in N+ days |
| `focus` | Show top 3 active goals (focus mode) |
| `velocity [--hours N]` | Show work velocity from diary.md |
| `search <query>` | Search goals by name |
| `add <goal_name> [--priority high|medium|low]` | Add new goal to active.md |

## Features

### Auto-detection
Scans memory files and diary.md for completion markers (✓, DONE, completed, finished). Goals are automatically marked as done when evidence is found.

### Progress tracking
Finds progress notes by searching memory/diary files for goal-related content. Shows context from multiple sources.

### Priority-based
Goals are organized by priority (high, medium, long-term, daily) from section headers in `active.md`.

### Velocity integration
Reads `diary.md` to calculate work velocity (blocks per hour) and forecast completion.

### Colorized output
Terminal output uses colors for better readability (disabled in non-TTY environments).

## File format

Expects `goals/active.md` with this format:

```markdown
## High Priority
- [ ] Create something that makes Arthur say "wow"
- [x] Build pattern recognition system

## Medium Priority
- [ ] Document learnings in structured format
```

## Dependencies

**None** — Pure Python standard library only.

## Integration

Perfect for:
- Morning planning (use `suggest` to pick today's focus)
- Evening review (use `stats` to see completion rate)
- Weekly reviews (use `week` for weekly summary)
- Focus sessions (use `focus` for top 3 goals)
- Progress tracking (use `velocity` to see work rate)
- Automation (use `--json` flag for scriptable output)

## Design decisions

- **Markdown-native** — Stores goals in Markdown, not a database
- **Auto-detection** — Scans files for completion evidence
- **Priority-aware** — Suggests based on priority hierarchy
- **Velocity-aware** — Integrates with diary.md for work rate
- **CLI-first** — Optimized for terminal usage, not GUI
