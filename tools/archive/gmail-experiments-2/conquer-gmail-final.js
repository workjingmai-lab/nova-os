const CDP = require('/home/node/.openclaw/workspace/node_modules/chrome-remote-interface');

(async () => {
    try {
        console.log('=== Gmail Conqueror - Final Version ===');
        console.log('Connecting to Chrome...');

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

        console.log('[3/7] Waiting for page to fully render (30 seconds)...');
        await new Promise(resolve => setTimeout(resolve, 30000));

        console.log('[4/7] Looking for input fields...');

        // Use returnByValue: true to get actual data instead of remote object
        const result = await Runtime.evaluate({
            expression: '(' + function() {
                const inputs = [];
                document.querySelectorAll('input').forEach(input => {
                    inputs.push({
                        tag: input.tagName,
                        type: input.type || 'text',
                        name: input.name || input.id || '',
                        id: input.id || '',
                        placeholder: input.placeholder || '',
                        visible: input.offsetParent !== null
                    });
                });

                return {
                    inputs: inputs,
                    inputCount: inputs.length,
                    url: window.location.href,
                    title: document.title
                };
            } + ')()',
            awaitPromise: true,
            returnByValue: true,
            timeout: 15000
        });

        const data = result.result.value;

        console.log('Found ' + data.inputCount + ' input elements');
        console.log('Page title: ' + data.title);

        if (data.inputCount > 0) {
            console.log('✅ Input fields found!');
            console.log('');
            console.log('First 10 input fields:');
            data.inputs.slice(0, 10).forEach((input, i) => {
                console.log('  ' + (i+1) + '. type=' + input.type + ', name=' + input.name + ', visible=' + input.visible);
            });

            // Wait a bit more
            await new Promise(resolve => setTimeout(resolve, 3000));

            console.log('');
            console.log('[5/7] Filling account details...');

            // Fill the form
            const fillResult = await Runtime.evaluate({
                expression: '(' + function() {
                    const firstName = 'Nova';
                    const lastName = 'Agent';
                    const username = 'novaagent2026';
                    const password = 'NovaSecure2026!';
                    const phone = '+66970965534';

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
                    const failedFields = [];

                    document.querySelectorAll('input').forEach(input => {
                        const name = (input.name || input.id || '').toLowerCase();

                        Object.keys(fieldPatterns).forEach(field => {
                            if (fieldPatterns[field].some(pattern => name.includes(pattern))) {
                                try {
                                    input.value = values[field];
                                    filled++;

                                    // Trigger all possible events
                                    input.dispatchEvent(new Event('input', { bubbles: true }));
                                    input.dispatchEvent(new Event('change', { bubbles: true }));
                                    input.dispatchEvent(new Event('blur', { bubbles: true }));

                                    filledFields.push(field + ' (' + name + ')');
                                } catch (e) {
                                    failedFields.push(field + ' (' + name + '): ' + e.message);
                                }
                            }
                        });
                    });

                    return {
                        filled: filled,
                        filledFields: filledFields,
                        failedFields: failedFields,
                        success: filled >= 3
                    };
                } + ')()',
                awaitPromise: true,
                returnByValue: true,
                timeout: 15000
            });

            const fillData = fillResult.result.value;

            console.log('✅ Filled ' + fillData.filled + ' fields!');
            console.log('');
            console.log('Fields filled:');
            fillData.filledFields.forEach(f => console.log('  ✓ ' + f));

            if (fillData.failedFields.length > 0) {
                console.log('');
                console.log('Failed fields:');
                fillData.failedFields.forEach(f => console.log('  ✗ ' + f));
            }

            if (fillData.success) {
                console.log('');
                console.log('[6/7] Form filled successfully!');
                await new Promise(resolve => setTimeout(resolve, 2000));

                console.log('[7/7] ✅ FORM CONQUERED!');
                console.log('');
                console.log('========================================');
                console.log('🎉 SUCCESS - Ready for submission');
                console.log('========================================');
                console.log('');
                console.log('Account details:');
                console.log('  Name: Nova Agent');
                console.log('  Username: novaagent2026');
                console.log('  Password: NovaSecure2026!');
                console.log('  Phone: +66970965534');
                console.log('');
                console.log('📱 Arthur:');
                console.log('   1. Check SMS at +66970965534');
                console.log('   2. Send me the 6-digit OTP code');
                console.log('   3. I will complete verification');
                console.log('');
                console.log('Browser is still running with filled form.');
                console.log('Waiting for your command to submit or OTP...');
            } else {
                console.log('');
                console.log('⚠️  Only filled ' + fillData.filled + ' fields');
                console.log('   May need manual assistance');
            }
        } else {
            throw new Error('No input fields found on page');
        }

        await client.close();

    } catch (error) {
        console.error('');
        console.error('❌ Error:', error.message);
        console.error('Stack:', error.stack);
        process.exit(1);
    }
})();
