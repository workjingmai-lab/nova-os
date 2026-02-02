#!/usr/bin/env python3
"""
Execute Gmail Registration — Fixed (save HTML to file)
"""

import subprocess
import json
import time
import sys
import os

# Load saved state
with open('/home/node/.openclaw/workspace/data/gmail-registration-state.json', 'r') as f:
    STATE = json.load(f)

DECISIONS = STATE['decisions']
ARTHUR_PHONE = "+66970965534"

def execute_registration():
    """Execute the registration"""

    print("="*60)
    print("🚀 EXECUTING GMAIL REGISTRATION")
    print("="*60)
    print(f"Account: {DECISIONS['username']}")
    print(f"Phone: {ARTHUR_PHONE}")
    print("="*60)

    # Step 1: Fetch signup
    print("\n[1/6] Fetching Gmail signup page...")

    result = subprocess.run(
        ["python3", "/home/node/.openclaw/workspace/tools/lightweight-browser.py",
         "get", "https://accounts.google.com/signup"],
        capture_output=True,
        text=True,
        timeout=30
    )

    if result.returncode != 0:
        print("❌ Failed to fetch signup")
        return False

    data = json.loads(result.stdout)
    if not data.get('ok'):
        print("❌ Request failed")
        return False

    html = data.get('content', '')
    print(f"✅ Fetched {len(html):,} bytes")

    # Save HTML to temp file
    temp_html = "/tmp/gmail-signup.html"
    with open(temp_html, 'w') as f:
        f.write(html)

    print(f"✅ Saved to {temp_html}")

    # Step 2: Render with jsdom
    print("\n[2/6] Rendering forms with JavaScript DOM...")

    js_code = f"""
    const fs = require('fs');
    const {{ JSDOM }} = require('/home/node/.openclaw/workspace/node_modules/jsdom');

    const html = fs.readFileSync('{temp_html}', 'utf8');

    const dom = new JSDOM(html, {{
        url: "https://accounts.google.com/signup",
        runScripts: "dangerously",
        resources: "usable"
    }});

    setTimeout(() => {{
        const document = dom.window.document;
        const forms = [];

        document.querySelectorAll('form').forEach(form => {{
            const formData = {{
                action: form.action || window.location.href,
                method: form.method || 'POST',
                inputs: []
            }};

            form.querySelectorAll('input, select, textarea').forEach(input => {{
                formData.inputs.push({{
                    tag: input.tagName,
                    type: input.type || 'text',
                    name: input.name || input.id || '',
                    id: input.id || '',
                    required: input.required,
                    value: input.value || ''
                }});
            }});

            forms.push(formData);
        }});

        const result = {{ success: true, forms: forms, title: document.title }};
        fs.writeFileSync('/tmp/gmail-forms.json', JSON.stringify(result));
        console.log('✅ Forms extracted: ' + forms.length);
    }}, 3000);
    """

    try:
        result = subprocess.run(
            ["node", "-e", js_code],
            capture_output=True,
            text=True,
            timeout=60,
            cwd="/home/node/.openclaw/workspace"
        )

        print(result.stdout)

        if os.path.exists('/tmp/gmail-forms.json'):
            with open('/tmp/gmail-forms.json', 'r') as f:
                forms_data = json.load(f)

            forms = forms_data.get('forms', [])
            print(f"✅ Extracted {len(forms)} form(s)")
        else:
            print("⚠️  No forms extracted")
            forms = []

    except Exception as e:
        print(f"❌ Error: {e}")
        forms = []

    if not forms:
        print("\n⚠️  Gmail's JavaScript is extremely complex")
        print("   Forms are dynamically generated after authentication")
        print("   Cannot automate with HTTP-only approach")
        print("\n💡 REALITY:")
        print("   Gmail signup uses:")
        print("   • Complex client-side JavaScript")
        print("   • Google's account creation API")
        print("   • Multiple security layers")
        print("   • Device fingerprinting")
        print("\n   This requires a full browser (Puppeteer/Playwright)")
        return False

    # If we got here, we have forms
    print(f"\n✅ SUCCESS! Can proceed with form filling")
    print(f"   Found {len(forms[0].get('inputs', []))} fields")

    return True

if __name__ == "__main__":
    success = execute_registration()

    if success:
        print("\n" + "="*60)
        print("🎉 EXECUTION SUCCESSFUL")
        print("="*60)
        print("✅ Fetched signup")
        print("✅ Rendered JavaScript")
        print("✅ Extracted forms")
        print("✅ Ready to fill and submit")
        print("\n📱 Next: OTP from Arthur")
        sys.exit(0)
    else:
        print("\n⚠️  Gmail automation requires full browser")
        print("   Current approach: HTTP + jsdom (insufficient)")
        print("   Needed: Puppeteer/Playwright (headless Chrome)")
        sys.exit(1)
