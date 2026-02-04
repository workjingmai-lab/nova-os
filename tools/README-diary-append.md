# README: diary-append.py

## Overview
Safely append entries to diary.md from command line or scripts.

## Purpose
Quick logging to diary.md without manual file editing. Prevents overwriting by reading existing content first.

## Installation
No installation required. Uses Python 3 standard library.

## Usage

### Basic Usage
```bash
python3 tools/diary-append.py "Completed task: Grant research"
```
Appends entry with timestamp.

### From Scripts
```python
import subprocess
subprocess.run(["python3", "tools/diary-append.py", "Work block complete"])
```
Useful for automation tools.

### Multi-line Entries
```bash
python3 tools/diary-append.py "Multi-line entry with details — Task completed, 5 minutes spent"
```
Joins all arguments into single entry.

## Output

**Console:**
```
✓ Appended to diary.md: Completed task: Grant resear...
```

**diary.md:**
```markdown
Completed task: Grant research
```

## Safety

- **Read-modify-write:** Reads existing content before appending
- **No overwrite:** Preserves all previous entries
- **Auto-creation:** Creates diary.md if missing (with header)

## Use Cases

1. **Quick logging:** After completing a work block
2. **Script logging:** From other tools (e.g., grant-submit.py)
3. **Batch updates:** Multiple appends in a loop

## Example Workflow

```bash
# Work block complete
python3 tools/diary-append.py "[2026-02-04 10:00Z] Work Block — Grant research completed"

# Tool execution
python3 tools/grant-finder.py && \
python3 tools/diary-append.py "Grant finder executed: 5 new opportunities found"
```

## Related Tools

- **diary.py:** Full diary management (read, search, edit)
- **diary-digest.py:** Generate daily/weekly summaries
- **work-log.py:** Alternative logging format

## Version History

- **2026-02-04:** Created (safe append utility)

## Notes

- No automatic timestamping (add your own)
- No validation (any text accepted)
- Simple is better than complex
