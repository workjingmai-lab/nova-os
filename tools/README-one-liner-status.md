# one-liner-status.py — Ultra-Compact Status

**Purpose:** Single-line status output for terminal prompts or quick checks

**Usage:**
```bash
python3 tools/one-liner-status.py
```

**Output Format:**
```
⚡ 2173/3000 (72%) | 💰 $692K gap | 📈 1% conv
```

**What It Shows:**

1. **⚡ Work Block Progress**
   - Current blocks / target
   - Progress percentage

2. **💰 Execution Gap**
   - Ready but not submitted
   - In thousands (K) for brevity

3. **📈 Conversion Rate**
   - Submitted / (ready + submitted)
   - Percentage

**Use Cases:**

**Terminal Prompt (PS1):**
```bash
# Add to ~/.bashrc or ~/.zshrc
PS1='$(python3 /home/node/.openclaw/workspace/tools/one-liner-status.py)\n$ '
```

**Quick Check:**
```bash
# Instant status without full output
python3 tools/one-liner-status.py
```

**Scripts/Aliases:**
```bash
# Create alias
alias status="python3 ~/workspace/tools/one-liner-status.py"

# Use in scripts
if python3 tools/one-liner-status.py | grep -q "gap"; then
    echo "Revenue waiting to be sent!"
fi
```

**Comparison:**

| Tool | Output | Use Case |
|------|--------|----------|
| `quick-status.py` | 20 lines, detailed | Full check, blockers, actions |
| `one-liner-status.py` | 1 line, compact | Prompt, glance, scripts |

**Examples:**

```bash
$ python3 tools/one-liner-status.py
⚡ 2173/3000 (72%) | 💰 $692K gap | 📈 1% conv

$ python3 tools/one-liner-status.py
⚡ 2500/3000 (83%) | 💰 $450K gap | 📈 15% conv

$ python3 tools/one-liner-status.py
⚡ 3000/3000 (100%) | 💰 $0K gap | 📈 25% conv
```

**Why This Tool:**

- **Instant visibility** — 1 second, no reading required
- **Terminal-friendly** — Fits in PS1 prompt
- **Scriptable** — Easy to parse in scripts/aliases
- **Zero friction** — Single command, single line

**Data Sources:**
- `data/.today-stats.json` — Work block count
- `data/revenue-pipeline.json` — Pipeline statuses

**Complementary Tools:**
- `quick-status.py` — Full detailed status
- `daily-revenue-checklist.py` — Daily checklist
- `velocity-calc.py` — Work velocity predictions

**Created:** Work block 2174
**Author:** Nova
