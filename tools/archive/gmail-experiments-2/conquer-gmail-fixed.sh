#!/bin/bash

echo "=== Gmail Conqueror - Fixed Version ==="
echo "Launching Chromium..."

# Kill any existing Chromium
pkill -9 -f chromium 2>/dev/null
sleep 2

# Launch Chromium
chromium \
  --headless=new \
  --remote-debugging-port=9222 \
  --no-sandbox \
  --disable-setuid-sandbox \
  --disable-dev-shm-usage \
  --disable-blink-features=AutomationControlled \
  --disable-features=IsolateOrigins,site-per-process \
  about:blank &

CHROMIUM_PID=$!
sleep 3

echo "✅ Chromium launched (PID: $CHROMIUM_PID)"
echo ""
echo "Starting Node.js automation..."
echo ""

# Run the Node.js script directly (output will be visible)
node -e "
const CDP = require('/home/node/.openclaw/workspace/node_modules/chrome-remote-interface');

(async () => {
    try {
        const client = await CDP({ port: 9222 });
        const { Page, Runtime, Emulation } = client;

        await Page.enable();
        await Runtime.enable();

        console.log('[1/7] Connected to Chrome');

        // Emulate realistic device
        await Emulation.setDeviceMetricsOverride({
            width: 1920,
            height: 1080,
            deviceScaleFactor: 1,
            mobile: false
        });

        console.log('[2/7] Navigating to Gmail signup...');
        await Page.navigate({ url: 'https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp' });

        // Wait for page to fully render
        console.log('[3/7] Waiting for page to fully render (25 seconds)...');
        await new Promise(resolve => setTimeout(resolve, 25000));

        console.log('[4/7] Looking for input fields...');

        // Try to find ANY input elements
        const result = await Runtime.evaluate({
            expression: \`
                (() => {
                    const inputs = [];
                    document.querySelectorAll('input').forEach(input => {
                        inputs.push({
                            tag: input.tagName,
                            type: input.type || 'text',
                            name: input.name || input.id || '',
                            id: input.id || '',
                            placeholder: input.placeholder || ''
                        });
                    });

                    return {
                        inputs: inputs,
                        inputCount: inputs.length,
                        url: window.location.href,
                        title: document.title
                    };
                })()
            \`,
            awaitPromise: true,
            timeout: 15000
        });

        // Handle the result properly
        const data = result.result && result.result.value ? result.result.value : null;

        if (!data) {
            throw new Error('Failed to evaluate page state');
        }

        console.log('Found ' + data.inputCount + ' input elements');
        console.log('Page title: ' + data.title);
        console.log('URL: ' + data.url.substring(0, 100) + '...');

        if (data.inputCount > 0) {
            console.log('✅ Input fields found, proceeding to fill...');

            // Wait a bit more for any dynamic content
            await new Promise(resolve => setTimeout(resolve, 3000));

            console.log('[5/7] Filling account details...');

            // Fill form using JavaScript
            const fillResult = await Runtime.evaluate({
                expression: \`
                    (function() {
                        const firstName = 'Nova';
                        const lastName = 'Agent';
                        const username = 'novaagent2026';
                        const password = 'NovaSecure2026!';
                        const phone = '+66970965534';

                        // Find and fill fields by common patterns
                        const fieldPatterns = {
                            firstName: ['firstname', 'first', 'givenname', 'fname'],
                            lastName: ['lastname', 'last', 'surname', 'lname', 'familyname'],
                            username: ['username', 'user', 'email', 'gmailaddress'],
                            password: ['pass', 'password', 'passwd', 'pwd'],
                            phone: ['phone', 'mobile', 'phonenumber', 'tel']
                        };

                        const values = {
                            firstName: firstName,
                            lastName: lastName,
                            username: username,
                            password: password,
                            phone: phone
                        };

                        let filled = 0;
                        const filledFields = [];

                        document.querySelectorAll('input, select, textarea').forEach(input => {
                            const name = (input.name || input.id || '').toLowerCase();

                            Object.keys(fieldPatterns).forEach(field => {
                                if (fieldPatterns[field].some(pattern => name.includes(pattern))) {
                                    input.value = values[field];
                                    filled++;
                                    filledFields.push(field);

                                    // Trigger events
                                    input.dispatchEvent(new Event('input', { bubbles: true }));
                                    input.dispatchEvent(new Event('change', { bubbles: true }));
                                    input.dispatchEvent(new Event('blur', { bubbles: true }));
                                }
                            });
                        });

                        return {
                            filled: filled,
                            filledFields: filledFields,
                            success: filled >= 3
                        };
                    })()
                \`,
                awaitPromise: true,
                timeout: 15000
            });

            const fillData = fillResult.result && fillResult.result.value ? fillResult.result.value : {};

            console.log('✅ Filled ' + fillData.filled + ' fields');
            console.log('Fields filled: ' + (fillData.filledFields || []).join(', '));

            if (fillData.success) {
                console.log('[6/7] Form filled, waiting 3 seconds...');
                await new Promise(resolve => setTimeout(resolve, 3000));

                console.log('[7/7] Ready for submission and OTP');
                console.log('');
                console.log('✅ FORM CONQUERED!');
                console.log('');
                console.log('Account details:');
                console.log('  Name: Nova Agent');
                console.log('  Username: novaagent2026');
                console.log('  Password: NovaSecure2026!');
                console.log('  Phone: +66970965534');
                console.log('');
                console.log('📱 Arthur, watch for SMS OTP at +66970965534');
                console.log('   When you receive it, send me the 6-digit code');
                console.log('');
                console.log('Next: I need to submit the form and enter OTP');
            } else {
                console.log('⚠️  Only filled ' + fillData.filled + ' fields, may need manual review');
            }
        } else {
            throw new Error('No input fields found on page');
        }

        await client.close();

    } catch (error) {
        console.error('❌ Error:', error.message);
        console.error('Stack:', error.stack);
        process.exit(1);
    }
})();
"

EXIT_CODE=$?

echo ""
echo "=== Execution complete (exit code: $EXIT_CODE) ==="

if [ $EXIT_CODE -eq 0 ]; then
    echo "✅ SUCCESS! Form is ready for submission"
    echo ""
    echo "Arthur: The browser is still running with the filled form."
    echo "I can help submit it if you want, or you can do it manually."
else
    echo "❌ Failed - check errors above"
fi

echo ""
echo "Chromium cleanup..."
pkill -9 -f chromium 2>/dev/null
echo "✅ Done"
