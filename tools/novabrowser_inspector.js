#!/usr/bin/env node
/**
 * NovaBrowser Inspector Mode (CDP)
 *
 * Usage:
 *   node tools/novabrowser_inspector.js [--port 9222] [--out artifacts/novabrowser]
 *   node tools/novabrowser_inspector.js --watch [--every-ms 2000] [--iterations 0]
 *
 * Expects Chromium running with --remote-debugging-port.
 */

const fs = require('fs');
const path = require('path');
const CDP = require('/home/node/.openclaw/workspace/node_modules/chrome-remote-interface');

function parseArgs(argv) {
  const args = {
    port: 9222,
    out: 'artifacts/novabrowser',
    watch: false,
    everyMs: 2000,
    iterations: 0, // 0 = infinite
  };

  for (let i = 2; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--port') args.port = Number(argv[++i]);
    else if (a === '--out') args.out = argv[++i];
    else if (a === '--watch') args.watch = true;
    else if (a === '--every-ms') args.everyMs = Number(argv[++i]);
    else if (a === '--iterations') args.iterations = Number(argv[++i]);
  }
  return args;
}

function ts() {
  // 2026-02-02T04-34-00Z style
  const d = new Date();
  const iso = d.toISOString().replace(/:/g, '-');
  return iso.replace(/\.\d{3}Z$/, 'Z');
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function ensureDir(p) {
  fs.mkdirSync(p, { recursive: true });
}

function stableJson(obj) {
  // Stable-ish stringify for diffs.
  // JSON.stringify with a key list only sorts the *current* object's keys and
  // can drop nested keys. We want a recursive sort.
  const stable = (v) => {
    if (v === null || v === undefined) return v;
    if (Array.isArray(v)) return v.map(stable);
    if (typeof v === 'object') {
      const out = {};
      for (const k of Object.keys(v).sort()) out[k] = stable(v[k]);
      return out;
    }
    return v;
  };

  return JSON.stringify(stable(obj), null, 2);
}

function summarizeInputs(inputs) {
  // Keep diff payload small + stable
  return inputs.map(i => ({
    tag: i.tag,
    type: i.type,
    name: i.name,
    id: i.id,
    autocomplete: i.autocomplete,
    ariaLabel: i.ariaLabel,
    label: i.label,
    placeholder: i.placeholder,
    disabled: i.disabled,
    required: i.required,
    visible: i.visible,
    rect: i.rect,
  }));
}

function flattenFrameTree(frameTree) {
  const out = [];
  const walk = (node, depth = 0) => {
    if (!node) return;
    const f = node.frame || {};
    out.push({
      id: f.id,
      parentId: f.parentId,
      url: f.url,
      name: f.name,
      securityOrigin: f.securityOrigin,
      mimeType: f.mimeType,
      depth,
    });
    const kids = (node.childFrames || []);
    for (const k of kids) walk(k, depth + 1);
  };
  walk(frameTree?.frameTree || frameTree);
  return out;
}

function inputKey(i) {
  // A stable-ish identifier for UI diffs.
  // Prefer id/name; fall back to tag+label+placeholder.
  return [
    i.tag || '',
    i.type || '',
    i.id ? `#${i.id}` : '',
    i.name ? `[name=${i.name}]` : '',
    i.ariaLabel ? `[aria=${i.ariaLabel}]` : '',
    i.label ? `[label=${i.label}]` : '',
    i.placeholder ? `[ph=${i.placeholder}]` : '',
  ].filter(Boolean).join('');
}

function inputsDelta(prevInputs = [], nextInputs = []) {
  const prevMap = new Map(prevInputs.map(i => [inputKey(i), i]));
  const nextMap = new Map(nextInputs.map(i => [inputKey(i), i]));

  const added = [];
  const removed = [];
  const changed = [];

  for (const [k, ni] of nextMap.entries()) {
    if (!prevMap.has(k)) {
      added.push({ key: k, input: ni });
      continue;
    }
    const pi = prevMap.get(k);
    if (stableJson(pi) !== stableJson(ni)) {
      changed.push({ key: k, before: pi, after: ni });
    }
  }

  for (const [k, pi] of prevMap.entries()) {
    if (!nextMap.has(k)) removed.push({ key: k, input: pi });
  }

  return {
    addedCount: added.length,
    removedCount: removed.length,
    changedCount: changed.length,
    // Keep payload bounded. If you need full details, open inputs.json from each iter.
    added: added.slice(0, 25),
    removed: removed.slice(0, 25),
    changed: changed.slice(0, 25),
  };
}

async function captureOnce(client, outDir) {
  const { Page, Runtime } = client;
  await Page.enable();
  await Runtime.enable();

  const pageEval = await Runtime.evaluate({
    expression: `(() => ({ url: location.href, title: document.title }))()`,
    returnByValue: true,
    timeout: 15000,
  });
  const page = pageEval.result.value || {};

  const frameTree = await Page.getFrameTree();

  const inputsEval = await Runtime.evaluate({
    expression: `(() => {
      const collectInputs = (root) => {
        const out = [];
        const seen = new Set();

        const add = (el) => {
          // De-dupe in case we encounter the same node via different traversal paths.
          const key = el && el.tagName ? (el.tagName + '|' + (el.id || '') + '|' + (el.getAttribute('name') || '') + '|' + (el.getAttribute('aria-label') || '') + '|' + (el.getAttribute('placeholder') || '') + '|' + (el.type || '')) : '';
          const k = key + '|' + (el && el.outerHTML ? el.outerHTML.slice(0, 80) : '');
          if (seen.has(k)) return;
          seen.add(k);
          out.push(el);
        };

        const walk = (node) => {
          if (!node) return;

          // Grab form controls under this subtree
          const els = node.querySelectorAll ? node.querySelectorAll('input, textarea, select') : [];
          for (const el of els) add(el);

          // Traverse shadow roots (closed shadow roots are not accessible)
          const all = node.querySelectorAll ? node.querySelectorAll('*') : [];
          for (const el of all) {
            if (el && el.shadowRoot) walk(el.shadowRoot);
          }
        };

        walk(root);
        return out;
      };

      const els = collectInputs(document);

      const pickLabel = (el) => {
        const aria = el.getAttribute('aria-label');
        if (aria) return aria;
        const ph = el.getAttribute('placeholder');
        if (ph) return ph;
        const id = el.id;
        if (id) {
          const lf = document.querySelector('label[for="' + CSS.escape(id) + '"]');
          if (lf && lf.innerText) return lf.innerText.trim();
        }
        const parentLabel = el.closest('label');
        if (parentLabel && parentLabel.innerText) return parentLabel.innerText.trim();
        return '';
      };

      return els.map(el => {
        const r = el.getBoundingClientRect();
        const style = window.getComputedStyle(el);
        const visible = !!(r.width && r.height) && style.visibility !== 'hidden' && style.display !== 'none' && style.opacity !== '0';
        return {
          tag: el.tagName,
          type: el.getAttribute('type') || (el.tagName === 'TEXTAREA' ? 'textarea' : ''),
          name: el.getAttribute('name') || '',
          id: el.id || '',
          autocomplete: el.getAttribute('autocomplete') || '',
          ariaLabel: el.getAttribute('aria-label') || '',
          label: pickLabel(el),
          placeholder: el.getAttribute('placeholder') || '',
          disabled: el.disabled === true,
          required: el.required === true,
          visible,
          rect: { x: r.x, y: r.y, width: r.width, height: r.height },
        };
      });
    })()`,
    returnByValue: true,
    timeout: 30000,
  });
  const inputs = inputsEval.result.value || [];

  const shot = await Page.captureScreenshot({ format: 'png' });
  const pngBuf = Buffer.from(shot.data, 'base64');

  ensureDir(outDir);
  fs.writeFileSync(path.join(outDir, 'page.json'), JSON.stringify({ capturedAt: new Date().toISOString(), ...page }, null, 2));
  fs.writeFileSync(path.join(outDir, 'frames.json'), JSON.stringify(frameTree, null, 2));
  const flatFrames = flattenFrameTree(frameTree);
  fs.writeFileSync(path.join(outDir, 'frames.flat.json'), JSON.stringify({ count: flatFrames.length, frames: flatFrames }, null, 2));
  fs.writeFileSync(path.join(outDir, 'inputs.json'), JSON.stringify({
    count: inputs.length,
    visibleCount: inputs.filter(i => i.visible).length,
    inputs,
  }, null, 2));
  fs.writeFileSync(path.join(outDir, 'screenshot.png'), pngBuf);

  return {
    page,
    frames: frameTree,
    flatFrames,
    inputs: summarizeInputs(inputs),
    counts: {
      total: inputs.length,
      visible: inputs.filter(i => i.visible).length,
      frames: flatFrames.length,
    },
  };
}

function diff(prev, next) {
  const d = {
    urlChanged: (prev?.page?.url || '') !== (next?.page?.url || ''),
    titleChanged: (prev?.page?.title || '') !== (next?.page?.title || ''),
    inputCountChanged: (prev?.counts?.total ?? null) !== (next?.counts?.total ?? null) || (prev?.counts?.visible ?? null) !== (next?.counts?.visible ?? null),
    frameCountChanged: (prev?.counts?.frames ?? null) !== (next?.counts?.frames ?? null),
    inputsChanged: stableJson({ inputs: prev?.inputs || [] }) !== stableJson({ inputs: next?.inputs || [] }),
  };

  // Provide a human-meaningful delta (bounded payload).
  d.inputDelta = inputsDelta(prev?.inputs || [], next?.inputs || []);

  d.any = d.urlChanged || d.titleChanged || d.inputCountChanged || d.frameCountChanged || d.inputsChanged;
  return d;
}

(async () => {
  const args = parseArgs(process.argv);
  const baseOut = path.resolve(args.out);

  let client;
  try {
    client = await CDP({ port: args.port });

    if (!args.watch) {
      const stamp = ts();
      const outDir = path.join(baseOut, stamp);
      const snap = await captureOnce(client, outDir);

      console.log('✅ NovaBrowser Inspector snapshot saved:');
      console.log(outDir);
      console.log('Page:', snap.page.title || '(no title)', '-', snap.page.url || '(no url)');
      console.log('Inputs:', snap.counts.total, '(visible:', snap.counts.visible + ')');
      return;
    }

    // Watch mode: write to a single session folder; each iteration gets its own child dir.
    const sessionDir = path.join(baseOut, `watch-${ts()}`);
    ensureDir(sessionDir);

    let prev = null;
    let n = 0;
    let step = 0;

    console.log(`👀 NovaBrowser Inspector watch mode started (every ${args.everyMs}ms). Output: ${sessionDir}`);

    while (args.iterations === 0 || n < args.iterations) {
      n++;
      const iterDir = path.join(sessionDir, `iter-${String(n).padStart(4, '0')}-${ts()}`);
      const next = await captureOnce(client, iterDir);

      const d = diff(prev, next);

      // Step detector (very lightweight): increment a "step" counter when we see
      // signals that usually indicate navigation/progress in a login/onboarding flow.
      const dd = d.inputDelta || {};
      const stepSignal = Boolean(
        d.urlChanged ||
        d.titleChanged ||
        d.frameCountChanged ||
        (dd.addedCount || 0) > 0 ||
        (dd.removedCount || 0) > 0
      );
      if (stepSignal) step++;

      fs.writeFileSync(path.join(iterDir, 'diff.json'), JSON.stringify({
        iter: n,
        step,
        stepSignal,
        capturedAt: new Date().toISOString(),
        diff: d,
        prev: prev ? { page: prev.page, counts: prev.counts } : null,
        next: { page: next.page, counts: next.counts },
      }, null, 2));

      if (d.any) {
        console.log(`• change @ iter ${n} (step ${step}${stepSignal ? '↑' : ''}): url=${d.urlChanged} title=${d.titleChanged} inputs=${d.inputsChanged} count=${d.inputCountChanged} frames=${d.frameCountChanged}`);
        if (d.inputsChanged) {
          const dd = d.inputDelta || {};
          console.log(`  inputs delta: +${dd.addedCount || 0} -${dd.removedCount || 0} ~${dd.changedCount || 0}`);
        }
        console.log(`  page: ${next.page.title || '(no title)'} — ${next.page.url || '(no url)'}`);
      }

      prev = next;
      await sleep(args.everyMs);
    }

  } catch (err) {
    console.error('❌ Inspector failed:', err && err.message ? err.message : err);
    process.exitCode = 1;
  } finally {
    if (client) {
      try { await client.close(); } catch {}
    }
  }
})();
