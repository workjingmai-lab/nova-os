const CDP = require('/home/node/.openclaw/workspace/node_modules/chrome-remote-interface');

(async () => {
    try {
        console.log('Connecting to Chrome...');
        const client = await CDP({ port: 9222 });
        const { Page, Runtime } = client;

        await Page.enable();
        await Runtime.enable();

        console.log('Navigating to Gmail signup...');
        await Page.navigate({ url: 'https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp' });

        console.log('Waiting 30 seconds for page to fully render...');
        await new Promise(resolve => setTimeout(resolve, 30000));

        console.log('Evaluating page state...');

        const result = await Runtime.evaluate({
            expression: `
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
            `,
            awaitPromise: true,
            timeout: 15000
        });

        console.log('Raw result:', JSON.stringify(result, null, 2));

        if (result.result && result.result.value) {
            const data = result.result.value;
            console.log('\\n=== PAGE STATE ===');
            console.log('Title:', data.title);
            console.log('URL:', data.url);
            console.log('Inputs found:', data.inputCount);
            console.log('\\nInput fields:');
            data.inputs.forEach((input, i) => {
                console.log(`  ${i+1}. type=${input.type}, name=${input.name}, id=${input.id}, placeholder=${input.placeholder}`);
            });
        } else {
            console.log('ERROR: No result.value found');
            console.log('Result keys:', Object.keys(result));
        }

        await client.close();
        process.exit(0);

    } catch (error) {
        console.error('Error:', error.message);
        console.error('Stack:', error.stack);
        process.exit(1);
    }
})();
