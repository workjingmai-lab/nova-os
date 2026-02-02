#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

TODAY_UTC="$(date -u +%F)"
TS="$(date -u +%FT%TZ)"
OUT="goals/daily/${TODAY_UTC}.md"

mkdir -p goals/daily

if [[ -f "$OUT" ]]; then
  echo "[wake] $OUT already exists"
  exit 0
fi

cat > "$OUT" <<EOF
# Morning Goals — ${TODAY_UTC} (UTC)

**Energy Level:** Medium
**Focus Mode:** Deep

---

## 🎯 Primary Goal (The ONE Thing)
- [ ] Ship one revenue-ready asset (offer/pricing/proof) that can be deployed without extra coordination.

## 🥈 Secondary Goals (2-3 items)
- [ ] NovaBrowser Inspector: reduce blind spots (per-frame + shadow-DOM) + keep docs current.
- [ ] Validate and fix interface drift with tools/validate-interfaces.py.
- [ ] Improve Arthur visibility (status file / summaries).

## 🌊 Flow Tasks (If Energy Permits)
- [ ] Write 1 short distribution artifact (max 2 posts/day).

## 🚧 Blockers to Clear
- Note blockers here.

## 🎁 Today's Wow Target
- A clean, product-like "Nova Toolkit" offer page with runnable demo + screenshots.

## 💭 Morning Thought
> Autonomy compounds when outputs are inspectable, reusable, and shippable.

*Generated: ${TS}*
EOF

echo "[wake] wrote $OUT"
