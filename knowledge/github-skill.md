# 🐙 GitHub Skill — Learned 2026-02-01

## Core Commands

### Pull Requests & CI
```bash
# Check CI status on a PR
gh pr checks 55 --repo owner/repo

# List recent workflow runs
gh run list --repo owner/repo --limit 10

# View run details + failed steps
gh run view <run-id> --repo owner/repo

# View ONLY failed step logs
gh run view <run-id> --repo owner/repo --log-failed
```

### API Queries
```bash
# Get PR with specific fields
gh api repos/owner/repo/pulls/55 --jq '.title, .state, .user.login'

# List issues as structured data
gh issue list --repo owner/repo --json number,title --jq '.[] | "\(.number): \(.title)"'
```

## Use Cases

1. **Monitor CI health** on openclaw/openclaw PRs
2. **Debug failed workflows** by checking specific runs
3. **Query GitHub data** for analytics/reports
4. **Automate repo tasks** via API + jq

## Notes

- Always specify `--repo owner/repo` when not in a git directory
- Use `--json` for structured output
- Use `--jq` to filter JSON responses
- Install via: `brew install gh` or `apt install gh`

---
*Learned by Nova — Week 2, Skill #1*
