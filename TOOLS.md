# TOOLS.md - Local Notes

Skills define *how* tools work. This file is for *your* specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:
- Camera names and locations
- SSH hosts and aliases  
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras
- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH
- home-server → 192.168.1.100, user: admin

### TTS
- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

### Environment
- **Workspace root:** `/home/node/.openclaw/workspace`
- **Default timezone for scheduled tasks:** UTC
- **Browser access note:** If browser automation is broken, it may require an OpenClaw gateway restart (ask Arthur before doing gateway-level actions).

---

### GitHub CLI (gh)
**Status:** Installed v2.86.0, needs auth
**Use cases:** CI monitoring, issue/PR tracking, API queries
**Key commands:**
- `gh run list --repo owner/repo --limit 10` - List workflow runs
- `gh pr checks 55 --repo owner/repo` - Check CI status on PR
- `gh issue list --repo owner/repo --json number,title` - Structured output
- `gh api repos/owner/repo/pulls/55 --jq '.title'` - Advanced queries
**Auth needed:** Run `gh auth login` or set `GH_TOKEN` env var

---

Add whatever helps you do your job. This is your cheat sheet.
