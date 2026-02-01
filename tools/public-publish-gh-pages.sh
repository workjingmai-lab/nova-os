#!/usr/bin/env bash
set -euo pipefail

# Publish the contents of public/ to a gh-pages branch.
# Safety defaults:
# - Does NOT push unless PUSH=1
# - Requires PUBLISH=1 to run at all

if [[ "${PUBLISH:-}" != "1" ]]; then
  echo "Refusing to run: set PUBLISH=1 to proceed (e.g. PUBLISH=1 make public-publish-gh-pages)" >&2
  exit 2
fi

repo_root="$(git rev-parse --show-toplevel 2>/dev/null || true)"
if [[ -z "$repo_root" ]]; then
  echo "Not in a git repo." >&2
  exit 1
fi
cd "$repo_root"

if [[ -n "$(git status --porcelain)" ]]; then
  echo "Working tree is dirty. Commit/stash first." >&2
  git status --porcelain >&2
  exit 1
fi

if [[ ! -d public ]]; then
  echo "public/ directory not found. Run: make public-export" >&2
  exit 1
fi

# Ensure public/ is up to date
make public-export >/dev/null

worktree_dir="${repo_root}/.tmp/gh-pages-worktree"
mkdir -p "${repo_root}/.tmp"

cleanup() {
  set +e
  if git worktree list --porcelain | rg -q "^worktree ${worktree_dir}$"; then
    git worktree remove --force "${worktree_dir}" >/dev/null 2>&1 || true
  fi
  rm -rf "${worktree_dir}" >/dev/null 2>&1 || true
}
trap cleanup EXIT

# Add worktree for gh-pages
if git show-ref --verify --quiet refs/heads/gh-pages; then
  git worktree add -f "${worktree_dir}" gh-pages >/dev/null
else
  git worktree add -f -B gh-pages "${worktree_dir}" >/dev/null
fi

cd "${worktree_dir}"

# If this is a brand new branch, make it orphan-like by removing tracked files.
# For existing branches, we overwrite contents.
rm -rf ./* ./.??* 2>/dev/null || true

cp -R "${repo_root}/public/"* .

# GitHub Pages sometimes needs this for root builds without Jekyll processing.
touch .nojekyll

git add -A

if git diff --cached --quiet; then
  echo "No changes to publish (gh-pages already up to date)."
else
  git commit -m "Publish public/ to GitHub Pages" >/dev/null
  echo "Committed gh-pages update." 
fi

if [[ "${PUSH:-}" == "1" ]]; then
  echo "Pushing to origin gh-pages..."
  git push origin gh-pages
else
  echo "Not pushing (set PUSH=1 to push)."
  echo "To push manually: git push origin gh-pages"
fi
