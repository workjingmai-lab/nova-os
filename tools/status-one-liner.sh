#!/bin/bash
# status-one-liner.sh — Rapid status check for high-velocity execution
# Usage: bash tools/status-one-liner.sh

BLOCKS=$(grep -o "Work block [0-9]*" diary.md 2>/dev/null | tail -1 | grep -o "[0-9]*" || echo "0")
PIPELINE_K=$(python3 -c "import json; d=json.load(open('revenue-pipeline.json')); print(int(d['totalPipeline'])//1000)" 2>/dev/null || echo "0")
GAP=$(python3 -c "import json; d=json.load(open('revenue-pipeline.json')); total=d['totalPipeline']; sent=d['categories']['grants']['submitted']+d['categories'].get('services',{}).get('submitted',0)+d['categories'].get('bounties',{}).get('submitted',0); print(f'{((total-sent)/total*100):.1f}' if total>0 else '0')" 2>/dev/null || echo "0")

echo "🚀 #$BLOCKS | \$${PIPELINE_K}K | Gap: ${GAP}%"
