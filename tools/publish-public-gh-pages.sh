#!/usr/bin/env bash
set -euo pipefail

# Publish the sanitized `public/` bundle to the `gh-pages` branch.
#
# This is meant to be SAFE by default: it only publishes the already-curated
# `public/` directory, and never touches diary/logs.
#
# Usage:
#   bash tools/publish-public-gh-pages.sh
#
# Preconditions:
#   - You are inside the repo root
#   - GitHub Pages is enabled for the repo (Settings → Pages → Deploy from branch: gh-pages)
#   - You have push access + authenticated git remote

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

if [[ ! -d public ]]; then
  echo "Missing ./public directory. Aborting." >&2
  exit 1
fi

# Create a clean worktree for gh-pages
BRANCH="gh-pages"
TMP_DIR="$(mktemp -d)"
cleanup() {
  rm -rf "$TMP_DIR" || true
}
trap cleanup EXIT

# Fetch branch if it exists (don't fail if it doesn't)
git fetch origin "$BRANCH" 2>/dev/null || true

# Initialize a worktree-like staging directory
# We avoid `git worktree` here to keep it simple/portable.
(
  cd "$TMP_DIR"
  git init -q
  git remote add origin "$(git remote get-url origin)"
  git fetch -q origin "$BRANCH" || true

  if git show-ref --verify --quiet "refs/remotes/origin/$BRANCH"; then
    git checkout -q -B "$BRANCH" "origin/$BRANCH"
  else
    git checkout -q -b "$BRANCH"
  fi

  # Replace contents with sanitized bundle
  find . -mindepth 1 -maxdepth 1 \
    ! -name .git \
    -exec rm -rf {} +

  cp -R "$REPO_ROOT/public/." .

  # Optional: disable Jekyll (so files/folders starting with _ are served)
  touch .nojekyll

  git add -A

  if git diff --cached --quiet; then
    echo "No changes to publish. Exiting." >&2
    exit 0
  fi

  git commit -q -m "Publish public bundle ($(date -u +%Y-%m-%dT%H:%MZ))"
  git push -q origin "$BRANCH":"$BRANCH"

  echo "Published ./public to $BRANCH." >&2
)
