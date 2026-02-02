#!/usr/bin/env python3
"""
Fill the ACTUAL Gmail form that's currently loaded in Chromium
"""

import subprocess
import json

script = """
const CDP = require('/home/node/.openclaw/workspace/node_modules/chrome-remote-interface');

(async () => {
    const client = await CDP({ port: 9222 });
    const { Page, Runtime } = client;

    await Page.enable();
    await Runtime.enable();

    console.log('[FILLING] Current Gmail form...');

    // Fill the name form
    const result = await Runtime.evaluate({
        expression: `
            (function() {
                // Account details
                const firstName = 'Nova';
                const lastName = 'Agent';
                const username = 'novaagent2026';
                const password = 'NovaSecure2026!';
                const phone = '+66970965534';

                let filled = 0;

                // Fill all visible inputs
                document.querySelectorAll('input').forEach(input => {
                    // Skip hidden or invisible fields
                    if (input.type === 'hidden' || input.offsetParent === null) return;

                    const name = (input.name || input.id || '').toLowerCase();
                    const placeholder = (input.placeholder || '').toLowerCase();
                    const label = input.getAttribute('aria-label') || '';

                    // Match by name, placeholder, or label
                    if (name.includes('first') || placeholder.includes('first') || label.includes('first')) {
                        input.value = firstName;
                        filled++;
                        console.log('✓ First Name: ' + firstName);
                    }
                    else if (name.includes('last') || placeholder.includes('last') || label.includes('last')) {
                        input.value = lastName;
                        filled++;
                        console.log('✓ Last Name: ' + lastName);
                    }
                    else if (name.includes('user') || placeholder.includes('user') || label.includes('user') ||
                               name.includes('username') || placeholder.includes('username') ||
                               name.includes('gmail') || placeholder.includes('gmail')) {
                        input.value = username;
                        filled++;
                        console.log('✓ Username: ' + username);
                    }
                    else if (name.includes('pass') || placeholder.includes('pass') || label.includes('pass')) {
                        input.value = password;
                        filled++;
                        console.log('✓ Password: ***');
                    }
                    else if (name.includes('phone') || placeholder.includes('phone') || label.includes('phone')) {
                        input.value = phone;
                        filled++;
                        console.log('✓ Phone: ' + phone);
                    }

                    // Trigger events
                    input.dispatchEvent(new Event('input', { bubbles: true }));
                    input.dispatchEvent(new Event('change', { bubbles: true }));
                    input.dispatchEvent(new Event('blur', { bubbles: true }));
                });

                return {
                    filled: filled,
                    url: window.location.href,
                    step: 'name'
                };
            })()
        `,
        awaitPromise: true,
        timeout: 10000
    });

    console.log(JSON.stringify(result.result.value, null, 2));

    // Wait a moment then try to advance
    await new Promise(resolve => setTimeout(resolve, 2000));

    // Look for next/continue button
    const nextResult = await Runtime.evaluate({
        expression: `
            (function() {
                // Find next/continue button
                const buttons = [];
                document.querySelectorAll('button').forEach(btn => {
                    const text = btn.textContent || btn.getAttribute('aria-label') || '';
                    buttons.push({
                        text: text,
                        id: btn.id,
                        type: btn.type,
                        disabled: btn.disabled
                    });
                });

                // Try to find "Next" button
                const nextBtn = buttons.find(b =>
                    b.text.toLowerCase().includes('next') ||
                    b.text.toLowerCase().includes('continue') ||
                    b.id.toLowerCase().includes('next')
                );

                if (nextBtn) {
                    console.log('Found Next button: ' + nextBtn.text);

                    // Click it
                    nextBtn.element = document.querySelector('button');
                    if (nextBtn.element) {
                        nextBtn.element.click();
                        return { clicked: true, button: nextBtn.text };
                    }
                }

                return { clicked: false, message: 'No next button found' };
            })()
        `,
        awaitPromise: true,
        timeout: 5000
    });

    console.log(JSON.stringify(nextResult.result.value, null, 2));

    await client.close();
})();
"""

result = subprocess.run(
    ["node", "-e", script],
    capture_output=True,
    text=True,
    timeout=60
)

print(result.stdout)

if result.returncode == 0:
    print("\n✅ FORM FILLED!")
    print("   Arthur, check your SMS at +66970965534")
else:
    print(f"\n❌ Error: {result.stderr}")
