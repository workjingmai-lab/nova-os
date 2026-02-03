# lightweight-browser.py — Minimal Browser Automation

**Version:** 1.0  
**Category:** Browser Automation  
**Created:** 2026-02-01

---

## What It Does

Lightweight browser control for simple automation tasks: navigation, screenshots, and element extraction.

### Features

- Navigate to URLs
- Take screenshots
- Extract page text
- Find elements by selector
- Simple form filling
- No heavy browser dependencies

---

## Usage

```bash
# Navigate to URL
python3 tools/lightweight-browser.py navigate https://example.com

# Take screenshot
python3 tools/lightweight-browser.py screenshot screenshot.png

# Extract page text
python3 tools/lightweight-browser.py extract https://example.com

# Find element
python3 tools/lightweight-browser.py find https://example.com "h1"

# Fill and submit form
python3 tools/lightweight-browser.py submit https://example.com "username:user" "password:pass"
```

---

## Commands

| Command | Description | Example |
|---------|-------------|---------|
| `navigate` | Open URL | `navigate https://example.com` |
| `screenshot` | Capture page | `screenshot output.png` |
| `extract` | Get page text | `extract https://example.com` |
| `find` | Find element text | `find https://example.com "h1"` |
| `submit` | Fill form | `submit https://example.com "name:value"` |

---

## Output

```bash
$ python3 tools/lightweight-browser.py extract https://example.com

✓ Navigated to https://example.com
✓ Extracted 1,234 characters

Title: Example Domain
Text:
  This domain is for use in illustrative examples...
```

---

## Dependencies

- Python 3.7+
- `requests` — HTTP client
- `beautifulsoup4` — HTML parsing
- (Optional) `selenium` for full browser support

---

## Configuration

Edit defaults:

```python
DEFAULT_TIMEOUT = 30  # seconds
DEFAULT_USER_AGENT = "Mozilla/5.0..."
SCREENSHOT_FORMAT = "png"
```

---

## Use Cases

- **Quick screenshots** — Capture pages without full browser
- **Text extraction** — Scrape content for analysis
- **Form testing** — Submit forms without UI
- **Monitoring** — Check page status periodically

---

## Integration

- Pair with `nova_browser.py` for advanced automation
- Use `moltbook-poster.py` for content publishing
- Schedule via cron for monitoring tasks

---

## Tips

1. Use `extract` for quick content checks
2. Use `screenshot` for visual regression testing
3. Prefer `find` over full `extract` when targeting specific elements
4. Add delays if pages load slowly
