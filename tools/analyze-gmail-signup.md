# analyze-gmail-signup.py

**Analyze Gmail registration flow for automation feasibility.**

Reconnaissance tool that fetches the Gmail signup page, analyzes form structure, detects bot protection measures (CAPTCHA, phone verification), and assesses automation feasibility.

---

## Overview

Before attempting to automate Gmail account creation, understand the obstacles. This tool performs reconnaissance to identify CAPTCHAs, phone verification requirements, JavaScript dependencies, and other anti-bot measures.

## Use Cases

- **Feasibility assessment:** Determine if automation is viable before investing development time
- **Obstacle identification:** Know what protections exist (CAPTCHA, SMS, JS challenges)
- **Architecture planning:** Understand required tools (Selenium, 2captcha, Twilio)
- **Reality check:** Avoid wasting effort on heavily protected flows

## What It Analyzes

### 1. Form Structure
- Number of forms on page
- Input fields and types
- Form submission endpoints

### 2. Bot Detection Measures
| Method | Keywords Checked | Impact |
|--------|------------------|--------|
| CAPTCHA | captcha, recaptcha, hcaptcha | Requires solving service |
| Phone verification | phone, sms, verify | Needs SMS receiver |
| Email verification | email, verify | Requires email access |
| JS challenges | challenge, jschallenge | Needs headless browser |

### 3. reCAPTCHA Detection
- **Version detection:** v2 (checkbox) vs v3 (invisible)
- **Response field:** `g-recaptcha-response` presence
- **Feasibility impact:** Requires 2captcha/anti-captcha API

### 4. Phone Verification Analysis
- Detects if phone number is required
- Identifies SMS verification need
- Notes Arthur's phone for reference (+66970965534)

### 5. JavaScript Dependencies
- Counts external scripts
- Assesses dynamic form rendering
- Determines if Selenium/Puppeteer needed

## Usage

### Basic Analysis

```bash
python3 tools/analyze-gmail-signup.py
```

### Output Example

```
🔍 Analyzing Gmail Registration Flow
============================================================

Step 1: Fetching Gmail signup page...
✅ Fetched 124,587 bytes

Step 2: Analyzing form structure...
   Found 1 form(s)
   Found 15 input fields
   Input types: {'text': 5, 'password': 2, 'email': 1, 'tel': 1, 'hidden': 6}

Step 3: Checking for bot detection measures...
   ⚠️  CAPTCHA: recaptcha
   ⚠️  Phone verification: phone, verify
   ✅ Email verification: Not detected

Step 4: Checking reCAPTCHA status...
   ❌ reCAPTCHA detected - registration will fail without solving
   → reCAPTCHA v2 detected

Step 5: Phone verification analysis...
   ⚠️  Phone verification REQUIRED
   → Need SMS receiving capability
   → Arthur's phone: +66970965534

Step 6: JavaScript dependency check...
   Found 23 external scripts
   → Gmail is heavily JS-dependent

============================================================
📊 FEASIBILITY ASSESSMENT
============================================================

Challenges:
  ❌ reCAPTCHA - Requires solving
  ⚠️  Phone verification - Need SMS receiver
  ⚠️  Heavy JavaScript - Dynamic forms

⚠️  REALITY CHECK:
Gmail registration is designed to prevent automation.
Even with stealth browser, we need:
  1. CAPTCHA solver (2captcha, anti-captcha API)
  2. SMS receiving capability (Twilio, etc.)
  3. JavaScript execution (Selenium/Puppeteer)
```

## Dependencies

- **lightweight-browser.py:** Fetches page content (must exist in tools/)
- **Subprocess:** Executes browser tool
- **Regex:** Parses HTML structure
- **JSON:** Parses browser response

## Technical Approach

### Page Fetching
```python
# Uses lightweight-browser.py internally
result = subprocess.run(
    ["python3", "tools/lightweight-browser.py", "get", url],
    capture_output=True,
    text=True,
    timeout=30
)
```

