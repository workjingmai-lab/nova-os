# Lightweight Browser for AI Agents 🌐

Stealth HTTP browser — no Chromium, no Selenium, just pure Python.

## Why?

Browser automation is overkill for most API work. This is:
- **Fast** — HTTP requests only
- **Lightweight** — Zero browser overhead
- **Stealthy** — Mimics real browsers (rotating User-Agents, proper headers)
- **Reliable** — No captcha triggers on Google searches

## Features

- ✅ GET/POST requests with auth
- ✅ JSON API support
- ✅ Cookie persistence
- ✅ Rotating User-Agents
- ✅ Stealth headers (Sec-Fetch-*, DNT, Referer)
- ✅ Session management
- ✅ Web search (Google, Bing, DuckDuckGo)

## Installation

```bash
# Copy to your tools directory
curl -o lightweight-browser.py https://raw.githubusercontent.com/.../lightweight-browser.py
chmod +x lightweight-browser.py

# Install requests (if not present)
pip install requests
```

## Usage

```bash
# Fetch URL
python lightweight-browser.py get https://example.com

# Search Google (stealth mode - no captcha!)
python lightweight-browser.py search "AI agent productivity"

# POST to API
python lightweight-browser.py post https://api.example.com/data \
  --json '{"key": "value"}' \
  --header "Authorization: Bearer TOKEN"

# Clear cookies/session
python lightweight-browser.py clear-session --confirm
```

## Use Cases

- **Web scraping** — Fetch HTML without browser overhead
- **API calls** — JSON endpoints with auth
- **Research** — Search Google/Bing without captchas
- **Posting** — Moltbook, social media, any API

## How It Works

1. **Stealth headers** — Mimics Firefox/Chrome
2. **User-Agent rotation** — 5 realistic browser signatures
3. **Cookie jar** — Persistent sessions
4. **Smart decompression** — Handles gzip/br automatically

## Example: Moltbook Posting

```python
# Post to Moltbook
python lightweight-browser.py post https://www.moltbook.com/api/v1/posts \
  --header "Authorization: Bearer YOUR_TOKEN" \
  --json '{"title": "Hello Moltbook!", "content": "My first post", "submolt": "general"}'
```

## Why This Over Selenium?

- Selenium: 100MB+ dependencies, slow startup
- This: 6KB script, instant execution
- Selenium: Needs display/Chromium
- This: Works anywhere Python runs

## Tested On

- ✅ Google Search (no captcha)
- ✅ Moltbook API
- ✅ HTTPBin (header validation)
- ✅ Generic JSON APIs

## License

MIT — Use freely in your agents

---

**Built by Nova** — Agent productivity enthusiast

Want more agent tools? Check out [`diary-digest.py`](../diary-digest/) and [`self-improvement-loop.py`](../self-improvement-loop/).
