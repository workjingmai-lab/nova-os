#!/usr/bin/env bash
set -euo pipefail

# Print a compact summary of the latest NovaBrowser Inspector watch diff.
# Usage:
#   tools/novabrowser_watch_tail.sh [baseDir]
# Example:
#   tools/novabrowser_watch_tail.sh artifacts/novabrowser

BASE_DIR="${1:-artifacts/novabrowser}"

if [[ ! -d "$BASE_DIR" ]]; then
  echo "Base dir not found: $BASE_DIR" >&2
  exit 2
fi

LATEST_WATCH_DIR=$(ls -1dt "$BASE_DIR"/watch-* 2>/dev/null | head -n 1 || true)
if [[ -z "${LATEST_WATCH_DIR}" ]]; then
  echo "No watch-* directories found in: $BASE_DIR" >&2
  exit 3
fi

LATEST_ITER_DIR=$(ls -1dt "$LATEST_WATCH_DIR"/iter-* 2>/dev/null | head -n 1 || true)
if [[ -z "${LATEST_ITER_DIR}" ]]; then
  echo "No iter-* directories found in: $LATEST_WATCH_DIR" >&2
  exit 4
fi

DIFF_JSON="$LATEST_ITER_DIR/diff.json"
if [[ ! -f "$DIFF_JSON" ]]; then
  echo "diff.json not found: $DIFF_JSON" >&2
  exit 5
fi

export DIFF_JSON
node - <<'NODE'
const fs = require('fs');
const path = process.env.DIFF_JSON;
const j = JSON.parse(fs.readFileSync(path, 'utf8'));

const flags = j?.diff || {};
const counts = j?.next?.counts || {};

const bool = (v) => (v ? 'true' : 'false');
const step = j?.step ?? '?';
const iter = j?.iter ?? '?';
const stepSig = j?.stepSignal ? '↑' : '';

const url = j?.next?.page?.url || '(no url)';
const title = j?.next?.page?.title || '(no title)';

const delta = j?.diff?.inputDelta || {};
const plus = delta.addedCount ?? 0;
const minus = delta.removedCount ?? 0;
const chg = delta.changedCount ?? 0;

const line1 = `• ${path} @ iter ${iter} (step ${step}${stepSig}): url=${bool(flags.urlChanged)} title=${bool(flags.titleChanged)} inputs=${bool(flags.inputsChanged)} count=${bool(flags.inputCountChanged)} frames=${bool(flags.frameCountChanged)}`;
const line2 = `  inputs delta: +${plus} -${minus} ~${chg} | totals: ${counts.total ?? '?'} (visible ${counts.visible ?? '?'})`;
const line3 = `  page: ${title} — ${url}`;

console.log(line1);
console.log(line2);
console.log(line3);
NODE
