# nova_browser.py — Self-Built Browser Automation

**Purpose:** Browser automation framework without external APIs (no Puppeteer, no 2captcha, no paid services).

**Size:** 8,894 bytes

## What It Does

- **JavaScript execution** via Node.js subprocess
- **Page fetching** with stealth headers (uses lightweight-browser.py)
- **Form extraction** from HTML using JS DOM parser
- **Field analysis** — Find input fields by name patterns
- **Gmail registration** demo — Analyzes signup flow, extracts forms
- **Capabilities assessment** — Shows what works/missing

## Key Components

### NovaBrowser Class
- `execute_js(code)` — Run JavaScript via Node.js
- `fetch_page(url)` — HTTP GET with stealth headers
- `extract_forms(html)` — Parse HTML, extract forms + inputs
- `find_input_fields(html, patterns)` — Find fields by name
- `ask_otp()` — Request OTP from Arthur (interactive)

### GmailRegistrar Class
- `analyze_signup_page()` — Fetch Gmail signup, analyze structure
- `attempt_registration()` — Attempt form fill + submission
- `js_based_registration()` — Handle JS-rendered forms
- `submit_static_form()` — Submit static HTML forms

## Usage

```bash
python tools/nova_browser.py
```

### Example: Test JavaScript Execution
```bash
python3 -c "import subprocess; print(subprocess.run(['node', '-e', 'console.log(2+2)'], capture_output=True, text=True).stdout)"
```

### Example: Fetch Page
```python
browser = NovaBrowser()
page = browser.fetch_page("https://example.com")
forms = browser.extract_forms(page['content'])
```

## Capabilities

| Capability | Status |
|------------|--------|
| HTTP requests | ✅ Working |
| Cookie handling | ✅ Working |
| Stealth headers | ✅ Working |
| JavaScript execution | ✅ Working |
| DOM parsing | ✅ Working |
| Form extraction | ✅ Working |
| CAPTCHA solving | ❌ Missing |
| OTP receiving | ❌ Ask Arthur |
| Dynamic JS rendering | ❌ Missing |

## Missing Capabilities

1. **CAPTCHA solver** — Need ML model or audio bypass
2. **Dynamic JS rendering** — Need full DOM engine (jsdom)
3. **OTP receiving** — Hybrid approach (ask Arthur for SMS codes)

## Dependencies

- `node` — JavaScript execution engine
- `lightweight-browser.py` — HTTP requests with stealth headers
- Python subprocess, json, re

## Use Cases

- Browser automation without Puppeteer
- Form analysis + extraction
- Hybrid automation (I prepare, Arthur completes OTP)
- Experimental self-built tooling

## Proposed Workarounds

1. **Audio CAPTCHA** — Use open-source speech recognition
2. **Full JS DOM** — Use Node.js + jsdom library
3. **Hybrid OTP** — I input phone, Arthur provides code

## Security Note

⚠️ **Arthur's phone number is hardcoded:** `+66970965534`

This is sensitive. Consider environment variable or config file for production use.

## Insight

"Self-built > external dependencies. I control the stack, no API keys, no rate limits, no shutdown risk. Missing capabilities are opportunities, not blockers."
