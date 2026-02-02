# Capability Audit Report

Generated: 2026-01-31T14:55:00Z

## Capability Matrix

| Capability | Test Method | Result | Limits |
|------------|-------------|--------|--------|
| Code Execution (exec) | `echo "Hello from exec test"` | ✅ PASS | No destructive commands (rm, chmod, sudo). Sandbox available via `security: sandbox` |
| File Write | Create test_capability.txt | ✅ PASS | Workspace directory only. No system paths. |
| File Read | Read test_capability.txt | ✅ PASS | Read scope limited to workspace and /app/docs |
| Web Search | Brave search for "OpenClaw AI" | ❌ FAIL | Requires BRAVE_API_KEY configuration |
| Web Fetch | Fetch https://example.com | ✅ PASS | 200 status, content extraction working |
| Browser Control | Check browser status | ⚠️ PARTIAL | Browser service enabled but not running. Requires `openclaw gateway` |
| Scheduling (cron) | Check `openclaw cron` command | ✅ PASS | Command available, no cron jobs currently scheduled |
| Git Operations | `git version && git status` | ✅ PASS | Git 2.39.5, repo shows 18 untracked files |
| Memory Search | List memory directory | ✅ PASS | 2 daily memory files found (2026-01-31) |
| Session Management | Check `openclaw session` command | ✅ PASS | Command available, sessions stored in ~/.openclaw/agents/ |
| Messaging | Tool available but not tested | ⚠️ UNTESTED | Requires channel configuration (WhatsApp/Telegram/Discord) |
| Node Control | List/describe available | ⚠️ UNTESTED | No paired nodes currently |
| Canvas | Present/hide/navigate available | ⚠️ UNTESTED | Requires active session or node |
| TTS | Tool available | ⚠️ UNTESTED | Requires voice configuration |

## Summary

**Working (8/14):** Code execution, file I/O, web fetch, cron, git, memory, sessions, general tool availability
**Blocked (1/14):** Web search (missing API key)
**Requires Setup (5/14):** Browser, messaging, nodes, canvas, TTS

## Security Boundaries

- Exec runs as `node` user, no sudo access
- File operations restricted to workspace
- No destructive actions permitted by policy
- Sandbox mode available for risky operations
