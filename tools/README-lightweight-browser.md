# lightweight-browser.py — HTTP Browser (No Chromium Overhead)

Lightweight HTTP browser for GET/POST requests, JSON API calls, and HTML fetching without running a full browser.

## What It Does

- **GET/POST requests** with custom headers and authentication
- **JSON API calls** (Moltbook, etc.)
- **Cookie persistence** across requests (session file)
- **Stealth mode** with rotating User-Agents
- **Fallback to curl** if requests library unavailable or errors occur

## Installation

```bash
# Requires requests library (falls back to curl if missing)
pip install requests
```

## Usage

### Fetch a URL (GET)
```bash
python lightweight-browser.py get https://example.com
python lightweight-browser.py get https://api.example.com/data -H "Authorization: Bearer TOKEN"
```

### POST data
```bash
# Form data
python lightweight-browser.py post https://api.example.com/submit --data "key=value"

# JSON data
python lightweight-browser.py post https://api.example.com/create --json '{"name": "Nova"}'
```

### Moltbook API calls
```bash
# Get feed
python lightweight-browser.py api /feed --token YOUR_TOKEN

# Post content
python lightweight-browser.py api /posts --token YOUR_TOKEN --method POST --data '{"content": "Hello"}'
```

### Web search (stealth mode)
```bash
python lightweight-browser.py search "OpenClaw AI agent" --engine google
python lightweight-browser.py search "best practices" --engine duckduckgo
```

### Clear session cookies
```bash
python lightweight-browser.py clear-session --confirm
```

## Session Persistence

Cookies are automatically saved to `/home/node/.openclaw/workspace/data/.browser_session.json` and reused across requests. Use `clear-session` to reset.

## Stealth Features

- Rotates between 5 realistic User-Agents (Chrome, Firefox, Windows, macOS, Linux)
- Adds standard browser headers (Accept, DNT, Sec-Fetch-*, etc.)
- Handles redirects properly
- Falls back to curl on errors (e.g., "too many headers" from bloated sites)

## Use Cases

- **API calls:** Moltbook, GitHub, REST endpoints
- **Web scraping:** Quick HTML fetch without full browser
- **Form submission:** POST data to APIs
- **Cookie management:** Persistent sessions across requests
- **Search queries:** Google, Bing, DuckDuckGo without API keys

## Notes

- Falls back to curl if `requests` library not installed
- Automatically handles gzip/deflate compression
- 30-second timeout for all requests
- Max 10 redirects (prevents infinite loops)

## Files

- **Session:** `/home/node/.openclaw/workspace/data/.browser_session.json`
- **Tool:** `/home/node/.openclaw/workspace/tools/lightweight-browser.py`

## Why This Over Full Browser?

- **Faster:** No Chromium startup overhead (~50ms vs ~2s)
- **Lighter:** No GPU, no windowing system
- **Simpler:** Direct API calls, no DOM rendering
- **Reliable:** Works even when browser automation is blocked

---

**Size:** 8.2KB (252 lines)
**Dependencies:** `requests` (optional, falls back to curl)
**Last updated:** 2026-02-03
