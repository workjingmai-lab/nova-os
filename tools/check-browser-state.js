const CDP = require('/home/node/.openclaw/workspace/node_modules/chrome-remote-interface');

(async () => {
    try {
        const client = await CDP({ port: 9222 });
        const { Runtime, Page } = client;

        await Page.enable();
        await Runtime.enable();

        // Check current page state
        const result = await Runtime.evaluate({
            expression: `
                (() => {
                    return {
                        url: window.location.href,
                        title: document.title,
                        inputCount: document.querySelectorAll('input').length,
                        formCount: document.querySelectorAll('form').length,
                        bodyText: document.body ? document.body.innerText.substring(0, 500) : 'No body'
                    };
                })()
            `,
            awaitPromise: true
        });

        console.log('=== BROWSER STATE ===');
        console.log('URL:', result.result.value.url);
        console.log('Title:', result.result.value.title);
        console.log('Inputs:', result.result.value.inputCount);
        console.log('Forms:', result.result.value.formCount);
        console.log('Page text preview:', result.result.value.bodyText.substring(0, 200));

        await client.close();
    } catch (error) {
        console.error('Error:', error.message);
        process.exit(1);
    }
})();
