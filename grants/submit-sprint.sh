#!/usr/bin/env bash
# submit-sprint.sh — Nova's Grant Submission Sprint Runner
# Usage: ./submit-sprint.sh [--dry-run]

set -euo pipefail

DRY_RUN=""
if [[ "${1:-}" == "--dry-run" ]]; then
  DRY_RUN="--dry-run"
  echo "DRY RUN MODE: No actual submissions will be made."
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HELPER="$SCRIPT_DIR/../tools/grant-submit-helper.py"

echo "Starting grant submission sprint..."
echo "Reading SUBMISSION-QUEUE.md..."
python3 "$HELPER" $DRY_RUN --queue "$SCRIPT_DIR/SUBMISSION-QUEUE.md"
echo "Sprint complete. Check grants/submission-tracker.md for results."