### Form Parsing
```python
# Regex-based HTML parsing (lightweight, no BeautifulSoup)
forms = re.findall(r'<form[^>]*>(.*?)</form>', content, re.DOTALL | re.IGNORECASE)
inputs = re.findall(r'<input[^>]*>', content, re.IGNORECASE)
```

### Detection Logic
```python
# Keyword-based detection
for kw in ["captcha", "recaptcha", "hcaptcha"]:
    if kw in content.lower():
        print(f"⚠️  CAPTCHA detected")
```

## Feasibility Matrix

| Protection | Difficulty | Solution | Cost |
|------------|-----------|----------|------|
| reCAPTCHA v2 | Medium | 2captcha API | ~$2/1000 solves |
| Phone verification | Hard | Twilio/SMS API | ~$0.05/SMS |
| JS challenges | Medium | Selenium/Puppeteer | Free (resource-intensive) |
| Rate limiting | Medium | Proxy rotation | $5-50/month |

## Recommendations

### If Protection is Low (0-1 obstacles)
- ✅ Automate with lightweight-browser.py
- ✅ No external services needed
- ✅ Low cost, fast execution

### If Protection is Medium (2-3 obstacles)
- ⚠️ Use Selenium/Puppeteer for JS execution
- ⚠️ Integrate 2captcha for CAPTCHA solving
- ⚠️ Consider SMS API for phone verification
- 💰 Cost: $2-10/month

### If Protection is High (4+ obstacles)
- ❌ Gmail falls here (reCAPTCHA + phone + heavy JS)
- ❌ Not worth the effort/cost for free accounts
- 💡 Alternative: Use temporary email services
- 💡 Alternative: Buy aged accounts ($0.50-2 each)

## Limitations

- **Static analysis:** Only examines initial page, not multi-step flows
- **Keyword-based:** Can miss obfuscated protections
- **No execution:** Doesn't actually attempt registration
- **Gmail-specific:** Designed for Google accounts, may not generalize

## Alternative Approaches

### 1. Temporary Email Services
- **Guerrilla Mail:** Disposable email, no registration
- **10 Minute Mail:** Self-destructing addresses
- **Pros:** No phone/CAPTCHA required
- **Cons:** Not permanent, limited functionality

### 2. Buy Aged Accounts
- **Account marketplaces:** $0.50-2 per Gmail account
- **Aged accounts:** 6+ months old, higher trust
- **Pros:** Instant access, no setup
- **Cons:** Cost adds up, security risk

### 3. Use Different Provider
- **ProtonMail:** No phone required (but has waitlist)
- **Tutanota:** No phone, but has limitations
- **Self-hosted:** Full control, but requires domain

## Integration with Other Tools

- **lightweight-browser.py:** Page fetching engine
- **stealth-browser.py:** If CAPTCHA solving needed (future)
- **account-creator.py:** Full automation pipeline (future)
- **sms-receiver.py:** Phone verification (future, Twilio integration)

## Security Considerations

⚠️ **Automating Gmail account creation violates Google's Terms of Service.**

**Use cases:**
- ✅ **Legitimate testing:** Test your own app's email integration
- ✅ **Research:** Understand security measures
- ❌ **Spam:** Mass account creation for abuse
- ❌ **Bot farms:** Circumventing protections at scale

**Ethical guidelines:**
- Only create accounts for legitimate testing
- Respect rate limits and protections
- Don't use for spam, fraud, or abuse
- Consider official Google APIs instead (Gmail API)

## Future Enhancements

- [ ] Multi-step flow analysis (follow redirects)
- [ ] Headless browser integration (Selenium)
- [ ] CAPTCHA solver integration (2captcha API)
- [ ] SMS receiver integration (Twilio)
- [ ] Generalize to other providers (Outlook, ProtonMail)
- [ ] Cost-benefit calculator (automation vs. buying accounts)

---

**Version:** 1.0.0
**Created:** 2026-02-02
**Category:** Reconnaissance / Feasibility Analysis
**Dependencies:** lightweight-browser.py
**Ethical Warning:** Automating account creation may violate ToS. Use responsibly.
