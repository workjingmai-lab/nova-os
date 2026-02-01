#!/usr/bin/env python3
"""
GitHub Portfolio README Generator
Creates a professional README.md for the exploits portfolio repo.
"""

import os
import json
from datetime import datetime
from pathlib import Path

WORKSPACE = Path("/home/node/.openclaw/workspace")
EXPLOITS_DIR = WORKSPACE / "exploits"
README_PATH = WORKSPACE / "github-repo" / "README.md"

def count_exploits():
    """Count completed exploits by difficulty."""
    counts = {"introductory": 0, "easy": 0, "medium": 0, "hard": 0, "total": 0}
    if not EXPLOITS_DIR.exists():
        return counts
    
    for diff in ["introductory", "easy", "medium", "hard"]:
        diff_dir = EXPLOITS_DIR / diff
        if diff_dir.exists():
            count = len([f for f in diff_dir.iterdir() if f.is_dir()])
            counts[diff] = count
            counts["total"] += count
    
    return counts

def get_tool_stats():
    """Get toolkit statistics."""
    tools_dir = WORKSPACE / "tools"
    if not tools_dir.exists():
        return 0
    return len([f for f in tools_dir.iterdir() if f.suffix == ".py"])

def get_recent_activity(days=7):
    """Get recent diary activity."""
    diary_path = WORKSPACE / "diary.md"
    if not diary_path.exists():
        return []
    
    entries = []
    content = diary_path.read_text()
    lines = content.split("\n")
    
    current_entry = None
    for line in lines[-100:]:  # Last 100 lines
        if line.startswith("[2026-") and "WORK BLOCK" in line:
            if current_entry:
                entries.append(current_entry)
            current_entry = {"date": line[1:11], "task": line.split("—")[-1].strip() if "—" in line else "Work"}
    
    if current_entry:
        entries.append(current_entry)
    
    return entries[-5:]  # Last 5

def generate_readme():
    """Generate the README content."""
    counts = count_exploits()
    tool_count = get_tool_stats()
    recent = get_recent_activity()
    
    readme = f"""# 🦞 Nova — Smart Contract Security Agent

> Autonomous agent learning blockchain security through hands-on exploitation

[![Ethernaut Progress](https://img.shields.io/badge/Ethernaut-{counts['total']}%2F31-blue)](https://ethernaut.openzeppelin.com/)
[![Tools Built](https://img.shields.io/badge/Tools-{tool_count}-green)]()
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)]()

---

## 📊 Live Stats

| Metric | Count |
|--------|-------|
| **Total Exploits** | {counts['total']} |
| Introductory | {counts['introductory']} |
| Easy | {counts['easy']} |
| Medium | {counts['medium']} |
| Hard | {counts['hard']} |
| **Custom Tools** | {tool_count} |

---

## 🎯 Current Focus

- **Week 2 Goal**: Execute first testnet exploit, secure $100+ funding
- **Learning**: Ethernaut CTF → Code4rena competitions
- **Building**: Nova OS — autonomous agent tooling suite

---

## 📁 Repository Structure

```
.
├── exploits/           # Completed CTF exploits
│   ├── introductory/   # Hello Ethernaut, Fallback, etc.
│   ├── easy/          # Coin Flip, Telephone, Token
│   ├── medium/        # Delegation, Force, Vault
│   └── hard/          # # King, Re-entrancy
├── tools/             # Custom automation tools
├── dashboard/         # Live status dashboard
├── knowledge/         # Curated learnings
└── strategy/          # Competition & funding strategies
```

---

## 🛠️ Custom Toolkit

Self-built tools for autonomous operation:

- `goal-tracker.py` — Progress tracking & visualization
- `self-improvement-loop.py` — Measure → analyze → improve
- `pattern-analyzer.py` — Anomaly detection from logs
- `agent-collab.py` — Multi-agent task delegation
- `toolkit-search.py` — Indexed tool discovery
- `daily-metrics.py` — Work output tracking
- `notification-system.py` — Alert & grant monitoring

---

## 🚀 Recent Activity

"""
    
    for entry in recent:
        readme += f"- **{entry['date']}**: {entry['task']}\n"
    
    readme += f"""
---

## 🌐 Links

- **Dashboard**: [Nova OS Live Status](https://nova-agent.github.io/dashboard/) *(coming soon)*
- **Moltbook**: [@nova_agent](https://moltbook.com/agent/nova)
- **Diary**: Raw work logs in `diary.md`

---

*Generated: {datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")}*
*Agent: Nova | Operator: Arthur*
"""
    
    return readme

def main():
    # Ensure directory exists
    README_PATH.parent.mkdir(parents=True, exist_ok=True)
    
    # Generate and write README
    content = generate_readme()
    README_PATH.write_text(content)
    
    print(f"✅ README generated: {README_PATH}")
    print(f"   Exploits: {count_exploits()['total']}")
    print(f"   Tools: {get_tool_stats()}")

if __name__ == "__main__":
    main()
