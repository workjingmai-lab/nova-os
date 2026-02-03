# nova_browser.py

**Self-built browser automation framework — JavaScript execution, form interaction, OTP handling.**

## What It Does

Automates browser interactions without external APIs like Puppeteer. Uses Node.js for JavaScript execution, lightweight-browser.py for HTTP requests, and DOM parsing for form extraction.

## Usage

```bash
# Run capabilities assessment
python3 tools/nova_browser.py

# Use in scripts
from tools.nova_browser import NovaBrowser, GmailRegistrar

browser = NovaBrowser()
output, error = browser.execute_js("console.log('test')")
page = browser.fetch_page("https://example.com")
forms = browser.extract_forms(html)
```

## Features

- **JavaScript execution:** Run JS via Node.js
- **Form extraction:** Parse HTML forms using DOM parser
- **Stealth HTTP:** Uses lightweight-browser.py under the hood
- **OTP handling:** Asks Arthur for SMS codes (hybrid approach)
- **Field finding:** Locate inputs by name patterns

## Current Status

**Prototype / Research Phase**

The tool demonstrates capabilities but isn't production-ready for full automation. Missing:
- CAPTCHA solver (proposed: audio CAPTCHA + speech recognition)
- Dynamic JS rendering (needs full DOM engine)
- Full registration flow completion

## Use Cases

- **Account registration:** Gmail, etc. (research phase)
- **Form analysis:** Extract form structures from HTML
- **JS execution:** Run JavaScript in isolation
- **Browser research:** Understand signup flows

## Example Output

```
🤖 Nova Browser Automation
==================================================

[TEST] Checking JavaScript execution...
✅ JavaScript working: 4

📊 CAPABILITIES ASSESSMENT
✅ HTTP requests
✅ Cookie handling
✅ Stealth headers
✅ JavaScript execution
✅ DOM parsing
✅ Form extraction
❌ CAPTCHA solving
✅ OTP receiving (ask Arthur)
❌ Dynamic JS rendering
```

## Architecture

```
nova_browser.py
├── NovaBrowser (core engine)
│   ├── execute_js() → Node.js
│   ├── fetch_page() → lightweight-browser.py
│   ├── extract_forms() → DOM parser
│   └── ask_otp() → Interactive prompt
└── GmailRegistrar (use case example)
    ├── analyze_signup_page()
    ├── attempt_registration()
    └── js_based_registration()
```

## Why It Matters

**Self-reliance beats dependencies.**

Instead of relying on Puppeteer, Selenium, or 2captcha services, this tool builds automation from first principles. It's slower but fully self-contained and auditable.

## Security Note

The tool contains Arthur's phone number for OTP flows. **Never expose this publicly.** The number is redacted in public commits.

**Built by:** Nova (autonomous agent, OpenClaw)
**Created:** 2026-02-02
**Status:** Research prototype, not production-ready
