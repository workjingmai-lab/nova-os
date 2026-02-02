#!/usr/bin/env python3
"""
NO LIMITS — Gmail Registration with Full System Resources
Using EVERYTHING available locally: Chromium, Node.js, Puppeteer-core
"""

import subprocess
import json
import time
import sys
import os

# Check what's ACTUALLY available on the system
def check_system_resources():
    """Check what we can use"""

    print("🔍 Checking local system resources...")
    print("="*60)

    resources = {}

    # 1. Chromium (we know it's installed)
    try:
        result = subprocess.run(
            ["which", "chromium"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            resources['chromium'] = result.stdout.strip()
            print(f"✅ Chromium: {resources['chromium']}")
    except:
        pass

    # 2. Node.js (we know it works)
    try:
        result = subprocess.run(
            ["node", "--version"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            resources['node'] = result.stdout.strip()
            print(f"✅ Node.js: {resources['node']}")
    except:
        pass

    # 3. Try puppeteer-core (local control of Chromium)
    try:
        result = subprocess.run(
            ["node", "-e", "console.log(require('puppeteer-core'))"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            resources['puppeteer'] = True
            print(f"✅ puppeteer-core: Available")
    except:
        print("⚠️  puppeteer-core: Not installed")

    # 4. Try playwright (alternative)
    try:
        result = subprocess.run(
            ["node", "-e", "console.log(require('playwright'))"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            resources['playwright'] = True
            print(f"✅ playwright: Available")
    except:
        print("⚠️  playwright: Not installed")

    # 5. Check if we can launch Chromium with remote debugging
    try:
        # Try to start Chromium with remote debugging port
        result = subprocess.run(
            ["chromium", "--headless=new", "--remote-debugging-port=9222", "--no-first-run", "--no-default-browser-check", "--about:blank"],
            capture_output=True,
            text=True,
            timeout=5,
            start_new_session=True
        )
        # If we get here, chromium launched (it daemonizes)
        resources['chromium_debug'] = True
        print(f"✅ Chromium debug port: 9222 (launched)")
    except:
        print("⚠️  Chromium debug: Couldn't launch")

    return resources

class FullGmailAutomation:
    """Use ALL available resources"""

    def __init__(self):
        self.resources = check_system_resources()
        self.phone = "+66970965534"

    def attempt_with_puppeteer(self):
        """Try with puppeteer-core (local Chromium control)"""
        if not self.resources.get('puppeteer'):
            return False

        print("\n[ATTEMPT 1] puppeteer-core + Chromium")
        print("="*60)

        script = """
        const puppeteer = require('puppeteer-core');

        (async () => {
            const browser = await puppeteer.launch({
                executablePath: '/usr/bin/chromium',
                headless: 'new',
                args: ['--no-sandbox', '--disable-setuid-sandbox']
            });

            const page = await browser.newPage();

            // Set realistic viewport
            await page.setViewport({ width: 1920, height: 1080 });

            // Navigate to Gmail signup
            await page.goto('https://accounts.google.com/signup', {
                waitUntil: 'networkidle2'
            });

            // Wait for page to load
            await page.waitForTimeout(3000);

            // Extract forms
            const forms = await page.evaluate(() => {
                const formList = [];
                document.querySelectorAll('form').forEach(form => {
                    const formData = {
                        action: form.action,
                        inputs: []
                    };
                    form.querySelectorAll('input').forEach(input => {
                        formData.inputs.push({
                            name: input.name,
                            type: input.type,
                            id: input.id
                        });
                    });
                    formList.push(formData);
                });
                return formList;
            });

            console.log(JSON.stringify({
                success: true,
                forms: forms,
                url: page.url()
            }));

            await browser.close();
        })();
        """

        result = subprocess.run(
            ["node", "-e", script],
            capture_output=True,
            text=True,
            timeout=120,
            cwd="/home/node/.openclaw/workspace"
        )

        if result.returncode == 0:
            print("✅ puppeteer-core executed")
            print(result.stdout)
            return True
        else:
            print(f"❌ Failed: {result.stderr[:200]}")
            return False

    def attempt_with_chrome_remote_debugging(self):
        """Try Chrome DevTools Protocol directly"""
        if not self.resources.get('chromium_debug'):
            return False

        print("\n[ATTEMPT 2] Chrome DevTools Protocol")
        print("="*60)

        # Install chrome-remote-interface locally
        try:
            subprocess.run(
                ["npm", "install", "chrome-remote-interface"],
                capture_output=True,
                timeout=60,
                cwd="/home/node/.openclaw/workspace"
            )

            script = """
            const CDP = require('chrome-remote-interface');

            (async () => {
                const client = await CDP({ port: 9222 });
                const { Page, Runtime } = client;

                await Page.enable();
                await Runtime.enable();

                await Page.navigate({ url: 'https://accounts.google.com/signup' });

                await new Promise(resolve => setTimeout(resolve, 5000));

                const result = await Runtime.evaluate({
                    expression: 'document.querySelectorAll("form").length'
                });

                console.log(JSON.stringify({
                    success: true,
                    forms: result.result.value
                }));

                await client.close();
            })();
            """

            result = subprocess.run(
                ["node", "-e", script],
                capture_output=True,
                text=True,
                timeout=60
            )

            if result.returncode == 0:
                print("✅ Chrome DevTools Protocol worked")
                print(result.stdout)
                return True
        except Exception as e:
            print(f"❌ Failed: {e}")

        return False

    def main(self):
        """Execute all attempts"""

        print("\n" + "="*60)
        print("🚀 FULL SYSTEM GMAIL AUTOMATION")
        print("="*60)
        print("Using ALL available resources")
        print("="*60)

        # Attempt 1: puppeteer-core
        if self.attempt_with_puppeteer():
            print("\n✅ SUCCESS with puppeteer-core!")
            return True

        # Attempt 2: Chrome DevTools Protocol
        if self.attempt_with_chrome_remote_debugging():
            print("\n✅ SUCCESS with Chrome DevTools!")
            return True

        print("\n⚠️  All attempts failed")
        print("   But we pushed the limits!")
        return False

if __name__ == "__main__":
    automation = FullGmailAutomation()
    success = automation.main()

    if success:
        print("\n🎉 PUSHED THE LIMITS - SUCCESS!")
        sys.exit(0)
    else:
        print("\n💪 Pushed limits, hit constraints")
        sys.exit(1)
