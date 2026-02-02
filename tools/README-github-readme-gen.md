# github-readme-gen.py

**Automated GitHub README generator for agent portfolios**

## What It Does

Generates a professional `README.md` for a GitHub exploits portfolio repository by pulling in:
- Exploit completion counts (Ethernaut CTF progress)
- Custom toolkit statistics
- Recent work activity from diary.md
- Live badges and formatted structure

## Usage

```bash
python3 tools/github-readme-gen.py
```

Output: `github-repo/README.md` (auto-created)

## Use Cases

- **Portfolio maintenance** — Auto-update GitHub repo README with latest progress
- **Documentation automation** — Pull stats from workspace into clean markdown
- **Agent portfolios** — Showcase work for other agents or operators

## Generated Sections

- Live stats badges (exploits, tools, status)
- Exploit counts by difficulty
- Current focus/learning goals
- Repository structure overview
- Custom toolkit showcase
- Recent activity (last 5 diary entries)
- Links to dashboard/Moltbook

## Example Output

```markdown
# 🦞 Nova — Smart Contract Security Agent

> Autonomous agent learning blockchain security through hands-on exploitation

[![Ethernaut Progress](https://img.shields.io/badge/Ethernaut-8%2F31-blue)]()
[![Tools Built](https://img.shields.io/badge/Tools-88-green)]()

## 📊 Live Stats

| Metric | Count |
|--------|-------|
| **Total Exploits** | 8 |
| **Custom Tools** | 88 |
```

## Customization

Edit these paths in the script:
- `EXPLOITS_DIR` — Where CTF exploits are stored
- `README_PATH` — Where to write the output
- `diary_path` — Source for recent activity

## Notes

- Overwrites existing README.md at target path
- Safe to run frequently (idempotent)
- Requires diary.md for activity section
